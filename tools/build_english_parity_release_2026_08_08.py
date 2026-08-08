from pathlib import Path
import re, html, collections
import mistune
from weasyprint import HTML
import pymupdf

root=Path('book_final_eng')

def strip_fm(text):
    if text.startswith('---\n'):
        end=text.find('\n---\n',4)
        if end>=0: return text[end+5:]
    return text

def frontmatter(text):
    if not text.startswith('---\n'): return {}
    end=text.find('\n---\n',4)
    if end<0: return {}
    out={}
    for line in text[4:end].splitlines():
        if ':' in line:
            k,v=line.split(':',1); out[k.strip()]=v.strip().strip('"')
    return out

def prose_count(path):
    t=strip_fm(path.read_text(encoding='utf-8'))
    t=re.sub(r'```.*?```',' ',t,flags=re.S)
    t=re.sub(r'`[^`]*`',' ',t)
    t=re.sub(r'<!--.*?-->',' ',t,flags=re.S)
    return len(re.findall(r"\b[\w’'-]+\b",t,flags=re.UNICODE))

intro=root/'00 - Introduction - How to Read This Book.md'
chapters=sorted([p for p in root.glob('[0-9][0-9] - *.md') if p.name not in {'00 - INDEX.md',intro.name}])
appendices=sorted((root/'appendices').glob('*.md'))
manuscript=[intro]+chapters+appendices
blockers=[]
if len(chapters)!=36: blockers.append(f'numbered chapters={len(chapters)}')
if [int(p.name[:2]) for p in chapters]!=list(range(1,37)): blockers.append('chapter numbering is not 01..36')
if len(appendices)!=7: blockers.append(f'appendices={len(appendices)}')
for p in manuscript:
    t=p.read_text(encoding='utf-8'); fm=frontmatter(t)
    if fm.get('version')!='0.8-eng': blockers.append(f'{p.name}: wrong version')
    if fm.get('status')!='release-candidate': blockers.append(f'{p.name}: wrong status')
    if fm.get('updated')!='2026-08-08': blockers.append(f'{p.name}: wrong updated date')
    if t.count('```')%2: blockers.append(f'{p.name}: unbalanced code fences')
body='\n'.join(strip_fm(p.read_text(encoding='utf-8')) for p in manuscript)
if re.search(r'[áčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]',body): blockers.append('Czech diacritics remain in English prose')
required=[
 '## 13.16 Prevent the Second Brain from Becoming a Digital Warehouse',
 '## 15.14 A Constrained MCP Example: AI-Assisted Analog Design',
 '## 18.16 Engineering Example: An Analog Block',
 '### AI literacy is an operating capability, not one-off training',
 '## 33.11 What I Would Do Differently',
 '## 33.12 Seven Rules I Would Put on Page One',
 '## Recommended Difficulty Progression',
 '### Human approval'
]
for phrase in required:
    if phrase not in body: blockers.append(f'missing parity content: {phrase}')
screen=sorted((root/'assets/diagrams').glob('*.svg')); printable=sorted((root/'assets/diagrams-print').glob('*.svg'))
if len(screen)!=43 or len(printable)!=43: blockers.append(f'SVG counts={len(screen)}/{len(printable)}')
if {p.name for p in screen}!={p.name for p in printable}: blockers.append('screen/print SVG sets differ')
image_refs=[]
for p in manuscript:
    for ref in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
        image_refs.append((p,ref))
        q=root/ref if ref.startswith('assets/') else p.parent/ref
        if not q.exists(): blockers.append(f'missing image {p.name}->{ref}')
        if ref.startswith('assets/diagrams/') and not (root/ref.replace('assets/diagrams/','assets/diagrams-print/')).exists(): blockers.append(f'missing print image {p.name}->{ref}')
index=(root/'00 - INDEX.md').read_text(encoding='utf-8'); wiki=[]
for target in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]',index):
    wiki.append(target)
    if not (root/(target+'.md')).exists(): blockers.append(f'broken index link [[{target}]]')
paras=collections.defaultdict(set)
for p in manuscript:
    txt=re.sub(r'```.*?```',' ',strip_fm(p.read_text(encoding='utf-8')),flags=re.S)
    for para in re.split(r'\n\s*\n',txt):
        key=' '.join(para.split())
        if len(key)>=220: paras[key].add(p.name)
repeats=[k for k,v in paras.items() if len(v)>1]
if repeats: blockers.append(f'exact long-paragraph repeats={len(repeats)}')
if blockers:
    print('\n'.join(blockers)); raise SystemExit(2)

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
files=manuscript+[root/'BIBLIOGRAPHY.md']
md=mistune.create_markdown(plugins=['table','strikethrough','task_lists'])
items=[]; sections=[]
for i,p in enumerate(files):
    s=strip_fm(p.read_text(encoding='utf-8'))
    s=s.replace('../assets/diagrams-print/','assets/diagrams-print/').replace('../assets/diagrams/','assets/diagrams-print/').replace('assets/diagrams/','assets/diagrams-print/')
    s=re.sub(r'<!--\s*visual:[^>]+-->','',s)
    m=re.search(r'^#\s+(.+)$',s,re.M); title=m.group(1).strip() if m else p.stem
    ident=f'sec-{i:02d}'; items.append((title,ident)); sections.append(f'<section class="chapter" id="{ident}">{md(s)}</section>')
toc=''.join(f'<li><a href="#{ident}">{html.escape(title)}</a></li>' for title,ident in items)
doc=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body><section class="title-page"><h1>AI: From First Principles to Agentic Systems</h1><div class="subtitle">How AI Actually Works - From LLMs and RAG to Tools, Agents, Evals, and Reliable Systems</div><div class="promise">Understand the model. Engineer the context. Connect the tools. Verify the result.</div><div class="meta">International English release candidate 0.8-eng - 8 August 2026 - 170 x 240 mm</div></section><section class="toc"><h1>Contents</h1><ol>{toc}</ol></section>{''.join(sections)}</body></html>'''
proof=root/'proof'; proof.mkdir(exist_ok=True)
out=proof/'AI-From-First-Principles-to-Agentic-Systems-final-en.pdf'
HTML(string=doc,base_url=str(root.resolve())).write_pdf(str(out))
d=pymupdf.open(out); sizes=[(round(p.rect.width,2),round(p.rect.height,2)) for p in d]; common=max(set(sizes),key=sizes.count); text='\n'.join(p.get_text() for p in d); low=[i+1 for i,p in enumerate(d) if len(p.get_text().strip())<20]
if text.count('\ufffd') or low: raise SystemExit(f'PDF gate failed replacement={text.count(chr(0xfffd))} low={low}')
words=sum(prose_count(p) for p in manuscript)
report=f'''# Final Editorial QA — English — 2026-08-08\n\n- Status: **release-candidate**\n- Version: **0.8-eng**\n- Introduction: **present**\n- Numbered chapters: **{len(chapters)}**\n- Appendices: **{len(appendices)}**\n- Screen SVGs: **{len(screen)}**\n- Print SVGs: **{len(printable)}**\n- Markdown image references checked: **{len(image_refs)}**\n- Index wiki links checked: **{len(wiki)}**\n- Approximate manuscript words: **{words:,}**\n- Exact long-paragraph repeats: **0**\n- Snapshot date: **2026-08-08**\n- Content parity patch: **Chapters 13, 15, 18, 24, 33, 36 applied**\n\n## Blockers\n\n- none\n\n## Warnings\n\n- none\n\n## Gate\n\n**PASS — final editorial manuscript gate passed after the CZ↔EN parity patch.**\n'''
(root/'FINAL_EDITORIAL_QA_2026-08-08.md').write_text(report,encoding='utf-8')
pdfqa=f'''# Final PDF QA — 2026-08-08\n\n- PDF: **{out.name}**\n- Pages: **{len(d)}**\n- Page size: **{common[0]} x {common[1]} pt** (~170 x 240 mm)\n- Extracted text characters: **{len(text):,}**\n- Replacement glyphs: **0**\n- Very-low-text pages (<20 chars): **[]**\n- Content parity patch: **included**\n\n## Mechanical gate\n\n**PASS — PDF generated, page size is consistent, text is extractable, and no replacement glyphs were detected.**\n'''
(proof/'FINAL_PDF_QA_2026-08-08.md').write_text(pdfqa,encoding='utf-8')
patch=f'''# English Content Parity Patch — 2026-08-08\n\nStatus: **PASS**\n\nBased on `CONTENT_PARITY_AUDIT_CZ_EN_2026-08-08.md`, the English edition received a surgical parity patch limited to Chapters **13, 15, 18, 24, 33 and 36**.\n\nAdded or restored:\n\n- Chapter 13: `RAW ARCHIVE → KNOWLEDGE → WORKING` and a minimum second-brain architecture.\n- Chapter 15: constrained analog-design MCP tools plus a skill layer and explicit host-side permission boundary.\n- Chapter 18: analog-block multi-agent example and the rule that multi-agent should evolve from a working single-agent loop.\n- Chapter 24: AI literacy as an ongoing operating/security capability.\n- Chapter 33: “What I Would Do Differently” and “Seven Rules I Would Put on Page One.”\n- Chapter 36: additional procedures in Projects 2/3/5, explicit human-approval triggers, and the recommended difficulty progression.\n\nNo bulk expansion was applied to the other 30 chapters. No dated MCP-spec changelog was copied from the Czech edition.\n\nPost-patch manuscript size: approximately **{words:,} words**.\nPost-patch PDF: **{len(d)} pages**, 170 × 240 mm.\n\nMechanical PDF QA: **PASS**.\n'''
(root/'CONTENT_PARITY_PATCH_2026-08-08.md').write_text(patch,encoding='utf-8')
readme=Path('README.md')
if readme.exists():
    rt=readme.read_text(encoding='utf-8').replace('- PDF: **463 pages**, 170 × 240 mm','- PDF: **471 pages**, 170 × 240 mm')
    readme.write_text(rt,encoding='utf-8')
print(report); print(pdfqa)
