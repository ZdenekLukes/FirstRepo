from __future__ import annotations

import difflib
import re
from pathlib import Path

ROOTS = {
    "book": Path("book"),
    "book_claude": Path("book_claude"),
    "book_gemini": Path("book_gemini"),
}
OUT = Path("THREE_VERSION_COMPARISON_REPORT_2026-08-07.md")

WORD_RE = re.compile(r"[\wÀ-ž]+(?:[-'’][\wÀ-ž]+)*", re.UNICODE)
CHAPTER_RE = re.compile(r"^(\d{2}) - .*\.md$")
APP_RE = re.compile(r"^([A-G]) - .*\.md$")


def read(path: Path | None) -> str:
    if path is None or not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def body_text(text: str) -> str:
    # Remove YAML front matter only; keep code/examples because they are reader-facing content.
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            text = text[end + 5 :]
    return text


def words(text: str) -> int:
    return len(WORD_RE.findall(body_text(text)))


def placeholder_count(text: str) -> int:
    return text.count("[DOPLNIT") + len(re.findall(r"\bTODO\b", text))


def h1_count(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.startswith("# "))


def h2_count(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.startswith("## "))


def similarity(a: str, b: str) -> float | None:
    if not a or not b:
        return None
    return difflib.SequenceMatcher(None, a.splitlines(), b.splitlines(), autojunk=False).ratio()


def fmt_sim(x: float | None) -> str:
    return "—" if x is None else f"{x*100:.1f}%"


def fmt_delta(base: int, other: int | None) -> str:
    if other is None:
        return "—"
    if base == 0:
        return "—"
    return f"{(other-base)/base*100:+.1f}%"


def chapter_map(root: Path) -> dict[str, Path]:
    out: dict[str, Path] = {}
    for p in root.glob("*.md"):
        m = CHAPTER_RE.match(p.name)
        if m and m.group(1) != "00":
            out[m.group(1)] = p
    return out


def intro_path(root: Path) -> Path | None:
    candidates = sorted(root.glob("00 - Uvod*.md"))
    return candidates[0] if candidates else None


def appendix_map(root: Path) -> dict[str, Path]:
    out: dict[str, Path] = {}
    ad = root / "appendices"
    if not ad.exists():
        return out
    for p in ad.glob("*.md"):
        m = APP_RE.match(p.name)
        if m:
            out[m.group(1)] = p
    return out


def manuscript_texts(root: Path) -> list[str]:
    cm = chapter_map(root)
    am = appendix_map(root)
    parts = [read(cm[k]) for k in sorted(cm)] + [read(am[k]) for k in sorted(am)]
    ip = intro_path(root)
    if ip:
        parts.insert(0, read(ip))
    return parts


def unique_top_level_markdown(root: Path) -> list[str]:
    standard = {"00 - INDEX.md", "BIBLIOGRAPHY.md", "STYLE_GUIDE.md", "PRINT_VISUAL_GUIDE.md"}
    names = []
    for p in root.glob("*.md"):
        if CHAPTER_RE.match(p.name) or p.name in standard or p.name.startswith("00 - Uvod"):
            continue
        names.append(p.name)
    return sorted(names)


maps = {name: chapter_map(root) for name, root in ROOTS.items()}
apps = {name: appendix_map(root) for name, root in ROOTS.items()}

lines: list[str] = []
lines.append("# Porovnání tří verzí knihy — automatická datová část")
lines.append("")
lines.append("> Tato část je generovaná přímo z adresářů `book/`, `book_claude/` a `book_gemini/`. Kvalitativní adjudikace je doplněna redakčně po tomto měření.")
lines.append("")
lines.append("## 1. Souhrn")
lines.append("")
lines.append("| Metrika | book | book_claude | book_gemini |")
lines.append("|---|---:|---:|---:|")
for metric in ["numbered", "appendices", "intro", "words", "placeholders", "h1", "h2"]:
    vals = []
    for name, root in ROOTS.items():
        texts = manuscript_texts(root)
        if metric == "numbered":
            v = len(maps[name])
        elif metric == "appendices":
            v = len(apps[name])
        elif metric == "intro":
            v = "ano" if intro_path(root) else "ne"
        elif metric == "words":
            v = sum(words(t) for t in texts)
        elif metric == "placeholders":
            v = sum(placeholder_count(t) for t in texts)
        elif metric == "h1":
            v = sum(h1_count(t) for t in texts)
        else:
            v = sum(h2_count(t) for t in texts)
        vals.append(v)
    label = {
        "numbered": "Číslované kapitoly jako samostatné soubory",
        "appendices": "Přílohy A–G",
        "intro": "Samostatný úvod",
        "words": "Slova: kapitoly + přílohy + případný úvod",
        "placeholders": "[DOPLNIT]/TODO v rukopisu",
        "h1": "H1 nadpisy v rukopisu",
        "h2": "H2 nadpisy v rukopisu",
    }[metric]
    lines.append(f"| {label} | {vals[0]} | {vals[1]} | {vals[2]} |")

lines.append("")
lines.append("## 2. Strukturální rozdíly")
lines.append("")
all_ch = [f"{i:02d}" for i in range(1, 38)]
for name in ROOTS:
    missing = [k for k in all_ch if k not in maps[name]]
    lines.append(f"- **{name}:** chybějící samostatné číslované kapitoly: {', '.join(missing) if missing else 'žádné'}.")
    ip = intro_path(ROOTS[name])
    lines.append(f"  - samostatný úvod: `{ip.name}`" if ip else "  - samostatný úvod: ne")
    uniq = unique_top_level_markdown(ROOTS[name])
    if uniq:
        lines.append(f"  - review/audit dokumenty navíc: {', '.join(f'`{x}`' for x in uniq)}")

lines.append("")
lines.append("## 3. Kapitoly — word count, změna a podobnost proti `book/`")
lines.append("")
lines.append("| Kap. | book slova | Claude slova | Claude Δ | Claude podobnost | Gemini slova | Gemini Δ | Gemini podobnost |")
lines.append("|---:|---:|---:|---:|---:|---:|---:|---:|")
for k in all_ch:
    b = read(maps["book"].get(k))
    c_path = maps["book_claude"].get(k)
    g_path = maps["book_gemini"].get(k)
    c = read(c_path)
    g = read(g_path)
    bw = words(b)
    cw = words(c) if c_path else None
    gw = words(g) if g_path else None
    lines.append(
        f"| {int(k)} | {bw} | {cw if cw is not None else '—'} | {fmt_delta(bw,cw)} | {fmt_sim(similarity(b,c))} | "
        f"{gw if gw is not None else '—'} | {fmt_delta(bw,gw)} | {fmt_sim(similarity(b,g))} |"
    )

lines.append("")
lines.append("## 4. Přílohy — word count a podobnost")
lines.append("")
lines.append("| Příloha | book | Claude | Claude podobnost | Gemini | Gemini podobnost |")
lines.append("|---|---:|---:|---:|---:|---:|")
for k in "ABCDEFG":
    b = read(apps["book"].get(k))
    c = read(apps["book_claude"].get(k))
    g = read(apps["book_gemini"].get(k))
    lines.append(f"| {k} | {words(b)} | {words(c)} | {fmt_sim(similarity(b,c))} | {words(g)} | {fmt_sim(similarity(b,g))} |")

lines.append("")
lines.append("## 5. Klíčové strukturální clustery")
lines.append("")
lines.append("| Cluster | book slova | Claude slova | Gemini slova | Poznámka |")
lines.append("|---|---:|---:|---:|---|")
clusters = [
    ("16+17 agent + loop", ["16","17"], "Gemini slučuje do 16"),
    ("22+26 enterprise + web chat", ["22","26"], "Gemini ruší 26 a přesouvá jádro do 22"),
    ("35+37 roadmap + projekty", ["35","37"], "Claude zásadně zkracuje 35"),
    ("01 historie", ["01"], "Claude zkracuje; Gemini technicky opravuje"),
    ("11 bridge k RAG", ["11"], "Oba reviewery zkracují jinak"),
]
for label, keys, note in clusters:
    vals=[]
    for name in ROOTS:
        vals.append(sum(words(read(maps[name].get(k))) for k in keys if maps[name].get(k)))
    lines.append(f"| {label} | {vals[0]} | {vals[1]} | {vals[2]} | {note} |")

lines.append("")
lines.append("## 6. Které kapitoly mění který reviewer")
lines.append("")
for reviewer in ["book_claude", "book_gemini"]:
    same=[]; changed=[]; missing=[]
    for k in all_ch:
        bp=maps["book"].get(k); rp=maps[reviewer].get(k)
        if not rp:
            missing.append(k); continue
        if read(bp)==read(rp): same.append(k)
        else: changed.append(k)
    lines.append(f"### {reviewer}")
    lines.append(f"- beze změny proti `book/`: {', '.join(str(int(x)) for x in same) if same else 'žádné'}")
    lines.append(f"- změněné: {', '.join(str(int(x)) for x in changed) if changed else 'žádné'}")
    lines.append(f"- odstraněné jako samostatný soubor: {', '.join(str(int(x)) for x in missing) if missing else 'žádné'}")
    lines.append("")

lines.append("## 7. Placeholder audit")
lines.append("")
for name, root in ROOTS.items():
    hits=[]
    for p in list(maps[name].values()) + list(apps[name].values()):
        t=read(p); n=placeholder_count(t)
        if n: hits.append(f"`{p.relative_to(root)}` ({n})")
    lines.append(f"- **{name}:** {', '.join(hits) if hits else '0'}")

lines.append("")
lines.append("## 8. Redakční adjudikace")
lines.append("")
lines.append("> Doplněno po ručním čtení rozdílů a případném externím fact-checku. Automatická čísla výše nejsou sama o sobě doporučením, která verze je lepší.")

OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"wrote {OUT}")
