# Sources, Primary Documentation, and Further Reading

This edition separates **slower-moving principles** from **fast-moving product snapshots**. For history and foundational concepts, I prefer original or canonical papers. For models, tools, security, and regulation, I prefer primary documentation from the provider, standard body, project, or regulator.

For any fast-moving product fact, use a simple rule:

> **Current primary documentation takes precedence over a printed snapshot in this book.**

## History and Foundations

1. Alan M. Turing — *On Computable Numbers, with an Application to the Entscheidungsproblem*, 1936.
2. Warren McCulloch, Walter Pitts — *A Logical Calculus of the Ideas Immanent in Nervous Activity*, 1943.
3. Alan M. Turing — *Computing Machinery and Intelligence*, *Mind*, 1950.
4. John McCarthy, Marvin Minsky, Nathaniel Rochester, Claude Shannon — *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence*, 1955/1956.
5. Frank Rosenblatt — early perceptron work, 1957–1958.
6. Marvin Minsky, Seymour Papert — *Perceptrons*, 1969.
7. David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams — *Learning representations by back-propagating errors*, *Nature*, 1986.
8. Yann LeCun et al. — *Gradient-Based Learning Applied to Document Recognition*, 1998.
9. Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton — *ImageNet Classification with Deep Convolutional Neural Networks*, 2012.

## Transformers, LLMs, and Post-Training

10. Ashish Vaswani et al. — *Attention Is All You Need*, 2017 — https://arxiv.org/abs/1706.03762
11. Tom B. Brown et al. — *Language Models are Few-Shot Learners*, 2020 — https://arxiv.org/abs/2005.14165
12. Long Ouyang et al. — *Training language models to follow instructions with human feedback*, 2022 — https://arxiv.org/abs/2203.02155

## Retrieval and RAG

13. Patrick Lewis et al. — *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, 2020 — https://arxiv.org/abs/2005.11401

## Agents, Tool Use, and Orchestration

14. Shunyu Yao et al. — *ReAct: Synergizing Reasoning and Acting in Language Models*, 2022/2023 — https://arxiv.org/abs/2210.03629
15. Model Context Protocol — official documentation — https://modelcontextprotocol.io/
16. Model Context Protocol — specification release 2026-07-28 — https://blog.modelcontextprotocol.io/posts/2026-07-28/
17. MCP Architecture — https://modelcontextprotocol.io/docs/learn/architecture
18. MCP server concepts — https://modelcontextprotocol.io/docs/learn/server-concepts
19. MCP Agent Skills — https://modelcontextprotocol.io/docs/2026-07-28/develop/build-with-agent-skills
20. OpenAI Agents SDK — https://openai.github.io/openai-agents-python/
21. Pydantic AI — https://ai.pydantic.dev/
22. LangGraph — https://docs.langchain.com/oss/python/langgraph/overview

## Local Inference and Practical Stack

23. llama.cpp — https://github.com/ggml-org/llama.cpp
24. Ollama — https://ollama.com/
25. vLLM — https://vllm.ai/
26. Open WebUI — https://openwebui.com/
27. Obsidian — https://obsidian.md/
28. Langfuse — https://langfuse.com/docs

## Security

29. OWASP GenAI Security Project — https://genai.owasp.org/
30. OWASP — Agentic AI threats and mitigations — https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/
31. OWASP — GenAI Data Security Risks & Mitigations 2026 — https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/
32. OWASP — State of Agentic AI Security and Governance — https://genai.owasp.org/resource/state-of-agentic-ai-security-and-governance/

## European Regulation and Privacy

These sources are included because the European Union provides a concrete governance case in Chapter 24. Other jurisdictions require their own current legal and sector-specific review.

33. European Commission — AI Act overview — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
34. European Commission — Guidelines on transparency obligations for providers and deployers of AI systems — https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems
35. European Commission — Transparency obligations under Article 50 — https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act
36. European Commission — GDPR principles — https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/principles-gdpr_en

## Model Snapshot — August 8, 2026

37. OpenAI — GPT-5.6 — https://openai.com/index/gpt-5-6/
38. OpenAI — Model Release Notes — https://help.openai.com/en/articles/9624314-model-release-notes
39. Anthropic — Claude Fable 5 — https://www.anthropic.com/claude/fable
40. Anthropic — Claude Sonnet 5 — https://www.anthropic.com/news/claude-sonnet-5
41. Anthropic — Claude Opus 4.8 — https://www.anthropic.com/news/claude-opus-4-8
42. Google — Gemini API changelog — https://ai.google.dev/gemini-api/docs/changelog
43. Google — Gemini 3.6 Flash — https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash
44. xAI — Grok 4.5 — https://x.ai/news/grok-4-5
45. DeepSeek — API updates — https://api-docs.deepseek.com/updates
46. Qwen — Qwen3.6 — https://qwen.ai/blog?id=qwen3.6-35b-a3b
47. Google — Gemma 4 model card — https://ai.google.dev/gemma/docs/core/model_card_4
48. Mistral — Mistral Small 4 — https://mistral.ai/news/mistral-small-4/
49. Cohere — Command A+ — https://cohere.com/blog/command-a-plus
50. Cohere — Rerank / Transcribe changelog — https://docs.cohere.com/v2/changelog

## How to Use This Bibliography

For understanding a principle, start with a paper or stable documentation. For deciding what to deploy today, open the current product documentation and run your own eval on your own workload.

> **The book is a compass. The vendor page is today’s weather report. Your eval set decides whether either one helps your journey.**