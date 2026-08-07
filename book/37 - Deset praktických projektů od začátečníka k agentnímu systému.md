---
title: "37. Deset praktických projektů od začátečníka k agentnímu systému"
part: "XIV — Praktická kuchařka"
status: draft
version: "0.2"
updated: 2026-08-07
---

# 37. Deset praktických projektů od začátečníka k agentnímu systému

Celá kniha postupovala od modelu k systému.

Teď stejnou cestu projdeme prakticky.

Ne jedním obřím projektem, ale deseti malými kroky, kde každý přidá právě jednu novou schopnost.

```text
jeden dokument
→ více dokumentů
→ knowledge base
→ local model
→ RAG
→ tool use
→ agent
→ coding agent
→ firemní workflow
→ multi-agent
```

Cílem není pouze jednotlivé projekty „rozchodit“.

U každého chci vědět:

- co je vstup,
- co je výstup,
- jak poznám úspěch,
- co se pokazilo,
- co jsem se naučil.

> **Každý projekt má být malý uzavřený experiment, který vytvoří použitelný artefakt a jednu novou zkušenost.**

Pokud některý krok nefunguje spolehlivě, nepřeskakuji jej jen proto, že další projekt vypadá zajímavěji.

---

## Projekt 1 — Chat nad jedním dokumentem

### Cíl

Vzít jeden dokument a naučit se rozlišit mezi:

```text
obecnou znalostí modelu
```

a

```text
odpovědí skutečně podloženou dokumentem
```

Vhodný vstup může být například:

- technický datasheet,
- krátká specifikace,
- článek,
- vlastní Markdown poznámka.

### Úkol

Položit přibližně deset otázek různých typů:

```text
1. najdi konkrétní hodnotu
2. shrň jednu sekci
3. vysvětli pojem z dokumentu
4. najdi podmínku nebo výjimku
5. odpověz na otázku, na kterou dokument odpověď neobsahuje
```

Poslední bod je důležitý.

Model musí umět říct:

> „Tato informace v dokumentu není.“

místo toho, aby ji doplnil z obecné znalosti a vydával ji za obsah zdroje.

### Co se učím

- context,
- grounding,
- citace,
- hallucination risk,
- rozdíl mezi source fact a inference.

### Výstup

Malá tabulka:

| Otázka | Správná odpověď | Odpověď AI | Zdroj správný? | Poznámka |
|---|---|---|---|---|

### Hotovo, když

```text
- umím otevřít zdroj odpovědi
- model nevymýšlí odpověď, když dokument informaci nemá
- rozumím, kde při práci s jedním dokumentem vznikají chyby
```

Než přidám RAG nebo vector database, chci nejdřív dobře pochopit tento nejjednodušší případ.

---

## Projekt 2 — Analýza několika dokumentů

### Cíl

Přestat pracovat pouze s jedním zdrojem a naučit se spojovat evidence.

Například vezmu:

```text
specification.pdf
review_notes.md
measurement_results.xlsx
```

A položím otázku:

> „Které požadavky nejsou podle dostupných výsledků splněné a z jakého zdroje to víme?“

### Úkol

AI musí:

1. identifikovat relevantní informace v několika zdrojích,
2. rozlišit jejich role,
3. spojit je,
4. uvést odkud každý závěr pochází,
5. označit konflikt nebo chybějící informaci.

### Důležitý princip

Nechci:

```text
nejdříve vytvořit příběh
→ potom hledat důkazy
```

Chci:

```text
evidence
→ struktura
→ závěr
```

### Co se učím

- multi-document context,
- provenance,
- konfliktní zdroje,
- version awareness,
- structured extraction.

### Výstup

Evidence table:

| Tvrzení | Zdroj | Strana/sekce/cell | Stav |
|---|---|---|---|

A krátký report vytvořený až z této tabulky.

### Hotovo, když

Každé důležité tvrzení lze zpětně ověřit v originálním dokumentu.

---

## Projekt 3 — Osobní knowledge base

### Cíl

Vytvořit malý druhý mozek, který zůstane užitečný i bez AI.

Nechci začínat tisíci souborů.

Stačí například:

```text
50–100 Markdown notes
+
několik PDF
+
několik experimentů
```

### Struktura

Například:

```text
Knowledge/
Projects/
Meetings/
Experiments/
Sources/
```

Každá důležitá poznámka dostane minimum metadat:

```yaml
---
title:
date:
type:
project:
status:
---
```

### Úkol

Vyzkoušet otázky, u kterých si přesné umístění informace nepamatuji.

Například:

> „Co jsem si za poslední měsíc poznamenal o lokálních modelech na 16 GB VRAM?“

### Co se učím

- human-readable knowledge layer,
- metadata,
- search,
- rozdíl archive / knowledge / working state,
- provenance.

### Výstup

Obsidian nebo jiný Markdown vault, který lze:

- ručně procházet,
- verzovat přes Git,
- prohledávat AI.

### Hotovo, když

AI není jediná cesta k mým datům.

Když model vypnu, znalosti stále zůstávají normálními čitelnými soubory.

---

## Projekt 4 — Lokální LLM

### Cíl

Rozběhnout vlastní inference a pochopit reálné omezení hardware.

Nejde o soutěž:

> „Jak největší model se mi podaří spustit?“

Chci zjistit:

> **Jaký model je na mém hardware dostatečně dobrý pro konkrétní práci?**

### Minimální setup

Například:

```text
Ollama nebo llama.cpp
+
1–3 modely různých velikostí
+
jednoduchý benchmark
```

### Testy

Stejnou sadu úloh spustím na každém modelu:

- summarization,
- extraction,
- technical Q&A,
- coding,
- structured output.

Měřím:

```text
TTFT
output tokens/s
RAM
VRAM
quality
success rate
```

### Co se učím

- inference,
- quantization,
- VRAM vs. RAM,
- latency,
- model quality vs. size.

### Výstup

Vlastní benchmark tabulka.

### Hotovo, když

Dokážu věcně říct například:

> „Na tomto hardware je pro můj use-case model A lepší než model B, protože kvalita je podobná, ale workflow je dvakrát rychlejší.“

Ne pouze:

> „Model A mi připadal chytřejší.“

---

## Projekt 5 — RAG nad vlastními daty

### Cíl

Postavit první skutečný retrieval pipeline.

Tentokrát nechci pouze použít hotové tlačítko „upload files“.

Chci vidět jednotlivé vrstvy:

```text
document
→ parse
→ chunk
→ embedding
→ index
→ search
→ rerank
→ context
→ answer + citation
```

### Dataset

Začnu malým, ale realistickým corpus:

```text
20–100 dokumentů
```

A vytvořím například 30–50 golden questions.

U každé znám:

- správnou odpověď,
- správný zdroj.

### Experimenty

Porovnám například:

```text
keyword search
vs.
semantic search
vs.
hybrid search
```

Potom:

```text
bez rerankeru
vs.
s rerankerem
```

### Co se učím

- ingestion,
- chunking,
- embeddings,
- metadata,
- retrieval eval,
- citation pipeline.

### Výstup

RAG systém a tabulka:

```text
retrieval Recall@K
answer correctness
citation correctness
```

### Hotovo, když

Když systém odpoví špatně, dokážu určit, zda selhal:

```text
ingestion
retrieval
reranking
context
nebo generation
```

---

## Projekt 6 — AI s jedním nástrojem

### Cíl

Poprvé nechat model něco skutečně **udělat**, ne pouze vytvořit text.

Vyberu jeden bezpečný nástroj.

Například:

```text
calculator
Python
read-only database
web search
simulation wrapper
```

### Příklad

Uživatel:

> „Porovnej dva CSV soubory a zjisti, kde se hodnoty liší o více než 5 %.“

Agentní vrstva:

```text
LLM
→ rozhodne, že potřebuje Python
→ tool call
→ exact calculation
→ result
→ LLM explanation
```

### Co se učím

- function calling,
- input schema,
- output schema,
- tool errors,
- oddělení LLM a deterministického výpočtu.

### Bezpečnost

Nástroj má co nejmenší oprávnění.

Python nemusí vidět celý disk.

Databáze může být read-only.

### Výstup

Jedna aplikace, ve které model spolehlivě rozhodne, kdy tool použít a správně interpretuje jeho výsledek.

### Hotovo, když

Mám testy také na situace:

```text
tool potřebný
```

a

```text
tool zbytečný
```

Model nemá volat nástroj automaticky při každé otázce.

---

## Projekt 7 — Agent nad filesystemem

### Cíl

Postavit první skutečnou smyčku:

```text
observe
→ decide
→ act
→ verify
→ repeat
```

Agent dostane sandbox directory s několika soubory.

Například:

```text
workspace/
  inputs/
  outputs/
  README.md
```

### Úkol

Například:

> „Najdi všechny soubory obsahující výsledky experimentu X, vytvoř souhrn a ulož `report.md`. Nic mimo workspace neměň.“

Agent může mít pouze:

```text
list_files()
read_file()
search_files()
write_file()
```

### Co se učím

- state,
- agent loop,
- stop condition,
- permissions,
- sandbox,
- logging.

### Verifikace

Po skončení zkontroluji:

- vznikl požadovaný soubor?
- obsahuje všechny relevantní zdroje?
- změnil agent něco, co neměl?
- kolik kroků potřeboval?

### Hotovo, když

Agent zvládne stejný typ úlohy na různých adresářích opakovaně, ne pouze jednou na přesně připraveném demo datasetu.

---

## Projekt 8 — Coding agent

### Cíl

Použít prostředí, kde máme mimořádně silný verifier — testy.

Vyberu malý Git repository s reálnou chybou nebo feature requestem.

### Workflow

```text
issue
 ↓
create branch
 ↓
search code
 ↓
edit
 ↓
targeted test
 ↓
full tests
 ↓
diff
 ↓
human review
```

### Úkol

Začnu jednoduchými změnami:

- opravit známý bug,
- doplnit validaci,
- přidat malou funkci,
- aktualizovat dokumentaci a testy.

### Co se učím

- repository context,
- code search,
- tool loop,
- Git jako audit a rollback,
- deterministická verifikace.

### Důležitá metrika

Nejen:

```text
tests pass
```

ale také:

```text
minimal diff
no unrelated changes
```

### Výstup

Branch nebo pull request s:

```text
WHAT
WHY
TESTS
RISKS
```

### Hotovo, když

Člověk může změnu schválit z diffu a evidence, aniž by musel znovu dělat celou práci od začátku.

---

## Projekt 9 — Agentní workflow nad firemními daty

### Cíl

Spojit několik předchozích schopností do jednoho reálného end-to-end use-case.

To je první projekt, který bych hodnotil jako skutečný **pilotní kandidát**.

Příklad:

> „Z nové sady regression výsledků vytvoř PASS/FAIL report proti aktuální released specifikaci.“

### Pipeline

```text
user / event
     ↓
identity + permissions
     ↓
load current data
     ↓
retrieve specification
     ↓
extract measurements
     ↓
deterministic comparison
     ↓
LLM interpretation
     ↓
report + citations
     ↓
human review
```

### Co se učím

- permissions,
- authoritative sources,
- orchestration,
- observability,
- end-to-end eval,
- business metric.

### Baseline

Nejdříve změřím současný lidský proces.

Například:

```text
human time
error rate
lead time
```

Potom stejnou práci provedu s AI.

### Výstup

Pilot report:

```text
quality
human time saved
errors
cost
limitations
recommended next step
```

### Hotovo, když

Umím udělat rozhodnutí:

```text
GO
ITERATE
REDESIGN
STOP
```

na základě dat.

---

## Projekt 10 — Multi-agentní systém s human approval

### Cíl

Teprve teď zkusit více agentů.

Ne proto, že multi-agent zní pokročileji.

Ale proto, abych ověřil, zda rozdělení rolí přináší měřitelnou hodnotu.

### Výchozí single-agent baseline

Nejdříve musí existovat jeden agent, který stejný use-case zvládá.

Potom jej rozdělím například:

```text
                 ORCHESTRATOR
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
     RESEARCHER     EXECUTOR     REVIEWER
          │            │            │
          └────────────┼────────────┘
                       ↓
                HUMAN APPROVAL
                       ↓
                    ACTION
```

### Role

**Researcher**

- read-only,
- hledá evidence,
- nemá write tools.

**Executor**

- používá úzké pracovní tools,
- pracuje v sandboxu.

**Reviewer**

- dostane zadání, výsledek a evidence,
- hledá chyby nezávisle.

**Human**

- schvaluje pouze citlivý finální krok.

### Co měřím

Multi-agent musí prokázat přínos proti single-agent baseline:

| Metrika | Single agent | Multi-agent |
|---|---:|---:|
| Success rate | | |
| Critical errors | | |
| Cost/task | | |
| Latency | | |
| Human correction | | |

### Co se učím

- handoffs,
- shared state,
- specialization,
- permission boundaries,
- independent review,
- orchestration.

### Hotovo, když

Dokážu věcně odpovědět:

> **Přinesli další agenti něco, co jeden agent neuměl dostatečně dobře?**

Pokud ne, správný výsledek experimentu může být:

```text
vrátit se k single-agent architektuře
```

To není neúspěch.

Je to dobré engineering rozhodnutí.

---

# Jak projekty verzovat

Každý projekt by měl mít jednoduchý adresář:

```text
project-05-rag/
│
├── README.md
├── data/
├── src/
├── evals/
├── results/
└── experiment-log.md
```

Do `README.md` zapíšu:

```text
GOAL
ARCHITECTURE
HOW TO RUN
SUCCESS CRITERIA
CURRENT RESULT
LIMITATIONS
```

A do experiment logu:

```text
datum
hypotéza
změna
výsledek
co jsem se naučil
```

Git pak vytvoří historii skutečného učení.

Ne pouze finálního stavu.

---

# Jedna společná metrika: roste moje schopnost systém vysvětlit?

Po každém projektu bych měl umět odpovědět:

```text
Co přesně tento systém dělá?
Kde bere informace?
Která část je pravděpodobnostní?
Která část je deterministická?
Jaká má oprávnění?
Jak ověřuji výsledek?
Co se stane při chybě?
```

Pokud umím pouze říct:

> „Nainstaloval jsem framework a nějak to funguje,“

experiment ještě nesplnil svůj účel.

Cílem této kuchařky není nasbírat deset technologií.

Cílem je postupně získat mentální model celého AI systému v praxi.

---

# Co si z kapitoly odnést

1. **Praktické učení má postupovat od jednoduchého systému ke složitějšímu, ne obráceně.**
2. **První projekty učí grounding, provenance a práci s vlastními daty ještě bez agentní složitosti.**
3. **Lokální model má smysl hodnotit vlastním benchmarkem, ne pouze podle velikosti.**
4. **RAG projekt musí měřit retrieval i answer quality.**
5. **Tool use je první krok od textové odpovědi k akci.**
6. **První agent má pracovat v omezeném sandboxu a mít jasný verifier.**
7. **Coding agent ukazuje sílu closed loopu díky Git a testům.**
8. **Firemní pilot musí porovnávat výsledek s baseline a business metrikou.**
9. **Multi-agent má být experiment proti single-agent baseline, ne automatický cíl.**
10. **Každý projekt má vytvořit artefakt, eval a konkrétní zkušenost, kterou lze později znovu použít.**

Těmito deseti projekty se uzavírá cesta, kterou kniha sleduje od začátku:

```text
MODEL
  ↓
CONTEXT
  ↓
KNOWLEDGE
  ↓
TOOLS
  ↓
AGENT
  ↓
SYSTEM
  ↓
VERIFICATION
  ↓
REAL WORK
```

A právě poslední šipka je nejdůležitější.

AI začne být opravdu zajímavá ve chvíli, kdy přestane být pouze tématem ke čtení a stane se měřitelnou součástí skutečné práce.