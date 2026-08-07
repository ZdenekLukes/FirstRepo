from pathlib import Path
import re
from collections import Counter, defaultdict

BOOK = Path('book_final')
chapters = sorted([p for p in BOOK.glob('[0-9][0-9] - *.md') if not p.name.startswith('00 -')])
intro = BOOK / '00 - Uvod - Jak cist tuto knihu.md'
appendices = sorted((BOOK/'appendices').glob('*.md'))

SUSPICIOUS = [
    r'průběžně doplň', r'prubezne dopln', r'\bTODO\b', r'\bFIXME\b', r'\bDOPLNIT\b',
    r'osobní kapitola', r'redakč', r'editorial', r'rough-draft', r'personal-draft', r'roadmap-draft',
    r'kapitola 37', r'kapitoly 37', r'kap\. 37', r'1–37', r'1-37',
    r'v další kapitole v pořadí', r'budu průběžně', r'budeme průběžně',
]

def strip_frontmatter(s):
    if s.startswith('---\n'):
        end=s.find('\n---\n',4)
        if end!=-1: return s[end+5:]
    return s

def prose(s):
    s=strip_frontmatter(s)
    s=re.sub(r'```.*?```',' ',s,flags=re.S)
    s=re.sub(r'<!--.*?-->',' ',s,flags=re.S)
    s=re.sub(r'!\[[^\]]*\]\([^)]*\)',' ',s)
    s=re.sub(r'https?://\S+',' ',s)
    return s

def paragraphs(s):
    s=prose(s)
    out=[]
    for x in re.split(r'\n\s*\n',s):
        x=' '.join(line.strip() for line in x.splitlines() if line.strip() and not line.startswith('#') and not line.startswith('|---'))
        x=re.sub(r'^[-*]\s+','',x)
        if len(x)>=45: out.append(x)
    return out

all_files=[intro]+chapters+appendices
texts={p: p.read_text(encoding='utf-8') for p in all_files}

# exact paragraph repetition across different files
para_map=defaultdict(list)
for p,s in texts.items():
    for para in paragraphs(s):
        key=re.sub(r'\s+',' ',para).strip()
        if len(key)>=110:
            para_map[key].append(p.name)
repeats=[(k,v) for k,v in para_map.items() if len(set(v))>1]
repeats.sort(key=lambda kv:(-len(set(kv[1])),-len(kv[0])))

# phrase habits
habit_patterns={
    'Například': r'\bNapříklad\b',
    'Prakticky': r'\bPrakticky\b',
    'To je': r'\bTo je\b',
    'Ne.': r'(?m)^Ne\.$',
    'Není': r'\bNení\b',
    'důležité': r'\bdůležit\w*\b',
    'model': r'\bmodel\w*\b',
    'systém': r'\bsystém\w*\b',
    'AI': r'\bAI\b',
}
habits=Counter()
for s in texts.values():
    pp=prose(s)
    for name,pat in habit_patterns.items(): habits[name]+=len(re.findall(pat,pp,re.I if name not in ('AI','Ne.') else 0))

# heading and numeric reference map
chapter_nums={int(p.name[:2]) for p in chapters}
section_ids=set()
for p,s in texts.items():
    for m in re.finditer(r'^#{2,4}\s+(\d+)\.(\d+)\b',s,re.M):
        section_ids.add(f'{m.group(1)}.{m.group(2)}')

crossref_issues=[]
for p,s in texts.items():
    body=prose(s)
    # chapter refs in Czech prose
    for m in re.finditer(r'(?i)\bkapitol(?:a|y|e|u|ou|ách|ami)?\s+(\d{1,2})\b',body):
        n=int(m.group(1))
        if n not in chapter_nums:
            crossref_issues.append((p.name, f'chapter {n}', 'missing chapter'))
    # section refs such as sekci 34.10 / sekce 3.8
    for m in re.finditer(r'(?i)\bsekc(?:e|i|í|emi|ích)\s+(\d{1,2}\.\d{1,2})\b',body):
        sec=m.group(1)
        if sec not in section_ids:
            crossref_issues.append((p.name, f'section {sec}', 'missing section'))

out=[]
out += ['# Raw final editorial scan', '', f'- Numbered chapters: **{len(chapters)}**', f'- Appendices: **{len(appendices)}**', '']
out += ['## Suspicious editorial residues', '']
found=0
for p,s in texts.items():
    for pat in SUSPICIOUS:
        for m in re.finditer(pat,s,re.I):
            line=s[:m.start()].count('\n')+1
            snippet=' '.join(s[m.start():m.start()+160].split())
            out.append(f'- `{p.name}:{line}` — `{snippet}`')
            found+=1
if not found: out.append('- none')

out += ['', '## Numeric cross-reference issues', '']
if crossref_issues:
    for file,ref,reason in crossref_issues:
        out.append(f'- `{file}` — **{ref}** — {reason}')
else:
    out.append('- none')

out += ['', '## Snapshot mentions by file', '']
for p,s in texts.items():
    n=len(re.findall(r'snapshot',s,re.I))
    if n: out.append(f'- `{p.name}` — {n}')

out += ['', '## Chapter openings and endings', '']
for p in chapters:
    s=texts[p]
    h1=re.search(r'^#\s+(.+)$',s,re.M)
    ps=paragraphs(s)
    opening=ps[0][:450] if ps else ''
    ending=ps[-1][-450:] if ps else ''
    h2s=re.findall(r'^##\s+(.+)$',s,re.M)
    out += [f'### {h1.group(1) if h1 else p.stem}', '', f'**Opening:** {opening}', '', f'**Last H2:** {h2s[-1] if h2s else "—"}', '', f'**Ending:** {ending}', '']

out += ['', '## Exact long paragraphs repeated across files', '']
if not repeats: out.append('- none')
for para,files in repeats[:50]:
    out.append(f'- **{len(set(files))} files:** {", ".join(sorted(set(files)))}')
    out.append(f'  - {para[:500]}')

out += ['', '## Recurrent language habits', '']
for k,v in habits.most_common(): out.append(f'- {k}: **{v}**')

out += ['', '## Chapters without expected takeaway heading', '']
for p in chapters:
    s=texts[p]
    if 'Co si z kapitoly odnést' not in s and 'Co si z kapitoly zapamatovat' not in s:
        out.append(f'- `{p.name}`')

out += ['', '## Image counts by chapter', '']
for p in chapters:
    n=len(re.findall(r'!\[[^\]]*\]\([^)]*\)',texts[p]))
    out.append(f'- `{p.name}` — {n}')

out += ['', '## H2 map', '']
for p in chapters:
    h2s=re.findall(r'^##\s+(.+)$',texts[p],re.M)
    out.append(f'### {p.name}')
    out.extend([f'- {h}' for h in h2s])
    out.append('')

(BOOK/'FINAL_EDITORIAL_SCAN_RAW.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
print('chapters',len(chapters),'suspicious',found,'crossrefs',len(crossref_issues),'repeats',len(repeats))
