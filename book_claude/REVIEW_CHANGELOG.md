# REVIEW CHANGELOG — book_claude (v0.5-claude)

Paralelní edice knihy se zapracovanými změnami z externího review (Claude, 7. 8. 2026). Referenční čísla ([P1-x], [P2-x]) odkazují na REVIEW_REPORT.

## Nové soubory

- **`00 - Uvod - Jak cist tuto knihu.md`** — nová úvodní kapitola [P1-2]: pro koho kniha je, co bude čtenář umět, tři čtenářské cesty (začátečník / inženýr / manažer), vysvětlení snapshot vrstvy.
- **`REVIEW_CHANGELOG.md`** — tento soubor.

## Strukturální změny

| Kapitola | Změna | Ref |
|---|---|---|
| 1 | Zkrácena o ~19 % (4 564 → 3 716 slov): sekce 2023–2026 zhuštěny do jedné s odkazem na kap. 5 a 33; tři závěrečné sumarizační sekce (1.6 + „Co nás historie učí" + „Mentální model") sloučeny do jedné „1.6 Co si z celé historie odnést". | [P1-5] |
| 3 | Odstraněn čtvrtý uzávěr kapitoly („Mentální model kapitoly" — duplicitní ASCII diagramy); můstek do kap. 4 zachován. | sekce 8 |
| 11 | Přepsána: nový podtitul role — kompaktní most (843 → ~700 slov) + **nový rozhodovací strom „kdy fine-tuning"** (prompt → context/RAG → tools → fine-tuning). | [P2-1] + chybějící téma 2 |
| 35 | Přepsána z 1 243 na ~550 slov: čistě osobní rámování (pořadí experimentů + „jak poznám, že jsem se něco naučil"), veškerá substance projektů zůstává v kap. 37. | [P1-4] |
| všechny | Hierarchie nadpisů sjednocena — 76 závěrečných sekcí demotováno z H1 na H2 (fence-aware skript). | [P2-2] |

## Deduplikace (kanonická místa + odkazy)

| Místo | Změna | Ref |
|---|---|---|
| 6.7 | Metafora pracovního stolu → odkaz na kap. 3 (kanonické místo 3.14). | sekce 6 |
| 8.19 | Tokens/s vs. produktivita zhuštěno na odstavec + odkaz na 6.8. | sekce 6 |
| 10.1 | Rovnice „model × context" zhuštěna do věty (kanonicky kap. 3). | sekce 6 |
| 14 | Tool permission ladder explicitně označen jako **kanonický žebřík** knihy. | [P2-8] |
| 15.11 | Prompt injection + exfiltration zhuštěny s odkazem na kap. 25. | sekce 6 |
| 23 | Stupně engineering autonomie uvedeny jako doménová konkretizace žebříku z kap. 14. | [P2-8] |
| 25.1 | Data classification → odkaz na kanonickou tabulku 7.8. | sekce 6 |
| 25.19 | Progressive trust → odkaz na žebřík z kap. 14. | [P2-8] |
| 26.9 | Měření výsledků zhuštěno + odkaz na kap. 29 a 31. | [P2-7] |
| 27.5 | Data classification → odkaz na 7.8. | sekce 6 |
| 29.4 | Doplněn odkaz na kap. 31 (kanonické místo pro evaluaci). | [P2-7] |
| 34.1 | Druhá systémová rovnice zhuštěna do věty (plný diagram zůstává v 34.10). | sekce 6 |

## Nový obsah

| Kapitola | Doplněno | Ref |
|---|---|---|
| 9.15 | Nový box **„AI a čeština"**: tokenizace a cena, kdy psát prompt anglicky, embeddings pro češtinu, český STT. | chybějící téma 4 |
| 11.2 | Rozhodovací strom **„kdy fine-tuning"**. | chybějící téma 2 |
| 18 | Nová sekce **„Jak vypadá skutečný běh"** — reálný trace agentního běhu (15 kroků, tool cally s argumenty, chyba → UNKNOWN recovery, deterministický verifier). | chybějící téma 3 |
| příloha G | **EXP-001 (8 GB vs. 32 GB VRAM) zdokumentován** z kap. 34.3; přesná čísla označena `[DOPLNIT]` pro autora. Backlog přečíslován (G.6→dokumentované, G.7→backlog, G.8→pravidlo). | [P1-3] |

## Aktualizace snapshotů a opravy

| Místo | Změna | Ref |
|---|---|---|
| 5 (Anthropic) | Claude Opus 4.8 → **Claude Opus 5** (aktuální řada Claude 5); aktualizovány zdroje. | FC-01 |
| příloha B | Řádek Anthropic aktualizován (Opus 5); u Command A+ doplněno **varování na ověření licence vah** (starší Command A byl nekomerční). | FC-01, FC-05 |
| 5.10 | Video generation zkráceno na odstavec. | [P2-6] |
| 8 | Doplněna snapshot hlavička + poznámka o stárnutí. | [P2-5] |
| 4 (intro) | Šipkový pseudo-pipeline schopností převeden na větu (nešlo o sekvenci). | [P2-3] |
| 4.11 | „Hallucinations" → „Halucinace (hallucinations)" dle style guide. | [P2-10] |
| 15 | Typo `verify-lDO-design` → `verify-LDO-design`. | [P2-4] |
| STYLE_GUIDE | Doplněno pravidlo pro „halucinace". | [P2-10] |
| 00 INDEX | Verze 0.5-claude, odkaz na úvod a tento changelog. | — |

## Co zbývá na autorovi (nelze udělat za něj)

1. **Doplnit čísla do EXP-001 v příloze G** (pole `[DOPLNIT]`) a ideálně dopsat EXP-002/003 z vlastních poznámek — [P1-3].
2. **Finální fact-check snapshotů kap. 5 / přílohy B k datu tisku** — zejména GPT-5.6, Gemini 3.x číslování, Grok 4.5, DeepSeek V4, Qwen3.6, Gemma 4, Mistral Small 4, Cohere Transcribe/Rerank 4, licence Command A+ a MCP spec 2026-07-28. Verze Claude byla aktualizována (Opus 5), ostatní vendory je třeba ověřit proti citovaným primárním zdrojům — sekce 9 review.
3. **Diagram pro kap. 33** (mapa trendů) — [P2-9]; vyžaduje grafickou konzistenci s ostatními SVG.
4. **Volitelně:** hlubší redukce jednoslovných ```text``` bloků napříč knihou — [P2-3] byl zapracován jen v nejkřiklavějších místech; plný průchod je vhodné dělat společně se sazbou.
