---
title: "34. Co mě ještě čeká"
part: "XIII — Co přijde dál"
status: release-candidate
version: "0.7"
updated: 2026-08-08
---

# 34. Co mě ještě čeká

<!-- visual:34-learning-roadmap.svg -->

![Roadmapa dalšího učení](assets/diagrams/34-learning-roadmap.svg)

*Obrázek: Lokální stack → RAG → tools → agent → production.*


Po třiceti čtyřech kapitolách by se mohlo zdát, že jsme prošli téměř všechno důležité.

Ve skutečnosti je velká část témat zatím pochopená hlavně **konceptuálně**. Další fáze musí být mnohem praktičtější. Ne „přečíst další článek o agentech", ale:

```text
postavit agenta
→ změřit
→ rozbít
→ opravit
```

Hlavní princip:

> **Každý další krok má skončit fungujícím artefaktem nebo měřitelným experimentem, ne pouze dalším seznamem poznámek.**

Konkrétní projekty — od chatu nad jedním dokumentem po multi-agentní systém s human approval — jsou rozpracované v kapitole 36, včetně metrik, failure modes a kritérií, kdy přejít na další. Nebudu je zde opakovat. Tato krátká kapitola říká jen dvě věci: v jakém pořadí je plánuji projít já a jak poznám, že jsem se skutečně něco naučil.

## 34.1 Moje pořadí

```text
1  Lokální stack, který umím postavit znovu od nuly
2  Vlastní model benchmark na mém hardware
3  RAG s měřitelným retrieval a answer score
4  Tool use — od read-only nástrojů k sandbox writes
5  Jeden spolehlivý agent s 50+ eval cases
6  Evals + observability jako trvalá součást všeho dalšího
7  Druhý mozek a memory — až po agentovi, který funguje bez ní
8  Multi-agent experiment proti single-agent baseline
9  Engineering integrace: closed loop přes simulátor
10 Bezpečný on-prem pilot na citlivá data
11 Měřitelný firemní pilot s go/no-go kritérii
12 Produkce: owner, SLA, monitoring, rollback
```

Některé kroky se budou překrývat, ale pořadí drží jednu zásadu:

> **Nejdříve jednoduchý systém, který umím měřit. Teprve potom složitost.**

Memory a multi-agent jsou v seznamu záměrně pozdě — přidávám je, až budu mít konkrétní důvod a baseline, proti které je změřím.

## 34.2 Jak poznám, že jsem se skutečně něco naučil

Ne podle počtu přečtených článků. Ale podle toho, zda u selhání umím odpovědět na otázku „proč tento systém selhal?" — a mám evidence.

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

To jsou zkušenosti, které se z tutorialu získávají těžko. Příloha G proto používá stejný experimentální formát: konfigurace, metriky, selhání, evidence a to, co se po výsledku změnilo.


## Co si z kapitoly odnést

1. **Další učení má končit artefaktem nebo měřením, ne pouze další poznámkou.**
2. **Nejdřív stavím jednoduchý systém, který umím změřit; teprve potom přidávám memory, multi-agent nebo větší autonomii.**
3. **Důkaz porozumění není počet přečtených článků, ale schopnost vysvětlit konkrétní failure mode z evidence.**
4. **Experiment log je součást znalosti — bez konfigurace, metrik a selhání se zkušenost těžko reprodukuje.**

Poslední část knihy už není teorie. Je to kuchařka:

> **Jaký minimální stack potřebuji (kapitola 35) a jaké projekty mám skutečně postavit (kapitola 36)?**
