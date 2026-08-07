from pathlib import Path
from collections import Counter
import fitz

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / 'book' / 'proof' / 'AI-book-proof-v0.4.pdf'
OUT = ROOT / 'book' / 'proof' / 'FINAL_PROOF_QA.md'

doc = fitz.open(PDF)
page_h = doc[0].rect.height if len(doc) else 0
page_w = doc[0].rect.width if len(doc) else 0

sparse = []
orphan_headings = []
margin_risks = []
overlap_risks = []
font_counts = Counter()
min_body = 999.0

for pno, page in enumerate(doc, start=1):
    words = page.get_text('words')
    drawings = page.get_drawings()
    images = page.get_images(full=True)
    text_dict = page.get_text('dict')
    spans = []

    for block in text_dict.get('blocks', []):
        for line in block.get('lines', []):
            for span in line.get('spans', []):
                txt = (span.get('text') or '').strip()
                if not txt:
                    continue
                size = float(span.get('size', 0) or 0)
                font = span.get('font', '')
                bbox = fitz.Rect(span.get('bbox'))
                spans.append((txt, size, font, bbox))
                font_counts[(round(size,2), font)] += 1
                # Ignore running header/footer when estimating body minimum.
                if bbox.y0 > 35 and bbox.y1 < page_h - 30:
                    min_body = min(min_body, size)
                # Safe trim check: anything inside 7 mm from page edge is suspicious,
                # except running header/footer.
                safe = 7 / 25.4 * 72
                if bbox.y0 > 35 and bbox.y1 < page_h - 30:
                    if bbox.x0 < safe or bbox.x1 > page_w - safe:
                        margin_risks.append((pno, round(size,2), txt[:80], tuple(round(v,1) for v in bbox)))

    # Sparse page heuristic: ignore pages with strong visual content.
    if pno > 4 and len(words) < 35 and not images and len(drawings) < 8:
        sparse.append((pno, len(words), len(drawings)))

    # Heading/orphan heuristic: large text very near bottom with no following body line.
    ordered = sorted(spans, key=lambda x: (x[3].y0, x[3].x0))
    for i, (txt, size, font, bbox) in enumerate(ordered):
        if size >= 10.5 and bbox.y0 > page_h * 0.78:
            below = [s for s in ordered[i+1:] if s[3].y0 >= bbox.y1 + 2 and s[3].y0 < page_h - 35]
            if not below:
                orphan_headings.append((pno, round(size,2), txt[:100], round(bbox.y0,1)))

    # Overlap heuristic for visible text spans. Ignore same text and tiny intersections.
    for i in range(len(spans)):
        t1, s1, f1, b1 = spans[i]
        if b1.y0 < 35 or b1.y1 > page_h - 30:
            continue
        for j in range(i+1, min(len(spans), i+80)):
            t2, s2, f2, b2 = spans[j]
            if b2.y0 > b1.y1 + 3:
                break
            inter = b1 & b2
            if inter.is_empty:
                continue
            a1 = max(b1.get_area(), 1)
            a2 = max(b2.get_area(), 1)
            if inter.get_area() / min(a1, a2) > 0.25 and t1 != t2:
                # Adjacent spans on the same baseline can touch by rounding; require real area.
                if inter.width > 1.5 and inter.height > 1.5:
                    overlap_risks.append((pno, t1[:50], t2[:50], tuple(round(v,1) for v in inter)))

# Deduplicate coarse heuristics.
def dedup(rows):
    seen=set(); out=[]
    for r in rows:
        key=r[:3]
        if key not in seen:
            seen.add(key); out.append(r)
    return out

sparse=dedup(sparse)
orphan_headings=dedup(orphan_headings)
margin_risks=dedup(margin_risks)
overlap_risks=dedup(overlap_risks)

lines = [
    '# Final proof QA', '',
    f'- Pages: **{len(doc)}**',
    f'- Minimum non-header/footer text span: **{min_body:.2f} pt**',
    f'- Suspicious sparse pages: **{len(sparse)}**',
    f'- Possible orphan headings: **{len(orphan_headings)}**',
    f'- Text inside 7 mm safety margin: **{len(margin_risks)}**',
    f'- Potential text overlaps: **{len(overlap_risks)}**', '',
]

blocking = []
if margin_risks:
    blocking.append('Text zasahuje do 7mm bezpečnostní zóny.')
if overlap_risks:
    blocking.append('Nalezeny potenciální překryvy textu.')
if orphan_headings:
    blocking.append('Nalezeny možné osiřelé nadpisy na konci strany.')

if blocking:
    lines += ['## Automated layout gate: REVIEW', ''] + [f'- {x}' for x in blocking]
else:
    lines += ['## Automated layout gate: PASS', '', 'Nebyl nalezen mechanický layout blocker.']

if sparse:
    lines += ['', '## Sparse page candidates']
    for r in sparse[:60]: lines.append(f'- page {r[0]}: {r[1]} words, {r[2]} drawings')
if orphan_headings:
    lines += ['', '## Possible orphan headings']
    for r in orphan_headings[:80]: lines.append(f'- page {r[0]}: {r[1]} pt — `{r[2]}` at y={r[3]}')
if margin_risks:
    lines += ['', '## Safety-margin candidates']
    for r in margin_risks[:80]: lines.append(f'- page {r[0]}: {r[1]} pt — `{r[2]}` bbox={r[3]}')
if overlap_risks:
    lines += ['', '## Potential text overlaps']
    for r in overlap_risks[:80]: lines.append(f'- page {r[0]}: `{r[1]}` / `{r[2]}` intersection={r[3]}')

lines += ['', '## Most common text sizes/fonts', '', '| Size | Font | Spans |', '|---:|---|---:|']
for (size,font),count in font_counts.most_common(15):
    lines.append(f'| {size} | {font} | {count} |')

OUT.write_text('\n'.join(lines)+'\n', encoding='utf-8')
print('qa', len(doc), len(sparse), len(orphan_headings), len(margin_risks), len(overlap_risks))
