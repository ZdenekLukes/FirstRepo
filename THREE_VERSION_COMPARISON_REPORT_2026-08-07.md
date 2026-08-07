# Porovnání tří verzí knihy — automatická datová část

> Tato část je generovaná přímo z adresářů `book/`, `book_claude/` a `book_gemini/`. Kvalitativní adjudikace je doplněna redakčně po tomto měření.

## 1. Souhrn

| Metrika | book | book_claude | book_gemini |
|---|---:|---:|---:|
| Číslované kapitoly jako samostatné soubory | 37 | 37 | 35 |
| Přílohy A–G | 7 | 7 | 7 |
| Samostatný úvod | ne | ano | ne |
| Slova: kapitoly + přílohy + případný úvod | 63659 | 63481 | 62727 |
| [DOPLNIT]/TODO v rukopisu | 0 | 7 | 0 |
| H1 nadpisy v rukopisu | 121 | 46 | 110 |
| H2 nadpisy v rukopisu | 560 | 623 | 544 |

## 2. Strukturální rozdíly

- **book:** chybějící samostatné číslované kapitoly: žádné.
  - samostatný úvod: ne
  - review/audit dokumenty navíc: `EDITORIAL_STYLE_AUDIT.md`, `FINAL_COPYEDIT_REPORT.md`, `FINAL_EDITORIAL_AUDIT_2026-08-07.md`, `PREPRESS_AUTOMATED_AUDIT.md`, `VISUAL_AUDIT.md`
- **book_claude:** chybějící samostatné číslované kapitoly: žádné.
  - samostatný úvod: `00 - Uvod - Jak cist tuto knihu.md`
  - review/audit dokumenty navíc: `REVIEW_CHANGELOG.md`, `REVIEW_REPORT.md`
- **book_gemini:** chybějící samostatné číslované kapitoly: 17, 26.
  - samostatný úvod: ne
  - review/audit dokumenty navíc: `EDITORIAL_STYLE_AUDIT.md`, `FINAL_COPYEDIT_REPORT.md`, `FINAL_EDITORIAL_AUDIT_2026-08-07.md`, `GEMINI_REVIEW_IMPLEMENTATION.md`, `PREPRESS_AUTOMATED_AUDIT.md`, `README.md`, `VISUAL_AUDIT.md`

## 3. Kapitoly — word count, změna a podobnost proti `book/`

| Kap. | book slova | Claude slova | Claude Δ | Claude podobnost | Gemini slova | Gemini Δ | Gemini podobnost |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 4138 | 3448 | -16.7% | 78.6% | 4216 | +1.9% | 97.3% |
| 2 | 2087 | 2087 | +0.0% | 100.0% | 2087 | +0.0% | 100.0% |
| 3 | 2901 | 2848 | -1.8% | 97.9% | 3049 | +5.1% | 99.0% |
| 4 | 2361 | 2366 | +0.2% | 98.4% | 2361 | +0.0% | 100.0% |
| 5 | 2379 | 2376 | -0.1% | 98.3% | 2512 | +5.6% | 96.4% |
| 6 | 1749 | 1751 | +0.1% | 99.5% | 1749 | +0.0% | 100.0% |
| 7 | 1435 | 1435 | +0.0% | 99.7% | 1435 | +0.0% | 100.0% |
| 8 | 2095 | 2109 | +0.7% | 96.9% | 2235 | +6.7% | 99.0% |
| 9 | 1434 | 1625 | +13.3% | 97.4% | 1570 | +9.5% | 97.3% |
| 10 | 1315 | 1308 | -0.5% | 97.5% | 1315 | +0.0% | 100.0% |
| 11 | 740 | 626 | -15.4% | 23.7% | 427 | -42.3% | 23.5% |
| 12 | 1781 | 1781 | +0.0% | 99.8% | 1895 | +6.4% | 99.0% |
| 13 | 1475 | 1475 | +0.0% | 99.7% | 1475 | +0.0% | 100.0% |
| 14 | 1290 | 1315 | +1.9% | 99.5% | 1290 | +0.0% | 100.0% |
| 15 | 1723 | 1727 | +0.2% | 98.1% | 1861 | +8.0% | 98.6% |
| 16 | 1120 | 1120 | +0.0% | 99.7% | 1002 | -10.5% | 16.2% |
| 17 | 1206 | 1206 | +0.0% | 99.7% | — | — | — |
| 18 | 1252 | 1511 | +20.7% | 95.2% | 1252 | +0.0% | 100.0% |
| 19 | 1529 | 1529 | +0.0% | 99.7% | 1529 | +0.0% | 100.0% |
| 20 | 1321 | 1321 | +0.0% | 99.7% | 1321 | +0.0% | 100.0% |
| 21 | 1305 | 1305 | +0.0% | 99.7% | 1305 | +0.0% | 100.0% |
| 22 | 1417 | 1417 | +0.0% | 99.7% | 1784 | +25.9% | 92.8% |
| 23 | 1150 | 1161 | +1.0% | 99.5% | 1150 | +0.0% | 100.0% |
| 24 | 1955 | 1955 | +0.0% | 99.8% | 1955 | +0.0% | 100.0% |
| 25 | 2513 | 2525 | +0.5% | 98.3% | 2605 | +3.7% | 99.0% |
| 26 | 1088 | 1087 | -0.1% | 96.4% | — | — | — |
| 27 | 1055 | 1057 | +0.2% | 98.0% | 1055 | +0.0% | 100.0% |
| 28 | 947 | 947 | +0.0% | 99.3% | 947 | +0.0% | 100.0% |
| 29 | 1048 | 1069 | +2.0% | 99.4% | 1048 | +0.0% | 100.0% |
| 30 | 1242 | 1242 | +0.0% | 99.6% | 1242 | +0.0% | 100.0% |
| 31 | 1141 | 1141 | +0.0% | 99.5% | 1307 | +14.5% | 93.4% |
| 32 | 1140 | 1140 | +0.0% | 99.6% | 1415 | +24.1% | 92.7% |
| 33 | 1435 | 1435 | +0.0% | 99.7% | 1435 | +0.0% | 100.0% |
| 34 | 1591 | 1595 | +0.3% | 97.7% | 1591 | +0.0% | 100.0% |
| 35 | 1097 | 383 | -65.1% | 20.7% | 1097 | +0.0% | 100.0% |
| 36 | 1409 | 1409 | +0.0% | 99.4% | 1409 | +0.0% | 100.0% |
| 37 | 1645 | 1645 | +0.0% | 99.5% | 1645 | +0.0% | 100.0% |

## 4. Přílohy — word count a podobnost

| Příloha | book | Claude | Claude podobnost | Gemini | Gemini podobnost |
|---|---:|---:|---:|---:|---:|
| A | 920 | 920 | 100.0% | 920 | 100.0% |
| B | 603 | 614 | 97.0% | 606 | 99.0% |
| C | 624 | 624 | 100.0% | 627 | 99.6% |
| D | 990 | 990 | 100.0% | 990 | 100.0% |
| E | 828 | 828 | 100.0% | 828 | 100.0% |
| F | 701 | 701 | 100.0% | 701 | 100.0% |
| G | 484 | 725 | 89.9% | 484 | 100.0% |

## 5. Klíčové strukturální clustery

| Cluster | book slova | Claude slova | Gemini slova | Poznámka |
|---|---:|---:|---:|---|
| 16+17 agent + loop | 2326 | 2326 | 1002 | Gemini slučuje do 16 |
| 22+26 enterprise + web chat | 2505 | 2504 | 1784 | Gemini ruší 26 a přesouvá jádro do 22 |
| 35+37 roadmap + projekty | 2742 | 2028 | 2742 | Claude zásadně zkracuje 35 |
| 01 historie | 4138 | 3448 | 4216 | Claude zkracuje; Gemini technicky opravuje |
| 11 bridge k RAG | 740 | 626 | 427 | Oba reviewery zkracují jinak |

## 6. Které kapitoly mění který reviewer

### book_claude
- beze změny proti `book/`: 2
- změněné: 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37
- odstraněné jako samostatný soubor: žádné

### book_gemini
- beze změny proti `book/`: 2, 4, 6, 7, 10, 13, 14, 18, 19, 20, 21, 23, 24, 27, 28, 29, 30, 33, 34, 35, 36, 37
- změněné: 1, 3, 5, 8, 9, 11, 12, 15, 16, 22, 25, 31, 32
- odstraněné jako samostatný soubor: 17, 26

## 7. Placeholder audit

- **book:** 0
- **book_claude:** `appendices/G - Vlastni experimenty.md` (7)
- **book_gemini:** 0

## 8. Redakční adjudikace

> Doplněno po ručním čtení rozdílů a případném externím fact-checku. Automatická čísla výše nejsou sama o sobě doporučením, která verze je lepší.
