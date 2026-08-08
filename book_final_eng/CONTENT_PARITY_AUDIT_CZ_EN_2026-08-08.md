# Content Parity Audit — Czech ↔ English — 2026-08-08

## Scope

This audit compares the **36 numbered chapters** of the Czech release-candidate (`book_final/`, v0.7) with the English international release-candidate (`book_final_eng/`, v0.8-eng).

The goal is **content parity, not sentence-by-sentence translation parity**. The English edition is intentionally a native-English adaptation. The audit therefore asks:

- Is the same core mental model present?
- Are the same technical mechanisms explained?
- Are important examples and engineering constraints preserved?
- Are failure modes and verification principles preserved?
- Are practical checklists / procedures preserved where they materially help the reader?
- Is a difference an accidental omission, a harmless editorial compression, or an intentional international adaptation?

## Quantitative signal

Across the 36 numbered chapters only:

| Metric | Czech | English | EN / CZ |
|---|---:|---:|---:|
| Approx. words | 47,483 | 45,492 | 95.8% |
| Headings | 1,025 | 720 | 70.2% |
| Bullet items | 2,157 | 1,145 | 53.1% |
| Code / text-diagram blocks | 960 | 718 | 74.8% |
| Paragraph / block units | 6,561 | 4,306 | 65.6% |
| Chapter image references | 42 | 42 | 100% |
| Table lines | 155 | 153 | 98.7% |

The key result is that the English chapters contain **95.8% as many words**, but use far fewer headings, bullets, and small blocks. The much shorter English PDF is therefore primarily a **layout and rhetorical-structure effect**, not evidence that roughly one quarter of the content disappeared.

## Status legend

- **✅ PARITY** — no meaningful Czech content is missing; no parity edit recommended.
- **🟡 COMPRESSED** — English merges headings/lists/examples into denser prose, but the substantive content is still present.
- **🔵 INTENTIONAL ADAPTATION** — divergence is appropriate for the international edition; do not restore the Czech wording mechanically.
- **🟠 MATERIAL GAP** — a useful Czech idea/example/procedure is not clearly represented in English and should be considered for porting.

## Chapter-by-chapter audit

| Ch. | CZ words | EN words | Status | Audit finding |
|---:|---:|---:|---|---|
| 1 | 3,146 | 2,808 | 🟡 COMPRESSED | The historical arc and lessons are preserved. The Czech first/second AI-winter chronology is merged into one tighter English section. Optional detail, not a conceptual gap. |
| 2 | 1,883 | 1,712 | ✅ PARITY | The AI → ML → neural networks → deep learning → generative AI → foundation models → LLM → multimodal → reasoning → agentic hierarchy is fully preserved. |
| 3 | 2,568 | 2,458 | 🟡 COMPRESSED | All major LLM mechanics are present: tokens, embeddings, transformer, attention, next-token generation, training/inference, post-training, context, sampling, Enter-to-answer loop, model vs. system, engineering example. Many Czech micro-headings are simply merged into prose. |
| 4 | 2,011 | 1,705 | 🟡 COMPRESSED | All 16 main capability/limitation sections are represented. Low/medium/high consequence and deterministic-vs-probabilistic examples are less fragmented but still present. |
| 5 | 2,177 | 1,869 | 🟡 COMPRESSED | Same model landscape. English combines STT/TTS into Speech Models and image/video into one section and reorganizes reasoning categories. No important modality or model class is lost. |
| 6 | 1,517 | 1,460 | 🟡 COMPRESSED | The evaluation dimensions and custom-benchmark method are preserved. TTFT/TPS and some benchmark steps are embedded in prose instead of separate subheadings. |
| 7 | 1,262 | 1,090 | 🟡 COMPRESSED | Cloud/on-prem/hybrid advantages, disadvantages, data sensitivity, capability, volume, latency, availability, tool access, failure cost, routing, and engineering example are all present. English is substantially denser. |
| 8 | 1,876 | 1,746 | ✅ PARITY | CPU/GPU/NPU, RAM/VRAM, Apple unified memory, model sizes, precision, quantization, KV cache, 8/16/32 GB classes, Apple vs. NVIDIA, Ollama, llama.cpp, vLLM, Open WebUI, model-server/UI distinction, and workload benchmarking are preserved. |
| 9 | 1,236 | 1,192 | 🔵 INTENTIONAL ADAPTATION | Czech-specific advice about Czech vs. English prompting is generalized into a stronger multilingual-engineering section covering tokenization, embeddings, speech and multilingual evaluation. Keep the English treatment. |
| 10 | 1,053 | 865 | 🟡 COMPRESSED | Despite 37 vs. 12 headings, the actual context-engineering content is present: instructions, history, retrieval, tool results, state, memory, schemas/examples, pollution, compression, working/long-term memory, and AI-ready metadata/ownership/permissions. |
| 11 | 599 | 556 | ✅ PARITY | Three kinds of information, five external-knowledge methods, and the fine-tuning distinction are preserved. |
| 12 | 1,467 | 1,435 | 🟡 COMPRESSED | RAG stages, ingestion, parsing/OCR, chunking, embeddings, vector/lexical signals, hybrid search, reranking, provenance, metadata, permissions, index freshness, failure modes, separate retrieval/answer evals, Graph RAG, and when not to use RAG are preserved. |
| 13 | 1,181 | 1,539 | 🟠 MATERIAL GAP | English is actually longer and stronger on notes/documents/email/transcripts/web/books. However, it does not explicitly preserve the Czech **Raw archive → Knowledge layer → Working layer** model or the compact minimum second-brain architecture. These are useful mental models and should be added. |
| 14 | 1,063 | 1,336 | ✅ PARITY | English is more developed. Email/calendar are consolidated, but permission ladder, read-before-write, validation, logging, rollback and approval remain. English additionally makes the valuable point that tool output is data, not authority. |
| 15 | 1,277 | 1,151 | 🟠 MATERIAL GAP | Core MCP/client/server/tools/resources/skills/plugins/connectors/API/security concepts are present. **Do not mechanically restore** the volatile Czech `2026-07-28` MCP changelog without a fresh spec check. But the Czech constrained **analog-design MCP example** (`run_spectre_simulation`, measurement tools, no arbitrary shell, skill above tools) is absent and is worth adding. |
| 16 | 798 | 907 | ✅ PARITY | English is at least as complete: agent anatomy, Observe→Reason/Plan→Act→Verify, approval dialog, loops, retry policy, budget, oscillation, stop conditions, logging and engineering example. |
| 17 | 1,063 | 1,128 | ✅ PARITY | The build sequence is fully preserved and English adds a realistic end-to-end run including failure recovery. Czech checklist ideas are embedded in the workflow and takeaways. |
| 18 | 1,166 | 1,108 | 🟠 MATERIAL GAP | Multi-agent rationale, roles, shared state, handoffs, parallelism, voting vs. verification, and single-agent baseline are preserved. The Czech **analog-block multi-agent example** and its rule “multi-agent is an evolution of a working single-agent loop” are absent. The example is distinctive and should be added. |
| 19 | 970 | 1,049 | ✅ PARITY | Workflow vs. agent, deterministic vs. agentic control, state machines, events, schedules, queues, retry, timeout, checkpoint, observability, cost, latency and reliability are preserved or strengthened. |
| 20 | 1,003 | 1,155 | ✅ PARITY | Coding-agent mechanics and safety pattern are fully preserved; English is more explicit about repository search and closed-loop testing. |
| 21 | 1,341 | 1,369 | ✅ PARITY | PDF/Word/spreadsheets/presentations/email/chat/transcripts/logs/technical docs, heterogeneous corpora, evidence tables, authorization, OCR audit, provenance and pipeline evaluation are all present. |
| 22 | 940 | 1,030 | ✅ PARITY | Documentation, datasheets, specifications, scripts, simulation, result reduction, optimization loops, LLM+simulator division of labor and engineering-autonomy ladder are preserved. |
| 23 | 1,543 | 1,470 | ✅ PARITY | The analog IC case study retains specification, knowledge, gm/ID, characterization, public/internal stacks, fixed topology, sizing, simulation, measurement extraction, deterministic PASS/FAIL, bounded iteration, human designer, automation boundaries and staged adoption. |
| 24 | 2,012 | 1,613 | 🟠 MATERIAL GAP | Core security is preserved: cloud/service terms, retention, on-prem boundaries, authorization, secrets, prompt injection, malicious documents, tools, least privilege, sandbox, approval, audit, supply chain, provenance, governance, EU example, system card and threat model. The meaningful omission is the Czech explicit section **AI literacy is an operating capability, not one-off training**. Add a short internationalized version. Primary source URLs can remain centralized in the bibliography. |
| 25 | 916 | 928 | ✅ PARITY | Organizational capability, process/data/tools/integration/governance/people/outcomes and the three adoption levels are preserved and sharpened. |
| 26 | 917 | 889 | ✅ PARITY | Process, data lineage, knowledge flow, ownership, sensitivity, structure, tacit knowledge, friction, baseline and readiness matrix are preserved. |
| 27 | 753 | 760 | ✅ PARITY | Frequency, attention/time, value, repeatability, data, risk, human judgment, technical complexity, quick wins, strategic bets and portfolio logic are preserved. |
| 28 | 819 | 735 | ✅ PARITY | Baseline, pilot, technical/operational/business/human metrics, quality, human vs. wall time, cost, error taxonomy, adoption, **GO / ITERATE / REDESIGN / STOP**, industrialization, scaling and pilot template are preserved. |
| 29 | 987 | 933 | ✅ PARITY | Adoption failure modes, fear/job change, skeptics, early adopters, champions, training, learning by doing, workflow sharing, community, responsibilities and competence-center role are preserved. |
| 30 | 946 | 926 | ✅ PARITY | Ground truth/rubrics, representative test set, golden questions, deterministic checks, LLM-as-judge, human eval, regressions, agent/RAG/tool evals and business metrics are preserved. |
| 31 | 1,097 | 965 | ✅ PARITY | Token/GPU economics, utilization, cloud/local/hybrid cost curves, integration, maintenance, cost of error, ROI/TCO, worked API-vs-dedicated-GPU example, on-prem conditions and cost dashboard are preserved. |
| 32 | 1,241 | 1,237 | ✅ PARITY | Future-facing themes are essentially one-to-one: reasoning, cheaper inference, local models, context, memory, multimodality, computer use, agent-ready software, background agents, robotics, simulation, science, personal and enterprise AI. |
| 33 | 1,619 | 1,442 | 🟠 MATERIAL GAP | English has valuable **unique** personal material on 8 GB vs. 32 GB VRAM and coding agents. It preserves the system-centric thesis, hype lessons, cloud/local routing and missing-layer diagnostic. But it drops the Czech closing sections **“What I would do differently”** and **“Seven things I would put on the first page.”** Those are strong personal/practical material and should be adapted back into EN. |
| 34 | 323 | 406 | ✅ PARITY | English is stronger, adding an explicit standard for future experiments while keeping the learning roadmap. |
| 35 | 1,092 | 1,146 | ✅ PARITY | Frontier model, local runtime, search, coding, STT, knowledge base, Git, automation, agent frameworks, monitoring/evals, day-one stack, on-prem pilot and intentionally excluded complexity are preserved. Named framework examples are also present. |
| 36 | 1,621 | 1,374 | 🟠 MATERIAL GAP | All ten projects are present and the important RAG negative-security test, filesystem guardrails, coding tests, enterprise pilot criteria and single-vs-multi-agent comparison survive. But several Czech step-by-step details are compressed. Most importantly, EN omits the **recommended difficulty progression** and the explicit **human-approval trigger list** in Project 10. These should be restored; selected procedure bullets from Projects 2/3/5 would also improve pedagogy. |

## Overall verdict

### 30 of 36 chapters do not need parity expansion

Breakdown:

- **21 chapters:** full or stronger parity — no change recommended.
- **8 chapters:** structurally compressed but substantively equivalent — no mandatory change.
- **1 chapter (9):** intentional international adaptation — keep the English approach.

### 6 chapters contain material worth porting into English

Priority order:

1. **Chapter 33 — What I Have Learned So Far**  
   Add an adapted “What I would do differently” section and the strongest version of the seven first-page rules. This strengthens the author's voice and practical value.

2. **Chapter 36 — Ten Projects**  
   Restore the difficulty ladder, explicit human-approval triggers, and selected procedure/checklist detail in Projects 2, 3 and 5.

3. **Chapter 13 — The Second Brain**  
   Add the three-layer model: `RAW ARCHIVE → KNOWLEDGE → WORKING`, plus a compact minimum architecture.

4. **Chapter 18 — Multi-Agent Systems**  
   Add the analog-block example and explicitly state that multi-agent architecture should evolve from a working single-agent loop.

5. **Chapter 15 — MCP, Skills, Plugins, and Connectors**  
   Add the constrained analog-design MCP example. Do **not** copy the dated MCP-spec changelog unless it is freshly verified against the current specification.

6. **Chapter 24 — AI Security**  
   Add a short internationalized subsection explaining AI literacy as an ongoing operating/security capability.

## Estimated impact of correcting the material gaps

The truly missing high-value material is much smaller than the 137-page PDF difference suggests.

A careful English adaptation of the six gaps above would likely add roughly **900–1,300 words**, plus some lists/code blocks. At the current English typesetting density that is likely on the order of **8–15 pages**, not 30–50 pages.

Therefore the earlier rough hypothesis that the English edition might naturally need to grow toward 480–510 pages was too conservative. After chapter-level inspection, a more evidence-based expectation is approximately **471–478 pages**, depending on final formatting.

The correct target is still **content completeness, not page-count equality**.

## Recommended action

Do one surgical English parity patch limited to Chapters **13, 15, 18, 24, 33 and 36**. Preserve the current native-English voice. Do not bulk-expand the other 30 chapters simply to make the page counts look similar.

After those edits:

1. rerun English editorial QA;
2. rerun snapshot/fact checks only for any time-sensitive material touched;
3. regenerate the English PDF;
4. visually inspect the newly affected chapter ranges;
5. compare chapter word counts and PDF page count again.

## Final conclusion

> **The English edition is not missing a quarter of the book. It is a much denser editorial adaptation. The parity audit found six localized gaps, not a systemic translation failure.**

The best next step is a small, deliberate parity patch — not a broad rewrite.
