---
title: "10. Context Engineering"
part: "V — Working with Models"
status: release-candidate
version: "0.8-eng"
updated: 2026-08-08
---

# 10. Context Engineering

<!-- visual:10-context-stack.svg -->

![Layers of model context](assets/diagrams/10-context-stack.svg)

*Figure: What the model actually has available at the moment it makes a decision.*

Prompting asks **what we tell the model**.

Context engineering asks the larger question:

> **What information is actually available to the model at the moment it has to decide?**

For a simple chat, context may be a few messages. For an agentic system it can include:

```text
system instructions
+
user request
+
conversation history
+
retrieved evidence
+
tool results
+
workflow state
+
memory
+
policy
+
examples and schemas
```

The model responds to that assembled environment.

That is why the same model can look brilliant in one application and unreliable in another. The model did not change. The **information architecture around it** did.

---

## 10.1 Better Context Can Beat a Bigger Model

Consider two systems using the same LLM.

System A receives:

```text
What is the current VDD_IO limit?
```

System B receives:

```text
policy
+
question
+
authoritative specification revision
+
document metadata
+
relevant section
+
change history
```

The second system has a much better chance of being correct.

> **A large part of practical AI engineering is not making the model “think harder.” It is making sure the right information arrives at the right moment.**

---

## 10.2 What Belongs in Context

Useful layers include:

- **System/application instructions** — role, policy, boundaries.
- **User request** — the current goal.
- **Conversation history** — only what remains relevant.
- **Retrieved knowledge** — evidence selected by search or RAG.
- **Tool results** — database queries, test logs, simulations, web results.
- **Memory** — selected information from previous work.
- **Workflow state** — current step, prior result, retry count, approvals.
- **Schemas/examples** — output contracts or behavior examples.

All of them compete for the same finite context budget.

---

## 10.3 More Context Is Not Automatically Better

A million-token window creates the temptation to send everything.

Imagine asking a human one question and dropping 500 folders on the desk. Technically, all the information is present. Practically, we made the task harder.

Models can also be distracted by:

- obsolete revisions,
- irrelevant meeting notes,
- duplicates,
- another project’s data,
- long stale chat history.

Good context engineering asks:

```text
What does the model need now?
```

not:

```text
What information do we own?
```

---

## 10.4 Context Pollution

**Context pollution** is information that is wrong, obsolete, contradictory, or irrelevant enough to degrade the decision.

Suppose the system sees:

```text
spec_v1.pdf
spec_v2.pdf
spec_v3_FINAL.pdf
```

with no indication of authority. If the answer uses an old value, the root cause is not necessarily “weak reasoning.” It may be poor data governance.

Pollution also comes from old instructions, previous model errors left in history, verbose tool output, and failed intermediate assumptions.

Agents amplify this problem because bad state can propagate:

```text
bad assumption
→ bad plan
→ tool call
→ new state
→ more bad decisions
```

Long workflows need **context hygiene**.

---

## 10.5 Compress History Without Destroying State

A 50-message conversation may be reducible to:

```text
Project: LDO revision C

Decisions:
- VDD = 1.8 V
- target Iq < 5 µA
- DRC-17 layout change approved

Open items:
- verify cold corner
- review startup
```

That summary can replace thousands of tokens.

But summaries are lossy. Critical values should often be stored as structured state rather than trusted to prose compression:

```json
{
  "vdd": "1.8 V",
  "revision": "C",
  "status": "verification"
}
```

Use summary for understanding; use structured state for precision.

---

## 10.6 Working Memory vs. Long-Term Memory

**Working memory** is the small set of information needed for the current task: goal, plan, current step, recent tool result, relevant evidence.

Think of it as a desk.

**Long-term memory** is persistent storage across tasks: decisions, user preferences, known failures, experiment results, project history.

It can live in SQL, documents, vector stores, knowledge graphs, or plain files.

Memory is not magical material inside the LLM. A typical mechanism is:

```text
event
 ↓
should this be remembered?
 ↓
store
 ↓
retrieve later
 ↓
insert into current context
```

If retrieval fails, the system technically has memory and practically remembers nothing.

---

## 10.7 Agents Need Active Context Management

An agent may execute dozens or hundreds of steps. Keeping the complete raw history forever causes cost, latency, and pollution to grow.

A serious orchestrator therefore decides:

- what to keep verbatim,
- what to summarize,
- what to discard,
- what to persist,
- what to retrieve again from the source of truth.

A production agent should not be one infinitely growing chat transcript. It should operate on **managed state and curated context**.

---

## 10.8 AI-Ready Data Starts Before the Model

A model cannot reliably resolve organizational chaos such as:

```text
final.docx
final2.docx
final_really_final.docx
new_final_comments.docx
```

Useful AI-ready information has explicit:

- stable identity,
- revision/version,
- lifecycle state (`DRAFT / RELEASED / OBSOLETE`),
- owner,
- validity date,
- project/type metadata,
- access control,
- relationships to other artifacts.

For example:

```text
specification
→ implementation
→ verification plan
→ test results
```

Better metadata can improve retrieval more than changing the LLM.

---

## 10.9 Example: “Why Did We Change This?”

User asks:

> Why did we change the startup capacitor in the latest revision?

The bad architecture sends the model 80,000 project documents.

A better pipeline is:

```text
1. identify project and block
2. resolve authoritative revision
3. search for “startup capacitor” and related identifiers
4. retrieve design-review notes and change records
5. rerank candidates
6. assemble a small evidence set
7. answer with citations
```

That is context engineering.

---

## 10.10 Context Engineering Is a Pipeline

Stop thinking of context as one giant string.

Think:

```text
user request
      ↓
intent / task classification
      ↓
permissions
      ↓
retrieval
      ↓
state and memory
      ↓
context assembly
      ↓
model
      ↓
verification
```

Now failures become diagnosable.

Was the wrong source retrieved? Did an obsolete revision enter context? Did the model miss evidence that was present? Were the instructions ambiguous?

That is more useful than saying:

> “The AI hallucinated again.”

---

## Key Takeaways

1. **The prompt is only one part of context.**
2. **A model can only use the information the system makes available at the right time.**
3. **More context is not automatically better.**
4. **Obsolete and conflicting information creates context pollution.**
5. **Long histories need compression, structured state, or re-retrieval.**
6. **Working memory and long-term memory solve different problems.**
7. **Agents need explicit context management or long workflows degrade.**
8. **AI-ready organizations need identity, metadata, versions, ownership, permissions, and data relationships.**

Now we reach one of the most common practical problems:

> **The model is capable, but it does not know my documents. How do I connect private knowledge without pretending the model learned it?**