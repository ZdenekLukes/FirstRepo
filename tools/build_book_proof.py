from __future__ import annotations
from pathlib import Path
import html, re, sys

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / 'book'
OUT = BOOK / 'proof'
OUT.mkdir(parents=True, exist_ok=True)

try:
    import markdown
    from weasyprint import HTML
except Exception as exc:
    print('Missing build dependencies:', exc)
    sys.exit(2)

chapters = sorted([p for p in BOOK.glob('[0-9][0-9] - *.md') if p.name != '00 - INDEX.md'])
appendices = sorted((BOOK / 'appendices').glob('*.md'))


def strip_frontmatter(text: str) -> str:
    if text.startswith('---\n'):
        end = text.find('\n---\n', 4)
        if end >= 0:
            return text[end+5:]
    return text


def first_h1(text: str, fallback: str) -> str:
    m = re.search(r'^#\s+(.+)$', text, re.M)
    return m.group(1).strip() if m else fallback


def slug(s: str) -> str:
    s = s.lower()
    repl = {'á':'a','č':'c','ď':'d','é':'e','ě':'e','í':'i','ň':'n','ó':'o','ř':'r','š':'s','ť':'t','ú':'u','ů':'u','ý':'y','ž':'z'}
    for a,b in repl.items(): s=s.replace(a,b)
    s = re.sub(r'[^a-z0-9]+','-',s).strip('-')
    return s


def md_to_html(path: Path, ident: str) -> tuple[str,str]:
    text = strip_frontmatter(path.read_text(encoding='utf-8'))
    title = first_h1(text, path.stem)
    # Use print-first diagrams for proof PDF.
    text = text.replace('assets/diagrams/', 'assets/diagrams-print/')
    # Remove visual generator markers from typeset output.
    text = re.sub(r'<!--\s*visual:[^>]+-->', '', text)
    body = markdown.markdown(text, extensions=['extra','tables','fenced_code','toc','sane_lists'])
    return title, f'<section class="chapter" id="{ident}">{body}</section>'

items=[]; sections=[]
for p in chapters:
    ident='ch-'+p.name[:2]
    title, section=md_to_html(p, ident)
    items.append((title, ident, 'chapter'))
    sections.append(section)
for idx,p in enumerate(appendices):
    ident='app-'+chr(ord('a')+idx)
    title, section=md_to_html(p, ident)
    items.append((title, ident, 'appendix'))
    sections.append(section)

# 170 x 240 mm gives technical material more width than A5 while remaining book-like.
css = r'''
@page {
  size: 170mm 240mm;
  margin: 17mm 16mm 19mm 18mm;
  @bottom-center { content: counter(page); font-size: 8pt; color: #586174; }
  @top-center { content: string(chapter-title); font-size: 7.4pt; color: #687386; }
}
@page:first { @top-center { content: none; } @bottom-center { content: none; } }
html { font-family: "DejaVu Sans", "Liberation Sans", sans-serif; color: #17202b; }
body { font-size: 9.7pt; line-height: 1.43; margin: 0; }
.title-page { page-break-after: always; min-height: 195mm; display: flex; flex-direction: column; justify-content: center; }
.title-page h1 { font-size: 28pt; line-height: 1.1; margin: 0 0 8mm; color: #10263b; }
.title-page .subtitle { font-size: 14pt; line-height: 1.35; color: #43566a; max-width: 120mm; }
.title-page .meta { margin-top: 20mm; font-size: 9pt; color: #687386; }
.toc { page-break-after: always; }
.toc h1 { font-size: 22pt; }
.toc ol { list-style: none; padding: 0; margin: 0; }
.toc li { border-bottom: .2mm solid #dfe4ea; padding: 2.2mm 0; }
.toc a { color: #17202b; text-decoration: none; }
.toc .part { margin-top: 5mm; font-size: 8pt; color: #687386; text-transform: uppercase; letter-spacing: .05em; }
.chapter { page-break-before: always; }
h1 { string-set: chapter-title content(); font-size: 21pt; line-height: 1.15; margin: 0 0 7mm; color: #0e2a43; page-break-after: avoid; }
h2 { font-size: 14.5pt; line-height: 1.2; margin: 8mm 0 3mm; color: #173d5c; page-break-after: avoid; }
h3 { font-size: 11.6pt; line-height: 1.2; margin: 6mm 0 2mm; color: #264f6b; page-break-after: avoid; }
h4 { font-size: 10.2pt; margin: 4mm 0 1.5mm; page-break-after: avoid; }
p { margin: 0 0 3.1mm; orphans: 3; widows: 3; }
blockquote { border-left: 1.2mm solid #3e759d; margin: 4mm 0; padding: 2.5mm 4mm; background: #f3f7fa; page-break-inside: avoid; }
blockquote p:last-child { margin-bottom: 0; }
strong { color: #102f47; }
pre { font-family: "DejaVu Sans Mono", "Liberation Mono", monospace; font-size: 7.8pt; line-height: 1.35; background: #f4f6f8; border: .2mm solid #d9dfe5; padding: 3mm; white-space: pre-wrap; word-break: break-word; page-break-inside: avoid; }
code { font-family: "DejaVu Sans Mono", "Liberation Mono", monospace; font-size: .92em; }
table { width: 100%; border-collapse: collapse; font-size: 7.7pt; line-height: 1.28; margin: 4mm 0 5mm; page-break-inside: avoid; }
th { background: #e9f0f5; color: #173d5c; font-weight: 700; }
th, td { border: .2mm solid #cfd7df; padding: 1.6mm 1.8mm; vertical-align: top; }
ul, ol { margin: 1mm 0 3mm 5mm; padding-left: 5mm; }
li { margin-bottom: 1mm; }
img { display: block; max-width: 100%; max-height: 155mm; height: auto; margin: 4mm auto 2mm; page-break-inside: avoid; }
p:has(> img) { page-break-inside: avoid; margin-bottom: 1mm; }
p:has(> img) + p em { font-size: 8pt; color: #586174; }
hr { border: 0; border-top: .2mm solid #d8dee5; margin: 7mm 0; }
a { color: #245d84; text-decoration: none; overflow-wrap: anywhere; }
/* Keep compact takeaway lists together when possible, but permit long sections to flow. */
h1 + p, h2 + p, h3 + p { page-break-before: avoid; }
'''

toc=[]
for title, ident, kind in items:
    cls=' class="part"' if kind=='appendix' and not any('PŘÍLOHY' in x for x in toc) else ''
    toc.append(f'<li><a href="#{ident}">{html.escape(title)}</a></li>')

doc = f'''<!doctype html>
<html lang="cs"><head><meta charset="utf-8"><title>AI od základů k agentním systémům - proof v0.4</title><style>{css}</style></head>
<body>
<section class="title-page">
  <h1>AI od základů k agentním systémům</h1>
  <div class="subtitle">Co jsem se zatím naučil, jak AI chápu v srpnu 2026 a co mě ještě čeká</div>
  <div class="meta">Proof v0.4 · 7. 8. 2026 · pracovní předtisková sazba 170 × 240 mm</div>
</section>
<section class="toc"><h1>Obsah</h1><ol>{''.join(toc)}</ol></section>
{''.join(sections)}
</body></html>'''

html_path = OUT / 'AI-book-proof-v0.4.html'
pdf_path = OUT / 'AI-book-proof-v0.4.pdf'
html_path.write_text(doc, encoding='utf-8')
HTML(string=doc, base_url=str(BOOK)).write_pdf(str(pdf_path))
print(pdf_path)
