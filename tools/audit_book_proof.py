from __future__ import annotations
from pathlib import Path
import math, re, sys

ROOT=Path(__file__).resolve().parents[1]
BOOK=ROOT/'book'; PROOF=BOOK/'proof'; PDF=PROOF/'AI-book-proof-v0.4.pdf'
try:
    import fitz
    from PIL import Image, ImageOps, ImageDraw
except Exception as exc:
    print('Missing audit dependencies:',exc); sys.exit(2)

if not PDF.exists():
    print('Missing PDF',PDF); sys.exit(3)

doc=fitz.open(PDF)
page_count=len(doc)
page_sizes=[]; empty=[]; outside=[]; min_font=999.0; small_spans=[]; total_words=0

for i,page in enumerate(doc):
    r=page.rect; page_sizes.append((round(r.width,1),round(r.height,1)))
    words=page.get_text('words'); total_words += len(words)
    drawings=len(page.get_drawings()); images=len(page.get_images(full=True))
    if not words and drawings==0 and images==0: empty.append(i+1)
    d=page.get_text('dict')
    for block in d.get('blocks',[]):
        if 'bbox' in block:
            x0,y0,x1,y1=block['bbox']
            if x0 < -0.5 or y0 < -0.5 or x1 > r.width+0.5 or y1 > r.height+0.5:
                outside.append((i+1,tuple(round(x,1) for x in block['bbox'])))
        for line in block.get('lines',[]):
            for span in line.get('spans',[]):
                size=float(span.get('size',0) or 0)
                if size>0:
                    min_font=min(min_font,size)
                    if size<6.5 and span.get('text','').strip():
                        small_spans.append((i+1,round(size,2),span.get('text','')[:60]))

# Page size should be 170 x 240 mm -> approx 481.9 x 680.3 pt.
unique_sizes=sorted(set(page_sizes))
expected=(round(170/25.4*72,1),round(240/25.4*72,1))
size_ok=all(abs(w-expected[0])<1.5 and abs(h-expected[1])<1.5 for w,h in page_sizes)

# Build a contact sheet from distributed samples for human visual review.
PROOF.mkdir(exist_ok=True)
max_samples=20
if page_count<=max_samples:
    samples=list(range(page_count))
else:
    samples=sorted(set(round(i*(page_count-1)/(max_samples-1)) for i in range(max_samples)))
thumbs=[]
for idx in samples:
    page=doc[idx]
    pix=page.get_pixmap(matrix=fitz.Matrix(0.7,0.7),alpha=False)
    im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
    im.thumbnail((260,360))
    canvas=Image.new('RGB',(280,390),'white')
    x=(280-im.width)//2; canvas.paste(im,(x,12))
    dr=ImageDraw.Draw(canvas); dr.text((10,370),f'page {idx+1}',fill='black')
    thumbs.append(canvas)
cols=4; rows=math.ceil(len(thumbs)/cols)
sheet=Image.new('RGB',(cols*280,rows*390),(225,225,225))
for i,im in enumerate(thumbs): sheet.paste(im,((i%cols)*280,(i//cols)*390))
sheet.save(PROOF/'proof-contact-sheet.jpg',quality=88)

blocking=[]
if not size_ok: blocking.append(f'Inconsistent/wrong page size: {unique_sizes}')
if empty: blocking.append(f'Completely empty pages: {empty}')
if outside: blocking.append(f'Text/drawing blocks outside MediaBox: {len(outside)}')
if small_spans: blocking.append(f'Text spans below 6.5 pt: {len(small_spans)}')
if page_count<50: blocking.append(f'Suspiciously low page count: {page_count}')
if total_words<40000: blocking.append(f'Suspiciously low extracted word count: {total_words}')

lines=['# Proof PDF audit','',f'- PDF: `{PDF.name}`',f'- Pages: **{page_count}**',f'- Page size: **{unique_sizes} pt** (target ~{expected[0]} × {expected[1]} pt / 170 × 240 mm)',f'- Extracted word tokens: **{total_words}**',f'- Minimum text span: **{min_font:.2f} pt**',f'- Completely empty pages: **{len(empty)}**',f'- Blocks outside page: **{len(outside)}**',f'- Text spans < 6.5 pt: **{len(small_spans)}**','']
if blocking:
    lines += ['## Automated proof gate: FAIL','']+[f'- {x}' for x in blocking]
else:
    lines += ['## Automated proof gate: PASS','', 'PDF prošlo mechanickou kontrolou. Stále je nutný vizuální proof: především tabulky, page breaks, captions, grayscale/CMYK a fyzická čitelnost na papíře.']
if small_spans:
    lines += ['','## Small-font samples']+[f'- page {p}: {s} pt — `{t}`' for p,s,t in small_spans[:50]]
if outside:
    lines += ['','## Outside-page samples']+[f'- page {p}: {bbox}' for p,bbox in outside[:30]]
lines += ['','## Visual sample','', '`proof-contact-sheet.jpg` obsahuje rovnoměrně rozložené náhledy stránek přes celý rukopis.']
(PROOF/'PROOF_AUDIT.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('pages',page_count,'min_font',min_font,'empty',len(empty),'outside',len(outside),'blocking',len(blocking))
