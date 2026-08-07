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

## G.6 Doporučený backlog prvních experimentů

### EXP-001 — 8GB vs. 16GB vs. 32GB local inference

Otázka:

> Jaký model je na daném hardware skutečně interaktivně použitelný, ne pouze spustitelný?

Měř:

- time to first token,
- tokens/s,
- peak memory,
- kvalitu na stejném eval setu.

### EXP-002 — Malý local model vs. frontier cloud

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

## G.7 Pravidlo této přílohy

Do publikované knihy patří pouze experimenty, u kterých lze dohledat alespoň:

```text
co bylo testováno
na čem
jak
proti čemu
s jakým výsledkem
```

Nechci z vlastního dojmu vyrábět univerzální benchmark. Smyslem této přílohy je ukázat proces, kterým si může čtenář vytvořit vlastní evidence.