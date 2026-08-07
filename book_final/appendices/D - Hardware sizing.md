---
title: "D. Hardware sizing"
part: "PŘÍLOHY"
status: final-draft
version: "0.7"
updated: 2026-08-07
---

# D. Hardware sizing

Tato příloha je praktický orientační návod pro lokální inference. Nejde o benchmark konkrétních GPU. Skutečná paměť a rychlost závisí na modelu, kvantizaci, runtime, context length, KV cache, batch size a míře offloadu.

## D.1 Nejdříve odhadni paměť modelu

Velmi hrubý mentální model:

```text
MODEL MEMORY
≈
počet parametrů
×
počet bitů na parametr
```

Příklad řádově:

```text
8B model
FP16  → ~16 GB pouze váhy
INT8  → ~8 GB pouze váhy
4-bit → ~4–5 GB pouze váhy
```

To ale **není celková potřebná paměť**.

Musíme přidat:

- KV cache,
- runtime buffers,
- context,
- případně multimodální encoder,
- další modely, například embeddings,
- rezervu pro operační systém a aplikaci.

Proto model, jehož soubor „se přesně vejde“, nemusí být prakticky použitelný.

## D.1a Praktický VRAM rozpočet

```text
VRAM ≈ weights podle quantizace
     + KV cache podle context length a batch size
     + runtime / workspace buffers
     + orientačně ~10 % provozní rezerva
```

Pro dense **70B Q4** nepočítej s 16 GB. Samotné váhy jsou v desítkách GB; po započtení overheadu, KV cache a runtime je **48 GB praktická minimální single-GPU třída**, nikoli garance pro každý dlouhý kontext.

## D.2 Context stojí paměť

Dlouhý context není zdarma.

```text
větší context
→ větší KV cache
→ více paměti
→ často vyšší latency
```

Při hardware sizingu proto vždy zapisuj:

```text
model
quantization
context length
batch size
runtime
```

Bez těchto údajů je tvrzení „model potřebuje 12 GB“ neúplné.

---

## D.3 CPU-only

### Hodí se pro

- první experiment,
- malé modely,
- embeddings,
- batch úlohy, kde latency není kritická,
- automatizaci běžící na pozadí.

### Výhody

- žádná dedikovaná GPU,
- velká systémová RAM může umožnit spustit model, který by se do VRAM nevešel,
- jednoduché laboratorní prostředí.

### Nevýhody

- generování bývá výrazně pomalejší než na moderní GPU,
- velký model může být technicky spustitelný, ale interaktivně nepříjemný.

Důležitý rozdíl:

```text
MODEL SE SPUSTÍ
≠
MODEL JE PRAKTICKY POUŽITELNÝ
```

---

## D.4 8 GB VRAM

Tuto třídu beru jako vstup do GPU lokální AI.

### Prakticky zajímavé

- malé 3B–8B modely,
- 7B/8B modely v rozumné kvantizaci,
- embeddings,
- lehčí vision modely,
- lokální coding / extraction experimenty.

### Limity

- málo prostoru pro dlouhý kontext,
- větší modely vyžadují offload do RAM,
- více současných komponent rychle vyčerpá VRAM.

Je možné spouštět větší model přes CPU/RAM offload, ale rychlost může dramaticky klesnout.

---

## D.5 16 GB VRAM

Pro malou pracovní stanici je to v roce 2026 velmi použitelná třída.

### Typický sweet spot

```text
7B–14B kvalitní model
+
4/5/8-bit quantization podle potřeby
```

Pro mnoho firemních úloh může tato třída stačit na:

- klasifikaci,
- extrakci,
- RAG generation,
- jednoduchého agenta,
- lokální coding,
- routing,
- structured output.

### Co od 16 GB neočekávat

Největší open-weight frontier modely.

Snaha nacpat příliš velký model pomocí agresivního offloadu může být horší než použít menší model, který běží celý na GPU.

> **Pro produktivitu je často důležitější dostatečně dobrý model s nízkou latencí než největší model, který se podaří technicky spustit.**

---

## D.6 24 GB VRAM

24 GB otevírá výrazně více prostoru pro:

- vyšší kvantizaci 14B modelů,
- část 20B–30B třídy,
- delší context,
- multimodalitu,
- větší batch.

Je to zajímavá třída pro jednoho power usera nebo malý lokální server.

Stále však neplatí:

```text
24 GB VRAM
→ libovolný open-weight model
```

Velké 70B+ a obří MoE modely zůstávají jiná kategorie.

---

## D.7 32 GB VRAM

32 GB je velmi příjemná workstation třída pro experimenty s modely přibližně 20B–40B podle konkrétní architektury a kvantizace.

Výhoda proti 16 GB není jen možnost většího modelu.

Máme více prostoru pro:

```text
model
+
KV cache
+
vision encoder
+
embedding model
+
runtime reserve
```

To je důležité při stavbě skutečného systému, ne pouze jednoho benchmarku.

---

## D.8 48 GB VRAM

48 GB posouvá workstation do menší serverové třídy.

Typické použití:

- větší modely,
- více concurrent requests,
- delší context,
- vývoj a testování interních AI služeb,
- kombinace více modelů v pipeline.

Zde už má smysl více přemýšlet o:

- throughput,
- batching,
- model serveru,
- monitoring,
- více uživatelích.

Neřešíme pouze „tokens/s pro mě“, ale:

```text
requests/min
users
p95 latency
GPU utilization
```

---

## D.9 Apple Silicon unified memory

Apple Silicon je zvláštní tím, že CPU a GPU sdílejí unified memory.

Výhoda:

- model může využít velkou část systémové paměti bez klasického kopírování mezi RAM a dedikovanou VRAM.

To umožňuje spustit překvapivě velké kvantizované modely na stroji s dostatečnou unified memory.

Nevýhoda:

- velikost paměti sama o sobě neříká rychlost,
- bandwidth a konkrétní generace čipu jsou zásadní,
- část paměti potřebuje macOS a aplikace.

Pro sizing proto nechávej rezervu a měř skutečný workload.

---

## D.10 Multi-GPU

Multi-GPU začíná dávat smysl, když:

- model se nevejde na jednu kartu,
- potřebujeme vyšší throughput,
- provozujeme více modelů nebo replicas.

Ale přináší další náklady:

- komunikaci mezi GPU,
- složitější runtime,
- power / cooling,
- vyšší pořizovací cenu,
- složitější debugging.

Multi-GPU není automatický další krok po 16GB kartě.

Pro menší firmu může být ekonomicky lepší:

```text
1 dobrý GPU server
+
menší efektivní model
+
cloud fallback
```

než lokálně replikovat frontier datacenter.

---

## D.11 Server pro více uživatelů

Sizing serveru musí začít workloadem.

Ptej se:

```text
Kolik uživatelů?
Kolik requestů současně?
Jak dlouhé vstupy?
Jak dlouhé výstupy?
Jaký p95 latency target?
Jaký model?
Kolik hodin denně bude systém vytížen?
```

Jednouživatelský benchmark tokens/s nestačí.

Pro server sleduj minimálně:

| Metrika | Proč |
|---|---|
| time to first token | pocitová odezva |
| output tokens/s | rychlost generování |
| requests/s | throughput |
| p50 / p95 latency | chování v reálném provozu |
| GPU memory | kapacitní limit |
| GPU utilization | zda hardware skutečně využíváme |
| queue time | zda je server přetížen |
| energy / task | část TCO |

---

## D.12 Model + RAG + agent je více než model

Reálný on-prem systém může současně potřebovat:

```text
LLM
embedding model
reranker
OCR / parser
vector index
agent runtime
web UI
observability
```

Není nutné, aby vše běželo na GPU.

Například:

- vector database může být CPU workload,
- embedding může běžet batchově,
- LLM dostane prioritu na GPU,
- OCR může být samostatná služba.

Hardware navrhujeme pro **celý pipeline**, ne pro modelový soubor.

---

## D.13 Rychlý rozhodovací strom

```text
Chci se učit / experimentovat?
→ použij hardware, který už máš

Potřebuji interaktivní local AI?
→ preferuj model, který se vejde do akcelerované paměti

Citlivá firemní data + stabilní workload?
→ zvaž dedikovaný on-prem server

Potřebuji frontier reasoning jen občas?
→ hybrid / cloud fallback

Potřebuji mnoho concurrent users?
→ benchmark serverového throughputu, ne desktop tokens/s
```

## D.14 Co zapisovat do každého benchmarku

Bez těchto údajů je výsledek obtížně reprodukovatelný:

```text
date
hardware
RAM / VRAM
OS
runtime + version
model exact name
quantization
context length
prompt tokens
output tokens
time to first token
tokens/s
peak memory
quality score na vlastním eval setu
```

> **Hardware sizing není hledání největšího modelu, který se vejde. Je to hledání nejlevnější konfigurace, která splní požadovanou kvalitu, latenci, privacy a throughput.**