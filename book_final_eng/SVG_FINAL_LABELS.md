# Final visible SVG labels — English edition

## 00-ai-system-stack.svg

- From Model to Value
- Model capability is only the beginning. The whole system determines the real outcome.
- From Model to Value
- Model capability is only the beginning. The whole system determines the real outcome.
- MODEL
- language
- reasoning
- CONTEXT
- task
- evidence
- DATA
- facts
- provenance
- TOOLS
- search
- code · API
- CONTROL
- state
- permissions
- EVALS
- verify
- measure
- VALUE
- correct result · safe action
- evidence that the system works
- The weakest layer often determines the quality of the whole result.

## 01-history-timeline.svg

- From Computation to Agentic Systems
- AI history is the convergence of algorithms, data, compute, and tools.
- From Computation to Agentic Systems
- AI history is the convergence of algorithms, data, compute, and tools.
- 1936
- Turing
- general-purpose computing
- 1956
- Dartmouth
- the term AI
- 1986
- Backprop
- neural networks
- 2012
- AlexNet
- deep learning
- 2017
- Transformer
- foundation of LLMs
- 2022
- ChatGPT
- mass market
- 2025
- Reasoning + tools
- practical agents
- 2026
- Agentic systems
- model as one system component

## 02-ai-taxonomy.svg

- AI → ML → Deep Learning → Generative AI → LLM
- An LLM is a model type; an agentic system is a system built around a model.
- AI → ML → Deep Learning → Generative AI → LLM
- An LLM is a model type; an agentic system is a system built around a model.
- Artificial Intelligence
- broadest class of intelligent systems
- Machine Learning
- learning patterns from data
- Deep Learning
- deep neural networks
- Generative AI
- generation of new content
- Foundation Models / LLM
- general models adaptable to many tasks

## 03-embeddings.svg

- Embeddings: Meaning Represented as Numbers
- Vector representations make semantic similarity computable.
- Embeddings: Meaning Represented as Numbers
- Vector representations make semantic similarity computable.
- Text / token
- “transistor”
- Embedding
- [0.13, −0.42, …]
- Vector space
- relative position
- Similar concepts
- MOSFET, gate…

## 03-enter-to-answer.svg

- From Enter to Answer
- A simplified inference path.
- From Enter to Answer
- A simplified inference path.
- Context
- system + user + history
- Tokenization
- text → tokens
- Model
- Transformer layers
- Decoding
- token selection
- Stream
- tokens to user

## 03-model-vs-database.svg

- An LLM Is Not a Database of Answers
- Training changes parameters; exact documents must come from search, RAG, or a tool.
- An LLM Is Not a Database of Answers
- Training changes parameters; exact documents must come from search, RAG, or a tool.
- Training data
- text and code
- Learning
- relationships and patterns
- Parameters
- compressed representation
- LLM
- generates the next token

## 03-token-generation-loop.svg

- How an LLM Generates an Answer
- An answer emerges by repeatedly predicting the next token.
- How an LLM Generates an Answer
- An answer emerges by repeatedly predicting the next token.
- Prompt
- context so far
- Transformer
- computation
- Probabilities
- candidate tokens
- Sampling
- token selection
- New context
- prompt + token
- The loop continues until the answer ends or a limit is reached.

## 04-llm-strengths-limits.svg

- Where LLMs Are Strong — and Where They Need Support
- A language model is an excellent interpreter and generator; external tools often provide precision.
- Where LLMs Are Strong — and Where They Need Support
- A language model is an excellent interpreter and generator; external tools often provide precision.
- Strength: transformation
- summarization, rewriting, translation, structuring
- Strength: extraction
- finding and classifying information in supplied context
- Strength: creation
- text, code, designs, and solution variants
- Verify: facts and reasoning
- confident output can still be wrong
- Add a tool: current world
- web, databases, APIs, and enterprise systems
- Add a tool: precision
- calculator, Python, tests, simulator

## 05-model-map.svg

- AI Model Map by Task
- There is no single best model; choose by modality, capability, and operating mode.
- AI Model Map by Task
- There is no single best model; choose by modality, capability, and operating mode.
- Use-case
- General LLM
- Reasoning
- Coding
- Vision
- Speech
- Embeddings

## 06-model-selection.svg

- How to Choose a Model for a Real Task
- A benchmark is only one input; your own test on the real workflow decides.
- How to Choose a Model for a Real Task
- A benchmark is only one input; your own test on the real workflow decides.
- Use-case
- real task
- Test set
- your own examples
- Quality
- correctness + robustness
- Operations
- latency + cost
- Constraints
- privacy + license
- Choose the model that best meets the full requirement set — not the one with the highest single benchmark.

## 07-cloud-onprem-hybrid.svg

- Cloud vs. on-prem vs. hybrid
- Route the task by data sensitivity, performance, cost, and operational risk.
- Cloud vs. on-prem vs. hybrid
- Route the task by data sensitivity, performance, cost, and operational risk.
- Cloud
- frontier models
- rapid scaling
- Hybrid
- sensitive data local
- selective cloud
- On-prem
- data control
- self-operated

## 08-local-memory-stack.svg

- Where Local LLM Memory Goes
- Model weights are only part of the total memory requirement.
- Where Local LLM Memory Goes
- Model weights are only part of the total memory requirement.
- Application / UI
- chat and agent framework
- Inference runtime
- Ollama / llama.cpp / vLLM
- KV cache + context
- grows with context length
- Model weights
- FP16 / INT8 / INT4
- VRAM / unified memory
- typical limit
- CPU RAM + storage
- offload and data

## 09-prompt-anatomy.svg

- Prompt as a Task Specification
- A strong prompt is structured context, not a magic phrase.
- Prompt as a Task Specification
- A strong prompt is structured context, not a magic phrase.
- Goal
- what the result should be
- Context
- what the model needs to know
- Constraints
- what it must and must not do
- Examples
- example of a correct solution
- Output format
- text / table / JSON
- Iteration
- feedback

## 10-context-stack.svg

- Context Engineering: What the Model Actually Sees
- Answer quality depends on having the right context right now.
- Context Engineering: What the Model Actually Sees
- Answer quality depends on having the right context right now.
- System instructions
- application rules
- User intent
- current task
- Relevant history
- only useful parts
- Retrieved knowledge
- RAG / files / web
- Tool results
- API / Python / simulator
- Working memory
- state and intermediate results

## 11-external-data-bridge.svg

- How to Bring My Data to the Model
- Private and current information must be brought into context by an external layer.
- How to Bring My Data to the Model
- Private and current information must be brought into context by an external layer.
- My data
- PDF / e-mail / DB
- Access layer
- search / RAG / MCP
- Relevant context
- only the needed slice
- LLM
- interpretation
- Answer
- ideally with a citation

## 12-model-rag-agent.svg

- Model vs. RAG vs. Agent
- These are not three competing things. Each additional layer adds a new system capability.
- Model vs. RAG vs. Agent
- These are not three competing things. Each additional layer adds a new system capability.
- Model
- generates and interprets
- + RAG
- retrieves private knowledge
- + Tools
- can perform an action
- + Agent loop
- chooses the next step
- AI system
- data + tools + controls

## 12-rag-pipeline.svg

- RAG: From Document to Sourced Answer
- Retrieval separates finding relevant evidence from generating the answer.
- RAG: From Document to Sourced Answer
- Retrieval separates finding relevant evidence from generating the answer.
- Documents
- parse + chunking
- Index
- embeddings + metadata
- Query
- semantic / hybrid search
- Rerank
- best passages
- LLM
- answer + citations
- RAG does not retrain the model; it supplies the right context at query time.

## 13-second-brain.svg

- The AI-Enabled Second Brain
- AI is a navigator over the knowledge base, not a replacement for the knowledge itself.
- The AI-Enabled Second Brain
- AI is a navigator over the knowledge base, not a replacement for the knowledge itself.
- Knowledge base
- Notes
- Documents
- Email
- Meetings
- Web
- Books

## 14-tool-use.svg

- Tool Use: The LLM Stops Only Writing
- The model selects a tool, receives the result, and continues with new context.
- Tool Use: The LLM Stops Only Writing
- The model selects a tool, receives the result, and continues with new context.
- User
- goal
- LLM
- tool selection
- Tool call
- function + arguments
- Tool
- DB / web / API
- LLM
- interpretation

## 15-mcp-architecture.svg

- MCP as a Standardized Interface
- MCP decouples the AI application from specific integrations.
- MCP as a Standardized Interface
- MCP decouples the AI application from specific integrations.
- AI host
- chat / IDE / agent
- MCP client
- standardized calls
- MCP server
- tools + resources
- Native API
- authentication + logic
- Real system
- files / DB / Git / CAD

## 16-agent-anatomy.svg

- Anatomy of an AI Agent
- An agent is software around an LLM: goal, state, tools, controls, and a loop.
- Anatomy of an AI Agent
- An agent is software around an LLM: goal, state, tools, controls, and a loop.
- Goal / instructions
- what the system must complete
- LLM / reasoning
- next-step selection
- Tools
- actions in the external world
- State / memory
- what has already happened
- Checks
- verify + human approval
- Loop
- repeat until a stop condition

## 16-agent-loop.svg

- Agent Loop
- Every step can change the next decision.
- Agent Loop
- Every step can change the next decision.
- Goal
- Observe
- Reason
- Plan
- Act
- Verify

## 17-build-agent.svg

- How to Build an Agent Without Unnecessary Autonomy
- Start with a deterministic skeleton and add autonomy only after measurement.
- How to Build an Agent Without Unnecessary Autonomy
- Start with a deterministic skeleton and add autonomy only after measurement.
- Use-case
- one precise task
- Tools + data
- only required permissions
- Checks
- validation
- Human gate
- risky actions
- Autonomy
- only after evals

## 18-multi-agent.svg

- Multi-Agent System
- Multiple agents make sense only when roles are clearly separated.
- Multi-Agent System
- Multiple agents make sense only when roles are clearly separated.
- Orchestrator
- Planner
- Researcher
- Coder
- Reviewer
- Executor
- Critic

## 19-orchestration.svg

- Orchestrating Agentic Systems
- The workflow owns state, retries, and checkpoints; the LLM decides only where it adds value.
- Orchestrating Agentic Systems
- The workflow owns state, retries, and checkpoints; the LLM decides only where it adds value.
- Input
- event / request
- State
- checkpoint
- Agent step
- LLM + tools
- Control
- retry / timeout
- Output
- result

## 20-coding-agent.svg

- Coding Agent as a Development Loop
- The power comes from connecting the model to the codebase, tests, and Git.
- Coding Agent as a Development Loop
- The power comes from connecting the model to the codebase, tests, and Git.
- Task
- Read code
- Plan
- Edit
- Run tests
- Review diff
- Commit

## 21-document-pipeline.svg

- AI over Heterogeneous Documents
- The hardest part is often high-quality parsing, metadata, permissions, and citations.
- AI over Heterogeneous Documents
- The hardest part is often high-quality parsing, metadata, permissions, and citations.
- PDF / Word / Excel
- PPT / logs
- Normalization
- parse / OCR
- Metadata + chunks
- structure
- Search / RAG
- retrieval + rerank
- LLM
- answer + sources

## 22-engineering-loop.svg

- AI + a Deterministic Engineering Tool
- The LLM proposes the next step; the simulator or solver determines the physics.
- AI + a Deterministic Engineering Tool
- The LLM proposes the next step; the simulator or solver determines the physics.
- Requirements
- Specification
- Design
- Simulation
- Extraction
- Comparison

## 23-analog-ic-loop.svg

- AI-assisted analog IC design
- Knowledge, gm/ID, simulation, and designer decisions in one loop.
- AI-assisted analog IC design
- Knowledge, gm/ID, simulation, and designer decisions in one loop.
- Designer
- Spec
- gm/ID sizing
- SPICE / Spectre
- Extract metrics
- Optimize

## 24-security-boundaries.svg

- Security Boundaries of an Agentic System
- Permissions and controls must separate untrusted data, the model, and tools.
- Security Boundaries of an Agentic System
- Permissions and controls must separate untrusted data, the model, and tools.
- Untrusted input
- web / mail / docs
- Policy boundary
- sanitization
- LLM / agent
- tool selection
- Permissions
- least privilege
- Tool
- read / write / external

## 25-ai-capability-stack.svg

- “We Have ChatGPT” Is Not an AI Capability
- Business value comes from connecting the model to processes, data, tools, and people.
- “We Have ChatGPT” Is Not an AI Capability
- Business value comes from connecting the model to processes, data, tools, and people.
- Business process
- what we want to improve
- Workflow / agent
- step control
- Tools + integrations
- APIs and applications
- Knowledge + data
- right context
- Model layer
- cloud / local / routing
- Governance + evals
- security and quality
- People
- skills and ownership

## 26-ai-readiness.svg

- AI Readiness Is Not Only Technology
- Processs, data, security, measurement, and people must be ready together.
- AI Readiness Is Not Only Technology
- Processs, data, security, measurement, and people must be ready together.
- Process
- clear process and owner
- Data
- availability and quality
- Knowledge
- what is documented
- Security
- sensitivity and permissions
- Measurement
- baseline and metrics
- People
- users and accountability

## 27-usecase-matrix.svg

- Choosing an AI Use Case
- Prefer high value with reasonable technical and operational complexity.
- Choosing an AI Use Case
- Prefer high value with reasonable technical and operational complexity.
- lower complexity
- higher complexity
- lower value
- higher value
- Strategic bet
- high value, high complexity
- Low priority
- low value and low complexity
- Quick win
- high value, low complexity
- Watch out
- complex, but low benefit

## 28-pilot-scale.svg

- Pilot → Evidence → Scale
- An AI project should pass through measurable gates.
- Pilot → Evidence → Scale
- An AI project should pass through measurable gates.
- Baseline
- time / quality / cost
- Pilot
- bounded use case
- Evidence
- evals + users
- Go / no-go
- decision
- Scale
- industrialization

## 29-adoption-loop.svg

- Adoption as a Learning Loop
- Technology alone is not enough; people must see the value and share results.
- Adoption as a Learning Loop
- Technology alone is not enough; people must see the value and share results.
- Use-case
- Experiment
- Measure
- Share
- Train
- Standardize

## 30-evaluation-stack.svg

- Evaluation from Component to Business Outcome
- One impressive answer is not evidence of system quality.
- Evaluation from Component to Business Outcome
- One impressive answer is not evidence of system quality.
- Business metric
- time / cost / error rate
- End-to-end task
- did it complete the real task?
- Agent / workflow
- correct steps and recovery
- RAG / retrieval
- did it find the right sources?
- Model
- answer quality
- Regression set
- golden questions over time

## 31-ai-tco.svg

- AI Solution TCO
- Token or GPU cost is only one layer of total cost.
- AI Solution TCO
- Token or GPU cost is only one layer of total cost.
- Cost of error
- impact of a bad result
- People and operations
- monitoring and support
- Integration
- development and maintenance
- Inference
- API tokens / GPU
- Hardware / cloud
- CAPEX / OPEX
- Security + compliance
- audit and governance

## 32-ai-trends.svg

- Where AI Is Going: From Model to Verified System
- Five trends — adaptive reasoning, multimodality, cheaper inference, tools, and agentic workflows — converge on verified AI systems.
- Where AI Is Going
- Not one “smarter model,” but a system with more adaptive compute, modalities, tools, and verification.
- Reasoning
- adaptive compute
- Multimodality
- text · image · audio
- Efficiency
- lower cost / task
- Tools
- data + actions
- Agents
- longer workflows
- VERIFIED AI SYSTEM
- context + tools + policy + evals + observability
- capability ≠ reliability

## 33-model-to-system.svg

- From Model to System
- The most important shift is not a larger model, but better questions about the system around it.
- From Model to System
- The most important shift is not a larger model, but better questions about the system around it.
- MODEL-CENTRIC
- Which model is best?
- How many parameters does it have?
- Who leads the benchmark?
- SYSTEM-CENTRIC
- What data can it see?
- What tools can it use?
- How will I verify the result?
- VALUE-CENTRIC
- Is the result correct?
- Is it safe?
- Is it better than the baseline?
- SHIFT
- model → system → measurable outcome
- Model capability is an input. Value is a property of the whole workflow.

## 34-learning-roadmap.svg

- Learning Roadmap: From Model to Production
- The next steps make sense in the order in which they build on one another.
- Learning Roadmap: From Model to Production
- The next steps make sense in the order in which they build on one another.
- Local stack
- model + runtime
- RAG
- your own data
- Tools
- real actions
- Agent
- reliable loop
- Multi-agent
- only where it adds value
- Production
- evals + observability

## 35-minimal-ai-stack.svg

- My Minimal AI Stack
- The minimum is not one chatbot, but a small set of layers for models, data, tools, and measurement.
- My Minimal AI Stack
- The minimum is not one chatbot, but a small set of layers for models, data, tools, and measurement.
- AI workspace
- Frontier LLM
- Local LLM
- Search + RAG
- Git + files
- Automation
- Monitoring

## 36-debug-ai-system.svg

- When AI Fails: Where to Look First
- Do not automatically reach for a “better model.” First locate the layer that failed.
- When AI Fails: Where to Look First
- Do not automatically reach for a “better model.” First locate the layer that failed.
- 1 · DATA
- correct source
- revision
- 2 · CONTEXT
- retrieval
- relevance
- 3 · TOOLS
- arguments
- outputs
- 4 · POLICY
- permissions
- approval
- 5 · STATE
- loop
- checkpoint
- 6 · VERIFY
- tests
- evals
- 7 · MODEL
- capability
- reasoning
- The model is only one possible cause. Debug the system, not the brand.

## 36-project-ladder.svg

- 10 Projects: A Path to Agentic Systems
- Each project adds one capability — and one new class of risk.
- 10 Projects: A Path to Agentic Systems
- Each project adds one capability — and one new class of risk.
- 1–2
- chat over documents
- 3–4
- knowledge + local
- 5–6
- RAG + tool
- 7–8
- filesystem + coding
- 9–10
- workflow + multi-agent

