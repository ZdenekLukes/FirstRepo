from pathlib import Path
import re
import html as htmlmod
import markdown

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / 'book'
HTML_PATH = BOOK / 'proof' / 'AI-book-proof-v0.4.html'
BIB = BOOK / 'BIBLIOGRAPHY.md'

html = HTML_PATH.read_text(encoding='utf-8')
text = BIB.read_text(encoding='utf-8')
text = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.S)
body = markdown.markdown(text, extensions=['extra','tables','fenced_code','toc','sane_lists'])
section = f'<section class="chapter" id="bibliography">{body}</section>'

# Build script is recreated on every proof run, so duplicate protection is only
# defensive for manual invocation.
if 'id="bibliography"' not in html:
    html = html.replace('</body></html>', section + '\n</body></html>', 1)

    toc_close = '</ol></section>'
    toc_item = '<li><a href="#bibliography">Zdroje a další čtení</a></li>'
    if toc_close in html:
        html = html.replace(toc_close, toc_item + toc_close, 1)

HTML_PATH.write_text(html, encoding='utf-8')
print('bibliography included')
