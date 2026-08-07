---
title: "B. Přehled modelů — snapshot 08/2026"
part: "PŘÍLOHY"
status: final-draft
version: "0.7"
updated: 2026-08-07
---

# B. Přehled modelů — snapshot 08/2026

**[Snapshot 08/2026]**

> **Snapshot k 7. 8. 2026.** Jde o mapu trhu, ne žebříček. Názvy, ceny, dostupnost i licence se mění rychle; před nasazením ověř primární zdroj výrobce.

## B.1 Frontier a cloudové rodiny

| Provider | Aktuální příklady | Typická role | Poznámka |
|---|---|---|---|
| OpenAI | GPT-5.6 Sol / Terra / Luna | frontier reasoning až high-throughput | Sol je flagship; Terra/Luna snižují cenu a latency podle workloadu |
| Anthropic | Claude Fable 5 / Sonnet 5 / Opus 4.8 | long-horizon, coding, agents, knowledge work | **nepoužívat neověřený název „Opus 5“**; Fable 5 je aktuální nejvýkonnější GA třída |
| Google | Gemini 3.1 Pro / 3.6 Flash / 3.5 Flash-Lite | complex reasoning, multimodal, agentic throughput | 3.6 Flash a 3.5 Flash-Lite jsou GA od 07/2026 |
| xAI / SpaceXAI | Grok 4.5 | coding, agentic tasks, knowledge work | snapshot 07/2026 |
| Cohere | Command A+ | enterprise, multilingual, RAG, sovereign deployment | open weights, **Apache 2.0**, 218B total / 25B active |

## B.2 Významné open-weight rodiny

| Rodina | Ověřený snapshot 08/2026 | Licence / poznámka |
|---|---|---|
| Qwen | Qwen3.6, včetně 35B-A3B MoE | open weights; konkrétní release vždy ověřit |
| DeepSeek | DeepSeek-V4 Pro / V4 Flash | API V4 od 24. 4. 2026; deployment/licenci kontrolovat podle release |
| Gemma | Gemma 4: E2B, E4B, 12B, 26B A4B, 31B | **Apache 2.0**, open weights |
| Mistral | Mistral Small 4 | **Apache 2.0**, reasoning + multimodal + agentic coding |
| Llama | aktuální Llama rodiny | vlastní licence; open-weight ≠ automaticky open-source licence |

## B.3 Specializované modely, které stojí za sledování

- **Cohere Rerank 4.0** — varianty Pro/Fast pro reranking.
- **Cohere Transcribe (`cohere-transcribe-03-2026`)** — 2B ASR, 14 jazyků, Apache 2.0.
- embedding modely, speech, image a video modely vybírej jako samostatné komponenty, ne jako přílepky k jednomu „hlavnímu LLM“.

## B.4 Praktické velikostní kategorie pro lokální AI

| Kategorie | Typické použití | Poznámka |
|---|---|---|
| velmi malé / edge | routing, klasifikace, function calling | vysoký throughput, omezenější reasoning |
| ~7B–14B | lokální chat, extraction, lehčí coding, RAG generation | často vhodná třída pro 16 GB VRAM v kvantizaci |
| ~20B–40B | náročnější workstation použití | typicky více VRAM / unified memory |
| ~70B dense | server / 48 GB+ praktická GPU třída v Q4 | dlouhý kontext a KV cache mohou potřebovat více |
| velké MoE | serverové nasazení | active parameters ≠ velikost všech vah v paměti |

## B.5 Primární zdroje snapshotu

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

## B.6 Pravidlo aktualizace

Před každým dalším vydáním znovu fact-checkuj kapitolu 5 a tuto přílohu. Principy knihy mají stárnout pomalu; tento snapshot má stárnout přiznaně.
