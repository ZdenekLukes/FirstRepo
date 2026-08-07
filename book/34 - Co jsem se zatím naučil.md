---
title: "34. Co jsem se zatím naučil"
part: "XIII — Co přijde dál"
status: personal-draft
version: "0.2"
updated: 2026-08-07
---

# 34. Co jsem se zatím naučil

> Osobní kapitola — průběžně doplňovat konkrétními experimenty, chybami a změnami názoru.

Když jsem se do AI začal ponořovat hlouběji, první přirozenou otázkou bylo:

> **Který model je nejlepší a co všechno už dnes dokáže?**

Po čase mi ale začala připadat zajímavější jiná otázka:

> **Jak z modelu postavit systém, který skutečně pomáhá v reálné práci?**

To je asi největší změna pohledu, kterou se snaží zachytit i celá tato kniha.

Na začátku je snadné vidět AI jako chytrý chat.

Potom člověk objeví:

- lokální modely,
- RAG,
- context engineering,
- tools,
- MCP,
- coding agents,
- agentní smyčky.

A začne být jasné, že samotný LLM je pouze jedna součást mnohem většího systému.

Tato kapitola proto není závěr ve smyslu:

> „Teď už AI rozumím.“

Spíše snapshot:

> **Takto ji chápu v srpnu 2026 a toto jsou věci, které mi dnes připadají nejdůležitější.**

---

## 34.1 Co jsem si o AI myslel na začátku

Na začátku je velmi snadné soustředit se na samotný model.

Otázky vypadají:

```text
GPT nebo Claude?
Kolik má parametrů?
Který vede benchmark?
Jak velký model rozběhnu lokálně?
```

To jsou stále legitimní otázky.

Jen dnes už je nevnímám jako hlavní.

Model bez dobrého contextu může být téměř k ničemu.

Model bez tools může pouze radit, ale nemůže ověřit výsledek.

A model bez dobře definovaného use-case může být jen velmi drahá hračka.

První mentální posun tedy je:

```text
AI ≠ model
```

Mnohem přesnější je:

```text
AI SYSTEM =
model
+
context
+
data
+
tools
+
workflow
+
verification
```

[DOPLNIT: vlastní konkrétní moment nebo experiment, kdy tento rozdíl začal být zřejmý.]

---

## 34.2 Co se ukázalo jako mylné

Několik intuitivních představ se ukázalo jako příliš jednoduchých.

### „Větší model vyřeší problém.“

Někdy ano.

Ale pokud model dostane špatný dokument nebo starou revizi, ani lepší reasoning nevytvoří správnou odpověď.

### „Dlouhý context znamená, že do něj můžu dát všechno.“

Technicky možná.

Prakticky tím můžeme zvýšit cenu a zároveň zhoršit relevance.

### „Když máme RAG, model zná firemní data.“

Ne.

RAG je search pipeline a její kvalita závisí na parsing, chunking, metadata, permissions a reranking.

### „Agent je LLM, který má delší prompt.“

Ne.

Agent je software se stavem, tools, smyčkou, verifierem a pravidly ukončení.

### „Open-weight znamená, že model snadno spustím lokálně.“

Také ne.

Model může mít otevřené váhy a přesto potřebovat stovky GB paměti.

Největší lekce je asi tato:

> **V AI je velmi snadné zaměnit hezkou abstrakci za fungující implementaci.**

---

## 34.3 Co mě překvapilo

Jedna věc mě překvapuje opakovaně: jak velký rozdíl dokáže vytvořit relativně jednoduché propojení modelu s nástrojem.

Například samotný LLM může udělat chybu v přesném výpočtu.

Přidáme Python:

```text
LLM
+
Python
```

a najednou máme mnohem spolehlivější data analysis.

Přidáme Git:

```text
LLM
+
filesystem
+
Git
+
tests
```

a vznikne coding agent.

Přidáme simulator:

```text
LLM
+
SPICE
+
measurement extraction
```

a vznikne základ engineering loopu.

To mi připadá důležitější než další drobný nárůst skóre benchmarku.

Druhé překvapení je, jak schopné mohou být relativně malé modely na úzkém dobře připraveném workflow.

Nemusí zvládat všechno.

Stačí, když velmi dobře zvládnou právě svou roli.

[DOPLNIT: konkrétní lokální model / coding / dokumentový experiment, který překvapil nejvíce.]

---

## 34.4 Co se ukázalo jako opravdu užitečné

Z toho, co jsem zatím zkoumal, mi dnes připadají nejpraktičtější hlavně tyto schopnosti.

### Práce s textem a dokumenty

```text
shrnutí
extrakce
porovnání
přepis
```

Nízká bariéra, okamžitá hodnota.

### Coding

Zvlášť když AI může:

```text
číst projekt
→ měnit soubory
→ spustit tests
```

### Search + RAG

Ne proto, že by vector database byla zázračná technologie.

Ale protože dostane firemní knowledge do pracovního contextu.

### Tool use

Zde se podle mě láme chatbot na pracovní systém.

### Automatická verifikace

Pokud můžu výsledek ověřit testem, databází nebo simulátorem, začínám AI věřit úplně jiným způsobem.

Právě kombinace:

```text
LLM flexibility
+
deterministic verification
```

mi dnes připadá jedna z nejsilnějších.

---

## 34.5 Co je podle mě jen hype

Nechci tuto část napsat jako seznam technologií, které „nefungují“.

V AI se situace mění příliš rychle.

Mnohem užitečnější je popsat typy tvrzení, vůči kterým jsem dnes skeptický.

### Demo bez baseline

```text
"Podívejte, AI vytvořila report za minutu."
```

Dobře.

Ale jak dlouho trval proces předtím a kolik je v reportu chyb?

### Multi-agent jen kvůli názvu

Pět agentů se stejným modelem a stejnými tools nemusí být lepších než jeden.

### Autonomie bez verifieru

Pokud agent výsledek sám prohlásí za správný, nemáme skutečný closed loop.

### „AI nahradí celý proces“ bez integrací

Pokud model nevidí data a nemá tools, zůstává poradce.

### Benchmark jako důkaz business value

Vyhrát benchmark neznamená vyhrát náš use-case.

Hype tedy podle mě není konkrétní technologie.

Hype je hlavně **přeskakování mezikroků mezi schopností modelu a reálným výsledkem**.

---

## 34.6 Cloud vs. local — jak se změnil můj pohled

Cloud a local je snadné chápat jako souboj dvou táborů.

Dnes mi dává větší smysl přemýšlet po úlohách.

### Local

Je velmi zajímavý pro:

- citlivá data,
- vysoký stabilní workload,
- experimentování,
- malé specializované modely.

### Cloud

Je obtížné ignorovat tam, kde potřebujeme:

- frontier reasoning,
- rychlý přístup k novým schopnostem,
- elasticitu.

Proto mi dnes nejlogičtější připadá hybrid:

```text
local where it makes sense
cloud where it adds real value
policy decides what can go where
```

To není kompromis.

Je to routing problém.

[DOPLNIT: vlastní zkušenosti s konkrétním hardware a modely — rychlost, VRAM, co už bylo překvapivě použitelné a co ne.]

---

## 34.7 Od chatbotu k agentům

Chatbot byl důležitý, protože ukázal, že s modelem lze komunikovat přirozeným jazykem.

Ale coding agents mi připadaly jako další zásadní krok.

Najednou AI:

```text
nejen odpovídá
```

ale:

```text
hledá
→ upravuje
→ spouští
→ kontroluje
→ opravuje
```

To je jiná kategorie nástroje.

A právě zde začíná být zřejmé, že podobný pattern lze přenést mimo coding.

Například:

```text
engineering
→ documentation
→ simulation
→ verification
```

Agent podle mě není „digitální zaměstnanec“ v jednoduchém smyslu.

Je to nový způsob, jak skládat software kolem LLM.

---

## 34.8 Proč je nejcennější context a přístup k nástrojům

Když model neví, co jsme rozhodli včera, není řešením nutně větší model.

Potřebuje memory nebo access k našim notes.

Když nezná dnešní data, potřebuje search.

Když má spočítat přesnou statistiku, potřebuje Python.

Když má ověřit obvod, potřebuje simulator.

Proto dnes často přemýšlím:

```text
Co modelu chybí k tomu,
aby mohl úlohu správně dokončit?
```

Možné odpovědi:

- informace,
- tool,
- permission,
- verifier.

Až potom:

- inteligence.

To je pro mě velký posun od čistého model-centric pohledu.

---

## 34.9 Proč nestačí nejlepší model

Představme si nejlepší model na světě.

Dáme mu:

```text
obsolete specification
```

Dostaneme velmi inteligentní odpověď nad špatným zdrojem.

Nebo mu dáme:

```text
root shell
+
špatné permission rules
```

Dostaneme velmi schopný rizikový systém.

Nebo:

```text
žádný verifier
```

Dostaneme odpovědi, kterým se obtížně věří.

Proto nejlepší model může být nejlepší **komponenta**.

Není automaticky nejlepší systém.

---

## 34.10 Proč je důležitější celý systém

Dnes bych AI stack viděl asi takto:

```text
                    USER
                      ↓
                   INTENT
                      ↓
                 AI SYSTEM
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
      MODEL        CONTEXT        TOOLS
        ↓             ↓             ↓
        └─────────────┼─────────────┘
                      ↓
                  EVIDENCE
                      ↓
                 VERIFICATION
                      ↓
              OUTPUT / ACTION
```

Kolem toho:

```text
security
permissions
memory
logging
evals
```

Model můžeme vyměnit.

Ale integrace, data, evals a knowledge, které jsme vybudovali, zůstávají.

To mi dnes připadá jako mnohem trvalejší investice.

---

## 34.11 Co bych dnes udělal jinak

Kdybych začínal znovu, pravděpodobně bych méně času věnoval hledání „nejlepšího“ modelu a dříve bych stavěl malé end-to-end experimenty.

Například:

```text
1. jeden dokument
2. jeden lokální model
3. jeden tool
4. jeden RAG
5. jeden agent
6. jeden reálný workflow
```

U každého bych měřil:

```text
co fungovalo
co selhalo
proč
```

Také bych dříve rozlišoval:

```text
MODEL PROBLEM
vs.
CONTEXT PROBLEM
vs.
TOOL PROBLEM
vs.
DATA PROBLEM
```

Protože bez tohoto rozdělení je snadné vyměňovat modely a vůbec neopravit skutečnou příčinu.

A hlavně bych se dříve soustředil na **closed loop**.

Ne pouze:

```text
AI něco navrhne
```

ale:

```text
AI navrhne
→ nástroj provede
→ systém změří
→ výsledek se ověří
```

Tam podle mě začíná nejzajímavější část celé technologie.

---

# Pracovní závěr

Kdybych měl svůj dnešní pohled zkrátit do jedné věty:

> **Nejdůležitější není mít nejchytřejší model, ale umět mu ve správný okamžik dodat správný kontext a nástroje a jeho výsledek spolehlivě ověřit.**

Tato věta se možná za několik let změní.

A právě proto má smysl tuto kapitolu průběžně aktualizovat.

Ne jako historii technologií.

Ale jako historii vlastního porozumění.
