# Externí peer review — Claude + Gemini

Tento adresář je určen pro poslední nezávislé review knihy před finálním designem a tiskovou produkcí.

## Vstup pro oba modely

Nahraj stejný soubor:

`book/proof/AI-book-proof-v0.4.pdf`

Jde o release-candidate proof knihy **AI od základů k agentním systémům**.

## Proč dva různé reviewery

Nechceme hlasování typu „dva modely řekly totéž, takže je to pravda“.

Chceme dvě částečně odlišné optiky:

- **Claude** — hlavně redakční soudržnost, pedagogika, srozumitelnost, opakování, tón, struktura a technická přesnost vysvětlení.
- **Gemini** — hlavně faktická/current kontrola, mezery v pokrytí, tabulky/diagramy, technické nuance, zdroje, regulatorní a budoucí tvrzení.

Oba ale musí zkontrolovat celou knihu, ne pouze svůj hlavní fokus.

## Postup

1. Nahraj PDF do Claude.
2. Vlož přesně obsah `CLAUDE_REVIEW_PROMPT.md`.
3. Ulož celý výstup do `CLAUDE_REVIEW_RESULT.md` nebo jej vrať do ChatGPT.
4. Nahraj stejné PDF do Gemini.
5. Vlož přesně obsah `GEMINI_REVIEW_PROMPT.md`.
6. Ulož celý výstup do `GEMINI_REVIEW_RESULT.md` nebo jej vrať do ChatGPT.
7. ChatGPT provede adjudikaci obou review proti skutečnému rukopisu.

## Severity

- **P0 — blocker**: faktická, právní, bezpečnostní nebo strukturální chyba, kvůli které by kniha neměla jít ven.
- **P1 — major**: významná chyba, rozpor, chybějící důležitá část nebo opakování, které znatelně zhoršuje knihu.
- **P2 — minor**: lokální redakční nebo stylistický problém, který stojí za opravu.
- **P3 — optional**: subjektivní vylepšení, které není nutné pro publikaci.

## Pravidlo pro zapracování

Externí review není autorita. Každou připomínku před zapracováním ověřujeme proti:

1. konkrétnímu místu v rukopisu,
2. primárnímu zdroji, pokud jde o fakt,
3. cíli a publiku knihy,
4. riziku, že oprava vytvoří novou nekonzistenci.

Výsledkem má být tabulka **accept / modify / reject** s krátkým odůvodněním.