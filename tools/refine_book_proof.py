from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / 'book'
PROOF = BOOK / 'proof'
HTML_PATH = PROOF / 'AI-book-proof-v0.4.html'
PDF_PATH = PROOF / 'AI-book-proof-v0.4.pdf'

html = HTML_PATH.read_text(encoding='utf-8')

replacements = {
    'body { font-size: 9.7pt; line-height: 1.43; margin: 0; }':
        'body { font-size: 9.5pt; line-height: 1.38; margin: 0; }',
    'h2 { font-size: 14.5pt; line-height: 1.2; margin: 8mm 0 3mm; color: #173d5c; page-break-after: avoid; }':
        'h2 { font-size: 14.5pt; line-height: 1.2; margin: 6mm 0 2.2mm; color: #173d5c; page-break-after: avoid; }',
    'h3 { font-size: 11.6pt; line-height: 1.2; margin: 6mm 0 2mm; color: #264f6b; page-break-after: avoid; }':
        'h3 { font-size: 11.6pt; line-height: 1.2; margin: 4.5mm 0 1.6mm; color: #264f6b; page-break-after: avoid; }',
    'h4 { font-size: 10.2pt; margin: 4mm 0 1.5mm; page-break-after: avoid; }':
        'h4 { font-size: 10.2pt; margin: 3mm 0 1.2mm; page-break-after: avoid; }',
    'p { margin: 0 0 3.1mm; orphans: 3; widows: 3; }':
        'p { margin: 0 0 1.55mm; orphans: 3; widows: 3; }',
    'blockquote { border-left: 1.2mm solid #3e759d; margin: 4mm 0; padding: 2.5mm 4mm; background: #f3f7fa; page-break-inside: avoid; }':
        'blockquote { border-left: 1.2mm solid #3e759d; margin: 2.8mm 0; padding: 2.2mm 3.5mm; background: #f3f7fa; page-break-inside: avoid; }',
    'pre { font-family: "DejaVu Sans Mono", "Liberation Mono", monospace; font-size: 7.8pt; line-height: 1.35; background: #f4f6f8; border: .2mm solid #d9dfe5; padding: 3mm; white-space: pre-wrap; word-break: break-word; page-break-inside: avoid; }':
        'pre { font-family: "DejaVu Sans Mono", "Liberation Mono", monospace; font-size: 7.8pt; line-height: 1.32; background: #f4f6f8; border: .2mm solid #d9dfe5; padding: 2.5mm; white-space: pre-wrap; word-break: break-word; page-break-inside: avoid; }',
    'ul, ol { margin: 1mm 0 3mm 5mm; padding-left: 5mm; }':
        'ul, ol { margin: .8mm 0 2mm 5mm; padding-left: 5mm; }',
    'hr { border: 0; border-top: .2mm solid #d8dee5; margin: 7mm 0; }':
        'hr { border: 0; border-top: .2mm solid #d8dee5; margin: 3.5mm 0; }',
    'img { display: block; max-width: 100%; max-height: 155mm; height: auto; margin: 4mm auto 2mm; page-break-inside: avoid; }':
        'img { display: block; width: 152mm; max-width: none; max-height: 160mm; height: auto; margin: 3.5mm -8mm 2mm; page-break-inside: avoid; }',
}

missing = []
for old, new in replacements.items():
    if old not in html:
        missing.append(old[:60])
    html = html.replace(old, new)

HTML_PATH.write_text(html, encoding='utf-8')
HTML(string=html, base_url=str(BOOK)).write_pdf(str(PDF_PATH))

if missing:
    print('Warning: expected CSS fragments not found:', len(missing))
else:
    print('Proof refinement applied')
