from pathlib import Path
import re, collections, html
import mistune
from weasyprint import HTML
import pymupdf

BASE=Path('.')

def frontmatter(text):
    if not text.startswith('---\n'): return {}
    end=text.find('\n---\n',4)
    if end<0: return {}
    out={}
    for line in text[4:end].splitlines():
        if ':' in line:
            k,v=line.split(':',1); out[k.strip()]=v.strip().strip('"')
    return out

def strip_frontmatter(text):
    if text.startswith('---\n'):
        end=text.find('\n---\n',4)
        if end>=0: return text[end+5:]
    return text

def prose(text):
    text=strip_frontmatter(text)
    text=re.sub(r'```.*?```',' ',text,flags=re.S)
    text=re.sub(r'`[^`]*`',' ',text)
    text=re.sub(r'<!--.*?-->',' ',text,flags=re.S)
    return text

def manuscript_files(root,lang):
    intro=root/('00 - Uvod - Jak cist tuto knihu.md' if lang=='cz' else '00 - Introduction - How to Read This Book.md')
    chapters=sorted([p for p in root.glob('[0-9][0-9] - *.md') if p.name not in {'00 - INDEX.md',intro.name}])
    appendices=sorted((root/'appendices').glob('*.md'))
    return intro,chapters,appendices,[intro]+chapters+appendices

def audit(root,lang):
    intro,chapters,appendices,manuscript=manuscript_files(root,lang)
    version='0.7' if lang=='cz' else '0.8-eng'
    title='AI od základů k agentním systémům' if lang=='cz' else 'AI: From First Principles to Agentic Systems'
    index=root/'00 - INDEX.md'; blockers=[]; warnings=[]
    nums=[int(p.name[:2]) for p in chapters]
    if nums!=list(range(1,37)): blockers.append(f'chapter numbering is not 01..36: {nums}')
    if len(chapters)!=36: blockers.append(f'numbered chapters={len(chapters)}')
    if len(appendices)!=7: blockers.append(f'appendices={len(appendices)}')
    for p in manuscript:
        t=p.read_text(encoding='utf-8'); fm=frontmatter(t)
        if fm.get('version')!=version: blockers.append(f'{p.name}: version={fm.get("version")}')
        if fm.get('status')!='release-candidate': blockers.append(f'{p.name}: status={fm.get("status")}')
        if fm.get('updated')!='2026-08-08': blockers.append(f'{p.name}: updated={fm.get("updated")}')
        if t.count('```')%2: blockers.append(f'{p.name}: unbalanced code fences')
    screen=sorted((root/'assets/diagrams').glob('*.svg')); printable=sorted((root/'assets/diagrams-print').glob('*.svg'))
    if len(screen)!=43: blockers.append(f'screen SVGs={len(screen)}')
    if len(printable)!=43: blockers.append(f'print SVGs={len(printable)}')
    if {p.name for p in screen}!={p.name for p in printable}: blockers.append('screen/print SVG sets differ')
    image_refs=[]
    for p in manuscript:
        t=p.read_text(encoding='utf-8')
        for ref in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',t):
            image_refs.append((p,ref))
            q=root/ref if ref.startswith('assets/') else p.parent/ref
            if not q.exists(): blockers.append(f'missing image {p.name} -> {ref}')
            if ref.startswith('assets/diagrams/') and not (root/ref.replace('assets/diagrams/','assets/diagrams-print/')).exists():
                blockers.append(f'missing print image {p.name} -> {ref}')
    wiki=[]; it=index.read_text(encoding='utf-8')
    for target in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]',it):
        wiki.append(target)
        if not (root/(target+'.md')).exists(): blockers.append(f'broken index link [[{target}]]')
    for p in manuscript:
        t=p.read_text(encoding='utf-8')
        for pat in [r'\bTODO\b',r'\bFIXME\b',r'\[TBD\]',r'\[DOPLNIT\]',r'PLACEHOLDER',r'rough-draft',r'personal-draft',r'roadmap-draft']:
            if re.search(pat,t,re.I): blockers.append(f'{p.name}: placeholder {pat}')
    body='\n'.join(prose(p.read_text(encoding='utf-8')) for p in manuscript)
    if lang=='cz':
        for bad in ['orchestravat','simulatoru','decision makerem','candidate sizing','Characterization data musí','Simulation je ideální','numerický optimizer']:
            if bad.lower() in body.lower(): blockers.append(f'residual Czech copy-edit term: {bad}')
        if '7. 8. 2026' in body+'\n'+(root/'BIBLIOGRAPHY.md').read_text(encoding='utf-8'): blockers.append('old Czech snapshot date remains')
    else:
        if re.search(r'[áčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]',body): blockers.append('Czech diacritics remain in English prose')
        if 'August 7, 2026' in body+'\n'+(root/'BIBLIOGRAPHY.md').read_text(encoding='utf-8'): blockers.append('old English snapshot date remains')
        old='How AI Actually Works — and How to Build Reliable Systems with Models, Data, Tools, and Verification'
        if old in '\n'.join((root/x).read_text(encoding='utf-8') for x in ['README.md','STYLE_GUIDE.md','ENGLISH_EDITION_NOTES.md']): blockers.append('obsolete English subtitle remains')
    paras=collections.defaultdict(set); words=0
    for p in manuscript:
        b=prose(p.read_text(encoding='utf-8')); words+=len(re.findall(r"\b[\w’'-]+\b",b,flags=re.UNICODE))
        for para in re.split(r'\n\s*\n',b):
            key=' '.join(para.split())
            if len(key)>=220: paras[key].add(p.name)
    repeats=[x for x,v in paras.items() if len(v)>1]
    if repeats: warnings.append(f'exact long paragraph repeats={len(repeats)}')
    if title not in it: blockers.append('index title mismatch')
    report=[f'# Final Editorial QA — {"Czech" if lang=="cz" else "English"} — 2026-08-08','',
            '- Status: **release-candidate**',f'- Version: **{version}**','- Introduction: **present**',
            f'- Numbered chapters: **{len(chapters)}**',f'- Appendices: **{len(appendices)}**',f'- Screen SVGs: **{len(screen)}**',f'- Print SVGs: **{len(printable)}**',
            f'- Markdown image references checked: **{len(image_refs)}**',f'- Index wiki links checked: **{len(wiki)}**',f'- Approximate manuscript words: **{words:,}**',
            f'- Exact long-paragraph repeats: **{len(repeats)}**','- Snapshot date: **2026-08-08**','','## Blockers','']
    report += ['- none'] if not blockers else [f'- {x}' for x in blockers]
    report += ['','## Warnings',''] + (['- none'] if not warnings else [f'- {x}' for x in warnings])
    report += ['','## Gate','', '**PASS — final editorial manuscript gate passed.**' if not blockers else '**FAIL — fix blockers before PDF export.**','']
    (root/'FINAL_EDITORIAL_QA_2026-08-08.md').write_text('\n'.join(report),encoding='utf-8')
    print('\n'.join(report))
    if blockers: raise SystemExit(2)

CSS=r'''
@page { size: 170mm 240mm; margin: 17mm 16mm 19mm 18mm;
 @bottom-center { content: counter(page); font-size:8pt; color:#596474; }
 @top-center { content:string(chapter-title); font-size:7.2pt; color:#6c7684; } }
@page:first { @top-center { content:none; } @bottom-center { content:none; } }
html { font-family:"DejaVu Sans","Liberation Sans",sans-serif; color:#17202b; }
body { font-size:9.65pt; line-height:1.44; margin:0; }
.title-page { page-break-after:always; min-height:195mm; display:flex; flex-direction:column; justify-content:center; }
.title-page h1 { font-size:27pt; line-height:1.08; margin:0 0 7mm; color:#10263b; string-set:none; }
.title-page .subtitle { font-size:13.2pt; line-height:1.38; color:#43566a; max-width:125mm; }
.title-page .promise { margin-top:9mm; font-size:11pt; font-weight:700; color:#173d5c; }
.title-page .meta { margin-top:20mm; font-size:8.6pt; color:#687386; }
.toc { page-break-after:always; }.toc h1{font-size:22pt;string-set:none}.toc ol{list-style:none;padding:0;margin:0}.toc li{border-bottom:.2mm solid #dfe4ea;padding:1.7mm 0;font-size:8.7pt}.toc a{color:#17202b;text-decoration:none}
.chapter{page-break-before:always}h1{string-set:chapter-title content();font-size:20.5pt;line-height:1.15;margin:0 0 6.5mm;color:#0e2a43;page-break-after:avoid}h2{font-size:14.1pt;line-height:1.22;margin:7.5mm 0 2.7mm;color:#173d5c;page-break-after:avoid}h3{font-size:11.4pt;line-height:1.22;margin:5.5mm 0 2mm;color:#264f6b;page-break-after:avoid}h4{font-size:10.1pt;margin:4mm 0 1.5mm;page-break-after:avoid}p{margin:0 0 3mm;orphans:3;widows:3}blockquote{border-left:1.1mm solid #3e759d;margin:4mm 0;padding:2.5mm 4mm;background:#f3f7fa;page-break-inside:avoid}blockquote p:last-child{margin-bottom:0}pre{font-family:"DejaVu Sans Mono",monospace;font-size:7.55pt;line-height:1.34;background:#f4f6f8;border:.2mm solid #d9dfe5;padding:2.8mm;white-space:pre-wrap;overflow-wrap:anywhere;page-break-inside:avoid}code{font-family:"DejaVu Sans Mono",monospace;font-size:.91em}table{width:100%;border-collapse:collapse;font-size:7.45pt;line-height:1.27;margin:4mm 0 5mm;page-break-inside:auto}thead{display:table-header-group}tr{page-break-inside:avoid}th{background:#e9f0f5;color:#173d5c;font-weight:700}th,td{border:.2mm solid #cfd7df;padding:1.45mm 1.65mm;vertical-align:top;overflow-wrap:anywhere}ul,ol{margin:1mm 0 3mm 5mm;padding-left:5mm}li{margin-bottom:.9mm}img{display:block;max-width:100%;max-height:150mm;height:auto;margin:4mm auto 2mm;page-break-inside:avoid}p:has(> img){page-break-inside:avoid;margin-bottom:1mm}p:has(> img)+p em{font-size:8pt;color:#586174}hr{border:0;border-top:.2mm solid #d8dee5;margin:7mm 0}a{color:#245d84;text-decoration:none;overflow-wrap:anywhere}h1+p,h2+p,h3+p{page-break-before:avoid}
'''

def build(root,lang):
    intro,chapters,appendices,manuscript=manuscript_files(root,lang)
    bib=root/'BIBLIOGRAPHY.md'; files=manuscript+[bib]
    if lang=='cz':
        title='AI od základů k agentním systémům'; subtitle='Jak AI skutečně funguje, jak ji používat a jak z modelů stavět spolehlivé systémy'; version='0.7'; label='Česká release candidate'; contents='Obsah'; promise='Pochopit model. Navrhnout kontext. Připojit nástroje. Ověřit výsledek.'; date='8. srpna 2026'; fn='AI-od-zakladu-k-agentnim-systemum-final-cz.pdf'
    else:
        title='AI: From First Principles to Agentic Systems'; subtitle='How AI Actually Works - From LLMs and RAG to Tools, Agents, Evals, and Reliable Systems'; version='0.8-eng'; label='International English release candidate'; contents='Contents'; promise='Understand the model. Engineer the context. Connect the tools. Verify the result.'; date='8 August 2026'; fn='AI-From-First-Principles-to-Agentic-Systems-final-en.pdf'
    md=mistune.create_markdown(plugins=['table','strikethrough','task_lists']); items=[]; sections=[]
    for i,p in enumerate(files):
        s=strip_frontmatter(p.read_text(encoding='utf-8')).replace('assets/diagrams/','assets/diagrams-print/').replace('../assets/diagrams/','assets/diagrams-print/').replace('../assets/diagrams-print/','assets/diagrams-print/')
        s=re.sub(r'<!--\s*visual:[^>]+-->','',s)
        m=re.search(r'^#\s+(.+)$',s,re.M); t=m.group(1).strip() if m else p.stem; ident=f'sec-{i:02d}'
        items.append((t,ident)); sections.append(f'<section class="chapter" id="{ident}">{md(s)}</section>')
    toc=''.join(f'<li><a href="#{ident}">{html.escape(t)}</a></li>' for t,ident in items)
    doc=f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>{CSS}</style></head><body><section class="title-page"><h1>{html.escape(title)}</h1><div class="subtitle">{html.escape(subtitle)}</div><div class="promise">{html.escape(promise)}</div><div class="meta">{html.escape(label)} {version} - {date} - 170 x 240 mm</div></section><section class="toc"><h1>{contents}</h1><ol>{toc}</ol></section>{"".join(sections)}</body></html>'
    proof=root/'proof'; proof.mkdir(exist_ok=True); pdf=proof/fn
    HTML(string=doc,base_url=str(root.resolve())).write_pdf(str(pdf))
    d=pymupdf.open(pdf); sizes=[(round(p.rect.width,2),round(p.rect.height,2)) for p in d]; common=max(set(sizes),key=sizes.count); text='\n'.join(p.get_text() for p in d); low=[i+1 for i,p in enumerate(d) if len(p.get_text().strip())<20]
    expected=(round(170/25.4*72,2),round(240/25.4*72,2))
    if abs(common[0]-expected[0])>1 or abs(common[1]-expected[1])>1: raise SystemExit(f'{fn}: bad page size {common}')
    if text.count('\ufffd'): raise SystemExit(f'{fn}: replacement glyphs')
    if low: raise SystemExit(f'{fn}: very-low-text pages {low}')
    qa=['# Final PDF QA — 2026-08-08','',f'- PDF: **{fn}**',f'- Pages: **{len(d)}**',f'- Page size: **{common[0]} x {common[1]} pt** (~170 x 240 mm)',f'- Extracted text characters: **{len(text):,}**','- Replacement glyphs: **0**',f'- Very-low-text pages (<20 chars): **{low}**','','## Mechanical gate','','**PASS — PDF generated, page size is consistent, text is extractable, and no replacement glyphs were detected.**','']
    (proof/'FINAL_PDF_QA_2026-08-08.md').write_text('\n'.join(qa),encoding='utf-8')
    print('\n'.join(qa))
    return pdf

for r,l in [(BASE/'book_final','cz'),(BASE/'book_final_eng','en')]: audit(r,l)
for r,l in [(BASE/'book_final','cz'),(BASE/'book_final_eng','en')]: build(r,l)
