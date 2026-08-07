---
title: "8. Jak provozovat LLM lokálně"
part: "IV — Cloud, lokální AI a hardware"
status: final-draft
version: "0.5"
updated: 2026-08-07
snapshot: "2026-08-07"
---

# 8. Jak provozovat LLM lokálně

> **Snapshot k 7. 8. 2026.** Konkrétní nástroje (Ollama, llama.cpp, vLLM, Open WebUI) a hardwarové třídy odpovídají stavu k tomuto datu. Principy — vztah velikosti modelu, kvantizace, paměti a KV cache — stárnou výrazně pomaleji.

<!-- visual:08-local-memory-stack.svg -->

![Paměťové vrstvy lokálního LLM](assets/diagrams/08-local-memory-stack.svg)

*Obrázek: VRAM není jen velikost modelových vah.*


Když poprvé začneme zkoušet lokální LLM, velmi rychle narazíme na záplavu pojmů:

```text
8B
32B
Q4_K_M
FP16
GGUF
VRAM
KV cache
CUDA
Metal
llama.cpp
vLLM
Ollama
```

Na první pohled to vypadá mnohem složitěji než otevřít cloudový chat.

Ve skutečnosti stačí pochopit několik základních vztahů.

Nejdůležitější je tento:

> **Velikost modelu určuje přibližně množství paměti, které potřebujeme. Kvantizace tuto potřebu snižuje. Context a runtime přidávají další paměť. Hardware potom určuje, jak rychle inference poběží.**

Zbytek jsou implementační detaily.

---

## 8.1 CPU, GPU a NPU

LLM je možné spustit na různých typech výpočetního hardware.

### CPU

CPU je univerzální procesor.

Výhodou je, že má přístup k velké systémové RAM.

Nevýhodou je nižší paralelní výpočetní propustnost proti moderním GPU.

CPU inference může být velmi užitečná pro:

- malé modely,
- experimenty,
- embedding modely,
- pomalé background úlohy,
- část modelu, která se nevejde do GPU.

### GPU

GPU je pro LLM zásadní hlavně díky masivní paralelizaci a vysoké paměťové propustnosti.

Při generování tokenu musí model opakovaně číst velké množství vah.

Proto je důležité nejen množství VRAM, ale také:

```text
memory bandwidth
```

Dvě grafické karty se stejnou kapacitou VRAM mohou mít velmi rozdílnou inference rychlost.

### NPU

NPU — Neural Processing Unit — je specializovaný akcelerátor pro AI operace.

Najdeme jej v:

- telefonech,
- noteboocích,
- moderních SoC.

NPU je výborná pro energeticky efektivní inference podporovaných modelů, ale ekosystém pro velká lokální LLM je stále méně univerzální než CUDA nebo Metal.

Prakticky tedy v roce 2026 stále často platí:

```text
větší lokální LLM
→ GPU nebo Apple unified memory
```

---

## 8.2 RAM vs. VRAM

### RAM

Systémová paměť počítače.

Používá ji:

- operační systém,
- aplikace,
- CPU inference,
- data.

### VRAM

Paměť přímo na diskrétní GPU.

Má velmi rychlé spojení s GPU, ale její kapacita bývá výrazně menší než systémová RAM.

Například:

```text
PC
├── 64 GB RAM
└── 16 GB VRAM
```

Pokud se celý model vejde do 16GB VRAM, může běžet kompletně na GPU.

Pokud ne, některé inference enginy umožňují část modelu držet v RAM:

```text
část modelu → VRAM
část modelu → RAM
```

To se označuje například jako **CPU offload**.

Funguje to.

Ale přenos mezi RAM a GPU je pomalejší než čtení přímo z VRAM.

Proto typicky platí:

> **Model, který se celý vejde do rychlé paměti akcelerátoru, poběží výrazně lépe než model, který musí neustále přesouvat data mezi pamětmi.**

---

## 8.3 Unified Memory u Apple Silicon

Apple Silicon používá jinou architekturu.

CPU a GPU sdílejí jednu **unified memory**.

Místo:

```text
64 GB RAM
+
16 GB VRAM
```

máme například:

```text
64 GB unified memory
      ↑
   CPU i GPU
```

To je pro LLM velmi zajímavé.

Velká část paměti může být použita pro model bez nutnosti kopírovat data mezi samostatnou RAM a VRAM.

Proto může Mac s 64 nebo 128 GB unified memory spustit model, který by na běžné NVIDIA kartě s 16 nebo 24 GB VRAM vůbec celý nevešel.

Ale existuje důležité **ale**.

Kapacita paměti není totéž jako rychlost.

Inference výrazně ovlivňuje:

- memory bandwidth,
- počet GPU jader,
- konkrétní generace čipu.

Mac může model **spustit**, ale nemusí jej generovat stejně rychle jako high-end NVIDIA GPU.

> **Apple Silicon je mimořádně zajímavý poměrem dostupné paměti, spotřeby a jednoduchosti. NVIDIA má stále velmi silnou výhodu ve výkonu a ekosystému CUDA.**

---

## 8.4 Co znamená 8B, 14B, 32B, 70B…

Číslo označuje přibližný počet parametrů.

```text
8B  = 8 miliard parametrů
14B = 14 miliard
32B = 32 miliard
70B = 70 miliard
```

Parametry jsou čísla, která se model během trénování naučil.

Čím více parametrů, tím více paměti potřebujeme pro jejich uložení.

Ale pozor:

```text
větší model
≠
automaticky lepší model
```

Novější 14B model může překonat starší 32B nebo 70B model v celé řadě úloh.

Velikost parametrů je proto hlavně:

- hrubý ukazatel kapacity,
- důležitý údaj pro sizing hardware.

---

## 8.5 FP16, FP8, INT8, INT4

Každý parametr musíme uložit jako číslo.

Pokud použijeme 16 bitů na parametr:

```text
8B × 16 bitů
≈ 16 GB
```

Použijeme-li 8 bitů:

```text
8B × 8 bitů
≈ 8 GB
```

A při přibližně 4bitové kvantizaci:

```text
8B × 4 bity
≈ 4 GB
```

To je pouze teoretická velikost vah.

Reálný soubor nebo inference bude potřebovat trochu více kvůli:

- quantization metadata,
- runtime strukturám,
- KV cache,
- kontextu.

Ale jako mentální model je výpočet velmi užitečný.

---

## 8.6 Quantization prakticky

Kvantizace sníží přesnost reprezentace vah.

Místo velmi přesných čísel používáme méně bitů.

Je to podobné jako komprese obrazu.

Původní fotografie může mít obrovský soubor.

JPEG ji zmenší a většina informace zůstane vizuálně zachována.

Podobně kvalitní kvantizace dokáže dramaticky zmenšit LLM s relativně malým poklesem kvality.

Běžně se setkáme s variantami jako:

```text
Q8
Q6
Q5
Q4
Q3
```

Velmi hrubě:

```text
vyšší číslo
→ více paměti
→ obvykle vyšší kvalita

nižší číslo
→ méně paměti
→ vyšší riziko ztráty kvality
```

Pro lokální použití bývá kvalitní Q4 nebo Q5 často velmi rozumný kompromis.

Extrémní kvantizace pouze proto, abychom spustili příliš velký model, nemusí být nejlepší strategie.

Někdy je lepší:

```text
novější 14B model v dobré kvantizaci
```

než:

```text
32B model stlačený na hranici použitelnosti
```

---

## 8.7 Kolik paměti model potřebuje

Pro rychlý odhad vah můžeme použít:

```text
paměť vah ≈ počet parametrů × počet bitů / 8
```

Přibližná tabulka pro 4bitové váhy:

| Model | Teoretické Q4 váhy | Prakticky počítej přibližně |
|---|---:|---:|
| 4B | 2 GB | 2.5–4 GB |
| 8B | 4 GB | 5–7 GB |
| 14B | 7 GB | 8–11 GB |
| 32B | 16 GB | 18–24 GB |
| 70B | 35 GB | 40–50+ GB |

Rozsah je záměrně široký.

Záleží na:

- quant formátu,
- architektuře modelu,
- délce kontextu,
- velikosti KV cache,
- runtime.

### KV cache

Při generování si model uchovává informace o předchozích tokenech.

Čím delší context, tím více paměti může KV cache spotřebovat.

Proto model, který se krásně vejde při 4K kontextu, může narazit na limit při 128K.

Toto je častá chyba při sizingu.

> **Nestačí, aby se vešly váhy. Musí se vejít celý běžící workload.**

---

## 8.8 Co reálně zvládne 8 GB VRAM

8 GB VRAM je dnes spodní hranice pro pohodlné experimentování s moderními lokálními LLM.

Rozumně zde poběží například:

- 3B–4B modely ve vysoké kvalitě,
- 7B–8B modely v Q4,
- embedding modely,
- malé vision modely.

Problém nastane u:

- velkého kontextu,
- multimodálních modelů,
- 14B a větších modelů.

Ty lze někdy spustit s offloadem do RAM, ale rychlost se může výrazně snížit.

8GB GPU je tedy výborná pro:

```text
učení
prototypy
malé agenty
specializované modely
```

Méně vhodná pro ambici:

```text
lokální náhrada nejlepšího frontier modelu
```

---

## 8.9 Co reálně zvládne 16 GB VRAM

16 GB VRAM je velmi zajímavá praktická třída.

Typicky umožní:

- 7B–8B modely s velkou rezervou,
- 14B modely v kvalitní kvantizaci,
- některé modely kolem 20B,
- experimenty s většími modely pomocí offloadu.

32B model v Q4 je už často na hranici nebo nad čistou VRAM kapacitou, protože samotné váhy mohou zabrat zhruba 16–20 GB a potřebujeme runtime a KV cache.

To ale neznamená, že 16GB karta je pro agentní systém slabá.

Naopak.

Pro mnoho úloh může být velmi výkonná kombinace:

```text
14B lokální model
+
embedding model
+
RAG
+
Python
+
search
+
specializované nástroje
```

Místo snahy spustit co největší LLM můžeme postavit **lepší systém**.

To je důležitý princip celé knihy.

---

## 8.10 Co přinese 32 GB VRAM

32 GB VRAM výrazně rozšiřuje možnosti.

Dostáváme se k pohodlnému provozu:

- 20B–32B modelů v kvalitních kvantizacích,
- větších multimodálních modelů,
- delšího kontextu,
- více současných workloadů.

Některé větší modely lze provozovat kombinací VRAM a RAM.

70B Q4 se ale stále typicky nevejde celý do 32GB VRAM.

Potřebujeme:

- více VRAM,
- unified memory,
- multi-GPU,
- nebo CPU offload.

32GB karta je velmi zajímavý sweet spot pro výkonnou osobní nebo menší firemní workstation.

---

## 8.11 Apple Silicon vs. NVIDIA

Neexistuje univerzální vítěz.

### Apple Silicon

Výhody:

- velká unified memory,
- nízká spotřeba,
- tichý provoz,
- jednoduché desktop prostředí,
- velmi dobrá podpora přes llama.cpp / Metal.

Nevýhody:

- nižší kompatibilita s CUDA-centric projekty,
- méně vhodný pro některé training nebo specializované frameworky,
- vysoké konfigurace paměti jsou drahé.

### NVIDIA

Výhody:

- CUDA ekosystém,
- vysoký inference výkon,
- široká podpora v AI software,
- vhodnost pro production servery,
- vLLM a další optimalizované inference enginy.

Nevýhody:

- VRAM je drahá,
- spotřeba,
- hluk a chlazení workstation,
- model je omezen kapacitou konkrétní GPU nebo multi-GPU konfigurací.

Zjednodušeně:

```text
chci velkou paměť a jednoduchý osobní lokální AI počítač
→ Apple Silicon je velmi zajímavý

chci maximální výkon, CUDA a produkční inference
→ NVIDIA je obvykle přirozenější volba
```

---

## 8.12 Linux workstation

Pro vážnější on-prem experimenty je Linux stále velmi přirozené prostředí.

Typický stack může vypadat:

```text
Linux
↓
NVIDIA driver
↓
CUDA
↓
inference engine
↓
model server
↓
OpenAI-compatible API
↓
aplikace / agenti
```

Výhoda je, že lokální model potom vypadá pro aplikaci téměř stejně jako cloudové API.

Například:

```text
cloud:
https://provider.example/v1/chat

local:
http://localhost:8000/v1/chat
```

Aplikace pouze změní endpoint a model.

To je ideální pro hybridní architekturu.

---

## 8.13 Ollama

**Ollama** je jeden z nejjednodušších způsobů, jak začít s lokálními modely.

Typický workflow:

```text
nainstalovat Ollama
↓
stáhnout model
↓
spustit
↓
chat nebo API
```

Je vhodná pro:

- začátečníky,
- desktop experimenty,
- lokální API,
- rychlé testování více modelů.

Ollama schovává velkou část detailů inference.

To je výhoda pro začátek.

Pro maximální optimalizaci produkčního serveru můžeme později použít jiné nástroje.

---

## 8.14 llama.cpp

**llama.cpp** je jeden ze základních projektů lokálního LLM ekosystému.

Je optimalizovaný pro efektivní inference na široké škále hardware:

- CPU,
- NVIDIA,
- Apple Metal,
- další backendy.

Velmi důležitý je formát **GGUF**, který se stal běžným způsobem distribuce kvantizovaných modelů pro lokální inference.

llama.cpp umožňuje jemnější kontrolu nad:

- kvantizací,
- offloadem vrstev,
- kontextem,
- výkonem.

Pokud Ollama představuje pohodlnou vrstvu pro uživatele, llama.cpp je často blíže samotnému inference motoru.

---

## 8.15 vLLM

**vLLM** je zaměřen spíše na serverovou a produkční inference.

Jeho silná stránka není primárně:

```text
spustit jeden model pro jednoho člověka na notebooku
```

ale například:

```text
jeden GPU server
↓
desítky nebo stovky souběžných requestů
```

Důležité oblasti:

- batching,
- efektivní práce s KV cache,
- vysoký throughput,
- OpenAI-compatible API,
- multi-GPU.

Pro malý firemní model server je vLLM velmi důležitý kandidát.

---

## 8.16 Open WebUI

**Open WebUI** je uživatelské rozhraní.

Není to samotný model ani inference engine.

Může se připojit k lokálním nebo vzdáleným model serverům a nabídnout prostředí podobné cloudovým chatovacím aplikacím.

To je užitečné, protože interní uživatel nemusí znát:

- Ollama API,
- vLLM endpoint,
- model parameters.

Vidí normální chat.

Pod ním ale může běžet náš vlastní stack.

---

## 8.17 Model server vs. uživatelské rozhraní

Toto rozlišení je velmi důležité.

### Model server

Provádí inference.

Například:

- Ollama,
- llama.cpp server,
- vLLM.

### User interface

Umožňuje člověku model používat.

Například:

- Open WebUI,
- vlastní webová aplikace.

Architektura:

```text
Open WebUI
     ↓
model server
     ↓
GPU
     ↓
model
```

Pokud tyto vrstvy oddělíme, můžeme později:

- změnit model,
- změnit server,
- přidat více GPU,
- zachovat stejné UI.

To je základ dobré architektury.

---

## 8.18 Lokální benchmark

Před rozhodnutím, zda hardware stačí, je nejlepší spustit vlastní benchmark.

Neměřme pouze:

```text
tokens per second
```

Změřme několik skutečných úloh.

Například:

### Test A — krátký chat

```text
500 tokenů input
300 tokenů output
```

### Test B — dlouhý dokument

```text
20 000 tokenů input
500 tokenů output
```

### Test C — coding

```text
5 souborů projektu
oprava funkce
```

### Test D — RAG

```text
retrieval
+
5 chunks
+
odpověď s citacemi
```

Měříme:

- TTFT,
- output tokens/s,
- celkový čas,
- peak RAM,
- peak VRAM,
- kvalitu výstupu.

Až potom víme, zda je hardware vhodný.

---

## 8.19 Tokens per second a proč nejsou všechno

Lokální AI komunita často porovnává výkon podle tokens per second. Je to užitečné číslo, ale může být zavádějící: model generující 80 tokens/s, který potřebuje tři pokusy, je reálně pomalejší než model s 25 tokens/s, který úlohu vyřeší napoprvé. A u agentů často většinu času zabírají nástroje (search, Python, simulace, testy), ne generování.

Platí stejná metrika jako při výběru modelu v kapitole 6.8: **čas od zadání úlohy k ověřenému použitelnému výsledku.**

---

## Praktická doporučená cesta

Pro začátečníka:

```text
Ollama
+
Open WebUI
+
7B–14B model
```

Pro technické experimenty:

```text
llama.cpp
+
GGUF
+
vlastní benchmark
```

Pro firemní model server:

```text
Linux
+
NVIDIA GPU
+
vLLM
+
OpenAI-compatible API
+
authentication
+
monitoring
```

A nad tím může běžet:

```text
RAG
agent
model router
firemní aplikace
```

---

## Co si z kapitoly odnést

1. **Kapacita paměti určuje, jak velký model můžeme rozumně spustit.**
2. **Kvantizace dramaticky snižuje paměťové nároky.**
3. **Nestačí počítat pouze váhy — context a KV cache potřebují další paměť.**
4. **8 GB je dobrý vstup do lokální AI, 16 GB je velmi použitelná praktická třída a 32 GB výrazně rozšiřuje možnosti.**
5. **Apple Silicon nabízí velkou unified memory; NVIDIA nabízí špičkový výkon a CUDA ekosystém.**
6. **Ollama je jednoduchý start, llama.cpp dává větší kontrolu a vLLM cílí na serverový throughput.**
7. **Open WebUI je UI, ne model server.**
8. **Tokens per second nejsou totéž jako produktivita celého workflow.**

Teď už víme, co model je, jak jej vybírat a kde jej provozovat.

Další část knihy se přesune od infrastruktury k člověku:

> **Jak vlastně modelu zadat práci tak, aby dostal správný cíl, kontext a omezení?**
