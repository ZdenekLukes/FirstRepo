---
title: "G. Your Own Experiments"
part: "APPENDICES"
status: international-draft
version: "0.8-eng"
updated: 2026-08-08
---

# G. Your Own Experiments

This appendix is not a catalog of internet benchmarks. It is a template for building your own evidence: what you tested, on which hardware, with which exact model/runtime, and what the experiment actually established.

A useful record looks like:

```text
Model X / quantization Y
on our 40-case test set
92% extraction accuracy
vs.
Model Z 95%

but X was 2.4× faster
```

## Required Experiment Header

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

## What to Record

### Question

One concrete sentence.

Good:

> Is an 8B local model sufficient to extract 12 parameters from our technical reports?

Bad:

> How good is local AI?

### Hypothesis

Write down what you expect before the experiment.

### Baseline

Record human/software time, error rate, and steps where applicable.

### Data

Record number of cases, version, real vs. synthetic origin, and edge-case coverage.

### Result

Separate:

```text
QUALITY
PERFORMANCE
COST
FAILURE MODES
```

## Minimal Results Table

| Metric | Baseline | Variant A | Variant B |
|---|---:|---:|---:|
| Correct cases | | | |
| Critical errors | | | |
| Median latency | | | |
| Human correction time | | | |
| Cost / task | | | |

## Failure Log

| Case | What happened | Root cause | Category | Fix | Regression test? |
|---|---|---|---|---|---|
| 001 | | | model / context / retrieval / tool / data | | |

Every important production failure should become a future test case.

## Experiment Template

### Experiment `[ID]` — `[name]`

**Date:**  
**Question:**  
**Hypothesis:**  
**Baseline:**  
**Model:**  
**Runtime:**  
**Hardware:**  
**Quantization:**  
**Context:**  
**Tools:**  
**Data / eval set:**  

#### Procedure
1. 
2. 
3. 

#### Results

| Metric | Value |
|---|---:|
| | |

#### What worked
- 

#### What did not
- 

#### Largest failure category

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

#### What I learned
- 

#### Next step
- 

---

## EXP-001 — What Changed from 8 GB to 32 GB VRAM

**Status:** observational experiment; not a published performance benchmark  
**Question:** What is the difference between a model that can technically run and a local AI stack that is practical to use?

**Hardware A:** laptop with NVIDIA RTX 4060, 8 GB VRAM  
**Hardware B:** workstation with Radeon AI PRO R9700, 32 GB VRAM  
**Observed workload:** text LLMs; on 32 GB also Open WebUI + Whisper speech-to-text + Kokoro text-to-speech  
**Model size class on 32 GB:** approximately 30B–40B depending on model and quantization

### What the experiment supports

| Observation | 8 GB VRAM | 32 GB VRAM |
|---|---|---|
| smaller local LLMs | practical | easy |
| larger models | interactivity drops strongly when spill/offload to RAM dominates | much more room for 30B–40B-class quantized models |
| several AI components at once | strongly constrained | LLM + UI + STT + TTS can coexist as one stack |

### What it does not support

The first experiment was not designed as a reproducible benchmark. We do not have a consistent archive of exact model/quantization, TTFT, tokens/s, power draw, and identical eval set across both GPUs.

So I do **not** turn it into a numerical speed claim.

Its valid conclusion is architectural:

> **VRAM capacity does not only set the maximum model size. It determines whether weights, KV cache, and additional components can coexist while the system remains interactive.**

## Recommended Backlog

### EXP-002 — Small Local Model vs. Frontier Cloud
Use the same 30–50 real tasks and identify which work is good enough locally.

### EXP-003 — Long Context vs. RAG
Compare quality, source accuracy, latency, and token cost.

### EXP-004 — Agent without Verifier vs. with Verifier
Choose a task with a programmatically checkable result.

### EXP-005 — Single-Agent vs. Multi-Agent
Compare success rate, steps, latency, cost, and debugging effort.

## Rule for Published Experiments

An experiment belongs in a published edition only when we can reconstruct:

```text
what was tested
on what
how
against which baseline
with what result
```

The purpose is not to turn personal impressions into universal benchmarks. It is to show readers how to create evidence of their own.