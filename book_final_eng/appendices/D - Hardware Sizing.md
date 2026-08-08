---
title: "D. Hardware Sizing"
part: "APPENDICES"
status: release-candidate
version: "0.8-eng"
updated: 2026-08-08
---

# D. Hardware Sizing

This appendix is a practical planning guide for local inference, not a benchmark of specific GPUs. Real memory use and speed depend on model architecture, quantization, runtime, context length, KV cache, batch size, and offload strategy.

## Estimate Weight Memory First

```text
weight memory ≈ parameter count × bits per parameter / 8
```

For an 8B model, roughly:

```text
FP16  ≈ 16 GB weights
INT8  ≈  8 GB weights
4-bit ≈  4–5 GB weights
```

That is not total memory. Also budget for KV cache, runtime/workspace buffers, context, multimodal components, and operating headroom.

A practical planning model is:

```text
required accelerator memory ≈
    model weights
  + KV cache
  + runtime / workspace buffers
  + operating headroom
```

Adding roughly 10% headroom is a useful first sanity check, then increase it for long context and concurrency.

For a dense **70B Q4** model, think in terms of a **48 GB-class single-GPU practical minimum**, not 16 GB. Exact requirements still depend on runtime and workload.

## Context Costs Memory

```text
larger context
→ larger KV cache
→ more memory
→ often higher latency
```

Always record model, quantization, context length, batch size, and runtime when reporting memory use.

## Practical Hardware Classes

### CPU-only

Useful for first experiments, embeddings, background work, and models that fit in RAM but not VRAM. The main disadvantage is lower interactive speed.

```text
THE MODEL RUNS
≠
THE MODEL IS PRACTICALLY USABLE
```

### 8 GB VRAM

Good entry point for 3B–8B models, quantized 7B/8B systems, embeddings, and lighter vision/coding experiments.

### 16 GB VRAM

A seriously useful small-workstation class. Strong 7B–14B models at sensible quantization are often the sweet spot for local RAG generation, extraction, classification, routing, simple agents, and coding.

### 24 GB VRAM

Adds more room for high-quality 14B inference, some 20B–30B-class models, longer context, and multimodal work.

### 32 GB VRAM

Comfortable workstation tier for many models in the 20B–40B range depending on architecture and quantization, with more space for KV cache and multi-model pipelines.

### 48 GB VRAM

Moves toward small-server territory: larger models, longer context, more concurrent users, internal AI service development.

At this point measure requests/min, concurrency, p95 latency, and GPU utilization — not only desktop tokens/s.

## Apple Silicon Unified Memory

Apple Silicon lets CPU and GPU share unified memory, which can make large quantized models practical on machines with large memory configurations.

Capacity is not speed. Bandwidth, chip generation, GPU resources, and OS/application reserve still matter.

## Multi-GPU

Useful when models exceed one card, throughput needs increase, or multiple replicas/models run concurrently. It also adds communication overhead, cost, power/cooling, and operational complexity.

For many smaller organizations:

```text
one strong GPU server
+
efficient smaller model
+
cloud fallback
```

may be more rational than recreating a frontier datacenter locally.

## Multi-User Server Sizing

Start with workload questions:

```text
How many users?
How many concurrent requests?
How long are inputs and outputs?
What p95 latency target?
Which model?
How many hours/day at high utilization?
```

Track at least:

| Metric | Why |
|---|---|
| time to first token | interactive feel |
| output tokens/s | generation speed |
| requests/s | throughput |
| p50 / p95 latency | real operating behavior |
| GPU memory | capacity limit |
| GPU utilization | hardware efficiency |
| queue time | overload indicator |
| energy / task | TCO input |

## Size the Whole Pipeline

A real on-prem system may include:

```text
LLM
embedding model
reranker
OCR / parser
search index
agent runtime
web UI
observability
```

Not everything has to run on the GPU. Size hardware for the whole pipeline, not one model file.

## Benchmark Record

For every benchmark record:

```text
date
hardware
RAM / VRAM
OS
runtime + version
exact model
quantization
context length
prompt tokens
output tokens
time to first token
tokens/s
peak memory
quality score on your own eval set
```

> **Hardware sizing is not the search for the largest model that fits. It is the search for the least expensive configuration that meets required quality, latency, privacy, and throughput.**