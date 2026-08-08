---
title: "C. Tooling Landscape — Snapshot 08/2026"
part: "APPENDICES"
status: release-candidate
version: "0.8-eng"
updated: 2026-08-08
---

# C. Tooling Landscape — Snapshot 08/2026

**[Snapshot 08/2026]**

> **Snapshot: August 8, 2026.** The point is not to recommend one correct stack, but to show the types of tools that solve different layers. Verify current licensing, supported models, and security assumptions before deployment.

## Cloud AI

Use for frontier reasoning, multimodality, research, coding, and elastic capacity. Evaluate the entire service: API, enterprise terms, retention, region/residency, tool calling, structured output, rate limits, and observability.

## Local Inference

- **Ollama** — simple local model management and API: https://ollama.com/
- **llama.cpp** — detailed GGUF/quantized inference control: https://github.com/ggml-org/llama.cpp
- **vLLM** — high-throughput serving for supported models/GPUs: https://vllm.ai/

## User Interface

- **Open WebUI** — web interface for local and remote backends: https://openwebui.com/

A UI is useful for experimentation. It is not the architecture. Production systems still need model routing, identity, permissions, logs, and evals.

## Coding Agents

The useful capability pattern is:

```text
read repository
→ search
→ edit files
→ run tests
→ inspect failures
→ use Git
```

The workflow matters more than the logo:

```text
branch → agent changes → tests → diff → review → merge
```

## Agent Runtimes and Frameworks

- OpenAI Agents SDK — https://openai.github.io/openai-agents-python/
- Pydantic AI — https://ai.pydantic.dev/
- LangGraph — https://docs.langchain.com/oss/python/langgraph/overview

Choose a framework only after requirements are clear: state, retries, durable execution, tool orchestration, approval, tracing.

## RAG

RAG is a pipeline, not one product:

```text
parser → chunking → metadata → embeddings → index/search → reranker → LLM → citations
```

When quality is poor, inspect ingestion and retrieval before replacing the generator model.

## Speech and Multimodality

Useful categories include speech-to-text, text-to-speech, OCR/document vision, screenshot understanding, image generation, and vision-language models.

For technical work, preserve the distinction between what the model observed and what it inferred.

## Automation

Schedulers, event triggers, queues, retries, and workflow state remain conventional software concerns. Often the best design is:

```text
deterministic workflow
+
LLM only where interpretation is needed
```

## Observability

- **Langfuse** — https://langfuse.com/docs

A useful trace can recover model version, instruction version, retrieval, tool calls, latency, cost, output, and eval result. Sensitive data should not be logged indiscriminately.

## Knowledge Layer

- **Obsidian** — https://obsidian.md/

Markdown + Git is a simple open foundation for a human-readable knowledge base.

## Tool Selection Rule

Before adding a component, answer:

1. What concrete problem does it solve?
2. Can that problem be solved more simply?
3. Where will it run?
4. What data can it see?
5. How does it authenticate?
6. How is it updated?
7. How will it be monitored?
8. What happens when it fails?

> **A good AI stack is not the one with the most frameworks. It is the smallest stack that reliably solves the required use cases.**