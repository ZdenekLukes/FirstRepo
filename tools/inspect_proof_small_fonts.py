from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / 'book' / 'proof' / 'AI-book-proof-v0.4.pdf'
OUT = ROOT / 'book' / 'proof' / 'SMALL_FONT_INSPECTION.md'

doc = fitz.open(PDF)
rows = []
for pno, page in enumerate(doc, start=1):
    data = page.get_text('dict')
    for block in data.get('blocks', []):
        for line in block.get('lines', []):
            for span in line.get('spans', []):
                text = (span.get('text') or '').strip()
                size = float(span.get('size', 0) or 0)
                if text and 0 < size < 7.5:
                    rows.append((pno, round(size,2), span.get('font',''), text[:120], tuple(round(v,1) for v in span.get('bbox',(0,0,0,0)))))

lines = ['# Small-font inspection', '', f'- Spans below 7.5 pt: **{len(rows)}**', '']
if rows:
    lines += ['| Page | Size | Font | Text | BBox |', '|---:|---:|---|---|---|']
    for p,s,f,t,b in rows[:300]:
        t=t.replace('|','\\|')
        lines.append(f'| {p} | {s} | {f} | {t} | `{b}` |')
else:
    lines.append('No spans below 7.5 pt.')
OUT.write_text('\n'.join(lines)+'\n', encoding='utf-8')
print('small spans', len(rows))
