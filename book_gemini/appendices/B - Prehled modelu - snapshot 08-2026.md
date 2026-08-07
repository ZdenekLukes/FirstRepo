---
title: "B. Přehled modelů — snapshot 08/2026"
part: "PŘÍLOHY"
status: final-draft
version: "0.4"
updated: 2026-08-07
---

# B. Přehled modelů — snapshot 08/2026

**[Snapshot 08/2026]**

> **Snapshot k 7. 8. 2026.** Tato tabulka je orientační mapa trhu, ne žebříček. Konkrétní dostupnost, ceny, limity a licence se mohou měnit rychle. Před nasazením vždy ověř aktuální primární zdroj výrobce.

## B.1 Frontier a cloudové rodiny

| Provider | Rodina / příklad | Typická role | Cloud / local | Open weights | Silné stránky | Poznámka |
|---|---|---|---|---|---|---|
| OpenAI | GPT-5.x / GPT-5.6 Sol | general + reasoning + coding | cloud | ne | komplexní reasoning, coding, tools, multimodalita | vybírat i podle inference effort, ne jen názvu modelu |
| Anthropic | Claude Sonnet 5 | general / coding / agents | cloud | ne | coding, tool use, dlouhé workflow | silný ekosystém kolem Claude Code |
| Anthropic | Claude Opus 4.8 | nejnáročnější knowledge work | cloud | ne | dlouhé a komplexní úlohy | vyšší třída pro případy, kde kvalita převáží cenu |
| Google | Gemini 3.x | general multimodal | cloud | ne | multimodalita, dlouhý kontext, Google ecosystem | více tříd Pro / Flash / specializované varianty |
| xAI | Grok 4.5 | general / coding / agents | cloud | ne | coding, agentní práce, web-connected workflow | ověřovat konkrétní produktové integrace |
| Cohere | Command A+ | enterprise / RAG / sovereign AI | cloud + private deployment | podle konkrétní varianty | enterprise, multilingual, RAG | zajímavý pro privátní nasazení a podnikové workflow |

## B.2 Významné open-weight rodiny

| Rodina | Typické varianty | Lokální použitelnost | Licence | Praktická poznámka |
|---|---|---|---|---|
| Qwen | general, Coder, VL, Omni, ASR, TTS, embeddings | od malých po velmi velké modely | ověřit konkrétní release | široký ekosystém pro lokální a specializované použití |
| DeepSeek | general / reasoning / coding, MoE | menší varianty lokálně; největší serverově | ověřit konkrétní release | aktivní parametry nejsou totéž jako paměť pro celé váhy |
| Llama | general + multimodal | široká podpora runtime | vlastní licence | velmi rozšířený ekosystém; open-weight ≠ automaticky Apache 2.0 |
| Mistral | malé a střední general / reasoning / multimodal | často praktická střední třída | některé modely Apache 2.0 | dobrý kompromis výkon / provozní náročnost |
| Gemma | general + FunctionGemma + MedGemma + embeddings | od edge po workstation | ověřit release | silná specializace malých modelů |

## B.3 Model nevybírej podle jediné tabulky

Při výběru pro reálný systém si připrav vlastní sloupce:

```text
use-case
quality score na mém test setu
latency
cost / request
tokens/s
VRAM / RAM
context requirement
tool calling
structured output
multimodalita
licence
privacy / deployment boundary
```

Model, který vede obecný benchmark, může být horší volba než menší model, pokud:

- úloha je jednoduchá a opakuje se milionkrát,
- potřebujeme nízkou latenci,
- data nesmí opustit infrastrukturu,
- vyžadujeme specifickou licenci,
- model musí spolehlivě vracet konkrétní schema.

## B.4 Praktické velikostní kategorie pro lokální AI

Velikost modelu berme jen jako hrubý první filtr.

| Kategorie | Typické použití | Poznámka |
|---|---|---|
| velmi malé / edge | routing, klasifikace, function calling | vysoký throughput, omezený reasoning |
| ~7B–14B | lokální chat, extrakce, lehčí coding, RAG generation | často rozumná třída pro 16GB VRAM v kvantizaci |
| ~20B–40B | náročnější lokální práce | typicky vyžaduje více VRAM / unified memory nebo offload |
| 70B+ | server / více GPU / velká unified memory | kvalita může růst, ale výrazně roste provozní náročnost |
| velké MoE | serverové nasazení | nízký počet aktivních parametrů neznamená malé modelové soubory |

Konkrétní paměť vždy závisí na:

- přesné architektuře,
- kvantizaci,
- context length,
- KV cache,
- runtime,
- batch size,
- offloadu.

Proto hardware sizing řeší samostatná příloha D.

## B.5 Primární zdroje snapshotu

- OpenAI Model Release Notes — https://help.openai.com/en/articles/9624314-model-release-notes
- Anthropic: Claude Sonnet 5 — https://www.anthropic.com/news/claude-sonnet-5
- Anthropic: Claude Opus 4.8 — https://www.anthropic.com/news/claude-opus-4-8
- Google DeepMind Models — https://deepmind.google/models/
- xAI: Grok 4.5 — https://x.ai/news/grok-4-5
- DeepSeek releases — https://api-docs.deepseek.com/news/news260424/
- Qwen official repositories — https://github.com/QwenLM
- Gemma releases — https://ai.google.dev/gemma/docs/releases
- Mistral Small 4 — https://mistral.ai/news/mistral-small-4/
- Cohere Command A+ — https://cohere.com/blog/command-a-plus

## B.6 Pravidlo pro budoucí aktualizaci

Před novým vydáním knihy aktualizuj nejprve kapitolu 5 a tuto přílohu. Zbytek knihy by měl být co nejméně závislý na konkrétních názvech modelů.
