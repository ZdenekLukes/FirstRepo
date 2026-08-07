---
title: "11. Proč model nezná moje data"
part: "VI — Data, RAG a druhý mozek"
status: final-draft
version: "0.2"
updated: 2026-08-07
---

# 11. Proč model nezná moje data

<!-- visual:11-external-data-bridge.svg -->

![Připojení modelu k vlastním datům](assets/diagrams/11-external-data-bridge.svg)

*Obrázek: Soukromá a aktuální data musí být do kontextu přivedena externí vrstvou.*


Velký jazykový model může vědět překvapivě mnoho o světě.

Můžeme se ho zeptat na:

- historii,
- programování,
- fyziku,
- ekonomii,
- elektroniku,
- desítky jazyků.

Pak ale položíme jednoduchou otázku:

> „Co jsme minulý týden rozhodli o projektu ABC?“

A model neví.

To není chyba.

Nemá automaticky přístup k našim:

- souborům,
- e-mailům,
- poznámkám,
- meetingům,
- databázím,
- firemnímu intranetu.

A ani bychom nechtěli, aby libovolný model mohl bez kontroly číst všechno.

Proto je důležité oddělit dvě věci:

```text
znalosti v modelu
```

a

```text
znalosti dostupné systému právě teď
```

---

## 11.1 Interní dokumenty

Představme si firmu s následujícími daty:

```text
Specifications/
Design_Notes/
Measurements/
Simulations/
Presentations/
Meeting_Minutes/
Source_Code/
```

Frontier model může být skvělý v technickém reasoningu.

Ale dokud tyto soubory nedostane jako vstup nebo k nim nemá nástroj, neví nic o jejich obsahu.

Model například obecně zná pojem bandgap reference.

Ale neví:

- jaká je naše topologie,
- jakou technologii používáme,
- jaké byly poslední PVT výsledky,
- proč jsme změnili konkrétní tranzistor,
- který dokument je aktuální.

To je zásadní rozdíl mezi:

```text
obecnou znalostí
```

a

```text
firemním kontextem
```

V praxi proto nejde pouze o otázku:

> Jak chytrý model používáme?

Stejně důležitá je otázka:

> **K jakým kvalitním interním informacím má model přístup?**

---

## 11.2 Osobní znalosti

Stejný problém existuje na osobní úrovni.

Člověk může mít roky poznámek v:

- Obsidianu,
- OneNote,
- Notion,
- e-mailech,
- PDF knihách,
- poznámkách z meetingů,
- vlastních dokumentech.

Část znalostí navíc není nikde strukturovaně zapsaná.

Například:

> „Když jsme před dvěma lety testovali tuto architekturu, nefungovala kvůli startupu.“

Pokud tato zkušenost není někde zachycena, AI ji nemá jak zjistit.

To vede k zajímavému efektu.

Člověk může mít stovky gigabajtů dat, ale jeho AI asistent přesto působí, jako by o něm nic nevěděl.

Problém není kapacita disku.

Problém je **retrieval**.

Informace musí být:

1. uložená,
2. dohledatelná,
3. přístupná podle oprávnění,
4. vložená do kontextu ve správný okamžik.

---

## 11.3 Aktuální informace

Další kategorie jsou informace, které se mění po skončení trénování modelu.

Například:

- dnešní počasí,
- cena akcie,
- nový AI model,
- aktuální verze software,
- dnešní e-mail,
- stav výrobní linky,
- poslední commit.

I model s velmi rozsáhlými znalostmi nemůže bez externího zdroje spolehlivě znát událost, která nastala před pěti minutami.

Proto moderní AI systém často vypadá:

```text
LLM
+
web search
+
databáze
+
firemní API
```

Aktuálnost tedy není vlastnost samotného modelu.

Je to vlastnost připojeného systému.

---

## 11.4 Připojení modelu k externím zdrojům

Existuje několik způsobů, jak modelu dodat externí informace.

### 1. Ručně vložit dokument do kontextu

Nejjednodušší varianta.

```text
PDF
↓
text
↓
context
↓
LLM
```

Výborné pro jeden nebo několik dokumentů.

### 2. Search

Model nebo aplikace vyhledá relevantní soubor nebo pasáž.

```text
otázka
↓
search
↓
relevantní výsledek
↓
LLM
```

### 3. RAG

Dokumenty předem zpracujeme a při dotazu automaticky vybereme relevantní části.

Tomu se budeme věnovat v další kapitole.

### 4. Databáze a API

Pro přesná strukturovaná data je často lepší nepoužívat RAG vůbec.

Například:

```text
Kolik kusů máme skladem?
```

Správný zdroj může být SQL databáze.

### 5. Nástroje

Agent může otevřít:

- filesystem,
- Git,
- web,
- e-mail,
- simulátor.

Tím se z obecného modelu stává systém schopný pracovat v našem prostředí.

---

# Training není běžný způsob, jak model naučit dokument

Častá představa je:

> „Máme 10 000 dokumentů. Natrénujeme na nich LLM a potom je bude znát.“

Pro většinu firemních knowledge use-cases to není ideální řešení.

Training nebo fine-tuning se hodí spíše pro změnu:

- chování,
- stylu,
- specializované schopnosti,
- formátu odpovědi.

Pro znalosti, které se často mění, chceme spíše:

```text
externí zdroj
+
retrieval
+
LLM
```

Proč?

Když se zítra změní specifikace, nechceme znovu trénovat model.

Chceme pouze aktualizovat dokument nebo index.

---

# Data musí mít autoritu

Připojení zdrojů vytváří nový problém.

Co když máme:

```text
spec_rev_A.pdf
spec_rev_B.pdf
spec_FINAL_old.pdf
spec_current.pdf
```

Model může najít všechny.

Ale která verze je autoritativní?

Knowledge systém proto potřebuje metadata:

```text
revision
status
owner
valid_from
obsolete
```

Bez nich může AI velmi přesně citovat špatný dokument.

> **Retrieval řeší „najdi informaci“. Governance řeší „které informaci smíme věřit“.**

Obojí je nutné.

---

# Co si z kapitoly odnést

1. **LLM automaticky nezná naše soubory, e-maily ani databáze.**
2. **Obecná znalost modelu a firemní znalost jsou dvě různé věci.**
3. **Aktuální informace musí systém získat z externího zdroje.**
4. **Training obvykle není nejlepší způsob, jak modelu dodat často se měnící dokumentaci.**
5. **Search, RAG, databáze a nástroje jsou různé způsoby připojení znalostí.**
6. **Nestačí informaci najít — musíme také vědět, která verze je autoritativní.**

A právě nejčastější mechanismus pro práci s velkým množstvím vlastních dokumentů má jméno:

> **RAG — Retrieval-Augmented Generation.**
