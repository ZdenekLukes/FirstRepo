---
title: "Úvod — Pro koho je tato kniha a jak ji číst"
part: "ÚVOD"
status: final-draft
version: "0.6"
updated: 2026-08-07
---

# Úvod — Pro koho je tato kniha a jak ji číst

Tato kniha není akademická učebnice ani encyklopedie AI.

Je to praktický zápisník mé cesty za pochopením AI, převedený do podoby příručky pro dalšího člověka. Zachycuje stav, jak AI chápu v srpnu 2026 — a je psaná tak, aby většina jejího obsahu platila i poté, co se dnešní názvy modelů změní.

## Pro koho kniha je

Počítám se čtenářem, který:

- má základní technické uvažování, ale není AI specialista,
- chce se rychle a správně zorientovat v současném světě AI,
- chce pochopit souvislosti, ne jen názvy nástrojů,
- chce AI skutečně používat — od chatbotů přes lokální modely, RAG a nástroje až k agentním systémům.

Pokud hledáte matematiku transformerů nebo přehled všech frameworků, tato kniha to záměrně není.

## Co budete po přečtení umět

1. Mít základní mentální model AI — a vědět, kde nejčastěji vzniká chybný.
2. Rozlišovat **model**, **aplikaci** a **celý AI systém**. Toto rozlišení je páteř celé knihy.
3. Chápat, jak fungují LLM — bez matematiky.
4. Orientovat se mezi cloudovými a lokálními modely a vědět, jak je porovnávat.
5. Zvládnout prompting a context engineering.
6. Rozumět RAG a práci s vlastními daty.
7. Chápat tool use, MCP a integrace.
8. Rozumět agentům a agentním systémům — včetně toho, kdy je nestavět.
9. Chápat bezpečnost, evaluaci a limity AI.
10. Být schopni začít stavět vlastní praktické AI workflow.

## Jak je kniha stavěná

Kniha postupuje po vrstvách a každá staví na předchozí:

```text
historie (I)
↓
co je model a co umí (II)
↓
mapa modelů a jejich výběr (III)
↓
cloud vs. lokální provoz (IV)
↓
prompting a kontext (V)
↓
vlastní data a RAG (VI)
↓
nástroje a integrace (VII)
↓
agenti (VIII)
↓
AI jako pracovní systém (IX)
↓
bezpečnost (X)
↓
zavádění do firmy (XI)
↓
evaluace a ekonomika (XII)
↓
kam to směřuje (XIII)
↓
praktická kuchařka (XIV)
```

Každá kapitola končí shrnutím **Co si z kapitoly odnést** a můstkem do další kapitoly. Kdo spěchá, může číst jen shrnutí a vracet se do textu tam, kde potřebuje detail.

## Tři čtenářské cesty

Kniha je lineární, ale nemusíte ji tak číst.

### Úplný začátečník

Čtěte od začátku. Kapitoly 2–4 jsou jádro — bez nich se zbytek knihy změní v hromadu buzzwordů. Kapitolu 1 (historie) můžete při prvním čtení přeskočit a vrátit se k ní později.

### Inženýr, který chce stavět

Proleťte části II–V, důkladně čtěte části VI–IX (RAG, nástroje, agenti, případová studie) a přeskočte na část XIV — kapitola 36 obsahuje deset projektů seřazených od nejjednoduššího po agentní systém. Přílohy D (hardware), E a F (checklisty) jsou určené k přímému použití.

### Manažer nebo člověk zavádějící AI do firmy

Přečtěte kapitoly 2–4 (mentální model), potom rovnou části X–XII (bezpečnost, zavádění, evaluace, ekonomika). Kapitola 25 vysvětluje, proč „máme ChatGPT" není AI strategie. Technické části VI–VIII čtěte podle potřeby — stačí shrnutí kapitol.

## Jak kniha zachází se stárnutím obsahu

AI se mění rychle. Proto kniha odděluje dvě vrstvy:

- **Principy** — jak LLM funguje, co je RAG, jak stavět agenty, jak evaluovat. Ty stárnou pomalu a tvoří většinu knihy.
- **Snapshoty** — konkrétní modely, nástroje a regulace k 7. 8. 2026. Tyto kapitoly (5, 15, 25, 33, 36 a přílohy B, C) jsou explicitně označené hlavičkou *snapshot* a odkazují na primární zdroje, kde lze ověřit aktuální stav.

Pokud čtete knihu později než v roce 2026, berte snapshot kapitoly jako mapu tehdejšího terénu — a principy jako to, co si máte odnést.

## Jedna věta, kterou kniha opakuje záměrně

> **Nejdůležitější není mít nejchytřejší model, ale umět mu ve správný okamžik dodat správný kontext a nástroje — a jeho výsledek spolehlivě ověřit.**

Pokud si z celé knihy odnesete jen tuto větu a mentální model `MODEL ≠ APLIKACE ≠ AGENT ≠ AI SYSTÉM`, splnila svůj hlavní účel.

Začneme tím, jak jsme se do dnešního stavu vůbec dostali.
