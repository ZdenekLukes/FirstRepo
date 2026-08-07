from pathlib import Path

BOOK=Path('book_final')

def chapter(n):
    xs=sorted(BOOK.glob(f'{n:02d} - *.md'))
    if len(xs)!=1: raise SystemExit(f'chapter {n}: {xs}')
    return xs[0]

def patch(n, old, new):
    p=chapter(n); s=p.read_text(encoding='utf-8')
    if old not in s:
        print(f'already absent: ch{n}: {old[:40]}')
        return
    p.write_text(s.replace(old,new),encoding='utf-8')

# Chapter endings must land on the chapter's thesis/bridge, not housekeeping.
patch(5,'\n\n*Primární zdroje pro tento snapshot jsou soustředěné v příloze B a v bibliografii.*\n','\n')
patch(15,'\n\n*Primární MCP specifikace a dokumentace použitá pro snapshot 08/2026 jsou uvedené v bibliografii.*\n','\n')
patch(24,'\n\n*Primární bezpečnostní, regulatorní a OWASP zdroje jsou soustředěné v bibliografii.*\n','\n')
patch(35,'\n\n*Aktuální odkazy na runtime, frameworky a observability nástroje jsou soustředěné v bibliografii a příloze C.*\n','\n')

patch(16,
      'V další kapitole v pořadí přejdeme od anatomie k receptu: **jak postavit prvního jednoduchého agenta tak, aby byl užitečný, měřitelný a bezpečný.**',
      'Teď můžeme přejít od anatomie k receptu: **jak postavit prvního jednoduchého agenta tak, aby byl užitečný, měřitelný a bezpečný.**')

# Qualitative scan should not flag ordinary Czech verb "doplnit"; mechanical
# placeholder detection is already covered by source/prepress QA.
p=Path('tools/final_editorial_award_scan.py')
s=p.read_text(encoding='utf-8')
s=s.replace(" r'\\bDOPLNIT\\b',","")
p.write_text(s,encoding='utf-8')

print('micro-polish applied')
