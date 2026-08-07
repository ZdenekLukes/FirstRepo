---
title: "G. Vlastní experimenty"
part: "PŘÍLOHY"
status: final-draft
version: "0.4"
updated: 2026-08-07
---

# G. Vlastní experimenty

Tato příloha není katalog benchmarků z internetu. Je to šablona pro vlastní evidence: co jsem skutečně zkusil, na jakém hardware, s jakou verzí modelu a co z toho vyplynulo.

Nejcennější informace po několika měsících není:

> „Model X mi připadal chytrý.“

Ale například:

```text
Model X / quantization Y
na našem 40-case test setu
92 % extraction accuracy
vs.
Model Z 95 %

ale X byl 2.4× rychlejší
```

## G.1 Povinná hlavička experimentu

```yaml
date:
experiment_id:
status: planned | running | completed
question:
hypothesis:
hardware:
os:
runtime:
model:
model_version:
quantization:
context_length:
tools:
data_version:
eval_set:
```

## G.2 Co zaznamenat

### Otázka

Jedna konkrétní věta.

Dobře:

> Stačí 8B lokální model pro extrakci 12 parametrů z našich technických reportů?

Špatně:

> Jak dobrá je lokální AI?

### Hypotéza

Před experimentem napiš, co očekáváš. Pomáhá to odhalit confirmation bias.

### Baseline

Pokud úlohu dnes dělá člověk:

```text
čas
chybovost
počet kroků
```

Pokud ji dělá existující software, zaznamenej jeho výsledek.

### Data

Uveď:

- počet případů,
- verzi,
- zda jsou reálné nebo syntetické,
- zda test set obsahuje edge cases.

### Výsledek

Odděl:

```text
QUALITY
PERFORMANCE
COST
FAILURE MODES
```

## G.3 Minimální tabulka výsledků

| Metrika | Baseline | Varianta A | Varianta B |
|---|---:|---:|---:|
| Correct cases |  |  |  |
| Critical errors |  |  |  |
| Median latency |  |  |  |
| Human correction time |  |  |  |
| Cost / task |  |  |  |

## G.4 Failure log

Nejhodnotnější část experimentu jsou chyby.

| Case | Co se stalo | Root cause | Kategorie | Fix | Přidán regression test? |
|---|---|---|---|---|---|
| 001 |  |  | model / context / retrieval / tool / data |  |  |

Každý důležitý production failure by měl skončit jako nový test case.

## G.5 Experiment template

### Experiment `[ID]` — `[název]`

**Datum:**  
**Otázka:**  
**Hypotéza:**  
**Baseline:**  

**Model:**  
**Runtime:**  
**Hardware:**  
**Quantization:**  
**Context:**  
**Nástroje:**  
**Data / eval set:**  

#### Postup

1. 
2. 
3. 

#### Výsledky

| Metrika | Hodnota |
|---|---:|
|  |  |

#### Co fungovalo

- 

#### Co nefungovalo

- 

#### Root cause největší chyby

```text
MODEL
CONTEXT
DATA
RETRIEVAL
TOOL
PERMISSION
VERIFICATION
OTHER
```

#### Co jsem se naučil

- 

#### Další krok

- 

---

## G.6 Dokumentované experimenty

### Experiment EXP-001 — Lokální inference: 8 GB vs. 32 GB VRAM

**Datum:** [DOPLNIT — období experimentů]
**Status:** completed (zpětně dokumentováno; kvalitativní závěry viz též kapitola 34.3)
**Otázka:** Jaký model je na daném hardware skutečně *interaktivně použitelný*, ne pouze spustitelný?
**Hypotéza:** Větší VRAM umožní větší modely; očekával jsem hlavně rozdíl v maximální velikosti modelu.

**Hardware A:** notebook, 8 GB VRAM, [DOPLNIT — přesná konfigurace]
**Hardware B:** workstation, 32 GB VRAM, [DOPLNIT — přesná konfigurace]
**Runtime:** Ollama / llama.cpp [DOPLNIT — verze]
**Modely:** [DOPLNIT — přesné názvy a kvantizace testovaných modelů]

#### Výsledky (kvalitativní; čísla doplnit z poznámek)

| Metrika | 8 GB VRAM | 32 GB VRAM |
|---|---|---|
| Interaktivně použitelná třída | menší textové modely (~7B–8B, Q4) | ~30B–40B třída v kvantizaci |
| Chování při překročení VRAM | offload do RAM výrazně zhoršil interaktivnost | dostatek rezervy i pro STT/TTS vedle LLM |
| TTFT / tokens/s | [DOPLNIT] | [DOPLNIT] |
| Sestavený stack | samotný LLM | LLM + Open WebUI + Whisper STT + TTS |

#### Co fungovalo

- 8 GB stačí na skutečné osahání lokální AI — experimenty s menšími textovými modely byly rozumně použitelné.
- Na 32 GB šlo vedle textového LLM provozovat celý stack (Open WebUI, speech-to-text přes Whisper, text-to-speech) současně.

#### Co nefungovalo

- Jakmile část modelu nebo KV cache přetekla do systémové RAM, papírově funkční konfigurace přestala být prakticky použitelná.

#### Root cause největšího omezení

```text
HARDWARE (memory bandwidth + kapacita), ne MODEL
```

#### Co jsem se naučil

Nejdůležitější zjištění nebylo, že větší model „běží". Bylo to zjištění, že **jednotlivé části stacku lze skládat a měřit odděleně** — malý model může být dostatečný pro jednu roli, zatímco těžší reasoning pošlu jinam. Hardware proto neberu jako soutěž o maximální počet parametrů, ale jako další routing constraint.

#### Další krok

EXP-002 — porovnat lokální modely proti frontier cloudu na stejném eval setu.

---

## G.7 Doporučený backlog dalších experimentů

### EXP-002 — Malý lokální model vs. frontier cloud

Použij stejných 30–50 reálných úloh.

Cíl není dokázat, že jeden je „lepší“.

Zjisti, pro které kategorie stačí lokální model a které zaslouží cloud routing.

### EXP-003 — Long context vs. RAG

Stejný corpus a stejné otázky:

```text
varianta A → vlož velkou část dokumentů do contextu
varianta B → retrieval + malé relevantní chunks
```

Měř:

- correctness,
- source accuracy,
- latency,
- token cost.

### EXP-004 — Agent bez verifieru vs. s verifierem

Vyber úlohu s numerickým nebo programově ověřitelným výsledkem.

Porovnej:

```text
LLM final answer
vs.
LLM + deterministic verification
```

### EXP-005 — Single-agent vs. multi-agent

Stejný end-to-end task.

Měř:

- success rate,
- steps,
- latency,
- cost,
- debugging effort.

Pokud multi-agent nepřinese výhodu, výsledek experimentu je stále velmi cenný.

## G.8 Pravidlo této přílohy

Do publikované knihy patří pouze experimenty, u kterých lze dohledat alespoň:

```text
co bylo testováno
na čem
jak
proti čemu
s jakým výsledkem
```

Nechci z vlastního dojmu vyrábět univerzální benchmark. Smyslem této přílohy je ukázat proces, kterým si může čtenář vytvořit vlastní evidence.