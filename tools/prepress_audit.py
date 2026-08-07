from __future__ import annotations
from pathlib import Path
import re, hashlib, xml.etree.ElementTree as ET
from collections import Counter, defaultdict

ROOT=Path(__file__).resolve().parents[1]
BOOK=ROOT/'book'
chapters=sorted([p for p in BOOK.glob('[0-9][0-9] - *.md') if p.name!='00 - INDEX.md'])
appendices=sorted((BOOK/'appendices').glob('*.md'))
svgs=sorted((BOOK/'assets'/'diagrams').glob('*.svg'))

def frontmatter(text):
    if not text.startswith('---\n'): return {}
    end=text.find('\n---\n',4)
    if end<0:return {}
    out={}
    for line in text[4:end].splitlines():
        if ':' in line:
            k,v=line.split(':',1); out[k.strip()]=v.strip().strip('"')
    return out

def plain_words(text):
    text=re.sub(r'```.*?```',' ',text,flags=re.S)
    text=re.sub(r'<!--.*?-->',' ',text,flags=re.S)
    text=re.sub(r'!\[[^\]]*\]\([^)]*\)',' ',text)
    text=re.sub(r'\[[^\]]*\]\([^)]*\)',' ',text)
    return re.findall(r"[A-Za-zÀ-ž0-9µ/+-]+",text)

def paragraphs(text):
    text=re.sub(r'^---\n.*?\n---\n','',text,flags=re.S)
    parts=re.split(r'\n\s*\n',text)
    out=[]
    for x in parts:
        y=' '.join(x.split())
        if len(y)>=120 and not y.startswith(('#','```','![')):
            out.append(y)
    return out

rows=[]; allpara=defaultdict(list); missing_images=[]; todo=[]; links=[]; bad_fences=[]; heading_issues=[]
for p in chapters+appendices:
    t=p.read_text(encoding='utf-8'); fm=frontmatter(t)
    words=plain_words(t); headings=re.findall(r'^(#{1,4})\s+(.+)$',t,re.M)
    images=re.findall(r'!\[([^\]]*)\]\(([^)]+)\)',t)
    extlinks=re.findall(r'(?<!\!)\[[^\]]+\]\((https?://[^)]+)\)',t)
    urls=re.findall(r'https?://[^\s)>]+',t)
    if t.count('```')%2: bad_fences.append(p.name)
    for m in re.finditer(r'(?i)\b(TODO|FIXME|TBD|PLACEHOLDER|DOPLNIT|DOPLNĚNÍ|DOPLNIT ZDROJ|DOPLNIT ODKAZ)\b',t): todo.append((p.name,t[:m.start()].count('\n')+1,m.group(0)))
    for alt,ref in images:
        target=(p.parent/ref).resolve()
        if not target.exists(): missing_images.append((p.name,ref))
    for u in extlinks+urls: links.append((p.name,u.rstrip('.,;')))
    for para in paragraphs(t):
        norm=re.sub(r'[^a-z0-9á-ž]+',' ',para.lower()).strip()
        if len(norm)>=120: allpara[hashlib.sha1(norm.encode()).hexdigest()].append((p.name,para[:170]))
    h1=[x for lvl,x in headings if lvl=='#']
    if p in chapters:
        num=int(p.name[:2])
        if not h1: heading_issues.append((p.name,'chybí H1'))
        elif not re.match(rf'{num}\.',h1[0]): heading_issues.append((p.name,f'H1 neodpovídá číslu souboru: {h1[0]}'))
    rows.append(dict(file=p.name,bytes=p.stat().st_size,words=len(words),h2=sum(1 for a,b in headings if a=='##'),images=len(images),links=len(set(extlinks+urls)),status=fm.get('status','—'),version=fm.get('version','—'),updated=fm.get('updated',fm.get('snapshot','—'))))

dups=[v for v in allpara.values() if len({x[0] for x in v})>1]

svg_issues=[]
for s in svgs:
    try:
        root=ET.parse(s).getroot()
        title=root.find('{http://www.w3.org/2000/svg}title')
        desc=root.find('{http://www.w3.org/2000/svg}desc')
        if title is None or not (title.text or '').strip(): svg_issues.append((s.name,'chybí <title>'))
        if desc is None or not (desc.text or '').strip(): svg_issues.append((s.name,'chybí <desc>'))
        if not root.get('viewBox'): svg_issues.append((s.name,'chybí viewBox'))
    except Exception as exc: svg_issues.append((s.name,f'XML chyba: {exc}'))

index=(BOOK/'00 - INDEX.md').read_text(encoding='utf-8')
index_numbers=[int(x) for x in re.findall(r'^##\s+(\d+)\.',index,re.M)]
expected=list(range(1,38))

out=[]
out += ['# Automatizovaný předtiskový audit','', '> Mechanické kontroly nad celým repozitářem. Nenahrazuje redakční a faktickou kontrolu člověkem/LLM.','']
out += ['## Souhrn','',f'- Kapitoly: **{len(chapters)}**',f'- Přílohy: **{len(appendices)}**',f'- SVG: **{len(svgs)}**',f'- Celkem slov v kapitolách: **{sum(r["words"] for r in rows[:len(chapters)])}**',f'- Celkem slov v přílohách: **{sum(r["words"] for r in rows[len(chapters):])}**',f'- Neexistující image reference: **{len(missing_images)}**',f'- SVG strukturální chyby: **{len(svg_issues)}**',f'- Kandidátní TODO/placeholder výskyty: **{len(todo)}**',f'- Neuzavřené code fences: **{len(bad_fences)}**',f'- Přesně duplicitní dlouhé odstavce mezi soubory: **{len(dups)}**','']
out += ['## Kapitoly — rozsah a metadata','','| Soubor | slov | kB | H2 | obr. | odkazy | status | verze | updated/snapshot |','|---|---:|---:|---:|---:|---:|---|---|---|']
for r in rows[:len(chapters)]: out.append(f'| {r["file"]} | {r["words"]} | {r["bytes"]/1024:.1f} | {r["h2"]} | {r["images"]} | {r["links"]} | {r["status"]} | {r["version"]} | {r["updated"]} |')
out += ['','## Přílohy — rozsah','','| Soubor | slov | bajtů | status |','|---|---:|---:|---|']
for r in rows[len(chapters):]: out.append(f'| {r["file"]} | {r["words"]} | {r["bytes"]} | {r["status"]} |')
out += ['','## Struktura','',f'- Číslované kapitoly v indexu: `{index_numbers}`',f'- Očekáváno: `{expected}`']
if heading_issues: out += ['', '### Problémy nadpisů']+[f'- {a}: {b}' for a,b in heading_issues]
if missing_images: out += ['', '## Chybějící obrázky']+[f'- {a}: `{b}`' for a,b in missing_images]
if svg_issues: out += ['', '## SVG problémy']+[f'- {a}: {b}' for a,b in svg_issues]
if todo: out += ['', '## TODO / placeholder kandidáti']+[f'- {a}:{ln} — `{m}`' for a,ln,m in todo]
if bad_fences: out += ['', '## Neuzavřené code fences']+[f'- {x}' for x in bad_fences]
if dups:
    out += ['', '## Přesně duplicitní dlouhé odstavce']
    for group in dups[:50]: out.append('- '+' | '.join(f'{f}: {p}' for f,p in group))
out += ['', '## Externí odkazy','','Počet unikátních URL: **%d**' % len(set(u for _,u in links)),'']
for f,u in sorted(set(links)): out.append(f'- {f}: {u}')
(BOOK/'PREPRESS_AUTOMATED_AUDIT.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
print('chapters',len(chapters),'appendices',len(appendices),'svgs',len(svgs),'words',sum(r['words'] for r in rows[:len(chapters)]))
