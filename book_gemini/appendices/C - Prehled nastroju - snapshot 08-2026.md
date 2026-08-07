---
title: "C. Přehled nástrojů — snapshot 08/2026"
part: "PŘÍLOHY"
status: final-draft
version: "0.4"
updated: 2026-08-07
---

# C. Přehled nástrojů — snapshot 08/2026

**[Snapshot 08/2026]**

> **Snapshot k 7. 8. 2026.** Smyslem není doporučit jeden „správný stack“, ale ukázat typy nástrojů, které řeší jednotlivé vrstvy AI systému. Před použitím ověř aktuální licenci, podporované modely a security model.

## C.1 Cloud AI

Použití: frontier reasoning, multimodalita, research, coding, elasticita.

Příklady ekosystémů:

- OpenAI,
- Anthropic,
- Google Gemini,
- xAI,
- Cohere,
- Mistral.

Výběr není jen otázka modelu. Kontroluj také:

```text
API
enterprise terms
data retention
region / residency
tool calling
structured output
rate limits
observability
```

## C.2 Lokální inference

### Ollama

Nejjednodušší start pro lokální modely a lokální API.

https://ollama.com/

### llama.cpp

Velmi rozšířený runtime pro GGUF a kvantizované modely, vhodný i pro detailnější experimenty s lokální inference.

https://github.com/ggml-org/llama.cpp

### vLLM

Serverově orientovaný inference engine pro vysoký throughput u podporovaných modelů a GPU.

https://vllm.ai/

## C.3 Chat UI

### Open WebUI

Webové rozhraní vhodné pro lokální i vzdálené modely.

https://openwebui.com/

Dobré UI je užitečné pro experimenty, ale není to samotná AI architektura. Produkční workflow má mít oddělený model gateway, oprávnění, logs a evals.

## C.4 Coding agents

Kategorie nástrojů, které umějí:

```text
read repository
search
edit files
run shell/tests
inspect failures
use Git
```

Patří sem dedicated coding agents, agentní IDE a rozšíření editorů. Při výběru je důležitější pracovní model než logo:

```text
branch
→ agent changes
→ tests
→ diff
→ human review
→ merge
```

## C.5 Agent runtimes a frameworky

### OpenAI Agents SDK

https://openai.github.io/openai-agents-python/

### Pydantic AI

https://ai.pydantic.dev/

### LangGraph

https://docs.langchain.com/oss/python/langgraph/overview

Framework vybírej až tehdy, když víš, co potřebuješ:

- state,
- retry,
- durable execution,
- tool orchestration,
- human approval,
- tracing.

Pro jednoduchý agent může být 50 řádků vlastního kódu srozumitelnější než velký framework.

## C.6 RAG

RAG není jeden produkt. Potřebuje několik vrstev:

```text
parser
chunking
metadata
embedding model
index / search
reranker
LLM
citations
```

První optimalizace má často začít na datech a retrievalu, ne výměnou generativního modelu.

## C.7 Vector databases

Používají se pro similarity search nad embeddings. Konkrétní volba závisí na velikosti dat, filtrování metadat, provozu a existující infrastruktuře.

Možnosti sahají od lokálních embedded indexů až po samostatné databázové služby. Pro malý pilot není nutné začínat distribuovaným clusterem.

## C.8 Speech

Typický lokální nebo cloudový pipeline:

```text
audio
→ speech-to-text
→ LLM processing
→ text-to-speech (volitelně)
```

Pro knowledge workflow je důležitější kvalita transcriptu, timestamps, speaker separation a možnost zpětně dohledat originální audio než samotný chatbot nad přepisem.

## C.9 Image a multimodalita

Kategorie zahrnuje:

- image generation,
- vision-language models,
- OCR / document vision,
- screenshot understanding,
- diagram analysis.

Pro technické dokumenty musí být vždy možné rozlišit:

```text
co model skutečně viděl
vs.
co pouze odhadl
```

## C.10 Automation

Automatizace řeší:

- schedule,
- event triggers,
- queue,
- retries,
- workflow state,
- notifications.

Agent není náhrada scheduleru nebo workflow enginu. Často je nejlepší kombinace:

```text
deterministic workflow
+
LLM pouze v krocích, kde je potřeba interpretace
```

## C.11 Observability

### Langfuse

https://langfuse.com/docs

Observability by měla umožnit dohledat:

```text
model version
prompt / instruction version
retrieved context
tool calls
latency
cost
final output
eval result
```

Citlivá data ale nemají být bezmyšlenkovitě kopírována do logů.

## C.12 Evaluation

Evaluace může být:

```text
unit / schema tests
exact match
retrieval metrics
LLM-as-a-judge
human rubric
end-to-end business KPI
```

Eval framework je méně důležitý než kvalitní test set a stabilní ground truth.

## C.13 Knowledge base

### Obsidian

https://obsidian.md/

Markdown + Git je jednoduchý způsob, jak udržovat osobní nebo projektovou knowledge base čitelnou člověkem i AI nástroji.

## C.14 Jak vybírat nástroj

Před přidáním nové komponenty odpověz:

1. Jaký konkrétní problém řeší?
2. Umím jej vyřešit jednodušeji?
3. Kde poběží?
4. Jaká data uvidí?
5. Jak se autentizuje?
6. Jak se aktualizuje?
7. Jak jej budu monitorovat?
8. Co se stane, když přestane fungovat?

> **Dobrý AI stack není ten s nejvíce frameworky. Je to nejmenší stack, který spolehlivě řeší požadované use-cases.**
