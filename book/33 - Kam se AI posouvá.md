---
title: "33. Kam se AI posouvá"
part: "XIII — Co přijde dál"
status: draft
version: "0.2"
updated: 2026-08-07
snapshot: "2026-08-07"
---

# 33. Kam se AI posouvá

Předpovídat AI několik let dopředu je nevděčná disciplína.

V posledních letech se opakovaně ukázalo, že:

- některé schopnosti přišly rychleji, než se čekalo,
- jiné vypadají v demu lépe než v produkci,
- ceny a velikosti modelů se mění velmi rychle.

Proto tato kapitola není seznam jistých předpovědí.

Je to mapa trendů, které jsou v srpnu 2026 dobře viditelné.

Nejdůležitější změna podle mě není jedna konkrétní schopnost modelu.

Je to posun:

```text
MODEL
"odpověz mi"
```

směrem k:

```text
SYSTEM
"vezmi tento cíl, použij data a nástroje,
pracuj několik kroků a přines ověřený výsledek"
```

To je hlavní osa celé knihy.

---

## 33.1 Silnější reasoning

Modely jsou stále lepší v úlohách, které vyžadují více kroků.

Trend je zároveň směrem k **adaptivnímu inference compute**.

Jednoduchý dotaz nepotřebuje stejnou práci jako těžký technický problém.

Budoucí systém může automaticky rozhodovat:

```text
simple task
→ fast / low reasoning

complex decision
→ deeper reasoning

critical decision
→ reasoning + tools + verifier
```

To je ekonomicky důležitější než pouze zvyšovat inteligenci každého requestu.

Silnější reasoning ale pravděpodobně neodstraní potřebu evidence.

Čím složitější problém, tím důležitější bude:

- tool use,
- external verification,
- source grounding.

---

## 33.2 Levnější inference

Historický trend AI compute je dvojí.

Nejlepší modely mohou být výpočetně náročnější.

Současně ale inference stejné úrovně schopností postupně zlevňuje díky:

- lepším modelům,
- quantization,
- sparsity / MoE,
- lepším GPU/accelerators,
- inference optimization,
- caching.

To má zásadní důsledek.

Úloha, která je dnes příliš drahá na použití 10 000× denně, může být za několik let běžný background proces.

Proto se nemění pouze cena existujících use-cases.

Vznikají **nové use-cases, které ekonomicky dříve nedávaly smysl**.

---

## 33.3 Menší a schopnější lokální modely

Menší modely se rychle zlepšují.

To podporuje několik trendů:

```text
local AI
edge AI
private AI
specialized models
```

Není pravděpodobné, že malý model na notebooku bude vždy stejně schopný jako nejdražší frontier systém.

Ale nemusí být.

Pokud úloha je:

- extraction,
- classification,
- function calling,
- local coding,
- routing,

může malý model stačit.

Budoucí AI stack proto může připomínat hierarchii:

```text
small local model
→ 80 % jednoduchých kroků

large local/server model
→ harder internal tasks

frontier cloud
→ exceptional reasoning
```

To je zároveň výkonová, ekonomická i bezpečnostní architektura.

---

## 33.4 Delší context

Context windows dál rostou.

To usnadňuje práci s:

- celými dokumenty,
- větší částí codebase,
- dlouhou historií agentního tasku.

Ale není pravděpodobné, že delší context zruší retrieval.

Důvody:

```text
více tokenů
→ vyšší cost
→ vyšší latency
→ více noise
```

A hlavně:

> Mít informaci někde v contextu není totéž jako ji správně použít.

Proto očekávám, že dlouhý context a RAG budou spolupracovat.

RAG vybere relevantní data.

Velký context umožní vložit širší okolí, když je potřeba.

---

## 33.5 Trvalejší memory

Dnešní chat history není skutečná robustní dlouhodobá paměť agenta.

Budoucí systémy budou pravděpodobně lépe řešit:

- co uložit,
- co zapomenout,
- jak aktualizovat zastaralý fakt,
- jak zachovat provenance,
- jak memory chránit proti poisoning.

Memory bude mít několik vrstev:

```text
working state
project memory
user preferences
validated facts
archive
```

Největší problém nebude kapacita.

Bude to **správa pravdy v čase**.

Například:

```text
VDD was 1.8 V in revision B
VDD is 1.2 V in revision C
```

Systém nemá „zapomenout“ historii.

Musí chápat temporalitu a autoritu informace.

---

## 33.6 Multimodalita

Rozdělení na:

```text
text model
vision model
audio model
```

se bude pro uživatele dále rozmazávat.

AI systém může přirozeně pracovat s:

- textem,
- obrazem,
- hlasem,
- videem,
- obrazovkou počítače.

To je zásadní pro engineering.

Reálná informace není pouze text.

Je v:

- schematic,
- plotu,
- waveform,
- microscope image,
- screenshotu nástroje.

Multimodalita může agentům umožnit pracovat s mnohem větší částí reálného pracovního prostředí.

---

## 33.7 Computer use

Pokud aplikace nemá API, AI může někdy používat její UI podobně jako člověk.

```text
screenshot
→ vision model
→ click / type
→ new screenshot
```

To dramaticky rozšiřuje počet nástrojů, které lze automatizovat.

Ale UI automation je obecně křehčí než API.

Změní se tlačítko nebo dialog a workflow může selhat.

Proto bych očekával hierarchii:

```text
API / MCP
→ preferred

CLI
→ excellent

computer use
→ fallback for systems without integration
```

Computer use je mimořádně silný most ke starším firemním aplikacím.

Není ale náhradou dobře navrženého API tam, kde jej můžeme mít.

---

## 33.8 Agentní software

Dnešní software je navržen hlavně pro člověka:

```text
menu
forms
dashboards
```

Budoucí software může být navržen pro dvě skupiny uživatelů:

```text
HUMAN
+
AGENT
```

To znamená:

- jasná API,
- machine-readable state,
- audit,
- scoped permissions,
- event streams,
- agent-friendly documentation.

Aplikace nebude pouze „mít chatbot“.

Může být **agent-ready**.

Podobně jako dnes software navrhujeme cloud-native nebo API-first.

---

## 33.9 Background agents

Mnoho agentních úloh nemusí probíhat v interaktivním chatu.

Například:

```text
každou noc
→ zkontroluj nové regression failures
```

nebo:

```text
když přijde nová spec revision
→ compare against current requirements
```

Agent se stává background workerem.

To vyžaduje:

- scheduler/event trigger,
- state,
- checkpoint,
- notification policy,
- audit.

Background agents mohou mít obrovský dopad, protože pracují i tehdy, když člověk aktivně nepíše prompt.

Ale právě proto potřebují výrazně silnější guardrails než jednorázový chat.

---

## 33.10 AI + robotics

Robotika přidává AI fyzické tělo.

Zatímco software agent může omylem změnit soubor, robot může poškodit reálný objekt.

Proto je potřeba ještě silnější separation:

```text
LLM planning
↓
robot policy / controller
↓
physical action
↓
sensors
↓
verification
```

LLM pravděpodobně nebude přímo řídit každý motorový proud.

Stejně jako v engineeringu bude fungovat na vyšší úrovni a deterministické control loops zůstanou níže.

---

## 33.11 AI + simulace

Toto je jedna z oblastí, které považuji za zvlášť zajímavé.

AI je pravděpodobnostní.

Simulator je deterministický model reality.

Kombinace vytváří loop:

```text
AI
→ hypothesis

SIMULATION
→ evidence

AI
→ updated hypothesis
```

To lze použít v:

- electronics,
- mechanical design,
- fluid dynamics,
- chemistry,
- manufacturing.

AI nemusí fyziku znát dokonale ve svých vahách.

Může umět **správně organizovat experimenty nad fyzikálním modelem**.

To je velmi silný koncept.

---

## 33.12 AI + věda a engineering

Vědecká práce má podobnou smyčku:

```text
hypothesis
→ experiment
→ data
→ analysis
→ new hypothesis
```

AI může pomáhat v každém kroku:

- literature search,
- návrh experimentu,
- code,
- data analysis,
- anomaly detection.

Ale vědecká validita stále vyžaduje:

- reprodukovatelnost,
- evidence,
- metodologii.

Nejzajímavější systémy tedy pravděpodobně nebudou „AI, která ví všechno“.

Budou to systémy, které umějí **rychleji uzavírat experimentální smyčku**.

---

## 33.13 Personal AI

Osobní AI se může posunout od generického chatu k dlouhodobému pracovnímu partnerovi.

Bude znát:

- projekty,
- notes,
- historii rozhodnutí,
- preference,
- dostupné tools.

Ale právě zde je kritická privacy.

Čím užitečnější personal AI je, tím více citlivého contextu může mít.

Proto budou důležité architektury:

```text
local memory
+
local processing
+
selective cloud reasoning
```

Personal AI může být velmi přirozeným příkladem hybridního systému.

---

## 33.14 Enterprise AI

Enterprise AI se podle mě bude méně točit kolem otázky:

> „Který chatbot zaměstnanci používají?“

A více kolem platformy:

```text
identity
model gateway
data access
RAG
MCP/tools
agent runtime
evals
observability
security
```

Nad touto vrstvou mohou vznikat desítky use-cases.

Firma tak nebude budovat jeden velký „AI projekt“.

Bude budovat **AI operating layer** pro své digitální procesy.

To je podobné jako cloud platforma nebo data platforma.

---

## 33.15 Co může změnit další zásadní průlom

Existují trendy, které lze extrapolovat.

A potom průlomy, které neumíme předvídat.

Zásadní změnu by mohl způsobit například skok v:

- efektivitě trainingu,
- dlouhodobém reasoningu,
- spolehlivé memory,
- continual learning,
- hardware,
- autonomní verifikaci,
- robotics.

Ale je užitečné navrhovat systém tak, aby na konkrétním průlomu nebyl závislý.

Například:

```text
MODEL GATEWAY
```

umožňuje vyměnit model.

```text
TOOL INTERFACE
```

umožňuje zachovat integrace.

```text
EVAL SUITE
```

umožňuje ověřit, zda nový model skutečně pomáhá.

To je možná nejlepší příprava na nejistou budoucnost:

> **Nestavět systém kolem jednoho modelu. Stavět capability, která umí nové modely rychle absorbovat a měřit.**

---

# Co považuji za nejpravděpodobnější směr

Ne jednu AGI aplikaci, která všechno nahradí.

Spíše stále hustší vrstvu AI uvnitř existující práce:

```text
HUMAN
  ↓
AI ORCHESTRATOR
  ↓
models + tools + company data + simulation
  ↓
verified artifacts
  ↓
HUMAN DECISION / AUTOMATED ACTION
```

Autonomie bude růst tam, kde:

- je úloha digitální,
- výsledek je ověřitelný,
- cena chyby je zvládnutelná,
- máme dobré tools a permissions.

Pomaleji poroste tam, kde je:

- nejasný cíl,
- vysoká odpovědnost,
- obtížná verifikace.

---

# Co si z kapitoly odnést

1. **Budoucnost AI je nejistá, ale posun od modelu k celému agentnímu systému je už dobře viditelný.**
2. **Reasoning bude pravděpodobně stále více adaptovat množství compute podle obtížnosti úkolu.**
3. **Levnější inference otevře use-cases, které dnes ekonomicky nedávají smysl.**
4. **Malé lokální a specializované modely budou důležitou součástí model routingu.**
5. **Dlouhý context retrieval nezruší; obě techniky se doplňují.**
6. **Memory bude hlavně problém validity, provenance a bezpečnosti, ne pouze kapacity.**
7. **Computer use otevře staré aplikace agentům, ale API/MCP zůstává robustnější cesta.**
8. **Background agents přesouvají AI z chatovacího okna do průběžné práce.**
9. **Spojení AI se simulací a experimentem může mít zásadní dopad na science a engineering.**
10. **Nejlepší příprava na další průlom je modulární architektura, tools a evals, které dovolí nový model rychle vyměnit a otestovat.**

Po celé knize jsme se posouvali od historie přes LLM až k agentním systémům.

Teď je čas vrátit se od technologie k osobnímu pohledu:

> **Co jsem se zatím o AI skutečně naučil?**
