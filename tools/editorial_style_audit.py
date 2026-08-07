from pathlib import Path
import re
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
BOOK=ROOT/'book'
chapters=sorted(BOOK.glob('[0-9][0-9] - *.md'))
chapters=[p for p in chapters if not p.name.startswith('00 - ')]

terms={
'context': [r'\bcontext\b',r'\bkontext\w*'],
'tool': [r'\btools?\b',r'\bnástroj\w*'],
'workflow': [r'\bworkflows?\b',r'\bpracovní\s+postup\w*'],
'use-case': [r'\buse[- ]cases?\b',r'\bpřípad\w*\s+použití\b'],
'local': [r'\blocal\b',r'\blokální\w*'],
'memory': [r'\bmemory\b',r'\bpaměť\w*'],
'knowledge base': [r'\bknowledge\s+base\b',r'\bznalostní\s+báz\w*'],
'reasoning': [r'\breasoning\b',r'\buvažován\w*'],
'permissions': [r'\bpermissions?\b',r'\boprávnění\w*'],
'verification': [r'\bverification\b|\bverifier\w*',r'\bověřen\w*|\bverifik\w*'],
'simulation': [r'\bsimulation\w*|\bsimulator\w*',r'\bsimulac\w*|\bsimulátor\w*'],
}

alltext='\n'.join(p.read_text(encoding='utf-8') for p in chapters)
out=['# Redakční style audit','', '> Automatická kontrola konzistence struktury a terminologie.','', '## Struktura kapitol','', '| Kapitola | metadata | takeaway | návaznost | obrázky |','|---|---|---|---|---:|']
for p in chapters:
    t=p.read_text(encoding='utf-8')
    metadata='ano' if t.startswith('---\n') else 'NE'
    take='ano' if re.search(r'^#\s+Co si z kapitoly odnést',t,re.M) else 'NE'
    trans='ano' if re.search(r'(další|následující)\s+kapitol',t,re.I) else 'NE'
    imgs=len(re.findall(r'!\[[^\]]*\]\([^)]*\)',t))
    out.append(f'| {p.name} | {metadata} | {take} | {trans} | {imgs} |')
out += ['','## Terminologické varianty','','Počty jsou orientační a zahrnují i kódové příklady. Ukazují, kde je potřeba redakční style sheet.','','| Koncept | anglická forma | česká forma |','|---|---:|---:|']
for name,(en,cz) in terms.items():
    ec=len(re.findall(en,alltext,re.I)); cc=len(re.findall(cz,alltext,re.I)); out.append(f'| {name} | {ec} | {cc} |')

out += ['','## Vizuální jazyk','','| Kapitola | caption `*Obrázek:` |','|---|---:|']
for p in chapters:
    t=p.read_text(encoding='utf-8'); out.append(f'| {p.name} | {len(re.findall(r"\*Obrázek:",t))} |')

(BOOK/'EDITORIAL_STYLE_AUDIT.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
