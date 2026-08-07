from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / 'book'
DATE = '2026-08-07'

# Conservative replacements only. English terms that are intentional in the
# style guide (workflow, use-case, reasoning, RAG, tool use, etc.) are retained.
REPLACEMENTS = [
    ('Simulator je deterministický model reality.', 'Simulátor poskytuje externě ověřitelný výsledek podle definovaného modelu a jeho předpokladů.'),
    ('zhoršit relevance', 'zhoršit relevanci'),
    ('zvýšit relevance', 'zvýšit relevanci'),
    ('v contextu', 'v kontextu'),
    ('do contextu', 'do kontextu'),
    ('z contextu', 'z kontextu'),
    ('dlouhý context', 'dlouhý kontext'),
    ('velký context', 'velký kontext'),
    ('celý context', 'celý kontext'),
    ('contextem', 'kontextem'),
    ('contextu', 'kontextu'),
    ('contexty', 'kontexty'),
    ('Local inference', 'Lokální inference'),
    ('local AI', 'lokální AI'),
    ('local models', 'lokální modely'),
    ('local modely', 'lokální modely'),
    ('local model', 'lokální model'),
    ('permissions model', 'model oprávnění'),
    ('permissions rules', 'pravidla oprávnění'),
    ('permissions', 'oprávnění'),
    ('verification', 'verifikace'),
    ('simulation results', 'výsledky simulace'),
]

counts = {old: 0 for old, _ in REPLACEMENTS}


def transform_prose(text: str) -> str:
    # Preserve fenced examples/code exactly; terminology there may intentionally
    # mirror APIs, logs or English system labels.
    parts = re.split(r'(```.*?```)', text, flags=re.S)
    for i in range(0, len(parts), 2):
        chunk = parts[i]
        for old, new in REPLACEMENTS:
            n = chunk.count(old)
            if n:
                counts[old] += n
                chunk = chunk.replace(old, new)
        parts[i] = chunk
    return ''.join(parts)

chapters = sorted([p for p in BOOK.glob('[0-9][0-9] - *.md') if p.name != '00 - INDEX.md'])
for p in chapters:
    text = p.read_text(encoding='utf-8')
    text = transform_prose(text)
    if text.startswith('---\n'):
        text = re.sub(r'^status:\s*.*$', 'status: final-draft', text, count=1, flags=re.M)
    p.write_text(text, encoding='utf-8')

appendices = sorted((BOOK / 'appendices').glob('*.md'))
for p in appendices:
    text = transform_prose(p.read_text(encoding='utf-8'))
    if not text.startswith('---\n'):
        m = re.search(r'^#\s+(.+)$', text, re.M)
        title = m.group(1).strip() if m else p.stem
        title_yaml = title.replace('"', '\\"')
        fm = (
            '---\n'
            f'title: "{title_yaml}"\n'
            'part: "PŘÍLOHY"\n'
            'status: final-draft\n'
            'version: "0.4"\n'
            f'updated: {DATE}\n'
            '---\n\n'
        )
        text = fm + text
    else:
        text = re.sub(r'^status:\s*.*$', 'status: final-draft', text, count=1, flags=re.M)
    p.write_text(text, encoding='utf-8')

# Bibliography is reader-facing in the release candidate.
biblio = BOOK / 'BIBLIOGRAPHY.md'
if biblio.exists():
    b = biblio.read_text(encoding='utf-8')
    b = b.replace('# BIBLIOGRAPHY — primární zdroje a další čtení', '# Zdroje a další čtení', 1)
    biblio.write_text(b, encoding='utf-8')

# Index becomes the release-candidate master and exposes bibliography as content,
# while keeping editorial-only files in their own section.
index = BOOK / '00 - INDEX.md'
t = index.read_text(encoding='utf-8')
if t.startswith('---\n'):
    t = re.sub(r'^status:\s*.*$', 'status: release-candidate', t, count=1, flags=re.M)
if '## ZDROJE A DALŠÍ ČTENÍ' not in t:
    marker = '\n\n## REDAKČNÍ PODKLADY'
    section = '\n\n## ZDROJE A DALŠÍ ČTENÍ\n- [[BIBLIOGRAPHY|Zdroje a další čtení]]'
    if marker in t:
        t = t.replace(marker, section + marker, 1)
    else:
        t += section + '\n'
index.write_text(t, encoding='utf-8')

readme = ROOT / 'README.md'
if readme.exists():
    r = readme.read_text(encoding='utf-8')
    r = r.replace('Stav: **finální redakční draft před sazbou**', 'Stav: **release candidate po redakční a proof kontrole**')
    r = r.replace('Aktuální pracovní verze knihy: **0.4 final-editorial-draft**', 'Aktuální pracovní verze knihy: **0.4 release-candidate**')
    readme.write_text(r, encoding='utf-8')

report = [
    '# Final copyedit report', '',
    f'- Chapters normalized to `final-draft`: **{len(chapters)}**',
    f'- Appendices normalized to `final-draft`: **{len(appendices)}**',
    '- Index status: **release-candidate**', '',
    '## Conservative terminology / grammar replacements', '',
    '| Original | Replacement | Count |',
    '|---|---|---:|',
]
for old, new in REPLACEMENTS:
    report.append(f'| `{old}` | `{new}` | {counts[old]} |')
report += ['', '> Deliberately retained English technical terms follow `STYLE_GUIDE.md`; this pass does not blindly translate APIs, code examples or standard names.']
(BOOK / 'FINAL_COPYEDIT_REPORT.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
print('copyedit', len(chapters), len(appendices), sum(counts.values()))
