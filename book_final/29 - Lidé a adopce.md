---
title: "29. Lidé a adopce"
part: "XI — Jak zavádět AI do firmy"
status: final-draft
version: "0.7"
updated: 2026-08-07
---

# 29. Lidé a adopce

<!-- visual:29-adoption-loop.svg -->

![Smyčka adopce AI](assets/diagrams/29-adoption-loop.svg)

*Obrázek: Experiment, měření, sdílení, trénink a standardizace.*


Technicky dobrý AI systém může mít přesná data, kvalitní model, perfektní security i výborné benchmarky.

A přesto může ve firmě selhat.

Protože software nepoužívají benchmarky.

Používají jej lidé.

AI navíc není obyčejný nový software.

Dotýká se otázky:

> „Která část mé práce má ještě hodnotu, když toto zvládne stroj?“

To je legitimní otázka.

Stejně legitimní je skeptická otázka:

> „Proč bych měl věřit systému, který někdy halucinuje?“

Proto adopce nemůže být postavená na heslech typu:

```text
AI is the future.
Everyone must adapt.
```

Mnohem silnější je:

```text
zde je konkrétní problém
↓
zde je současná baseline
↓
zde je AI-assisted workflow
↓
zde jsou výsledky a chyby
↓
zde rozhodneme, zda nám to pomáhá
```

> **Nejlepší argument pro AI je fungující nástroj, který řeší skutečný problém a jehož limity jsou otevřeně viditelné.**

---

## 29.1 Proč technicky dobrý projekt může selhat

Typické příčiny nemusí být technické.

### Řeší problém, který nikoho netrápí

Demo je efektní, ale lidé jej nepotřebují.

### Přidává práci

Například uživatel musí vyplnit pět nových formulářů, aby AI ušetřila dvě minuty.

### Výsledek není důvěryhodný

AI neukazuje zdroje a uživatel musí vše zkontrolovat od začátku.

### Narušuje zavedený workflow

Technicky funguje, ale nutí člověka opustit nástroje, ve kterých skutečně pracuje.

### Není jasné, kdo je owner

Pilot vytvoří nadšenec, odejde na jiný projekt a systém přestane fungovat.

Adopce je proto součást designu produktu od prvního dne.

---

## 29.2 Strach z nahrazení

Pokud zaměstnancům řekneme:

> „Chceme automatizovat vaši práci pomocí AI,“

nelze se divit, že část lidí nebude nadšená.

Navíc by bylo nepoctivé tvrdit, že AI nikdy žádnou práci nenahradí.

Některé úkoly skutečně automatizuje.

Užitečnější je mluvit konkrétně:

```text
Které úkoly chceme odstranit?
Které chceme zrychlit?
Kde zůstává lidské rozhodnutí?
Jak se změní role?
```

Například:

```text
Dnes designer:
- 2 h sbírá výsledky
- 30 min je analyzuje

Cíl:
AI sbírá a strukturuje results
Designer analyzuje trade-off
```

Taková změna je srozumitelnější než abstraktní diskuse o „nahrazování lidí“.

---

## 29.3 Skeptici

Skeptik může být pro AI projekt velmi cenný.

Zvlášť technický skeptik se obvykle ptá:

- kde jsou evidence?
- jak jste měřili accuracy?
- co se stane na edge case?
- proč tomu mám věřit?

To jsou přesně otázky, které potřebujeme před produkčním nasazením.

Místo snahy skeptika „přesvědčit“ jej můžeme zapojit jako reviewer.

Například:

```text
Tady je 30 výsledků AI.
Najdi případy, kde je systém špatně.
```

Každá nalezená chyba zlepšuje eval set.

Dobrý skeptik se tak může stát nejsilnější součástí quality loopu.

---

## 29.4 Early adopters

Early adopters jsou lidé, kteří nový nástroj začnou používat dříve než ostatní.

Jejich hodnota není jen v nadšení.

Poskytují rychlou zpětnou vazbu:

- co skutečně funguje,
- kde je friction,
- jaké use-cases vznikají spontánně,
- kde AI selhává.

Ale early adopter není reprezentativní běžný uživatel.

Může tolerovat:

- command line,
- ruční setup,
- občasnou chybu.

Industrializovaný nástroj musí fungovat i pro člověka, který nechce AI zkoumat — chce pouze udělat svou práci.

---

## 29.5 AI champions

AI champion je člověk uvnitř týmu, který:

- rozumí doméně,
- rozumí možnostem AI,
- pomáhá kolegům,
- sbírá use-cases,
- komunikuje s centrálním AI týmem.

Nemusí být AI engineer.

Naopak jeho největší hodnota může být hluboká znalost procesu.

Příklad:

```text
centrální AI tým
→ zná platformu

analog AI champion
→ ví, kde designer ztrácí čas

společně
→ vytvoří správný use-case
```

Bez doménových championů hrozí, že centrální tým vytvoří technicky krásné řešení pro špatný problém.

---

## 29.6 Training

Training by neměl být pouze:

> „Zde je 50 prompt tricks.“

Důležitější je mentální model.

Lidé potřebují vědět:

```text
co LLM je
co umí
co neumí
jak pracuje s contextem
co je hallucination
co jsou citlivá data
kdy použít tool
jak ověřovat výsledek
```

A potom konkrétní use-cases jejich práce.

Například pro engineering:

- datasheet analysis,
- script generation,
- log triage,
- report drafting.

Pro finance budou příklady úplně jiné.

Generický AI kurz je začátek.

Doménový training vytváří skutečnou adopci.

---

## 29.7 Learning by doing

AI se těžko učí pouze z prezentace.

Mnohem účinnější je krátký experiment.

Například workshop:

```text
20 min
vysvětlení principu

40 min
každý použije vlastní reálný dokument

20 min
sdílení toho, co fungovalo a nefungovalo
```

Lidé velmi rychle pochopí:

- kde model překvapí,
- kde potřebuje context,
- kde se nesmí slepě věřit.

Learning by doing také snižuje přehnaná očekávání.

AI přestane být abstraktní magie a stane se nástrojem se silnými i slabými stránkami.

---

## 29.8 Sdílení use-cases

Jednotlivci často objeví velmi dobrý workflow, ale nikdo další se o něm nedozví.

Proto je užitečné sdílet krátké use-case karty.

Například:

```text
USE-CASE
Regression log triage

BEFORE
45 min manual search

AI WORKFLOW
upload log → identify anomalies → source lines

RESULT
10–15 min

LIMITATIONS
must manually verify root cause

OWNER
...
```

To je mnohem užitečnější než sdílení náhodných promptů bez kontextu.

Firma postupně vytváří katalog ověřených pracovních patternů.

---

## 29.9 Interní komunita

Jednoduchá interní komunita může mít velkou hodnotu.

Například:

- Teams/Slack channel,
- měsíční AI demo,
- use-case repository,
- office hours.

Důležité je, aby obsah nebyl pouze:

```text
"Nový model je úžasný!"
```

Ale hlavně:

```text
co jsme vyzkoušeli
co fungovalo
co nefungovalo
kolik času to ušetřilo
```

Tím se AI knowledge stává praktická a lokální pro konkrétní firmu.

---

## 29.10 Nové role

AI nemusí vytvořit jednu novou profesi.

Spíše mění mnoho existujících rolí a přidává několik funkcí.

Například:

### Domain AI champion

Propojuje doménu a AI.

### AI engineer

Staví integrace, RAG, agenty.

### AI product owner

Vlastní use-case a business metric.

### AI security / governance

Řeší policy a risk.

### Evaluation owner

Spravuje test sets a quality thresholds.

Ve malé firmě může několik těchto rolí dělat jeden člověk.

Ve velké mohou být rozdělené.

Důležitější než název je odpovědnost.

---

## 29.11 AI leader / AI officer / competence center

Centrální AI funkce má smysl hlavně tam, kde vytváří reusable capability.

Například:

```text
approved model gateway
security policy
RAG platform
MCP/tool registry
evaluation framework
training
use-case portfolio
```

Neměla by se stát bottleneckem, který musí ručně schválit každý experiment.

Dobrý model může být:

```text
CENTRAL COMPETENCE CENTER
→ platform, governance, support

DOMAIN TEAMS
→ use-cases, knowledge, adoption
```

Centrum poskytuje bezpečné koleje.

Týmy po nich mohou rychle stavět vlastní řešení.

---

## 29.12 AI jako augmentace člověka

Slovo **augmentation** je užitečné, pokud jej nepoužíváme jako prázdné heslo.

Prakticky znamená rozdělit workflow podle silných stránek.

```text
AI
- search
- summarize
- draft
- transform
- run tools
- repeat

HUMAN
- define intent
- judge ambiguity
- own trade-offs
- accept risk
- approve critical decisions
```

Toto rozdělení není navždy fixní.

Jak se AI zlepšuje a jak roste naše důvěra, některé kroky se mohou posouvat.

Ale nejlepší workflow nevznikne otázkou:

> „Kde odstraníme člověka?“

Spíše:

> **„Jak rozdělit práci mezi člověka a stroj tak, aby celý systém byl rychlejší a spolehlivější?“**

---

## Adoption loop

Praktický cyklus:

```text
REAL PROBLEM
    ↓
small pilot
    ↓
early adopters
    ↓
measure
    ↓
show evidence
    ↓
collect criticism
    ↓
improve
    ↓
train broader group
    ↓
scale
```

Důvěra se nevynucuje komunikací.

Buduje se opakovanou zkušeností s výsledkem, který je užitečný a kontrolovatelný.

---

## Co si z kapitoly odnést

1. **Technicky dobrý projekt může selhat, pokud nezapadne do skutečného workflow lidí.**
2. **Obavy ze změny práce je lepší řešit konkrétním popisem změny úkolů než abstraktními sliby.**
3. **Skeptici jsou cenní revieweři a mohou odhalit failure modes, které nadšenci přehlédnou.**
4. **Early adopters pomáhají rychle iterovat, ale nejsou reprezentativní pro všechny uživatele.**
5. **AI champions propojují centrální platformu s doménovou znalostí.**
6. **Training má učit mentální model a reálné use-cases, ne seznam kouzelných promptů.**
7. **Nejrychlejší učení vzniká praktickým experimentem.**
8. **Sdílet je užitečnější ověřené workflows a výsledky než izolované prompty.**
9. **Competence center má vytvářet reusable platformu a guardrails, ne brzdit lokální experimenty.**
10. **Nejlepší otázka není, jak odstranit člověka, ale jak optimálně rozdělit práci člověk–AI.**

Abychom ale věděli, zda nový workflow skutečně funguje, potřebujeme systematickou evaluaci.

To je tématem další části.
