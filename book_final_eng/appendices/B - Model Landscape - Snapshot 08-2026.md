---
title: "B. Model Landscape — Snapshot 08/2026"
part: "APPENDICES"
status: international-draft
version: "0.8-eng"
updated: 2026-08-08
---

# B. Model Landscape — Snapshot 08/2026

**[Snapshot 08/2026]**

> **Snapshot: August 7, 2026.** This is a market map, not a ranking. Names, prices, availability, and licenses change quickly; verify the provider’s primary source before deployment.

## Frontier and Cloud Families

| Provider | Examples in this snapshot | Typical role |
|---|---|---|
| OpenAI | GPT-5.6 family | frontier reasoning through lower-cost/high-throughput tiers |
| Anthropic | Claude Fable 5 / Sonnet 5 / Opus 4.8 | long-horizon work, coding, agents, knowledge work |
| Google | Gemini 3.1 Pro / 3.6 Flash / 3.5 Flash-Lite | complex reasoning, multimodal work, high throughput |
| xAI | Grok 4.5 | coding, agentic tasks, knowledge work |
| Cohere | Command A+ | enterprise, multilingual, RAG, sovereign deployment |

## Important Open-Weight Families

| Family | Snapshot note |
|---|---|
| Qwen | Qwen3.6 family; broad coding, vision, speech, embedding ecosystem |
| DeepSeek | V4-era API/model family in the source snapshot |
| Gemma | Gemma 4 family and specialist variants |
| Mistral | Mistral Small 4 and other efficient open-weight models |
| Llama | major open-weight ecosystem; verify custom license per release |

## Practical Local Size Classes

| Class | Typical use | Planning note |
|---|---|---|
| very small / edge | routing, classification, function calling | high throughput, limited hard reasoning |
| ~7B–14B | local chat, extraction, lighter coding, RAG generation | practical class for many 16 GB VRAM systems |
| ~20B–40B | harder workstation workloads | generally needs more VRAM/unified memory |
| ~70B dense | server / practical 48 GB+ GPU class at Q4 | context and KV cache can require more |
| large MoE | server deployment | active parameters are not total weight memory |

## Primary Sources Used by the Snapshot

- OpenAI GPT-5.6: https://openai.com/index/gpt-5-6/
- Anthropic Fable 5: https://www.anthropic.com/claude/fable
- Anthropic Sonnet 5: https://www.anthropic.com/news/claude-sonnet-5
- Anthropic Opus 4.8: https://www.anthropic.com/news/claude-opus-4-8
- Google Gemini API releases: https://ai.google.dev/gemini-api/docs/changelog
- Google Gemini 3.6 Flash: https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash
- xAI Grok 4.5: https://x.ai/news/grok-4-5
- DeepSeek API updates: https://api-docs.deepseek.com/updates
- Qwen3.6: https://qwen.ai/blog?id=qwen3.6-35b-a3b
- Gemma 4: https://ai.google.dev/gemma/docs/core/model_card_4
- Mistral Small 4: https://mistral.ai/news/mistral-small-4/
- Cohere Command A+: https://cohere.com/blog/command-a-plus
- Cohere Rerank / Transcribe: https://docs.cohere.com/v2/changelog

## Update Rule

Before every new edition, fact-check Chapter 5 and this appendix from primary sources. The principles of the book should age slowly; this snapshot is designed to age openly.