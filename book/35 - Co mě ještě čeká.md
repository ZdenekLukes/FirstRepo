---
title: "35. Co mě ještě čeká"
part: "XIII — Co přijde dál"
status: roadmap-draft
version: "0.2"
updated: 2026-08-07
---

# 35. Co mě ještě čeká

<!-- visual:35-learning-roadmap.svg -->

![Roadmapa dalšího učení](assets/diagrams/35-learning-roadmap.svg)

*Obrázek: Lokální stack → RAG → tools → agent → production.*


> Roadmapa dalšího učení a experimentů.

Po třiceti čtyřech kapitolách by se mohlo zdát, že jsme prošli téměř všechno důležité.

Ve skutečnosti je velká část témat zatím pochopená hlavně **konceptuálně**.

Další fáze musí být mnohem praktičtější.

Ne:

```text
přečíst další článek o agentech
```

ale:

```text
postavit agenta
→ změřit
→ rozbít
→ opravit
```

Proto tuto kapitolu chápu jako roadmapu experimentů, které postupně promění znalost z knihy ve vlastní zkušenost.

Hlavní princip:

> **Každý další krok má skončit fungujícím artefaktem nebo měřitelným experimentem, ne pouze dalším seznamem poznámek.**

---

## 35.1 Postavit kvalitní lokální AI stack

První cíl je mít lokální prostředí, které je jednoduché, reprodukovatelné a dostatečně otevřené pro experimenty.

Minimální architektura:

```text
hardware
↓
model runtime
↓
OpenAI-compatible API
↓
chat UI
↓
Python / tools
↓
logging
```

Prakticky chci umět:

- vyměnit model bez změny celé aplikace,
- měřit tokens/s a latency,
- sledovat RAM/VRAM,
- připojit agent framework nebo vlastní skript.

**Výstup:** dokumentovaný lokální stack, který lze znovu postavit od nuly.

---

## 35.2 Prakticky otestovat více lokálních modelů

Modely nechci hodnotit podle pocitu z chatu.

Vytvořím malý vlastní benchmark.

Například:

```text
5× summarization
5× extraction
5× coding
5× technical reasoning
5× tool calling
```

U každého modelu změřím:

- kvalitu,
- tokens/s,
- TTFT,
- RAM/VRAM,
- stability,
- success rate.

**Výstup:** tabulka vlastních výsledků pro konkrétní hardware.

---

## 35.3 Postavit vlastní RAG

Ne pouze nahrát PDF do hotové aplikace.

Chci si projít celý pipeline:

```text
document
→ parse
→ chunk
→ embed
→ index
→ retrieve
→ rerank
→ answer + citation
```

A hlavně vytvořit test set.

Například 50 otázek, u kterých znám správný dokument a odpověď.

Pak mohu měnit:

- chunk size,
- embedding model,
- hybrid search,
- reranker,

a vidět reálný dopad.

**Výstup:** RAG s měřitelným retrieval a answer score.

---

## 35.4 Postavit druhý mozek

Druhý mozek nechci chápat jako „naházet všechno do vector database“.

Chci oddělit:

```text
RAW ARCHIVE
KNOWLEDGE
WORKING PROJECTS
```

A zachovat člověkem čitelnou vrstvu například v Markdownu.

AI nad ní dostane:

- search,
- RAG,
- summary,
- linking.

**Experiment:** položit systému otázky, které dnes vyžadují ruční hledání napříč poznámkami a dokumenty.

**Výstup:** fungující osobní knowledge workflow, ne pouze index.

---

## 35.5 Připojit AI k reálným nástrojům

Další velký krok je tool use.

Začnu read-only nástroji.

Například:

```text
filesystem search
Git read
web
Python
```

Potom sandbox writes.

Cílem je pochopit:

- function calling,
- schema design,
- error handling,
- permissions.

**Výstup:** agent, který dokáže kombinovat minimálně tři tools v jednom workflow.

---

## 35.6 Postavit jednoho spolehlivého agenta

Ne multi-agent.

Jeden agent.

Jeden use-case.

Například:

```text
input documents
→ research
→ structured report
→ citation verification
```

nebo technická úloha:

```text
results
→ analysis
→ deterministic check
→ report
```

Cílem není autonomie.

Cílem je success rate.

**Výstup:** agent s minimálně 50 historickými eval cases a známou úspěšností.

---

## 35.7 Postavit multi-agentní workflow

Až potom rozdělit jednu část práce.

Například:

```text
researcher
↓
writer
↓
reviewer
```

A porovnat proti single-agent baseline.

Měřit:

```text
quality
cost
latency
errors
```

Pokud multi-agent nepřináší měřitelnou výhodu, vrátit se k jednoduššímu systému.

**Výstup:** data, ne pouze dojem, zda multi-agent stojí za komplikaci.

---

## 35.8 Vyřešit memory

Memory budu přidávat až po agentovi, který funguje bez ní.

Potřebuji otestovat:

- co ukládat,
- jak memory aktualizovat,
- jak řešit obsolete facts,
- jak memory znovu retrieve,
- jak zabránit poisoning.

Experiment:

```text
agent pracuje na projektu několik týdnů
→ musí si pamatovat decisions
→ ale respektovat nové revisions
```

**Výstup:** strukturovaná project memory s provenance a timestamps.

---

## 35.9 Vyřešit observability

Agent, kterému nevidím do workflow, se špatně ladí.

Potřebuji sledovat:

```text
run
step
model call
tool call
retrieval
latency
tokens
cost
error
```

A mít jednoduchý trace viewer.

**Výstup:** schopnost otevřít failed run a během několika minut určit, kde selhal.

---

## 35.10 Vyřešit evaluaci

Eval není poslední krok.

Musí doprovázet všechny experimenty.

Potřebuji:

```text
golden set
automatic checks
human rubric
regression suite
```

Každá změna modelu nebo promptu pak projde stejnými testy.

**Výstup:** jeden příkaz nebo workflow, který spustí kompletní regression eval.

---

## 35.11 Bezpečný on-prem agentní systém

Další milestone je malý interní stack pro citlivá data.

Architektura:

```text
internal network
↓
model server
↓
identity / policy
↓
read-only knowledge
↓
approved tools
↓
audit
```

Začít bez production write.

Ověřit:

- isolation,
- secrets,
- permissions,
- logs,
- prompt injection behavior.

**Výstup:** threat model + bezpečnostní checklist + funkční pilot.

---

## 35.12 Propojení s engineering tools

Toto je pro mě jedna z nejzajímavějších částí.

Ne chat nad dokumentací, ale closed loop:

```text
specification
→ agent
→ engineering tool
→ result
→ verifier
→ next step
```

První nástroj může být jednoduchý simulátor.

Později specializovaný firemní CAD.

**Výstup:** jeden reálný engineering workflow, který agent zvládne od zadání po ověřený report.

---

## 35.13 Měřitelný firemní pilot

Technický experiment není ještě business pilot.

Potřebuji:

```text
baseline
users
real data
metrics
risk owner
go/no-go criteria
```

Ideální první pilot má nízké riziko a snadno měřitelný výsledek.

Například:

- document search,
- verification triage,
- report generation.

**Výstup:** krátký evidence report pro management: co fungovalo, co ne, kolik to ušetřilo a co doporučujeme dál.

---

## 35.14 Od experimentu k produkčnímu systému

Poslední krok je záměrně nejnudnější.

A proto důležitý.

Produkce potřebuje:

```text
owner
SLA
monitoring
security
versioning
rollback
evals
support
cost control
```

Experiment může být postavený jedním člověkem za víkend.

Produkční systém musí přežít:

- změnu modelu,
- dovolenou autora,
- outage,
- security review,
- změnu dat.

**Výstup:** AI služba, kterou lze provozovat jako normální software.

---

# Navržené pořadí experimentů

Roadmapa by neměla být paralelních čtrnáct projektů.

Dává mi smysl toto pořadí:

```text
1  Local stack
2  Model benchmark
3  RAG
4  Tool use
5  Single agent
6  Evals + observability
7  Second brain / memory
8  Multi-agent experiment
9  Engineering integration
10 Secure on-prem pilot
11 Business pilot
12 Production
```

Některé kroky se budou překrývat.

Ale pořadí drží jednu zásadu:

> **Nejdříve jednoduchý systém, který umím měřit. Teprve potom složitost.**

---

# Jak poznám, že jsem se skutečně něco naučil

Ne podle počtu přečtených článků.

Ale podle toho, zda umím odpovědět:

```text
Proč tento systém selhal?
```

A mám evidence.

Například:

```text
model nebyl problém
retrieval našel obsolete dokument
```

nebo:

```text
agent uměl úlohu vyřešit,
ale tool schema vedlo k chybné akci
```

nebo:

```text
multi-agent zvýšil cost 3×
a quality jen o 1 %
```

To jsou zkušenosti, které se z tutorialu získávají těžko.

---

# Co si z kapitoly odnést

1. **Další fáze učení má být experimentální, ne pouze informační.**
2. **Každý krok má skončit artefaktem, benchmarkem nebo evalem.**
3. **Nejdříve má smysl postavit jednoduchý local stack, RAG a single-agent workflow.**
4. **Memory a multi-agent přidáváme až tehdy, když máme konkrétní důvod.**
5. **Observability a evaluace nejsou produkční bonus — jsou součást učení.**
6. **Engineering integration je nejzajímavější ve chvíli, kdy uzavírá smyčku přes skutečný nástroj a verifier.**
7. **Firemní pilot potřebuje baseline, reálné uživatele a go/no-go criteria.**
8. **Produkce znamená ownership, security, monitoring, versioning a support.**

Poslední část knihy už nebude teorie.

Bude to kuchařka:

> **Jaký minimální stack potřebuji a jaké projekty mám skutečně postavit?**
