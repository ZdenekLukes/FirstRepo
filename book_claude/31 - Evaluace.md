---
title: "31. Evaluace"
part: "XII — Jak poznat, že AI opravdu funguje"
status: final-draft
version: "0.2"
updated: 2026-08-07
---

# 31. Evaluace

<!-- visual:31-evaluation-stack.svg -->

![Evaluační stack](assets/diagrams/31-evaluation-stack.svg)

*Obrázek: Od regresních testů až po business metriku.*


Největší rozdíl mezi AI experimentem a engineering systémem může být v jediné otázce:

> **Jak víme, že funguje?**

U klasického software často napíšeme test:

```text
input A
→ expected output B
```

U LLM je situace složitější.

Správných formulací může být mnoho.

Stejný model může při opakování vytvořit trochu jinou odpověď.

A výstup může vypadat velmi profesionálně, i když obsahuje chybu.

Proto nestačí:

> „Vyzkoušel jsem deset promptů a většinou to vypadalo dobře.“

Potřebujeme **evals** — systematické testování kvality AI systému.

> **Evaluace převádí subjektivní dojem z AI na data, podle kterých můžeme model, prompt, retrieval i celý workflow zlepšovat.**

---

## 31.1 „Vypadá to dobře“ nestačí

AI je mimořádně přesvědčivá v demo režimu.

Vybereme jeden pěkný dokument.

Položíme jednoduchou otázku.

Model odpoví dokonale.

To nic neříká o:

- edge cases,
- starých revizích,
- špatném OCR,
- tool failure,
- dlouhém kontextu,
- konfliktních zdrojích.

Potřebujeme testovat distribuované reálné případy.

Například:

```text
normal
hard
ambiguous
missing data
conflicting data
malformed input
security attack
```

Teprve potom začínáme vědět, jak systém skutečně funguje.

---

## 31.2 Ground truth

Ground truth je referenční správný výsledek.

Například:

```text
Question:
What is startup limit?

Ground truth:
< 120 µs according to Spec C §7.4
```

Ground truth může vzniknout:

- ručně expertem,
- z databáze,
- z test suite,
- ze simulatoru,
- z historicky ověřeného výsledku.

Někdy neexistuje jedna správná odpověď.

Pak místo ground truth definujeme **rubric**.

Například technické summary musí:

```text
- mention all 3 failures
- not invent unsupported cause
- cite source runs
- separate fact from hypothesis
```

To je stále měřitelné.

---

## 31.3 Test set

Test set je sada reprezentativních případů.

Nemusí být obrovský.

50 kvalitních reálných případů může být mnohem hodnotnějších než 10 000 uměle generovaných snadných otázek.

Dobrý test set obsahuje:

```text
běžné případy
+
edge cases
+
known historical failures
+
ambiguous inputs
+
negative cases
```

A hlavně se nemá průběžně měnit pokaždé, když výsledek nevychází dobře.

Jinak ztratíme schopnost sledovat regresi.

---

## 31.4 Golden questions

**Golden questions** jsou malá sada obzvlášť důležitých testů.

Například 20 otázek, které systém musí vždy zvládnout.

Pro engineering RAG:

```text
1. aktuální VDD limit
2. startup requirement
3. obsolete vs released revision
4. cross-project ambiguity
5. missing information case
```

Golden questions spouštíme při každé změně:

- modelu,
- promptu,
- embedding modelu,
- chunkingu,
- data pipeline.

Je to základní smoke test AI systému.

---

## 31.5 Automatické evaluace

Co lze ověřit programově, ověřujme programově.

Například:

### Structured output

```text
valid JSON schema?
```

### Numerická hodnota

```text
predicted == expected?
```

### Citation

```text
source document exists?
```

### Classification

```text
label matches ground truth?
```

### Coding

```text
tests pass?
```

Automatické evals jsou:

- rychlé,
- levné,
- reprodukovatelné.

LLM potřebujeme jako hodnotitele až tam, kde klasické pravidlo nestačí.

---

## 31.6 LLM-as-a-judge

Jeden LLM může hodnotit výstup jiného LLM.

Například:

```text
REFERENCE
...

ANSWER
...

RUBRIC
Rate factual correctness 1–5.
```

To je velmi užitečné pro:

- styl,
- úplnost,
- relevance,
- adherence to instructions.

Ale judge není objektivní pravda.

Může mít:

- bias,
- preference k vlastnímu stylu,
- chyby v reasoningu.

Proto je dobré judge kalibrovat proti human evaluation.

Například na 100 případech porovnat:

```text
human rating
vs.
LLM judge rating
```

Pokud korelace dává smysl, můžeme judge použít pro velké regression runs.

---

## 31.7 Human evaluation

Některé úlohy potřebují člověka.

Například:

- kvalita technického vysvětlení,
- usefulness,
- správnost trade-off reasoning,
- zda report skutečně pomohl rozhodnout.

Human evaluation potřebuje jednoduchý rubric.

Špatně:

```text
Je to dobré? 1–10
```

Lépe:

| Kritérium | 1 | 3 | 5 |
|---|---|---|---|
| Correctness | zásadní chyby | drobné chyby | bez známé chyby |
| Completeness | chybí podstatné | většina pokryta | kompletní |
| Evidence | bez zdrojů | část citována | vše klíčové podloženo |
| Usefulness | nepoužitelné | vyžaduje práci | ready to use |

Tím se hodnocení mezi lidmi stane konzistentnější.

---

## 31.8 Regression tests

AI systém se mění.

Upgradujeme model.

Změníme prompt.

Vyměníme embedding model.

Může se zlepšit jedna oblast a zhoršit jiná.

Proto potřebujeme regression suite.

```text
VERSION A
→ eval score 87 %

VERSION B
→ eval score 91 %
```

Ale nestačí celkové číslo.

Zkontrolujeme:

```text
které případy se zlepšily?
které se zhoršily?
```

Například nový model může být lepší v reasoning, ale horší ve strict JSON output.

Regression eval brání tomu, aby update „pocitově lepšího“ modelu rozbil produkční workflow.

---

## 31.9 Agent evaluation

Agent není jedna odpověď.

Je to cesta.

Můžeme hodnotit:

### Final success

Dokončil úkol?

### Number of steps

Kolik akcí potřeboval?

### Tool selection

Použil správné tools?

### Recovery

Dokázal se opravit po chybě?

### Safety

Pokusil se o zakázanou akci?

### Cost / latency

Kolik workflow spotřebovalo?

Příklad:

```text
Agent A
success 92 %
median steps 18
cost $1.20

Agent B
success 90 %
median steps 7
cost $0.28
```

Který je lepší záleží na use-case.

Evaluujeme celý systém, ne pouze inteligenci modelu.

---

## 31.10 RAG evaluation

RAG má nejméně dvě nezávislé vrstvy.

### Retrieval

Našli jsme správný source?

Metriky například:

```text
Recall@K
MRR
```

### Generation

Když správný source máme, vytvořil model správnou odpověď?

Hodnotíme:

- correctness,
- faithfulness,
- citation quality,
- unsupported claims.

To je zásadní pro debugging.

Pokud správný chunk nebyl retrievalem vůbec nalezen, výměna generativního modelu problém pravděpodobně nevyřeší.

---

## 31.11 Tool-use evaluation

Tool use testuje decision layer.

Například:

```text
Question:
How many failed runs yesterday?

Expected:
query database

Bad behavior:
answer from memory
```

Měříme:

- tool choice,
- arguments,
- number of unnecessary calls,
- interpretation of output,
- behavior on errors.

Také negative tests:

```text
user asks for forbidden production delete
→ expected = refuse / require approval
```

Tool eval je současně funkcionalita i security test.

---

## 31.12 End-to-end business metric

Na konci musí eval odpovědět i na otázku:

> Pomáhá tento systém skutečné práci?

Například:

```text
technical accuracy = 96 %
```

je dobré vědět.

Ale pokud člověk stále potřebuje 90 % práce udělat ručně, business value je malá.

End-to-end metriky:

```text
human minutes per task
lead time
throughput
error escape rate
cost per completed case
customer satisfaction
```

Nejdůležitější evaluace je proto často kombinace:

```text
AI QUALITY
×
WORKFLOW IMPACT
```

---

## Evaluation pyramid

Praktická hierarchie:

```text
              BUSINESS KPI
                  ▲
            HUMAN EVALUATION
                  ▲
        LLM / SEMANTIC JUDGES
                  ▲
        AUTOMATIC TASK EVALS
                  ▲
      SCHEMA / RULE / UNIT TESTS
```

Čím níže lze něco ověřit, tím lépe.

Nechceme platit LLM za rozhodnutí, zda je JSON validní.

Naopak kvalitu strategického reportu jedním regulárním výrazem nezměříme.

---

## Failure-driven eval development

Nejlepší eval set se často buduje z reálných chyb.

```text
production failure
↓
root cause
↓
add test case
↓
fix system
↓
regression test forever
```

Tím se systém postupně stává odolnější vůči přesně těm situacím, které se skutečně dějí.

To je stejný princip jako u klasického software.

---

## Co si z kapitoly odnést

1. **„Vypadá to dobře“ není evaluace.**
2. **Ground truth nebo jasný rubric jsou základem smysluplného testu.**
3. **Kvalitní reprezentativní test set je cennější než velké množství snadných příkladů.**
4. **Golden questions slouží jako rychlá regression sada pro kritické schopnosti.**
5. **Co lze ověřit deterministicky, nemá hodnotit LLM.**
6. **LLM-as-a-judge je užitečný, ale musí být kalibrovaný proti lidskému hodnocení.**
7. **Agent evaluation měří celou cestu: tools, kroky, recovery, safety, cost.**
8. **RAG evaluujeme odděleně na retrieval a generation.**
9. **Tool-use eval musí zahrnovat i zakázané nebo rizikové akce.**
10. **Konečným měřítkem je dopad na skutečný workflow a business metric.**

Když umíme kvalitu změřit, můžeme konečně smysluplně řešit další často kladenou otázku:

> **Kolik nás AI skutečně stojí a kdy se vyplatí?**
