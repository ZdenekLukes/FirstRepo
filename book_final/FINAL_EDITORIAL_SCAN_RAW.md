# Raw final editorial scan

- Numbered chapters: **36**
- Appendices: **7**

## Suspicious editorial residues

- `04 - Co LLM umí - a co neumí.md:210` — `doplnit“. U extrakce je proto velmi užitečná instrukce typu: ```text Pokud hodnotu ve zdroji nenajdeš, vrať null. Nevymýšlej chybějící údaje. ``` --- ## 4.4`
- `04 - Co LLM umí - a co neumí.md:292` — `doplnit unit test, - refaktorovat program, - hledat chybu, - převést kód mezi jazyky, - napsat skript pro analýzu dat, - upravit více souborů v projektu. Samot`
- `05 - Mapa modelů.md:111` — `redakční oprava: **„Opus 5“ není k datu tohoto snapshotu správný veřejný název modelu.** Číslo generace a produktová třída už nejsou vždy jedna jednoduchá osa.`
- `16 - Co je AI agent.md:434` — `V další kapitole v pořadí přejdeme od anatomie k receptu: **jak postavit prvního jednoduchého agenta tak, aby byl užitečný, měřitelný a bezpečný.**`
- `33 - Co jsem se zatím naučil.md:11` — `průběžně doplňovat konkrétními experimenty, chybami a změnami názoru. Když jsem se do AI začal ponořovat hlouběji, první přirozenou otázkou bylo: > **Který mo`
- `33 - Co jsem se zatím naučil.md:11` — `Osobní kapitola — průběžně doplňovat konkrétními experimenty, chybami a změnami názoru. Když jsem se do AI začal ponořovat hlouběji, první přirozenou otázkou b`
- `34 - Co mě ještě čeká.md:83` — `průběžně doplňovat do přílohy G. Poslední část knihy už není teorie. Je to kuchařka: > **Jaký minimální stack potřebuji (kapitola 35) a jaké projekty mám skut`
- `34 - Co mě ještě čeká.md:83` — `budu průběžně doplňovat do přílohy G. Poslední část knihy už není teorie. Je to kuchařka: > **Jaký minimální stack potřebuji (kapitola 35) a jaké projekty mám`

## Numeric cross-reference issues

- `33 - Co jsem se zatím naučil.md` — **section 34.10** — missing section

## Snapshot mentions by file

- `00 - Uvod - Jak cist tuto knihu.md` — 3
- `05 - Mapa modelů.md` — 5
- `08 - Jak provozovat LLM lokálně.md` — 2
- `15 - MCP, skills, plugins a connectors.md` — 2
- `24 - Bezpečnost AI.md` — 3
- `31 - Ekonomika AI.md` — 1
- `32 - Kam se AI posouvá.md` — 1
- `33 - Co jsem se zatím naučil.md` — 1
- `35 - Můj minimální AI stack.md` — 2
- `B - Prehled modelu - snapshot 08-2026.md` — 8
- `C - Prehled nastroju - snapshot 08-2026.md` — 4

## Chapter openings and endings

### 1. Sto let vývoje AI na několika stránkách

**Opening:** *Obrázek: Zlomové body od obecného výpočtu po agentní systémy.*

**Last H2:** 1.6 Co si z celé historie odnést

**Ending:** V další kapitole si nejprve přesně ujasníme, co znamenají pojmy **AI, Machine Learning, Neural Networks, Deep Learning, Generative AI, Foundation Model, LLM, Reasoning Model a Agentic AI**. Bez tohoto slovníku by se další části knihy rychle změnily v hromadu buzzwords.

### 2. AI, Machine Learning, Deep Learning a Generative AI

**Opening:** *Obrázek: Pojmy tvoří vrstvy; agentní systém je nadstavba kolem modelu.*

**Last H2:** Shrnutí kapitoly

**Ending:** V další kapitole se podíváme podrobněji na to, **jak LLM funguje uvnitř** — od tokenů a embeddings přes Transformer a attention až po vznik výsledné odpovědi.

### 3. Jak funguje LLM — bez matematiky

**Opening:** Velký jazykový model působí při používání téměř magicky. Napíšeme otázku a během několika sekund dostaneme odpověď, která může připomínat text napsaný člověkem. Model dokáže vysvětlovat, programovat, překládat, shrnovat dokumenty nebo diskutovat o problému.

**Last H2:** Co si z kapitoly zapamatovat

**Ending:** V další kapitole se podíváme na to, **co LLM skutečně umí, kde jsou jeho hranice a proč plynulá odpověď ještě neznamená správnou odpověď**.

### 4. Co LLM umí — a co neumí

**Opening:** *Obrázek: LLM je silný v práci s jazykem; přesná nebo aktuální data často dodává nástroj.*

**Last H2:** Co si z kapitoly odnést

**Ending:** Tím se dostáváme k další části knihy — k mapě dnešních AI modelů.

### 5. Mapa modelů

**Opening:** *Obrázek: Model vybíráme podle konkrétního use-case, ne podle jediné univerzální tabulky.*

**Last H2:** Zdroje pro snapshot 08/2026

**Ending:** OpenAI Model Release Notes — - Anthropic: Claude Sonnet 5 — - Anthropic: aktuální přehled modelů Claude — - Google DeepMind Models — - xAI: Grok 4.5 — - DeepSeek V4 — - Qwen official repositories — - Google Gemma releases — - Mistral Small 4 — - Cohere Command A+ —

### 6. Jak modely porovnávat

**Opening:** *Obrázek: Vlastní test set propojuje kvalitu modelu s provozními omezeními.*

**Last H2:** Co si z kapitoly odnést

**Ending:** > **Má model běžet v cloudu, lokálně, nebo použijeme hybrid obou světů?**

### 7. Cloud vs. on-prem vs. hybrid

**Opening:** *Obrázek: Rozdělení úloh podle dat, výkonu, ceny a provozní odpovědnosti.*

**Last H2:** Co si z kapitoly odnést

**Ending:** > **Kolik RAM, VRAM a výpočetního výkonu vlastně lokální LLM potřebuje?**

### 8. Jak provozovat LLM lokálně

**Opening:** > **Snapshot k 7. 8. 2026.** Konkrétní nástroje (Ollama, llama.cpp, vLLM, Open WebUI) a hardwarové třídy odpovídají stavu k tomuto datu. Principy — vztah velikosti modelu, kvantizace, paměti a KV cache — stárnou výrazně pomaleji.

**Last H2:** Co si z kapitoly odnést

**Ending:** > **Jak vlastně modelu zadat práci tak, aby dostal správný cíl, kontext a omezení?**

### 9. Prompting

**Opening:** *Obrázek: Prompt jako strukturovaná specifikace úlohy.*

**Last H2:** Co si z kapitoly odnést

**Ending:** > **Jak řídit celý kontext modelu, ne pouze poslední větu, kterou mu napíšeme?**

### 10. Context Engineering

**Opening:** *Obrázek: Co model při řešení úlohy skutečně vidí.*

**Last H2:** Co si z kapitoly odnést

**Ending:** > **Model je chytrý, ale nezná moje dokumenty. Jak jej k nim bezpečně a efektivně připojit?**

### 11. Proč model nezná moje data

**Opening:** *Obrázek: Soukromá a aktuální data musí být do kontextu přivedena externí vrstvou.*

**Last H2:** Co si z kapitoly odnést

**Ending:** A právě nejčastější mechanismus pro práci s velkým množstvím vlastních dokumentů má jméno:

### 12. RAG — Retrieval-Augmented Generation

**Opening:** *Obrázek: Od dokumentů přes retrieval až k odpovědi s citacemi.*

**Last H2:** Co si z kapitoly odnést

**Ending:** Když tuto infrastrukturu rozšíříme z firemních dokumentů na naše osobní poznámky, e-maily, knihy a historii práce, dostáváme se k dalšímu populárnímu pojmu:

### 13. Druhý mozek

**Opening:** *Obrázek: AI jako navigátor nad znalostní bází.*

**Last H2:** Co si z kapitoly odnést

**Ending:** > **Co se stane, když LLM přestane jen odpovídat a začne používat nástroje?**

### 14. Tool Use

**Opening:** *Obrázek: Model zvolí nástroj, obdrží výsledek a pokračuje.*

**Last H2:** Co si z kapitoly odnést

**Ending:** Tím se dostáváme k MCP, skills, plugins a connectors.

### 15. MCP, skills, plugins a connectors

**Opening:** *Obrázek: Standardizované propojení AI aplikace s nástroji a zdroji.*

**Last H2:** Zdroje pro snapshot 08/2026

**Ending:** MCP Introduction — - MCP Architecture — - Understanding MCP Servers — - MCP 2026-07-28 Specification release — - Agent Skills for MCP development —

### 16. Anatomie a smyčka AI agenta

**Opening:** *Obrázek: Agent je software kolem LLM: cíl, stav, nástroje, kontroly a smyčka.*

**Last H2:** Co si z kapitoly odnést

**Ending:** V další kapitole v pořadí přejdeme od anatomie k receptu: **jak postavit prvního jednoduchého agenta tak, aby byl užitečný, měřitelný a bezpečný.**

### 17. Jak postavit jednoduchého agenta

**Opening:** *Obrázek: Autonomii přidávat až po validaci a měření.*

**Last H2:** Co si z kapitoly odnést

**Ending:** > **Pomohlo by rozdělit práci mezi více specializovaných agentů?**

### 18. Multi-agentní systémy

**Opening:** *Obrázek: Orchestrátor koordinuje specialisty s jasnými rolemi.*

**Last H2:** Co si z kapitoly odnést

**Ending:** > **Kdo řídí všechny tyto kroky, stavy, retry, timeouty a dlouhotrvající úlohy?**

### 19. Orchestrace agentních systémů

**Opening:** *Obrázek: State, retry, checkpointy a agentní kroky v jednom workflow.*

**Last H2:** Co si z kapitoly odnést

**Ending:** V další části se podíváme na první oblast, kde už dnes můžeme velmi dobře pozorovat, jak tento přístup mění skutečnou práci:

### 20. Coding Agents

**Opening:** *Obrázek: Čtení kódu, editace, testy, review diffu a commit.*

**Last H2:** Co si z kapitoly odnést

**Ending:** > **dokumenty, e-maily, tabulky, prezentace, chaty a logy.**

### 21. AI nad dokumenty a firemními daty

**Opening:** *Obrázek: Heterogenní soubory se musí normalizovat, indexovat a citovat.*

**Last H2:** 21.14 OCR, citlivá data a audit ingestion pipeline

**Ending:** > **výpočty, simulátory, měřením a optimalizační smyčkou.**

### 22. AI pro technické a inženýrské úlohy

**Opening:** *Obrázek: LLM orchestruje; specializovaný nástroj rozhoduje fyziku.*

**Last H2:** Co si z kapitoly odnést

**Ending:** V další kapitole tento obecný princip převedeme na konkrétní případovou studii:

### 23. Případová studie — AI-assisted analog IC design

**Opening:** *Obrázek: Specifikace → gm/ID → simulace → extrakce → optimalizace.*

**Last H2:** Co si z kapitoly odnést

**Ending:** Čím více agent umí, tím větší škodu může způsobit chyba nebo špatná instrukce.

### 24. Bezpečnost AI

**Opening:** *Obrázek: Data, LLM a nástroje musí oddělovat oprávnění a kontroly.*

**Last H2:** Zdroje pro snapshot 08/2026

**Ending:** OWASP Gen AI Security Project — - State of Agentic AI Security and Governance 2.01 — - OWASP GenAI Data Security Risks & Mitigations 2026 — - Agentic AI — Threats and Mitigations —

### 25. Proč nestačí „máme ChatGPT“

**Opening:** *Obrázek: Chatbot je jen jedna vrstva celého pracovního systému.*

**Last H2:** Co si z kapitoly odnést

**Ending:** > **Jak poznat, zda je firma a její data na AI vůbec připravená?**

### 26. AI readiness

**Opening:** *Obrázek: Proces, data, security, measurement a lidé musí být připraveni společně.*

**Last H2:** Co si z kapitoly odnést

**Ending:** > **Z desítek možných nápadů vybrat ty use-cases, které mají nejlepší poměr hodnoty, proveditelnosti a rizika.**

### 27. Jak vybírat AI use-cases

**Opening:** *Obrázek: Hodnota versus složitost rozlišuje quick wins a strategic bets.*

**Last H2:** Co si z kapitoly odnést

**Ending:** > **Jak z něj udělat pilot, který skutečně něco prokáže — a ne jen hezké demo?**

### 28. Pilot → důkaz → škálování

**Opening:** *Obrázek: Každá fáze má vlastní měřitelnou bránu.*

**Last H2:** Co si z kapitoly odnést

**Ending:** > **lidi, důvěru a změnu pracovních návyků.**

### 29. Lidé a adopce

**Opening:** *Obrázek: Experiment, měření, sdílení, trénink a standardizace.*

**Last H2:** Co si z kapitoly odnést

**Ending:** Abychom ale věděli, zda nový workflow skutečně funguje, potřebujeme systematickou evaluaci.

### 30. Evaluace

**Opening:** *Obrázek: Od regresních testů až po business metriku.*

**Last H2:** 30.12 End-to-end business metric

**Ending:** > **Kolik nás AI skutečně stojí a kdy se vyplatí?**

### 31. Ekonomika AI

**Opening:** *Obrázek: Tokeny a GPU jsou jen část celkových nákladů.*

**Last H2:** 31.11 Kdy se vyplatí on-prem

**Ending:** Tím jsme uzavřeli praktickou část o tom, jak AI vybrat, měřit a ekonomicky hodnotit.

### 32. Kam se AI posouvá

**Opening:** *Obrázek: Trend nesměřuje jen k větším modelům, ale k ověřeným systémům s adaptivním compute, modalitami a nástroji.*

**Last H2:** Co si z kapitoly odnést

**Ending:** Teď je čas vrátit se od technologie k osobnímu pohledu:

### 33. Co jsem se zatím naučil

**Opening:** > Osobní kapitola — průběžně doplňovat konkrétními experimenty, chybami a změnami názoru.

**Last H2:** Pracovní závěr

**Ending:** A právě proto má smysl tuto kapitolu průběžně aktualizovat.

### 34. Co mě ještě čeká

**Opening:** *Obrázek: Lokální stack → RAG → tools → agent → production.*

**Last H2:** 34.2 Jak poznám, že jsem se skutečně něco naučil

**Ending:** > **Jaký minimální stack potřebuji (kapitola 35) a jaké projekty mám skutečně postavit (kapitola 36)?**

### 35. Můj minimální AI stack

**Opening:** *Obrázek: Modely, data, nástroje, Git, automatizace a monitoring.*

**Last H2:** Zdroje a projekty pro snapshot 08/2026

**Ending:** Ollama — - llama.cpp — - vLLM — - Open WebUI — - Obsidian — - OpenAI Agents SDK — - Pydantic AI — - LangGraph — - Langfuse —

### 36. Deset praktických projektů od začátečníka k agentnímu systému

**Opening:** *Obrázek: Postupné přidávání schopností i rizik.*

**Last H2:** Co si z kapitoly odnést

**Ending:** Končíme systémem, který dokážeme postavit, změřit, omezit, ověřit a postupně zlepšovat.


## Exact long paragraphs repeated across files

- none

## Recurrent language habits

- model: **995**
- AI: **516**
- Například: **373**
- systém: **336**
- Není: **266**
- důležité: **193**
- To je: **145**
- Prakticky: **27**
- Ne.: **2**

## Chapters without expected takeaway heading

- `01 - Sto let vývoje AI na několika stránkách.md`
- `02 - AI, Machine Learning, Deep Learning a Generative AI.md`
- `33 - Co jsem se zatím naučil.md`
- `34 - Co mě ještě čeká.md`

## Image counts by chapter

- `01 - Sto let vývoje AI na několika stránkách.md` — 1
- `02 - AI, Machine Learning, Deep Learning a Generative AI.md` — 1
- `03 - Jak funguje LLM - bez matematiky.md` — 4
- `04 - Co LLM umí - a co neumí.md` — 1
- `05 - Mapa modelů.md` — 1
- `06 - Jak modely porovnávat.md` — 1
- `07 - Cloud vs. on-prem vs. hybrid.md` — 1
- `08 - Jak provozovat LLM lokálně.md` — 1
- `09 - Prompting.md` — 1
- `10 - Context Engineering.md` — 1
- `11 - Proč model nezná moje data.md` — 1
- `12 - RAG - Retrieval-Augmented Generation.md` — 2
- `13 - Druhý mozek.md` — 1
- `14 - Tool Use.md` — 1
- `15 - MCP, skills, plugins a connectors.md` — 1
- `16 - Co je AI agent.md` — 2
- `17 - Jak postavit jednoduchého agenta.md` — 1
- `18 - Multi-agentní systémy.md` — 1
- `19 - Orchestrace agentních systémů.md` — 1
- `20 - Coding Agents.md` — 1
- `21 - AI nad dokumenty a firemními daty.md` — 1
- `22 - AI pro technické a inženýrské úlohy.md` — 1
- `23 - Případová studie - AI-assisted analog IC design.md` — 1
- `24 - Bezpečnost AI.md` — 1
- `25 - Proč nestačí „máme ChatGPT“.md` — 1
- `26 - AI readiness.md` — 1
- `27 - Jak vybírat AI use-cases.md` — 1
- `28 - Pilot → důkaz → škálování.md` — 1
- `29 - Lidé a adopce.md` — 1
- `30 - Evaluace.md` — 1
- `31 - Ekonomika AI.md` — 1
- `32 - Kam se AI posouvá.md` — 1
- `33 - Co jsem se zatím naučil.md` — 0
- `34 - Co mě ještě čeká.md` — 1
- `35 - Můj minimální AI stack.md` — 1
- `36 - Deset praktických projektů od začátečníka k agentnímu systému.md` — 1

## H2 map

### 01 - Sto let vývoje AI na několika stránkách.md
- 1.1 Kořeny moderní AI
- 1.2 První velké nadšení: když jsme se snažili inteligenci naprogramovat
- 1.3 AI winters — když očekávání předběhla technologii
- 1.4 Machine Learning přebírá vedení
- 1.5 Od Deep Learningu ke generativní AI
- 1.6 Co si z celé historie odnést

### 02 - AI, Machine Learning, Deep Learning a Generative AI.md
- 2.1 Co znamená „AI“
- 2.2 Machine Learning
- 2.3 Neural Networks
- 2.4 Deep Learning
- 2.5 Generative AI
- 2.6 Foundation Models
- 2.7 LLM
- 2.8 Multimodal Models
- 2.9 Reasoning Models
- 2.10 Agentic AI
- 2.11 Co je model a co už je celý AI systém
- Shrnutí kapitoly

### 03 - Jak funguje LLM - bez matematiky.md
- 3.1 LLM není databáze odpovědí
- 3.2 Text se rozděluje na tokeny
- 3.3 Co je token
- 3.4 Co znamenají embeddings
- 3.5 Transformer
- 3.6 Attention — proč je tak důležitá
- 3.7 Jak model předpovídá další token
- 3.8 Proč z jednoduchého principu vzniká složité chování
- 3.9 Training vs. inference
- 3.10 Pre-training
- 3.11 Post-training
- 3.12 Instruction tuning
- 3.13 Reinforcement learning
- 3.14 Context window
- 3.15 System prompt, user prompt a další části kontextu
- 3.16 Temperature a sampling
- 3.17 Proč stejný prompt nemusí dát stejnou odpověď
- 3.18 Co se děje od stisku Enter po odpověď
- Jeden obrázek, který vysvětluje téměř celou kapitolu
- Ještě důležitější obrázek: model není systém
- Praktický příklad: návrh integrovaného obvodu
- Praktická poznámka: čeština a tokeny
- Co si z kapitoly zapamatovat

### 04 - Co LLM umí - a co neumí.md
- 4.1 Generování textu
- 4.2 Shrnutí a transformace informací
- 4.3 Extrakce informací
- 4.4 Klasifikace
- 4.5 Programování
- 4.6 Analýza dat
- 4.7 Práce s obrazem, zvukem a videem
- 4.8 Reasoning
- 4.9 Plánování
- 4.10 Používání nástrojů
- 4.11 Halucinace (hallucinations)
- 4.12 Proč sebevědomá odpověď nemusí být pravdivá
- 4.13 Knowledge cutoff vs. aktuální informace
- 4.14 Proč dlouhý kontext neznamená dokonalou paměť
- 4.15 Kdy AI věřit a kdy výsledek ověřovat
- 4.16 Deterministické nástroje vs. pravděpodobnostní model
- Co si z kapitoly odnést

### 05 - Mapa modelů.md
- 5.1 Frontier cloud modely
- 5.2 Open-weight a lokálně provozovatelné modely
- 5.3 General-purpose modely
- 5.4 Reasoning modely
- 5.5 Coding modely
- 5.6 Vision a multimodální modely
- 5.7 Speech-to-Text
- 5.8 Text-to-Speech
- 5.9 Image generation
- 5.10 Video generation
- 5.11 Embedding modely
- 5.12 Rerankery
- 5.13 Malé specializované modely
- Co si z kapitoly odnést
- Zdroje pro snapshot 08/2026

### 06 - Jak modely porovnávat.md
- 6.1 Inteligence není jedno číslo
- 6.2 Benchmark vs. reálný use-case
- 6.3 Kvalita odpovědi
- 6.4 Reasoning
- 6.5 Coding
- 6.6 Tool use
- 6.7 Context length
- 6.8 Rychlost
- 6.9 Cena
- 6.10 Privátnost
- 6.11 Licence
- 6.12 Velikost modelu
- 6.13 Aktivní vs. celkový počet parametrů u MoE
- 6.14 Kvantizace
- 6.15 Jak si vytvořit vlastní benchmark
- Praktická scorecard
- Co si z kapitoly odnést

### 07 - Cloud vs. on-prem vs. hybrid.md
- 7.1 Čistý cloud
- 7.2 Čistý on-prem
- 7.3 Hybridní architektura
- 7.4 Výhody cloudu
- 7.5 Nevýhody cloudu
- 7.6 Výhody lokální AI
- 7.7 Nevýhody lokální AI
- 7.8 Kdy data nesmějí opustit firmu
- 7.9 Jak rozhodnout, která úloha poběží kde
- 7.10 Model routing
- 7.11 Budoucnost: více modelů místo jednoho univerzálního modelu
- Praktický příklad — technická firma
- Co si z kapitoly odnést

### 08 - Jak provozovat LLM lokálně.md
- 8.1 CPU, GPU a NPU
- 8.2 RAM vs. VRAM
- 8.3 Unified Memory u Apple Silicon
- 8.4 Co znamená 8B, 14B, 32B, 70B…
- 8.5 FP16, FP8, INT8, INT4
- 8.6 Quantization prakticky
- 8.7 Kolik paměti model potřebuje
- 8.8 Co reálně zvládne 8 GB VRAM
- 8.9 Co reálně zvládne 16 GB VRAM
- 8.10 Co přinese 32 GB VRAM
- 8.11 Apple Silicon vs. NVIDIA
- 8.12 Linux workstation
- 8.13 Ollama
- 8.14 llama.cpp
- 8.15 vLLM
- 8.16 Open WebUI
- 8.17 Model server vs. uživatelské rozhraní
- 8.18 Lokální benchmark
- 8.19 Tokens per second a proč nejsou všechno
- Praktická doporučená cesta
- Praktický VRAM vzorec
- Co si z kapitoly odnést

### 09 - Prompting.md
- 9.1 Prompt není kouzelná formulka
- 9.2 Kontext je důležitější než „prompt engineering“
- 9.3 Role
- 9.4 Cíl
- 9.5 Kontext
- 9.6 Omezení
- 9.7 Příklady
- 9.8 Požadovaný výstup
- 9.9 Zero-shot
- 9.10 Few-shot
- 9.11 Structured output
- 9.12 Iterativní práce
- 9.13 Prompt jako specifikace
- 9.14 Kdy prompt přestává stačit
- 9.15 AI a čeština
- Praktický příklad
- Co si z kapitoly odnést

### 10 - Context Engineering.md
- 10.1 Proč je context engineering důležitější než samotný prompt
- 10.2 Co všechno patří do kontextu
- 10.3 Relevantní vs. nerelevantní informace
- 10.4 Context pollution
- 10.5 Komprese kontextu
- 10.6 Summarization
- 10.7 Working memory
- 10.8 Long-term memory
- 10.9 Context management u agentů
- 10.10 Jak připravovat firemní data pro AI
- Praktický příklad — otázka nad projektem
- Context engineering jako pipeline
- Co si z kapitoly odnést

### 11 - Proč model nezná moje data.md
- 11.0 Tři druhy informací
- 11.1 Pět způsobů, jak modelu dodat externí znalosti
- 11.2 A co model prostě dotrénovat?
- Co si z kapitoly odnést

### 12 - RAG - Retrieval-Augmented Generation.md
- 12.1 Co je RAG
- 12.2 Nejjednodušší RAG bez buzzwords
- 12.3 Dokument → text
- 12.4 Chunking
- 12.5 Embeddings
- 12.6 Vector database
- 12.7 Semantic search
- 12.8 Keyword search
- 12.9 Hybrid search
- 12.10 Reranking
- 12.11 Retrieval
- 12.12 Generation
- 12.13 Citace zdrojů
- 12.14 Metadata
- 12.15 Oprávnění k dokumentům
- 12.16 Aktualizace indexu
- 12.17 Kdy RAG funguje špatně
- 12.18 Jak měřit kvalitu RAG
- 12.19 Graph RAG
- 12.20 Kdy místo RAG stačí search
- Celý RAG pipeline na jednom obrázku
- Co si z kapitoly odnést

### 13 - Druhý mozek.md
- 13.1 Co znamená „second brain“
- 13.2 Druhý mozek bez AI
- 13.3 Co do něj přidává AI
- 13.4 Notes
- 13.5 Dokumenty
- 13.6 E-maily
- 13.7 Meeting transcripts
- 13.8 Webové zdroje
- 13.9 Knihy
- 13.10 Osobní knowledge base
- 13.11 Firemní knowledge base
- 13.12 Search vs. memory
- 13.13 RAG vs. agentní práce nad dokumenty
- 13.14 Obsidian jako lidská vrstva znalostí
- 13.15 AI jako navigátor nad znalostmi
- 13.16 Jak zabránit tomu, aby se z druhého mozku stal digitální sklad
- Praktická minimální architektura druhého mozku
- Co si z kapitoly odnést

### 14 - Tool Use.md
- 14.1 Proč samotný LLM nestačí
- 14.2 Function Calling
- 14.3 Web search
- 14.4 Calculator
- 14.5 Python
- 14.6 Databáze
- 14.7 Filesystem
- 14.8 E-mail
- 14.9 Calendar
- 14.10 Git
- 14.11 API
- 14.12 Shell
- 14.13 Specializované firemní aplikace
- 14.14 Kdy smí AI pouze číst
- 14.15 Kdy smí AI zapisovat
- Tool permission ladder
- Co si z kapitoly odnést

### 15 - MCP, skills, plugins a connectors.md
- 15.1 Problém integrace AI s nástroji
- 15.2 Co je MCP
- 15.3 MCP server
- 15.4 MCP client
- 15.5 Tools
- 15.6 Resources
- 15.7 Skills
- 15.8 Plugins
- 15.9 Connectors
- 15.10 API vs. MCP
- 15.11 Bezpečnost nástrojových integrací
- 15.12 Proč standardizované rozhraní mění možnosti agentů
- Praktický příklad — AI-assisted analog design
- Co si z kapitoly odnést
- Zdroje pro snapshot 08/2026

### 16 - Co je AI agent.md
- 16.1 Anatomie agenta
- 16.2 Jedna smyčka: Observe → Reason → Plan → Act → Verify
- 16.3 Agent vs. pevný workflow
- 16.4 Human-in-the-loop a approval gates
- 16.5 Failure Modes: jak se agent rozbije
- 16.6 Logging a audit trail
- 16.7 Praktický engineering příklad
- Co si z kapitoly odnést

### 17 - Jak postavit jednoduchého agenta.md
- 17.1 Vyber jeden přesně definovaný use-case
- 17.2 Definuj vstupy
- 17.3 Definuj výstupy
- 17.4 Vyber model
- 17.5 Přidej nástroje
- 17.6 Přidej znalosti
- 17.7 Přidej paměť pouze pokud je potřebná
- 17.8 Přidej kontrolu výsledků
- 17.9 Přidej human approval
- 17.10 Loguj každý krok
- 17.11 Měř úspěšnost
- 17.12 Teprve potom přidávej autonomii
- Jak vypadá skutečný běh
- Minimální agent v pseudokódu
- Checklist prvního agenta
- Co si z kapitoly odnést

### 18 - Multi-agentní systémy.md
- 18.1 Proč vůbec více agentů
- 18.2 Jeden silný agent vs. více agentů
- 18.3 Orchestrator
- 18.4 Specialist agents
- 18.5 Planner
- 18.6 Researcher
- 18.7 Coder
- 18.8 Reviewer
- 18.9 Critic
- 18.10 Executor
- 18.11 Shared memory
- 18.12 Předávání úkolů mezi agenty
- 18.13 Paralelní práce
- 18.14 Hlasování a konsenzus
- 18.15 Verifikace
- 18.16 Kdy multi-agent přidává hodnotu
- 18.17 Kdy je multi-agent pouze dražší chaos
- Praktický příklad — návrh analogového bloku
- Co si z kapitoly odnést

### 19 - Orchestrace agentních systémů.md
- 19.1 Workflow vs. agent
- 19.2 Deterministický workflow
- 19.3 LLM-driven workflow
- 19.4 State machine
- 19.5 Event-driven agent
- 19.6 Scheduler
- 19.7 Queues
- 19.8 Retry
- 19.9 Timeout
- 19.10 Checkpoint
- 19.11 Observability
- 19.12 Náklady
- 19.13 Latence
- 19.14 Spolehlivost
- Doporučený produkční pattern
- Co si z kapitoly odnést

### 20 - Coding Agents.md
- 20.1 Od autocomplete ke coding agentovi
- 20.2 Čtení celého projektu
- 20.3 Vyhledávání v codebase
- 20.4 Editace více souborů
- 20.5 Spouštění testů
- 20.6 Debugging
- 20.7 Git
- 20.8 Pull request
- 20.9 Code review
- 20.10 Dokumentace
- 20.11 Agentní vývoj aplikace
- 20.12 Proč coding agents ukazují budoucnost knowledge work
- Praktický model bezpečné práce s coding agentem
- Co si z kapitoly odnést

### 21 - AI nad dokumenty a firemními daty.md
- Od webového chatu k firemnímu systému
- 21.1 PDF
- 21.2 Word
- 21.3 Excel
- 21.4 PowerPoint
- 21.5 E-mail
- 21.6 Chat
- 21.7 Meeting transcripts
- 21.8 Log files
- 21.9 Technická dokumentace
- 21.10 Velké heterogenní datové sady
- 21.11 Jak najít informaci rozptýlenou ve stovkách dokumentů
- 21.12 Jak z odpovědi udělat auditovatelný výsledek
- Conclusion
- Evidence
- Uncertainties
- Recommended next action
- 21.13 Permissioning: AI nesmí vytvořit nový boční vchod k datům
- 21.14 OCR, citlivá data a audit ingestion pipeline

### 22 - AI pro technické a inženýrské úlohy.md
- 22.1 AI jako technický asistent
- 22.2 Dokumentace
- 22.3 Datasheety
- 22.4 Specifikace
- 22.5 Skripty
- 22.6 Simulace
- 22.7 Analýza výsledků
- 22.8 Optimalizační smyčka
- 22.9 LLM + klasický simulátor
- 22.10 Proč AI nemá nahrazovat fyzikální simulaci
- 22.11 Agent jako orchestrátor deterministických nástrojů
- Stupně engineering autonomie
- Co si z kapitoly odnést

### 23 - Případová studie - AI-assisted analog IC design.md
- 23.1 Zadání analogového bloku
- 23.2 Specifikace
- 23.3 Knowledge base
- 23.4 Datasheety, design notes a předchozí projekty
- 23.5 gm/ID jako strukturovaná návrhová metoda
- 23.6 Characterization data
- 23.7 Generování kandidátního návrhu
- 23.8 SPICE / Spectre simulation
- 23.9 Automatická extrakce výsledků
- 23.10 Porovnání se specifikací
- 23.11 Iterace parametrů
- 23.12 Agentní optimalizační smyčka
- 23.13 Human designer jako decision maker
- 23.14 Co lze automatizovat dnes
- 23.15 Co zatím automatizovat nechceme
- 23.16 Co může přijít v dalších letech
- Praktická cesta od demo k internímu pilotu
- Co si z kapitoly odnést

### 24 - Bezpečnost AI.md
- 24.1 Jaká data posíláme modelu
- 24.2 Cloud privacy
- 24.3 Data retention
- 24.4 Training on customer data
- 24.5 Enterprise smluvní ochrany
- 24.6 On-prem isolation
- 24.7 Přístupová práva
- 24.8 Secrets
- 24.9 Prompt injection
- 24.10 Indirect prompt injection
- 24.11 Malicious documents
- 24.12 Tool oprávnění
- 24.13 Least privilege
- 24.14 Sandboxing
- 24.15 Human approval
- 24.16 Audit log
- 24.17 Supply-chain riziko open-source modelů
- 24.18 Model provenance
- 24.19 Bezpečnost vs. použitelnost
- 24.20 EU AI Act, GDPR a firemní governance
- Jednoduchý threat model agentního systému
- Defense in depth
- System prompt není security boundary
- Co si z kapitoly odnést
- Zdroje pro snapshot 08/2026

### 25 - Proč nestačí „máme ChatGPT“.md
- 25.1 Chatbot není AI strategie
- 25.2 AI jako nový interface k práci
- 25.3 Procesy
- 25.4 Data
- 25.5 Nástroje
- 25.6 Integrace
- 25.7 Governance
- 25.8 Kompetence lidí
- 25.9 Měření výsledků
- 25.10 AI capability jako dlouhodobá firemní schopnost
- Tři úrovně adopce
- Co si z kapitoly odnést

### 26 - AI readiness.md
- 26.1 Které procesy máme
- 26.2 Kde vznikají data
- 26.3 Kde jsou znalosti
- 26.4 Kdo vlastní data
- 26.5 Co je citlivé
- 26.6 Co je dobře strukturované
- 26.7 Co je jen v hlavách lidí
- 26.8 Kde se ztrácí nejvíce času
- 26.9 Kde AI přinese měřitelnou hodnotu
- 26.10 AI readiness matrix
- Readiness není předprojekt na dva roky
- Co si z kapitoly odnést

### 27 - Jak vybírat AI use-cases.md
- 27.1 Frekvence
- 27.2 Časová náročnost
- 27.3 Hodnota
- 27.4 Opakovatelnost
- 27.5 Dostupnost dat
- 27.6 Riziko
- 27.7 Nutnost lidského rozhodnutí
- 27.8 Technická složitost
- 27.9 Quick wins
- 27.10 Strategic bets
- Jednoduchá prioritizační matice
- Portfolio: 70 / 20 / 10
- Co si z kapitoly odnést

### 28 - Pilot → důkaz → škálování.md
- 28.1 Začít malým problémem
- 28.2 Baseline bez AI
- 28.3 Pilot s AI
- 28.4 Metriky
- 28.5 Kvalita
- 28.6 Čas
- 28.7 Náklady
- 28.8 Chybovost
- 28.9 Přijetí uživateli
- 28.10 Rozhodnutí go / no-go
- 28.11 Industrializace
- 28.12 Škálování
- Pilot jako experiment
- Co si z kapitoly odnést

### 29 - Lidé a adopce.md
- 29.1 Proč technicky dobrý projekt může selhat
- 29.2 Strach z nahrazení
- 29.3 Skeptici
- 29.4 Early adopters
- 29.5 AI champions
- 29.6 Training
- 29.7 Learning by doing
- 29.8 Sdílení use-cases
- 29.9 Interní komunita
- 29.10 Nové role
- 29.11 AI leader / AI officer / competence center
- 29.12 AI jako augmentace člověka
- Adoption loop
- Co si z kapitoly odnést

### 30 - Evaluace.md
- 30.1 „Vypadá to dobře“ nestačí
- 30.2 Ground truth
- 30.3 Test set
- 30.4 Golden questions
- 30.5 Automatické evaluace
- 30.6 LLM-as-a-judge
- 30.7 Human evaluation
- 30.8 Regression tests
- 30.9 Agent evaluation
- 30.10 RAG evaluation
- 30.11 Tool-use evaluation
- 30.12 End-to-end business metric

### 31 - Ekonomika AI.md
- 31.1 Cena tokenů
- 31.2 Cena GPU
- 31.3 Cloud API
- 31.4 Lokální inference
- 31.5 Náklady na integraci
- 31.6 Náklady na údržbu
- 31.7 Cena chyby
- 31.8 ROI
- 31.9 TCO
- 31.9.1 Konkrétní TCO příklad: API vs. dedicated GPU
- 31.10 Kdy je dražší model ve skutečnosti levnější
- 31.11 Kdy se vyplatí on-prem

### 32 - Kam se AI posouvá.md
- 32.1 Silnější reasoning
- 32.2 Levnější inference
- 32.3 Menší a schopnější lokální modely
- 32.4 Delší context
- 32.5 Trvalejší memory
- 32.6 Multimodalita
- 32.7 Computer use
- 32.8 Agentní software
- 32.9 Background agents
- 32.10 AI + robotics
- 32.11 AI + simulace
- 32.12 AI + věda a engineering
- 32.13 Personal AI
- 32.14 Enterprise AI
- 32.15 Co může změnit další zásadní průlom
- Co považuji za nejpravděpodobnější směr
- Co si z kapitoly odnést

### 33 - Co jsem se zatím naučil.md
- 33.1 Co jsem si o AI myslel na začátku
- 33.2 Co se ukázalo jako mylné
- 33.3 Co mě překvapilo
- 33.4 Co se ukázalo jako opravdu užitečné
- 33.5 Co je podle mě jen hype
- 33.6 Cloud vs. local — jak se změnil můj pohled
- 33.7 Od chatbotu k agentům
- 33.8 Proč je nejcennější context a přístup k nástrojům
- 33.9 Proč nestačí nejlepší model
- 33.10 Proč je důležitější celý systém
- 33.11 Co bych dnes udělal jinak
- Pracovní závěr

### 34 - Co mě ještě čeká.md
- 34.1 Moje pořadí
- 34.2 Jak poznám, že jsem se skutečně něco naučil

### 35 - Můj minimální AI stack.md
- 35.1 Chat / frontier model
- 35.2 Lokální LLM
- 35.3 Web search
- 35.4 Coding agent
- 35.5 Speech-to-text
- 35.6 Knowledge base
- 35.7 Git
- 35.8 Automation
- 35.9 Agent framework
- 35.10 Monitoring
- Můj skutečně minimální setup pro začátek
- Stack pro malý on-prem pilot
- Co do stacku záměrně nedávám hned
- Co si z kapitoly odnést
- Zdroje a projekty pro snapshot 08/2026

### 36 - Deset praktických projektů od začátečníka k agentnímu systému.md
- Projekt 1 — Chat nad jedním dokumentem
- Projekt 2 — Analýza několika dokumentů
- Projekt 3 — Osobní knowledge base
- Projekt 4 — Lokální LLM
- Projekt 5 — RAG nad vlastními daty
- Projekt 6 — AI s jedním nástrojem
- Projekt 7 — Agent nad filesystemem
- Projekt 8 — Coding agent
- Projekt 9 — Agentní workflow nad firemními daty
- Projekt 10 — Multi-agentní systém s human approval
- Jak projekty dokumentovat
- Doporučená obtížnost
- Kdy přejít na další projekt
- Co si z kapitoly odnést

