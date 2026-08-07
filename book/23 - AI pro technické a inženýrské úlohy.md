---
title: "23. AI pro technické a inženýrské úlohy"
part: "IX — AI jako pracovní systém"
status: draft
version: "0.2"
updated: 2026-08-07
---

# 23. AI pro technické a inženýrské úlohy

<!-- visual:23-engineering-loop.svg -->

![AI a deterministické engineering nástroje](assets/diagrams/23-engineering-loop.svg)

*Obrázek: LLM orchestruje; specializovaný nástroj rozhoduje fyziku.*


Engineering je pro AI velmi zajímavé prostředí.

Na jedné straně obsahuje mnoho nestrukturovaných informací:

- specifikace,
- datasheety,
- design notes,
- e-maily,
- review comments.

Na druhé straně má velmi silné deterministické nástroje:

- simulátory,
- solvery,
- compilers,
- CAD,
- měřicí přístroje,
- verification frameworks.

To je ideální kombinace.

LLM může dělat to, v čem je dobrý:

```text
porozumění zadání
→ práce s dokumenty
→ plánování
→ generování skriptů
→ interpretace výsledků
```

A klasický engineering software může dělat to, v čem je dobrý on:

```text
výpočet
→ simulace
→ fyzikální model
→ měření
→ deterministická kontrola
```

> **Nejzajímavější engineering AI není náhrada simulátoru. Je to inteligentní vrstva, která dokáže simulátor a další nástroje správně použít.**

---

## 23.1 AI jako technický asistent

Nejjednodušší role je technický asistent.

Může pomáhat například s:

- vysvětlením neznámého pojmu,
- hledáním v dokumentaci,
- porovnáním variant,
- přípravou checklistu,
- převodem poznámek do reportu,
- psaním skriptů.

Výhoda proti klasickému search je schopnost spojit kontext.

Například:

> „Porovnej tyto dvě architektury z hlediska power, area a testability a vyznač, které závěry jsou podložené našimi daty a které jsou pouze obecná inference.“

Takový úkol kombinuje:

- retrieval,
- reasoning,
- strukturovaný výstup.

Důležité je, aby AI oddělovala:

```text
FACT FROM SOURCE
```

od

```text
ENGINEERING INFERENCE
```

To je u technické práce zásadní.

---

## 23.2 Dokumentace

Technici tráví značnou část práce dokumentací.

AI může pomoci například:

```text
raw measurement notes
→ structured report
```

```text
code / schematic changes
→ release notes
```

```text
long design review
→ decisions + actions
```

Ale dokumentace není pouze textová kosmetika.

Musí správně zachytit:

- čísla,
- units,
- conditions,
- version,
- evidence.

Proto je vhodné generovat text z předem extrahovaných strukturovaných dat.

Například:

```json
{
  "gain_db": 62.4,
  "corner": "TT_25C",
  "spec_min_db": 60,
  "status": "PASS"
}
```

LLM z toho vytvoří vysvětlení.

Nesmí si číslo sám odhadnout ze screenshotu, pokud máme k dispozici přesný measurement output.

---

## 23.3 Datasheety

Datasheet je typický zdroj, který člověk dobře chápe vizuálně, ale automatizace s ním bojuje.

Obsahuje:

- tables,
- graphs,
- footnotes,
- conditions,
- timing diagrams.

AI může pomoci:

- najít relevantní parametr,
- vysvětlit podmínky,
- porovnat dva komponenty,
- extrahovat parametry do tabulky.

Ale musí zachovat vazbu:

```text
VALUE
+
UNIT
+
CONDITION
+
FOOTNOTE
+
SOURCE
```

Například údaj:

```text
Iq = 3 µA typ.
```

může být velmi zavádějící bez informace:

```text
VIN = 3.3 V
no load
25 °C
```

Technický RAG proto nemůže zacházet s parametrem jako s izolovaným slovem a číslem.

---

## 23.4 Specifikace

Specifikace je pro engineering agenta jeden z nejdůležitějších zdrojů pravdy.

Agent může:

- extrahovat requirements,
- najít rozpory,
- mapovat requirements na tests,
- porovnat revisions,
- zjistit missing verification.

Je velmi užitečné převést požadavky do struktury:

```json
{
  "id": "REQ-174",
  "parameter": "startup_time",
  "operator": "<",
  "value": 120,
  "unit": "us",
  "conditions": {
    "temperature": "-40..125C"
  },
  "source": "Spec C §7.4"
}
```

Pak lze část vyhodnocení provádět deterministicky.

LLM může stále řešit složité textové podmínky, ale výsledná kontrola se stává auditovatelnější.

---

## 23.5 Skripty

Engineering obsahuje obrovské množství malých skriptů.

Například:

- parsing results,
- data conversion,
- sweep generation,
- plotting,
- report generation.

To je ideální use-case pro coding model.

Například:

> „Načti všechny CSV z této directory, normalizuj názvy corners a vytvoř summary tabulku podle tohoto schema.“

Agent může:

```text
inspect files
→ write Python
→ run
→ inspect output
→ repair
```

Člověk nemusí programovat každý jednorázový pomocný nástroj ručně.

To může dramaticky snížit bariéru automatizace malých úloh, které se dříve „nevyplatilo skriptovat“.

---

## 23.6 Simulace

Simulace je pro agentní AI téměř ideální nástroj.

Má:

- definovaný vstup,
- reprodukovatelný výpočet,
- strukturovaný výstup.

Agent může například:

```text
vybrat testbench
↓
nastavit parameters
↓
spustit simulator
↓
čekat na completion
↓
extrahovat measurements
```

Důležité je nevystavit agentovi nutně celý shell.

Lepší jsou úzké tools:

```text
list_testbenches()
run_simulation()
get_measurements()
```

To omezuje prostor chyb a zvyšuje bezpečnost.

---

## 23.7 Analýza výsledků

Simulátor může vyprodukovat tisíce čísel.

LLM není nejlepší nástroj pro jejich numerické zpracování.

Pipeline může být:

```text
raw simulator output
↓
Python / measurement engine
↓
structured metrics
↓
LLM
↓
interpretation
```

Například Python spočítá:

- min/max,
- yield,
- worst corner,
- delta proti baseline.

LLM potom vysvětlí:

> „Největší degradace nastává v SS při -40 °C a koreluje s prodloužením startupu.“

A odkáže na přesná data.

---

## 23.8 Optimalizační smyčka

Jakmile dokážeme:

```text
změnit parametry
→ simulovat
→ vyhodnotit
```

můžeme vytvořit optimalizační smyčku.

```text
TARGET SPEC
    ↓
select candidate parameters
    ↓
simulation
    ↓
measurements
    ↓
compare with target
    ↓
choose next candidate
    ↓
repeat
```

LLM zde může navrhovat další experiment podle trendu.

Ale nemusí být nejlepší optimizer pro všechny problémy.

Pokud máme čistě numerickou objective function, může být vhodnější:

- Bayesian optimization,
- gradient method,
- evolutionary algorithm,
- grid / adaptive sweep.

LLM je zajímavý tam, kde optimalizace kombinuje čísla s engineering heuristikou a volbou strategie.

---

## 23.9 LLM + klasický simulátor

Toto spojení je velmi silné, protože obě komponenty mají opačné vlastnosti.

### LLM

Silné:

- flexibilní reasoning,
- text,
- heuristika,
- plánování.

Slabé:

- numerická přesnost,
- fyzikální garance.

### Simulator

Silný:

- fyzikální model,
- přesný definovaný výpočet,
- reprodukovatelnost.

Slabý:

- sám neví, co chceme zkoumat,
- nevysvětluje automaticky design trade-off.

Kombinace:

```text
LLM
→ navrhne experiment

SIMULATOR
→ vytvoří evidence

LLM
→ interpretuje evidence
```

To je obecný pattern použitelný daleko za electronics.

---

## 23.10 Proč AI nemá nahrazovat fyzikální simulaci

LLM může mít velmi dobrou intuici.

Může například říct:

> „Zvětšení tranzistoru pravděpodobně sníží mismatch.“

To je obecně rozumná engineering knowledge.

Ale skutečný návrh závisí na:

- technologii,
- bias point,
- parasitics,
- topology,
- corners.

Model nemá být zdrojem finálního fyzikálního výsledku.

Při otázce:

> „Splní tento circuit stability přes všechny PVT?“

správná cesta není:

```text
LLM thinks yes
→ PASS
```

ale:

```text
LLM determines required verification
→ simulator executes
→ measurements extracted
→ limits evaluated
```

> **AI může navrhovat hypotézy. Simulator rozhoduje o tom, co daný model obvodu skutečně predikuje.**

A měření následně rozhoduje o skutečném siliconu.

---

## 23.11 Agent jako orchestrátor deterministických nástrojů

Tím se dostáváme k nejpraktičtější definici engineering agenta.

Není to virtuální inženýr, který všechno ví.

Je to orchestrátor:

```text
                ENGINEER
                   ↓
                 AGENT
       ┌───────────┼───────────┐
       ↓           ↓           ↓
 documentation   Python     simulator
       ↓           ↓           ↓
       └───────────┼───────────┘
                   ↓
                evidence
                   ↓
              verification
                   ↓
                ENGINEER
```

Agent dokáže:

1. pochopit cíl,
2. najít správné zdroje,
3. vytvořit plán experimentu,
4. použít nástroje,
5. spojit výsledky,
6. označit uncertainty,
7. připravit rozhodnutí pro člověka.

Člověk zůstává ownerem engineering rozhodnutí.

To není slabší vize AI.

Naopak je to realistická cesta k velmi silnému systému.

---

# Stupně engineering autonomie

Můžeme postupovat postupně.

```text
LEVEL 1
AI vysvětluje dokumenty

LEVEL 2
AI generuje scripts a analysis

LEVEL 3
AI spouští read-only / sandbox simulations

LEVEL 4
AI navrhuje další experiments podle výsledků

LEVEL 5
AI optimalizuje v omezeném design space

LEVEL 6
AI navrhuje změnu a člověk ji schvaluje
```

Nemusíme mířit rovnou na autonomní design.

Velká hodnota může vzniknout už na úrovních 2–4.

---

# Co si z kapitoly odnést

1. **Engineering kombinuje nestrukturované znalosti s velmi kvalitními deterministickými nástroji.**
2. **AI je silný technický asistent pro dokumenty, datasheety, specifications a scripting.**
3. **Numerická data má zpracovat vhodný výpočetní nástroj; LLM je interpretuje.**
4. **Simulation je ideální zdroj zpětné vazby pro agentní smyčku.**
5. **LLM nemusí být nejlepší numerický optimizer; může orchestravat specializovaný optimalizační algoritmus.**
6. **AI nemá nahrazovat fyzikální simulaci — má rozhodovat, co simulovat a jak výsledky použít.**
7. **Engineering agent je nejlépe chápaný jako orchestrátor dokumentů, výpočtů, simulátorů a verifikace.**
8. **Autonomii lze přidávat po stupních a člověk zůstává decision makerem pro zásadní trade-offy.**

V další kapitole tento obecný princip převedeme na konkrétní případovou studii:

> **AI-assisted analog IC design.**
