# Porovnání tří verzí knihy a redakční adjudikace

**Datum:** 2026-08-07  
**Porovnávané verze:** `book/`, `book_claude/`, `book_gemini/`

## Executive verdict

**Nedoporučuji vydat žádnou ze tří verzí beze změny.**

- `book/` je nejlepší **ověřený základ**: prošel dosavadním copyeditem, prepress auditem a proof buildem, nemá placeholdery a drží osobní/inženýrský tón. Slabina je zbytečná délka, několik duplicit a absence skutečného úvodu.
- `book_claude/` přináší nejlepší **redakční zásahy**: nový úvod, lepší navigaci pro čtenáře, zkrácení kapitol 1 a 35, deduplikaci, sjednocení hierarchie nadpisů a výborný reálný trace v kapitole 18. Současně ale zavádí **novou faktickou chybu v modelovém snapshotu** a **7 placeholderů `[DOPLNIT]`**, takže není release-ready.
- `book_gemini/` přináší nejlepší **technické a strukturální opravy**: historie deep learningu, reasoning/test-time compute, VRAM/KV cache, produkční prompting, přesnější RAG, MCP, sloučení agentních kapitol, enterprise dokumenty, defense-in-depth, LLM-as-a-judge a TCO. Je informačně nejhustší, ale chybí mu úvod, neprovedl globální heading cleanup a některé řezy jsou až příliš agresivní.

### Doporučení

Vytvořit **čtvrtou, finální hybridní verzi**:

> **Gemini jako technická páteř + Claude jako redakční vrstva + `book/` jako referenční zdroj pro vše, co není důvod měnit.**

Nejprve sloučit obsah, potom teprve vytvořit nový proof PDF a zopakovat všechny prepress kontroly.

---

# 1. Kvantitativní porovnání

Automatický diff byl proveden přímo nad aktuálními třemi adresáři v repozitáři.

| Metrika | `book/` | `book_claude/` | `book_gemini/` |
|---|---:|---:|---:|
| Samostatné číslované kapitoly | 37 | 37 | 35 |
| Přílohy A–G | 7 | 7 | 7 |
| Samostatný úvod | ne | **ano** | ne |
| Slova: kapitoly + přílohy + případný úvod | 63 659 | 63 481 | **62 727** |
| `[DOPLNIT]` / TODO v rukopisu | **0** | **7** | **0** |
| H1 nadpisy v rukopisu | 121 | **46** | 110 |
| H2 nadpisy v rukopisu | 560 | **623** | 544 |

## Co z čísel plyne

Claude deklaruje výraznou deduplikaci, ale celkově je rukopis pouze o **178 slov kratší** než `book/`, protože úspory v kapitolách 1 a 35 kompenzuje nový úvod, rozšířená kapitola 9, nový trace v kapitole 18 a rozpracovaný experiment v příloze G.

Gemini je proti `book/` kratší o **932 slov**, přestože přidává nový technický obsah. Největší úspora vzniká sloučením 16+17 a odstraněním 26.

Největší skutečný produkční přínos Claude varianty v automatických metrikách je **hierarchie nadpisů**: 121 H1 → 46 H1. To je správný směr pro sazbu a mělo by se převzít do finální verze.

---

# 2. Profil jednotlivých variant

## `book/` — stabilní referenční baseline

### Silné stránky

- prošel dosavadním redakčním, technickým a proof auditem,
- 0 placeholderů,
- nejnižší riziko, že edit zanesl novou chybu,
- zachovává plný osobní tón a praktické příklady,
- kapitola 24 a engineering příklady jsou už velmi dobré.

### Slabiny

- chybí reader-facing úvod,
- opakování některých mentálních modelů,
- kapitola 1 je příliš dlouhá,
- 35 a 37 se významně překrývají,
- 16 a 17 lze spojit bez velké ztráty,
- 26 lze z větší části absorbovat do 22,
- heading hierarchy je příliš plochá a používá příliš mnoho H1.

**Role ve finální verzi:** bezpečný master/reference, nikoli finální obsahová volba.

---

## `book_claude/` — nejlepší redakční editor, ale ne spolehlivý fact-check master

### Co je velmi dobré

1. **Nový úvod** — vysvětluje pro koho kniha je, co si čtenář odnese a nabízí tři čtenářské cesty.
2. **Kapitola 1 −16,7 %** — čitelnější historie bez tolik opakování.
3. **Kapitola 35 −65,1 %** — výrazně lepší, protože už neopakuje kapitolu 37.
4. **Kapitola 18 +20,7 %** — přidaný konkrétní 15krokový agentní trace je jeden z nejlepších praktických přírůstků mezi všemi review.
5. **Kapitola 11** — dobrý rozhodovací strom `context/RAG/tools vs. fine-tuning`.
6. **Globální heading cleanup** — velmi vhodný pro tisk i Obsidian.
7. Několik dobrých lokálních deduplikací a cross-reference na kanonické kapitoly.

### Co je problém

#### C-1 — faktická regrese v kapitole 5 / příloze B

Claude změnil aktuální Anthropic řadu na **„Claude Sonnet 5 a Claude Opus 5“**.

Externí kontrola proti aktuálnímu primárnímu zdroji Anthropic k 7. 8. 2026 ukazuje:

- **Claude Sonnet 5** existuje,
- aktuální Opus je stále **Claude Opus 4.8**,
- oficiální API označení je `claude-opus-4-8`.

Proto změnu **Opus 4.8 → Opus 5 REJECT**.

Primární zdroj: Anthropic, *Claude Opus 4.8*, 28. 5. 2026: https://www.anthropic.com/claude/opus

#### C-2 — příloha G znovu zavádí placeholdery

Claude vytvořil EXP-001, ale obsahuje sedm polí `[DOPLNIT]`, včetně hardware konfigurace, runtime verze, modelů a TTFT/tokens/s.

To je horší release stav než `book/`, kde bylo po korekturách **0 placeholderů**.

**Verdikt:** myšlenku zdokumentovat EXP-001 přijmout, ale současný text **nepřebírat**, dokud nejsou skutečná data. Nic nevymýšlet.

#### C-3 — historická korekce není dostatečná

Claude kapitolu 1 dobře zkrátil, ale neřeší explicitně celý problém požadovaný technickým review: jednovrstvý perceptron / lineární separabilita / Minsky & Papert / popularizace backpropagation 1986 / Transformer 2017 = self-attention, nikoli objev gradientního tréninku.

**Verdikt:** použít Claude strukturu kapitoly 1, ale technické formulace převzít z Gemini.

---

## `book_gemini/` — nejlepší technická korekce a informační hustota

### Co je velmi dobré

- historie perceptronu, backpropagation a Transformeru,
- praktický dopad české tokenizace bez falešné univerzální konstanty,
- reasoning modely a test-time compute,
- VRAM sizing včetně KV cache a runtime rezervy,
- anatomie produkčního promptu,
- structured output místo falešné jistoty `temperature = 0`,
- přesné rozlišení semantic/vector vs. lexical/full-text retrieval,
- MCP analogie zpřesněná tak, aby z USB-C metafory nevznikl dojem „bez adaptérů úplně pro všechno“,
- velmi dobré sloučení agentní anatomie a smyčky,
- explicitní infinite-loop/retry/budget guardrails,
- kap. 22 zaměřená na parsing/OCR/ACL/provenance/audit,
- system prompt správně popsán jako behaviorální vrstva, nikoli security boundary,
- konkrétní LLM-as-a-judge prompt,
- konkrétní TCO příklad,
- explicitní `[Snapshot 08/2026]` v dynamických přílohách.

### Co je slabší

1. Nemá úvod knihy.
2. Heading hierarchy zůstává téměř stejně fragmentovaná jako v `book/`.
3. Sloučení 16+17 je redakčně správné, ale z 2 326 slov dělá přibližně 1 002 slov. To je už velký řez; část pedagogické hodnoty je vhodné vrátit konkrétním Claude trace v kap. 18.
4. Odstranění 26 je správné, ale ve finální publikaci nesmí zůstat reader-facing číslování `25 → 27` bez vysvětlení.
5. Totéž platí pro `16 → 18` po odstranění 17.
6. Nemá nový proof build — starý release-candidate proof `book/` automaticky nevaliduje tuto strukturálně jinou verzi.

---

# 3. Adjudikace po kapitolách

Legenda:

- **BASE** — ponechat `book/`, jen aplikovat globální style/heading cleanup.
- **CLAUDE** — převzít primárně Claude úpravu.
- **GEMINI** — převzít primárně Gemini úpravu.
- **HYBRID** — ručně spojit nejlepší části obou.

| Kapitola | Doporučení | Co udělat ve finální verzi |
|---:|---|---|
| Úvod | **CLAUDE / MODIFY** | Převzít nový úvod a tři čtenářské cesty. Po sloučení kapitol opravit odkazy — manažerská cesta nesmí odkazovat na zrušenou 26. |
| 1 | **HYBRID** | Claude zkrácení + Gemini faktická historie perceptron/backprop/Transformer. Toto je jasně lepší než každá varianta samostatně. |
| 2 | **BASE** | Obsahově neměnit. |
| 3 | **HYBRID** | Zachovat jádro, převzít Gemini krátkou poznámku o české tokenizaci a Claude odstranění duplicitního čtvrtého závěru. |
| 4 | **BASE + microcopy** | Pouze Claude terminologické/strukturální drobnosti, žádný obsahový rewrite. |
| 5 | **HYBRID** | Gemini reasoning/test-time compute. Z Claude lze převzít redakční zkrácení méně důležitých pasáží, ale **REJECT „Opus 5“**; ponechat aktuální Opus 4.8. |
| 6 | **CLAUDE minor** | Převzít deduplikaci metafory/odkaz na kanonické místo; jinak base. |
| 7 | **BASE** | Jen sjednotit heading hierarchy. |
| 8 | **HYBRID** | Gemini VRAM/KV cache + practical 70B Q4 sizing; Claude zkrácení duplicitního `tokens/s ≠ produktivita`. |
| 9 | **HYBRID** | Gemini anatomie produkčního promptu + structured output. Z Claude zachovat pouze opravdu užitečná česká specifika; tokenizaci držet primárně v kap. 3, embeddings v kap. 12 a STT u modelů/nástrojů, aby 9.15 nebyla nový mix témat. |
| 10 | **CLAUDE minor** | Deduplikovat rovnici model × context; jinak base. |
| 11 | **HYBRID, bližší CLAUDE** | Claude fine-tuning decision tree je velmi užitečný. Zachovat Gemini snahu udělat z kapitoly krátký most k RAG. Cíl ~550–650 slov. |
| 12 | **GEMINI** | Převzít explicitní vector/semantic vs. lexical/full-text rozdíl. |
| 13 | **BASE** | Beze změny kromě heading cleanup. |
| 14 | **CLAUDE minor** | Označit permission ladder za kanonické místo knihy; jinak base. |
| 15 | **HYBRID** | Gemini MCP mentální model + Claude odstranění security duplicity/typo. |
| 16+17 | **GEMINI + CLAUDE support** | Sloučit do jedné kapitoly **Anatomie a smyčka AI agenta**. ReAct neopakovat. Pedagogickou konkrétnost doplní trace v kap. 18. |
| 18 | **CLAUDE** | Převzít 15krokový konkrétní trace včetně `UNKNOWN`, verifieru a tool callů. Velmi vysoká praktická hodnota. |
| 19 | **BASE** | Beze změny. |
| 20 | **BASE** | Beze změny. |
| 21 | **BASE** | Beze změny. |
| 22+26 | **GEMINI** | Zrušit samostatnou 26; web chat vs. API/script/agent vložit do úvodu 22. Kap. 22 držet čistě enterprise: parsing, OCR, tabulky, ACL, audit, data protection. |
| 23 | **CLAUDE minor** | Explicitně odkázat autonomy/permission stupně na kanonický žebřík v 14. |
| 24 | **BASE** | Případovou studii zachovat. Je diferenciátorem knihy a oba reviewery ji prakticky nechaly být. |
| 25 | **HYBRID** | Gemini defense-in-depth + Claude deduplikace data classification/progressive trust. |
| 26 | **REMOVE** | Obsah absorbovat do 22; samostatný soubor ve finální struktuře nepotřebujeme. |
| 27 | **CLAUDE minor** | Data classification pouze odkazem na kanonickou tabulku; jinak base. |
| 28 | **BASE** | Beze změny. |
| 29 | **CLAUDE minor** | Přidat odkaz na kanonickou evaluaci v 31; jinak base. |
| 30 | **BASE** | Beze změny. |
| 31 | **GEMINI** | Převzít konkrétní LLM-as-a-judge prompt, schema output a kalibraci proti člověku. |
| 32 | **GEMINI** | Převzít konkrétní API vs. dedicated GPU TCO model, explicitně jako ilustrativní `[Snapshot 08/2026]`. |
| 33 | **BASE** | Obsah ponechat; případný nový diagram řešit až při finálním design passu. |
| 34 | **CLAUDE minor** | Zachovat osobní zkušenosti, pouze odstranit duplicitní systémovou rovnici. |
| 35 | **CLAUDE** | Převzít silné zkrácení. Kapitola má být osobní roadmapa, ne druhá kopie kap. 37. |
| 36 | **BASE** | Beze změny. |
| 37 | **BASE** | Zachovat jako hlavní praktický projektový žebřík. |

---

# 4. Adjudikace příloh

| Příloha | Doporučení | Poznámka |
|---|---|---|
| A — Slovník | **BASE** | Všechny verze jsou prakticky stejné. |
| B — Modely | **GEMINI / fact-check** | Převzít explicitní `[Snapshot 08/2026]`; nepřebírat Claude „Opus 5“. Před tiskem ještě jednou ověřit všechny modely z primárních zdrojů. |
| C — Nástroje | **GEMINI minor** | Převzít explicitní snapshot štítek. |
| D — Hardware | **BASE** | Beze změny; Gemini VRAM vysvětlení je vhodněji v kapitole 8. |
| E — Security checklist | **BASE** | Beze změny. |
| F — Agent checklist | **BASE** | Beze změny. |
| G — Experimenty | **BASE NOW / NEW LATER** | Claude EXP-001 je dobrý koncept, ale nepublikovat 7× `[DOPLNIT]`. Buď doplnit skutečná čísla, nebo ponechat čistou šablonu z `book/`. |

---

# 5. Nejdůležitější ACCEPT / MODIFY / REJECT

## ACCEPT

- Claude nový úvod.
- Claude zkrácení kap. 35.
- Claude konkrétní trace v kap. 18.
- Claude globální sjednocení nadpisů H1/H2.
- Claude deduplikace s odkazy na kanonická místa.
- Gemini technické opravy historie.
- Gemini reasoning/test-time compute.
- Gemini VRAM/KV cache model.
- Gemini production prompt anatomy.
- Gemini semantic vs. lexical search vysvětlení.
- Gemini MCP zpřesnění.
- Gemini merge 16+17.
- Gemini merge 22+26.
- Gemini defense-in-depth.
- Gemini LLM-as-a-judge.
- Gemini TCO příklad.
- Gemini snapshot štítky.

## MODIFY

- Claude kapitolu 1: použít strukturu a škrt, ale doplnit Gemini fakta.
- Kapitolu 11: spojit Claude fine-tuning strom s Gemini stručností.
- Kapitolu 9: neskládat všechna česká specifika do promptingu; rozdělit je do správných kanonických kapitol.
- Gemini agentní kompresi: zachovat, ale doplnit Claude konkrétním trace v následující kapitole.
- Claude EXP-001: jen pokud budou dostupná skutečná data.

## REJECT

- Claude `Claude Opus 5` — fakticky neověřeno a proti aktuálnímu primárnímu zdroji chybné.
- Jakékoli `[DOPLNIT]` v release rukopisu.
- Tvrzení, že `temperature = 0` garantuje validní JSON/schema.
- Univerzální konstanta „čeština = 1,5–2 tokeny/slovo“ bez konkrétního tokenizeru.
- Ponechání duplicitního plného výkladu RAG v kap. 22.
- Ponechání 26 jako samostatné kapitoly po přesunu jejího jádra do 22.

---

# 6. Důležitá strukturální otázka: číslování po sloučení

`book_gemini/` záměrně zachoval interní čísla souborů, takže reader-facing pořadí je:

```text
15
16
18
19
...
25
27
28
...
```

Pro interní review je to praktické, protože Git diff a odkazy zůstávají stabilní.

**Pro finální tištěnou knihu to ale nedoporučuji.** Čtenář bude chybějící 17 a 26 vnímat jako chybu.

Doporučený postup:

1. během tvorby `book_final/` ponechat technické názvy souborů stabilní,
2. po uzamčení obsahu udělat jednorázové **reader-facing přečíslování** kapitol a aktualizaci cross-referencí,
3. teprve potom stavět finální PDF/EPUB/HTML.

Alternativa je ponechat stabilní názvy souborů, ale generátor knihy musí mít samostatné `display_number`, aby čtenář viděl souvislou řadu.

---

# 7. Která verze vyhrává v které oblasti

| Oblast | Nejlepší zdroj | Proč |
|---|---|---|
| Dosavadní proof/prepress jistota | `book/` | Je to jediná verze, nad kterou proběhl kompletní release-candidate proof audit. |
| Reader onboarding | `book_claude/` | Jediná má skutečný úvod a čtenářské cesty. |
| Redakční koncentrace | `book_claude/` na vybraných kapitolách | Kap. 1 a 35 jsou výrazně lepší po zkrácení. |
| Technická přesnost nových oprav | `book_gemini/` | Nejlépe řeší historii, reasoning, VRAM, RAG, MCP, security a evals. |
| Agentní architektura | **hybrid** | Gemini compact 16 + Claude trace 18. |
| Enterprise dokumenty | `book_gemini/` | Nejčistší oddělení obecného RAG od firemní praxe. |
| Sazební struktura | `book_claude/` | Nejlepší H1/H2 normalizace. |
| Release hygiene | `book/` / `book_gemini/` | 0 placeholderů; Claude má 7. |
| Osobní/engineering charakter | `book/` jako baseline | Případová studie a osobní zkušenosti mají zůstat nedotčené, pokud není konkrétní důvod editovat. |

---

# 8. Doporučená finální struktura

Finální verze by měla obsahově vypadat přibližně takto:

```text
Úvod                        ← Claude, upravený
1 Historie                   ← Claude structure + Gemini facts
2–15                         ← base + cílené adjudikované změny
16 Anatomie a smyčka agenta  ← Gemini merge
17 Jak postavit agenta       ← původní 18 + Claude trace
18 Multi-agent               ← původní 19
19 Orchestrace               ← původní 20
20 Coding Agents             ← původní 21
21 AI nad firemními daty     ← Gemini 22 + jádro původní 26
22 Engineering AI            ← původní 23
23 Analog IC case study      ← původní 24
24 Bezpečnost                ← hybrid 25
25 AI readiness              ← původní 27
...
```

Přesné reader-facing číslo se má dopočítat jednorázově až po definitivním sloučení všech kapitol.

---

# 9. Release gates po vytvoření hybridu

Hybridní rukopis nebude automaticky release-ready jen proto, že kombinuje nejlepší části.

Musí znovu projít:

1. **broken-link / cross-reference audit** po odstranění a přečíslování kapitol,
2. **placeholder audit = 0**,
3. **snapshot fact-check** kap. 5 + příloh B/C proti primárním zdrojům,
4. **terminology/style audit**,
5. **duplicate paragraph / repeated concept audit**,
6. **nový proof build**,
7. **font, overflow, orphan heading, sparse-page a safety-margin QA**,
8. cílenou kontrolu, že Claude heading normalization nezměnila význam dokumentu,
9. fyzický print proof před tiskem.

---

# 10. Finální doporučení

**Nevolil bych vítěze mezi Claude a Gemini.** Oba reviewery našli jiný typ problému a jejich nejlepší změny se překrývají jen málo.

Prakticky:

```text
book/
= ověřený základ

book_claude/
= redakční editor

book_gemini/
= technický editor

book_final/
= adjudikovaný rukopis
```

### Můj doporučený pořadník pro `book_final/`

1. Převzít Claude úvod a heading cleanup.
2. Převzít Claude zkrácení 1 a 35.
3. Do kap. 1 vložit Gemini historické opravy.
4. Převzít všechny potvrzené Gemini technické změny 3/5/8/9/12/15/25/31/32.
5. Sloučit 16+17 podle Gemini.
6. Přidat Claude trace do následující praktické agentní kapitoly.
7. Sloučit 22+26 podle Gemini.
8. Udělat Claude-style deduplikaci napříč zbývajícími kapitolami.
9. Přílohu G ponechat bez nevyplněných experimentálních čísel.
10. Udělat jeden nový fact-check, přečíslování a kompletní proof pipeline.

**Výsledkem by měla být verze lepší než všechny tři současné varianty: kratší, přesnější, lépe navigovatelná a stále osobní.**
