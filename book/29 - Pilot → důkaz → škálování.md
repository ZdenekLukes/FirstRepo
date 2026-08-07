---
title: "29. Pilot → důkaz → škálování"
part: "XI — Jak zavádět AI do firmy"
status: draft
version: "0.2"
updated: 2026-08-07
---

# 29. Pilot → důkaz → škálování

AI pilot má velmi jednoduchý účel:

> **Snížit nejistotu dostatečně na to, abychom mohli udělat další rozhodnutí.**

Nemusí být produkční systém.

Nemusí mít perfektní UI.

Ale musí odpovědět na konkrétní otázku.

Například:

```text
Dokáže AI zkrátit regression triage ze 3 hodin pod 1 hodinu
bez zvýšení počtu přehlédnutých failures?
```

To je mnohem lepší pilotní cíl než:

> „Vyzkoušíme agentní AI.“

Dobrá cesta vypadá:

```text
malý problém
→ baseline
→ pilot
→ evidence
→ go / no-go
→ industrializace
→ škálování
```

Přeskakování kroků často vede buď k nekonečným experimentům, nebo k předčasnému nasazení křehkého dema do produkce.

---

## 29.1 Začít malým problémem

Malý neznamená bezvýznamný.

Dobrý pilot má:

- úzký scope,
- reálná data,
- skutečné uživatele,
- měřitelný výsledek.

Například místo:

```text
"AI pro analog design"
```

začneme:

```text
"Automaticky vyhodnotit existující regression run
pro jeden blok a jednu skupinu parametrů."
```

To nám umožní přesně zjistit:

- funguje retrieval?
- fungují tools?
- jsou data kvalitní?
- věří výsledku designer?

Pilot má izolovat nejistotu, ne vytvořit celý budoucí systém najednou.

---

## 29.2 Baseline bez AI

Bez baseline nemáme s čím porovnávat.

Změříme současný proces.

Například na 20 reálných případech:

```text
median human time: 142 min
errors requiring correction: 6 %
missed failures: 1 / 20
report lead time: 1 day
```

Baseline může být nepohodlná, protože zjistíme, že současný proces není vůbec měřený.

To je cenné zjištění.

AI projekt nás nutí pojmenovat, jak práce vypadá dnes.

---

## 29.3 Pilot s AI

Pilot by měl být co nejpodobnější reálnému použití.

Pokud jej testujeme jen na pěti ručně vybraných jednoduchých dokumentech, nevíme, jak bude fungovat v běžném provozu.

Použijeme reprezentativní dataset:

```text
normal cases
edge cases
bad data
missing data
old revisions
known failures
```

A ideálně oddělíme:

```text
development set
```

od

```text
final evaluation set
```

Jinak systém ladíme přímo na testovacích otázkách a získáme falešně dobrý výsledek.

---

## 29.4 Metriky

Metriky rozdělíme do několika vrstev.

### Technical

- retrieval accuracy,
- tool success,
- end-to-end success.

### Operational

- čas,
- náklady,
- reliability.

### Business

- lead time,
- throughput,
- quality,
- ušetřená práce.

### Human

- correction time,
- adoption,
- důvěra.

Jedno číslo obvykle nestačí.

Například 95% accuracy může být skvělá nebo nepřijatelná podle toho, **kterých 5 % je chybných**.

---

## 29.5 Kvalita

Kvalitu definujeme před pilotem.

Například u reportu:

```text
100 % numerických hodnot musí odpovídat source data
100 % FAIL musí mít source limit
summary musí správně identifikovat top issues
```

Pro generativní text můžeme použít human review.

Pro strukturované části použijeme automatické kontroly.

Dobrý systém minimalizuje počet věcí, které hodnotíme pouze pocitem.

---

## 29.6 Čas

Neměříme jen latenci modelu.

Měříme end-to-end:

```text
od chvíle, kdy je práce připravená
→ po použitelný výsledek
```

A také aktivní lidský čas.

Příklad:

```text
BEFORE
3 h engineer work

AFTER
10 min setup
40 min autonomous run
15 min review

human time = 25 min
```

I když AI workflow trvá 65 minut wall-clock, ušetřilo velkou část lidské pozornosti.

---

## 29.7 Náklady

Pilot musí ukázat realistické cost drivers:

- API tokens,
- GPU time,
- search,
- storage,
- engineering maintenance,
- human review.

Náklad na jeden úspěšný run:

```text
inference
+
external tools
+
compute
+
human correction
```

je důležitější než samotná cena modelu.

Pokud AI ušetří dvě hodiny seniorního člověka za cenu několika dolarů compute, ekonomika může být velmi dobrá.

Ale musíme to změřit.

---

## 29.8 Chybovost

Ne všechny chyby jsou stejně závažné.

Například ve verification:

```text
FALSE FAIL
→ člověk zbytečně něco kontroluje

FALSE PASS
→ skutečný problém může projít dál
```

False PASS může být řádově nebezpečnější.

Proto nesledujeme pouze celkové accuracy.

Sledujeme **error taxonomy**.

Například:

| Typ chyby | Počet | Závažnost |
|---|---:|---|
| wrong citation | 3 | medium |
| missed requirement | 1 | high |
| false FAIL | 4 | low/medium |
| false PASS | 0 | critical target |

To vede k lepším rozhodnutím o guardrails.

---

## 29.9 Přijetí uživateli

Technicky perfektní systém může selhat, pokud jej lidé nepoužívají.

Důvody mohou být:

- workflow je pomalejší než původní,
- UI je nepříjemné,
- lidé výsledku nevěří,
- přidává další povinný krok,
- nerozumí citacím nebo limitations.

Měříme například:

```text
weekly active users
repeat usage
acceptance rate
correction rate
qualitative feedback
```

Velmi důležitá otázka je:

> „Kdy se rozhodnete výsledek AI ignorovat a proč?“

Tato odpověď často odhalí důležitější problém než technický benchmark.

---

## 29.10 Rozhodnutí go / no-go

Pilot musí skončit rozhodnutím.

Předem definujeme thresholds.

Například:

```text
GO if:
- no false PASS on evaluation set
- >60 % human time reduction
- median correction < 10 min
- cost < target
```

Možné výsledky nejsou jen GO a FAIL.

### GO

Přínos i kvalita jsou prokázané.

### ITERATE

Use-case dává smysl, ale jeden blocker je řešitelný.

### REDESIGN

Například model je dobrý, ale data pipeline špatná.

### STOP

Hodnota nepokryje náklady nebo riziko.

No-go je legitimní dobrý výsledek pilotu, pokud jsme se levně vyhnuli špatné investici.

---

## 29.11 Industrializace

Funkční notebook není produkční systém.

Industrializace přidá:

```text
authentication
permissions
monitoring
versioning
error handling
SLA
backup / recovery
security review
evaluation regression suite
support owner
```

Také změníme způsob vývoje.

Experiment může mít prompt přímo v Python souboru.

Produkční systém potřebuje:

- prompt/version registry,
- model version,
- release process,
- rollback.

Industrializace je často dražší než vytvoření prvního dema.

To je normální.

---

## 29.12 Škálování

Škálování má několik významů.

### Více uživatelů

Potřebujeme throughput, queues, identity.

### Více dat

Potřebujeme ingestion lifecycle a permissions.

### Více use-cases

Potřebujeme reusable platform components.

### Více týmů

Potřebujeme governance a ownership.

Největší chyba je kopírovat každý pilot jako samostatný stack.

Po prvních úspěšných use-casech hledáme společné komponenty:

```text
model gateway
identity
RAG layer
MCP / tool registry
observability
evaluation platform
approval framework
```

Tím se z jednotlivých experimentů postupně stává firemní AI platforma.

---

# Pilot jako experiment

Dobrý pilot může být popsán na jednu stránku:

```text
HYPOTHESIS
AI zkrátí X bez zhoršení Y.

BASELINE
aktuální čísla.

SCOPE
co přesně testujeme.

DATASET
na čem.

METRICS
jak poznáme úspěch.

RISKS
co může selhat.

DECISION DATE
kdy uděláme go/no-go.
```

To chrání projekt před nekonečným „ještě trochu vylepšíme demo“.

---

# Co si z kapitoly odnést

1. **Pilot má snížit konkrétní nejistotu, ne obecně ukázat, že AI je zajímavá.**
2. **Bez baseline nelze prokázat zlepšení.**
3. **Evaluation dataset musí obsahovat i edge cases a známé failure modes.**
4. **Měříme kvalitu, čas, náklady, chybovost i lidskou korekci.**
5. **Typ chyby může být důležitější než celkové accuracy.**
6. **User adoption je součást výsledku pilotu, ne problém „po nasazení“.**
7. **Go/no-go criteria definujeme předem.**
8. **No-go může být velmi úspěšný výsledek experimentu.**
9. **Industrializace přidává security, observability, ownership a release discipline.**
10. **Při škálování stavíme reusable capability, ne desítky izolovaných chatbotů.**

Technologie ale není jediná proměnná.

Další kapitola se podívá na často nejtěžší část adopce:

> **lidi, důvěru a změnu pracovních návyků.**
