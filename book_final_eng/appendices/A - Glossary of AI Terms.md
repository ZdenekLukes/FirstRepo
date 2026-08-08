---
title: "A. Glossary of AI Terms"
part: "APPENDICES"
status: release-candidate
version: "0.8-eng"
updated: 2026-08-08
---

# A. Glossary of AI Terms

This glossary uses the terminology of the book. The definitions are intentionally practical rather than exhaustive academic definitions.

| Term | Practical meaning in this book |
|---|---|
| **AI — Artificial Intelligence** | The broadest category: systems that perform tasks associated with intelligent behavior. AI is not a synonym for LLM. |
| **ML — Machine Learning** | Methods that learn patterns from data instead of requiring every rule to be programmed manually. |
| **DL — Deep Learning** | Machine learning based on deep neural networks. |
| **Generative AI** | Models that generate new content such as text, images, audio, video, or code. |
| **Foundation model** | A broadly trained general-purpose model that can support many downstream tasks. |
| **LLM — Large Language Model** | A foundation model centered primarily on language/token representations and autoregressive generation. |
| **Multimodal model / LMM** | A model that works across multiple modalities such as text, image, audio, or video. |
| **Token** | A unit produced by a tokenizer: a word, word fragment, punctuation, number, or other unit. |
| **Tokenizer** | Converts text to token IDs and back. It affects context length, cost, and multilingual efficiency. |
| **Parameter / weight** | A learned numerical value in a model. Parameters are not a document database. |
| **Embedding** | A vector representation used to encode relationships; commonly used in retrieval. |
| **Transformer** | The attention-based neural-network architecture underlying much of modern LLM development. |
| **Attention** | A mechanism that lets the model weight relationships among parts of the current context. |
| **Inference** | Running an already trained model on a particular input. |
| **Training** | Learning model parameters from data. |
| **Pre-training** | Large-scale initial training before later specialization/post-training. |
| **Fine-tuning** | Additional training for particular behavior, style, or domain performance. |
| **Quantization** | Lower-precision representation of weights/computation to reduce memory and often increase inference efficiency. |
| **Context** | Information available to the model for the current inference: instructions, conversation, evidence, tool results, state. |
| **Context window** | Maximum token capacity the model can process in a request. A long context is not perfect memory. |
| **Prompt** | An instruction/request sent to a model; only one component of broader context. |
| **System instruction** | Application-level instruction with higher priority than ordinary user input. It is not by itself a security boundary. |
| **Context engineering** | Designing which instructions, data, history, retrieved knowledge, state, and tool results the model receives. |
| **RAG** | Retrieval of relevant external evidence before generation, with that evidence placed into model context. |
| **Retrieval** | Finding relevant documents, records, or chunks for a query. |
| **Chunk** | A smaller unit of a document stored or returned by a retrieval system. |
| **Vector database** | A store/index optimized for vector similarity. RAG may use one, but does not require one. |
| **Reranker** | A model/algorithm that reorders retrieval candidates using a more precise relevance score. |
| **Tool** | External capability such as a function, API, program, database, calculator, or simulator. |
| **Tool/function calling** | Structured mechanism by which a model selects a tool and supplies arguments. |
| **MCP** | Model Context Protocol: an open protocol for connecting AI applications to tools and data/resources. |
| **Skill** | Reusable instructions or procedure for performing a task; packaging varies by platform. |
| **Plugin** | Platform-specific extension package. |
| **Connector** | Integration between an AI system and a service/data source. |
| **Agent** | Software around a model that keeps state, selects actions/tools, and repeats steps toward a goal. |
| **Agent loop** | Observe → reason/plan → act → verify, repeated until success or stop/escalation. |
| **State** | Information about current task progress that must survive between steps. |
| **Memory** | Persistent information outside immediate context; must handle validity, provenance, lifecycle, and permissions. |
| **Multi-agent system** | System with multiple separated agent roles justified by specialization, parallelism, permissions, models, or independent review. |
| **Orchestration** | Control of step order, state, agents, tools, retries, timeouts, queues, and approvals. |
| **MoE** | Mixture of Experts: architecture that activates part of a larger set of experts for each token; total weight memory may still be large. |
| **Reasoning** | Capability for harder multi-step tasks, often using more inference-time computation. Not a correctness guarantee. |
| **Open-weight** | Model weights are downloadable. This does not automatically imply an open-source license or public training data. |
| **Benchmark** | Standardized capability test. Public benchmark performance may not predict your workload. |
| **Eval / evaluation** | Systematic measurement of a model or full AI system on a defined test set. |
| **Ground truth** | Reference-correct result used for evaluation. |
| **Golden question** | Critical regression case that should continue to work after model/prompt/pipeline changes. |
| **LLM-as-a-judge** | Using a model to evaluate another output, with calibration and controls. |
| **Hallucination** | Fluent generated claim that is false or unsupported by available evidence. |
| **Grounding** | Anchoring an answer in external evidence such as documents, databases, tests, or tools. |
| **Prompt injection** | Input intended to manipulate model/system behavior through instructions. |
| **Indirect prompt injection** | Injection contained in web pages, files, email, tool results, or other loaded content. |
| **Guardrail** | Technical or process control reducing probability or impact of undesired behavior. |
| **Human-in-the-loop** | Workflow in which a human reviews or approves selected AI steps. |
| **Approval gate** | Explicit point beyond which the system cannot proceed without required approval. |
| **Sandbox** | Isolated environment with constrained permissions for safer execution. |
| **Observability** | Logs, traces, and metrics exposing what the system did and how it behaved. |
| **Provenance** | Information about origin and version of data, documents, models, or outputs. |

## How to Use the Glossary

When two terms look similar — model vs. application, tool vs. skill, context vs. memory, RAG vs. knowledge base — preserve the distinction rather than treating the words as interchangeable.