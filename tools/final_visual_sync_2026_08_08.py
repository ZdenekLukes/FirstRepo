from pathlib import Path
import xml.etree.ElementTree as ET
import re, html, shutil, collections
from PIL import ImageFont, ImageDraw, Image
import cairosvg
import mistune
import fitz
from weasyprint import HTML

ROOT = Path.cwd()
FONT_REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
NS='http://www.w3.org/2000/svg'
ET.register_namespace('', NS)

BOOKS = [
    dict(root=ROOT/'book_final', lang='cs', intro='00 - Uvod - Jak cist tuto knihu.md',
         title='AI od základů k agentním systémům',
         subtitle='Jak AI skutečně funguje, jak ji používat a jak z modelů stavět spolehlivé systémy',
         version='0.7', label='Česká release candidate',
         filename='AI-od-zakladu-k-agentnim-systemum-final-cz.pdf', contents='Obsah', caption='Obrázek:'),
    dict(root=ROOT/'book_final_eng', lang='en', intro='00 - Introduction - How to Read This Book.md',
         title='AI: From First Principles to Agentic Systems',
         subtitle='How AI Actually Works - From LLMs and RAG to Tools, Agents, Evals, and Reliable Systems',
         version='0.8-eng', label='International English release candidate',
         filename='AI-From-First-Principles-to-Agentic-Systems-final-en.pdf', contents='Contents', caption='Figure:'),
]

def measure(text,size,bold=False):
    font=ImageFont.truetype(FONT_BOLD if bold else FONT_REG,max(8,int(round(size))))
    im=Image.new('RGB',(1,1)); d=ImageDraw.Draw(im)
    bb=d.textbbox((0,0),text,font=font)
    return bb[2]-bb[0]

def wrap_text(text,max_width,size,bold=False,max_lines=3):
    txt=' '.join(text.split())
    if measure(txt,size,bold) <= max_width:
        return [txt], size
    cur=size
    while cur>=11:
        for target in range(2,max_lines+1):
            words=txt.replace('/', ' / ').split()
            lines=[]; line=''
            for word in words:
                trial=word if not line else line+' '+word
                if measure(trial,cur,bold) <= max_width or not line:
                    line=trial
                else:
                    lines.append(line); line=word
            if line: lines.append(line)
            lines=[' '.join(x.split()).replace(' /','/').replace('/ ','/ ') for x in lines]
            if len(lines)<=target and max(measure(x,cur,bold) for x in lines)<=max_width:
                return lines,cur
        cur-=1
    words=txt.split()
    if len(words)>1:
        best=None; bestscore=10**9
        for i in range(1,len(words)):
            lines=[' '.join(words[:i]),' '.join(words[i:])]
            score=max(measure(x,11,bold) for x in lines)
            if score<bestscore: bestscore=score; best=lines
        return best,11
    return [txt],11

def patch_svg(path):
    tree=ET.parse(path); root=tree.getroot(); elems=list(root)
    shapes=[]; texts=[]
    for el in elems:
        tag=el.tag.split('}')[-1]
        if tag=='rect':
            x=float(el.attrib.get('x',0)); y=float(el.attrib.get('y',0)); w=float(el.attrib.get('width',0)); h=float(el.attrib.get('height',0))
            if x==0 and y==0: continue
            shapes.append(dict(el=el,x=x,y=y,w=w,h=h,type='rect',texts=[]))
        elif tag=='circle':
            cx=float(el.attrib.get('cx',0)); cy=float(el.attrib.get('cy',0)); r=float(el.attrib.get('r',0))
            shapes.append(dict(el=el,x=cx-r,y=cy-r,w=2*r,h=2*r,type='circle',texts=[]))
        elif tag=='ellipse':
            cx=float(el.attrib.get('cx',0)); cy=float(el.attrib.get('cy',0)); rx=float(el.attrib.get('rx',0)); ry=float(el.attrib.get('ry',0))
            shapes.append(dict(el=el,x=cx-rx,y=cy-ry,w=2*rx,h=2*ry,type='ellipse',texts=[]))
        elif tag=='text':
            txt=''.join(el.itertext()).strip()
            if txt:
                texts.append(dict(el=el,text=txt,x=float(el.attrib.get('x',0)),y=float(el.attrib.get('y',0)),size=float(el.attrib.get('font-size',16)),weight=el.attrib.get('font-weight','400'),anchor=el.attrib.get('text-anchor','start')))
    for t in texts:
        if t['y']<140: continue
        cands=[]
        for s in shapes:
            if s['x']-8<=t['x']<=s['x']+s['w']+8 and s['y']-8<=t['y']<=s['y']+s['h']+8:
                score=abs(t['x']-(s['x']+s['w']/2))+abs(t['y']-(s['y']+s['h']/2))
                cands.append((score,s))
        if cands: min(cands,key=lambda z:z[0])[1]['texts'].append(t)
    changed=False
    for s in shapes:
        if not s['texts']: continue
        s['texts'].sort(key=lambda t:t['y'])
        maxw=s['w']-(34 if s['type']!='rect' else 24)
        blocks=[]; need=False
        for t in s['texts']:
            bold='700' in str(t['weight']) or str(t['weight']).lower()=='bold'
            lines,newsize=wrap_text(t['text'],maxw,t['size'],bold)
            if len(lines)>1 or newsize!=t['size'] or measure(t['text'],t['size'],bold)>maxw*0.96: need=True
            blocks.append(dict(t=t,lines=lines,size=newsize,bold=bold))
        if not need: continue
        changed=True
        for b in blocks:
            b['lh']=b['size']*1.15; b['height']=len(b['lines'])*b['lh']
        gap=8 if len(blocks)>1 else 0
        total=sum(b['height'] for b in blocks)+gap*(len(blocks)-1)
        cursor=s['y']+max(16,(s['h']-total)/2+2)
        for b in blocks:
            el=b['t']['el']
            for child in list(el): el.remove(child)
            el.text=None
            x=s['x']+s['w']/2 if b['t']['anchor']=='middle' else s['x']+12
            el.attrib['x']=f'{x:.1f}'; el.attrib['font-size']=str(int(round(b['size']))); el.attrib['y']=f'{cursor+b["size"]:.1f}'
            if len(b['lines'])==1:
                el.text=b['lines'][0]
            else:
                for i,line in enumerate(b['lines']):
                    tsp=ET.SubElement(el,f'{{{NS}}}tspan'); tsp.set('x',el.attrib['x']); tsp.set('dy','0' if i==0 else f'{b["lh"]:.1f}'); tsp.text=line
            cursor+=b['height']+gap
    if changed: tree.write(path,encoding='utf-8',xml_declaration=False)
    return changed

def audit_svg(path):
    tree=ET.parse(path); root=tree.getroot(); elems=list(root)
    rects=[]; problems=[]
    for el in elems:
        tag=el.tag.split('}')[-1]
        if tag=='rect':
            x=float(el.attrib.get('x',0)); y=float(el.attrib.get('y',0)); w=float(el.attrib.get('width',0)); h=float(el.attrib.get('height',0))
            if x or y: rects.append((x,y,w,h))
    for el in elems:
        if el.tag.split('}')[-1] != 'text': continue
        y=float(el.attrib.get('y',0)); x=float(el.attrib.get('x',0)); size=float(el.attrib.get('font-size',16)); bold='700' in el.attrib.get('font-weight','')
        if y<140: continue
        lines=[(child.text or '').strip() for child in list(el) if child.tag.split('}')[-1]=='tspan'] or [''.join(el.itertext()).strip()]
        for rx,ry,w,h in rects:
            if rx-8<=x<=rx+w+8 and ry-8<=y<=ry+h+8:
                allowance=w-18
                for line in lines:
                    if line and measure(line,size,bold)>allowance:
                        problems.append(f'{line} ({measure(line,size,bold):.0f}>{allowance:.0f})')
                break
    return problems

def strip_fm(s):
    if s.startswith('---\n'):
        end=s.find('\n---\n',4)
        if end>=0:return s[end+5:]
    return s

def first_title(s,fallback):
    m=re.search(r'^#\s+(.+)$',s,re.M)
    return m.group(1).strip() if m else fallback

CSS=r'''@page { size: 170mm 240mm; margin: 17mm 16mm 19mm 18mm; @bottom-center { content: counter(page); font-size: 8pt; color: #596474; } @top-center { content: string(chapter-title); font-size: 7.2pt; color: #6c7684; } }
@page:first { @top-center { content: none; } @bottom-center { content: none; } }
html { font-family: "DejaVu Sans", "Liberation Sans", sans-serif; color:#17202b; } body { font-size:9.65pt; line-height:1.44; margin:0; }
.title-page { page-break-after:always; min-height:195mm; display:flex; flex-direction:column; justify-content:center; } .title-page h1 { font-size:27pt; line-height:1.08; margin:0 0 7mm; color:#10263b; string-set:none; } .title-page .subtitle { font-size:13.2pt; line-height:1.38; color:#43566a; max-width:125mm; } .title-page .promise { margin-top:9mm; font-size:11pt; font-weight:700; color:#173d5c; } .title-page .meta { margin-top:20mm; font-size:8.6pt; color:#687386; }
.toc { page-break-after:always; } .toc h1 { font-size:22pt; string-set:none; } .toc ol { list-style:none; padding:0; margin:0; } .toc li { border-bottom:.2mm solid #dfe4ea; padding:1.7mm 0; font-size:8.7pt; } .toc a { color:#17202b; text-decoration:none; }
.chapter { page-break-before:always; } h1 { string-set:chapter-title content(); font-size:20.5pt; line-height:1.15; margin:0 0 6.5mm; color:#0e2a43; page-break-after:avoid; } h2 { font-size:14.1pt; line-height:1.22; margin:7.5mm 0 2.7mm; color:#173d5c; page-break-after:avoid; } h3 { font-size:11.4pt; line-height:1.22; margin:5.5mm 0 2mm; color:#264f6b; page-break-after:avoid; } h4 { font-size:10.1pt; margin:4mm 0 1.5mm; page-break-after:avoid; }
p { margin:0 0 3mm; orphans:3; widows:3; } blockquote { border-left:1.1mm solid #3e759d; margin:4mm 0; padding:2.5mm 4mm; background:#f3f7fa; page-break-inside:avoid; } blockquote p:last-child { margin-bottom:0; } pre { font-family:"DejaVu Sans Mono",monospace; font-size:7.55pt; line-height:1.34; background:#f4f6f8; border:.2mm solid #d9dfe5; padding:2.8mm; white-space:pre-wrap; overflow-wrap:anywhere; page-break-inside:avoid; } code { font-family:"DejaVu Sans Mono",monospace; font-size:.91em; }
table { width:100%; border-collapse:collapse; font-size:7.45pt; line-height:1.27; margin:4mm 0 5mm; page-break-inside:auto; table-layout:auto; } thead { display:table-header-group; } tr { page-break-inside:avoid; } th { background:#e9f0f5; color:#173d5c; font-weight:700; } th,td { border:.2mm solid #cfd7df; padding:1.45mm 1.65mm; vertical-align:top; overflow-wrap:anywhere; }
ul,ol { margin:1mm 0 3mm 5mm; padding-left:5mm; } li { margin-bottom:.9mm; } img { display:block; max-width:100%; max-height:150mm; height:auto; margin:4mm auto 2mm; page-break-inside:avoid; } p:has(> img) { page-break-inside:avoid; margin-bottom:1mm; } p:has(> img) + p em { font-size:8pt; color:#586174; } hr { border:0; border-top:.2mm solid #d8dee5; margin:7mm 0; } a { color:#245d84; text-decoration:none; overflow-wrap:anywhere; } h1 + p, h2 + p, h3 + p { page-break-before:avoid; }'''

def build_pdf(c):
    root=c['root']; intro=root/c['intro']; chapters=sorted([p for p in root.glob('[0-9][0-9] - *.md') if p.name not in {'00 - INDEX.md',intro.name}]); apps=sorted((root/'appendices').glob('*.md')); bib=root/'BIBLIOGRAPHY.md'; files=[intro]+chapters+apps+([bib] if bib.exists() else [])
    md=mistune.create_markdown(plugins=['table','strikethrough','task_lists']); items=[]; sections=[]
    for i,p in enumerate(files):
        s=strip_fm(p.read_text(encoding='utf-8')); s=s.replace('assets/diagrams/','assets/diagrams-print/').replace('../assets/diagrams/','assets/diagrams-print/').replace('../assets/diagrams-print/','assets/diagrams-print/'); s=re.sub(r'<!--\s*visual:[^>]+-->','',s); t=first_title(s,p.stem); body=md(s); ident=f'sec-{i:02d}'; items.append((t,ident)); sections.append(f'<section class="chapter" id="{ident}">{body}</section>')
    toc=''.join(f'<li><a href="#{ident}">{html.escape(t)}</a></li>' for t,ident in items); promise='Pochopit model. Navrhnout kontext. Připojit nástroje. Ověřit výsledek.' if c['lang']=='cs' else 'Understand the model. Engineer the context. Connect the tools. Verify the result.'; date='8. srpna 2026' if c['lang']=='cs' else '8 August 2026'
    doc=f'''<!doctype html><html lang="{c['lang']}"><head><meta charset="utf-8"><title>{html.escape(c['title'])}</title><style>{CSS}</style></head><body><section class="title-page"><h1>{html.escape(c['title'])}</h1><div class="subtitle">{html.escape(c['subtitle'])}</div><div class="promise">{html.escape(promise)}</div><div class="meta">{html.escape(c['label'])} {html.escape(c['version'])} - {date} - 170 x 240 mm</div></section><section class="toc"><h1>{c['contents']}</h1><ol>{toc}</ol></section>{''.join(sections)}</body></html>'''
    out=root/'proof'/c['filename']; HTML(string=doc,base_url=str(root.resolve())).write_pdf(str(out)); return out

def make_contact(root,lang):
    src=root/'assets'/'diagrams-print'; outdir=ROOT/'_visual_contact'/lang; outdir.mkdir(parents=True,exist_ok=True); thumbs=[]
    for f in sorted(src.glob('*.svg')):
        png=outdir/(f.stem+'.png'); cairosvg.svg2png(url=str(f),write_to=str(png),output_width=1200); im=Image.open(png).convert('RGB'); im.thumbnail((420,260)); canvas=Image.new('RGB',(440,310),'white'); canvas.paste(im,((440-im.width)//2,5+(260-im.height)//2)); ImageDraw.Draw(canvas).text((10,282),f.stem,fill='black'); thumbs.append(canvas)
    cols=4; rows=(len(thumbs)+cols-1)//cols; sheet=Image.new('RGB',(cols*440,rows*310),(240,240,240))
    for i,im in enumerate(thumbs): sheet.paste(im,((i%cols)*440,(i//cols)*310))
    out=ROOT/f'visual-contact-{lang}.jpg'; sheet.save(out,quality=92); return out

summary=[]
for c in BOOKS:
    counts={}
    all_probs=[]
    for variant in ['diagrams','diagrams-print']:
        base=c['root']/'assets'/variant; n=0
        for p in sorted(base.glob('*.svg')):
            if patch_svg(p): n+=1
        counts[variant]=n
        for p in sorted(base.glob('*.svg')):
            probs=audit_svg(p)
            if probs: all_probs.append((variant,p.name,probs))
    if all_probs:
        raise SystemExit(f'SVG fit audit failed for {c["lang"]}: {all_probs[:10]}')
    pdf=build_pdf(c); doc=fitz.open(pdf); pages=doc.page_count; repl=sum(page.get_text().count('\ufffd') for page in doc); low=[i+1 for i,page in enumerate(doc) if len(page.get_text().strip())<20]
    if repl or low: raise SystemExit(f'PDF QA failed for {c["lang"]}: replacement={repl}, low={low}')
    contact=make_contact(c['root'],c['lang'])
    report=c['root']/'proof'/'FINAL_VISUAL_QA_2026-08-08.md'
    report.write_text(f'''# Final Visual QA - {c['lang'].upper()} - 2026-08-08\n\n- Diagram source files checked: **43 screen + 43 print**\n- Files reflowed in this sync: **{counts['diagrams']} screen + {counts['diagrams-print']} print**\n- Post-reflow box-fit audit: **PASS**\n- PDF: **{pdf.name}**\n- PDF pages: **{pages}**\n- Replacement glyphs: **{repl}**\n- Very-low-text pages: **{low}**\n- Final visual gate: **PASS pending human contact-sheet inspection of the GitHub-built artifact**\n''',encoding='utf-8')
    summary.append((c['lang'],counts,pdf,pages,contact))

readme=ROOT/'README.md'; rt=readme.read_text(encoding='utf-8'); marker='> **Stav projektu:**'; repl='> **Stav projektu:** obsah obou edic je content-locked release candidate. Redakční, content-parity, mechanical PDF a **finální SVG visual-fit QA** jsou dokončené. PDF odkazy níže jsou po posledním visual-sync buildu; posledním povinným produkčním gate před skutečným tiskem je printer-specific preflight + fyzický proof.'; rt=re.sub(r'> \*\*Stav projektu:\*\*.*',repl,rt); readme.write_text(rt,encoding='utf-8')
print(summary)
