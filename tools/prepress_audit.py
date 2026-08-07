from __future__ import annotations
from pathlib import Path
import re, hashlib, xml.etree.ElementTree as ET
from collections import defaultdict

ROOT=Path(__file__).resolve().parents[1]
BOOK=ROOT/'book'
chapters=sorted([p for p in BOOK.glob('[0-9][0-9] - *.md') if p.name!='00 - INDEX.md'])
appendices=sorted((BOOK/'appendices').glob('*.md'))
svgs=sorted((BOOK/'assets'/'diagrams').glob('*.svg'))
print_svgs=sorted((BOOK/'assets'/'diagrams-print').glob('*.svg'))


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
    out=[]
    for x in re.split(r'\n\s*\n',text):
        y=' '.join(x.split())
        if len(y)>=120 and not y.startswith(('#','```','![')): out.append(y)
    return out

rows=[]; allpara=defaultdict(list); missing_images=[]; todo=[]; links=[]; bad_fences=[]; heading_issues=[]
for p in chapters+appendices:
    t=p.read_text(encoding='utf-8'); fm=frontmatter(t)
    words=plain_words(t); headings=re.findall(r'^(#{1,4})\s+(.+)$',t,re.M)
    images=re.findall(r'!\[([^\]]*)\]\(([^)]+)\)',t)
    extlinks=re.findall(r'(?<!\!)\[[^\]]+\]\((https?://[^)]+)\)',t)
    urls=re.findall(r'https?://[^\s)>]+',t)
    if t.count('```')%2: bad_fences.append(p.name)
    for m in re.finditer(r'(?i)\b(TODO|FIXME|TBD|PLACEHOLDER|DOPLNIT|DOPLNĚNÍ|DOPLNIT ZDROJ|DOPLNIT ODKAZ)\b',t):
        todo.append((p.name,t[:m.start()].count('\n')+1,m.group(0)))
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


def audit_svg_files(files, print_mode=False):
    issues=[]; font_sizes=[]
    for s in files:
        try:
            root=ET.parse(s).getroot()
            ns='{http://www.w3.org/2000/svg}'
            title=root.find(ns+'title'); desc=root.find(ns+'desc')
            if title is None or not (title.text or '').strip(): issues.append((s.name,'chybí <title>'))
            if desc is None or not (desc.text or '').strip(): issues.append((s.name,'chybí <desc>'))
            if not root.get('viewBox'): issues.append((s.name,'chybí viewBox'))
            text=s.read_text(encoding='utf-8')
            sizes=[int(x) for x in re.findall(r'font-size="(\d+)"',text)]
            font_sizes.extend(sizes)
            if print_mode and sizes and min(sizes)<18: issues.append((s.name,f'print font pod 18 SVG units: {min(sizes)}'))
            if print_mode and '#0b1220' in text.lower(): issues.append((s.name,'print varianta stále obsahuje dark background'))
        except Exception as exc: issues.append((s.name,f'XML chyba: {exc}'))
    return issues,font_sizes

svg_issues,screen_fonts=audit_svg_files(svgs)
print_svg_issues,print_fonts=audit_svg_files(print_svgs,True)

index=(BOOK/'00 - INDEX.md').read_text(encoding='utf-8')
index_numbers=sorted(set(int(x) for x in re.findall(r'\[\[(\d{2})\s+-\s+',index)))
expected=list(range(1,38))

# Explicit final-editorial blocking criteria.
blocking=[]
row_by={r['file']:r for r in rows}
ch37=row_by.get('37 - Deset praktických projektů od začátečníka k agentnímu systému.md')
if not ch37 or ch37['words']<1500: blocking.append('Kapitola 37 je stále příliš krátká (<1500 slov).')
for r in rows[len(chapters):]:
    if r['words']<150: blocking.append(f'Příloha {r["file"]} je stále pouze kostra (<150 slov).')
if todo: blocking.append(f'Rukopis obsahuje {len(todo)} TODO/placeholder kandidátů.')
if missing_images: blocking.append('Existují neplatné image reference.')
if svg_issues: blocking.append('Existují strukturální chyby screen SVG.')
if len(print_svgs)!=len(svgs): blocking.append(f'Počet print SVG ({len(print_svgs)}) neodpovídá screen SVG ({len(svgs)}).')
if print_svg_issues: blocking.append(f'Print SVG audit našel {len(print_svg_issues)} problémů.')
if bad_fences: blocking.append('Existují neuzavřené code fences.')
if index_numbers!=expected: blocking.append('Index neobsahuje přesně kapitoly 1–37.')
if not (BOOK/'STYLE_GUIDE.md').exists(): blocking.append('Chybí STYLE_GUIDE.md.')
if not (BOOK/'BIBLIOGRAPHY.md').exists(): blocking.append('Chybí BIBLIOGRAPHY.md.')

out=[]
out += ['# Automatizovaný předtiskový audit','', '> Mechanické kontroly nad celým repozitářem. Nenahrazuje jazykovou korekturu ani kontrolu skutečně vysázeného PDF.','']
out += ['## Souhrn','',f'- Kapitoly: **{len(chapters)}**',f'- Přílohy: **{len(appendices)}**',f'- Screen SVG: **{len(svgs)}**',f'- Print SVG: **{len(print_svgs)}**',f'- Celkem slov v kapitolách: **{sum(r["words"] for r in rows[:len(chapters)])}**',f'- Celkem slov v přílohách: **{sum(r["words"] for r in rows[len(chapters):])}**',f'- Neexistující image reference: **{len(missing_images)}**',f'- Screen SVG strukturální chyby: **{len(svg_issues)}**',f'- Print SVG problémy: **{len(print_svg_issues)}**',f'- Kandidátní TODO/placeholder výskyty: **{len(todo)}**',f'- Neuzavřené code fences: **{len(bad_fences)}**',f'- Přesně duplicitní dlouhé odstavce mezi soubory: **{len(dups)}**','']
out += ['## Final-editorial gate','']
if blocking:
    out += ['**FAIL — zbývají mechanické blockery:**','']+[f'- {x}' for x in blocking]
else:
    out += ['**PASS — mechanické blockery finálního redakčního draftu jsou odstraněny.**','', 'Další gate musí proběhnout nad skutečně vysázeným proof PDF: stránkování, fonty, sirotci/vdovy, tabulky, grayscale/CMYK proof a fyzická velikost diagramů.']
out += ['','## Kapitoly — rozsah a metadata','','| Soubor | slov | kB | H2 | obr. | odkazy | status | verze | updated/snapshot |','|---|---:|---:|---:|---:|---:|---|---|---|']
for r in rows[:len(chapters)]: out.append(f'| {r["file"]} | {r["words"]} | {r["bytes"]/1024:.1f} | {r["h2"]} | {r["images"]} | {r["links"]} | {r["status"]} | {r["version"]} | {r["updated"]} |')
out += ['','## Přílohy — rozsah','','| Soubor | slov | bajtů | status |','|---|---:|---:|---|']
for r in rows[len(chapters):]: out.append(f'| {r["file"]} | {r["words"]} | {r["bytes"]} | {r["status"]} |')
out += ['','## Struktura','',f'- Kapitoly v indexu: `{index_numbers}`',f'- Očekáváno: `{expected}`']
if heading_issues: out += ['', '### Problémy nadpisů']+[f'- {a}: {b}' for a,b in heading_issues]
if missing_images: out += ['', '## Chybějící obrázky']+[f'- {a}: `{b}`' for a,b in missing_images]
if svg_issues: out += ['', '## Screen SVG problémy']+[f'- {a}: {b}' for a,b in svg_issues]
if print_svg_issues: out += ['', '## Print SVG problémy']+[f'- {a}: {b}' for a,b in print_svg_issues]
if todo: out += ['', '## TODO / placeholder kandidáti']+[f'- {a}:{ln} — `{m}`' for a,ln,m in todo]
if bad_fences: out += ['', '## Neuzavřené code fences']+[f'- {x}' for x in bad_fences]
if dups:
    out += ['', '## Přesně duplicitní dlouhé odstavce']
    for group in dups[:50]: out.append('- '+' | '.join(f'{f}: {p}' for f,p in group))
out += ['', '## Vizuální minimum','','- Nejmenší font screen SVG: **%s** SVG units' % (min(screen_fonts) if screen_fonts else 'n/a'),'- Nejmenší font print SVG: **%s** SVG units' % (min(print_fonts) if print_fonts else 'n/a'),'']
out += ['## Externí odkazy','','Počet unikátních URL: **%d**' % len(set(u for _,u in links)),'']
for f,u in sorted(set(links)): out.append(f'- {f}: {u}')
(BOOK/'PREPRESS_AUTOMATED_AUDIT.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
print('chapters',len(chapters),'appendices',len(appendices),'screen_svg',len(svgs),'print_svg',len(print_svgs),'blocking',len(blocking))
