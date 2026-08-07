# English Edition Style Guide — v0.8-eng

## Editorial Positioning

**Title:** *AI: From First Principles to Agentic Systems*  
**Subtitle:** *How AI Actually Works — and How to Build Reliable Systems with Models, Data, Tools, and Verification*

The English edition is an **international adaptation**, not a sentence-by-sentence translation of the Czech master.

Its target reader is technically minded but may be completely new to AI. A second target reader is the experienced AI practitioner who wants a compact engineering model of how the parts fit together.

## Voice

Write like an experienced engineer explaining what finally made the system click.

The voice should be direct, precise, curious without hype, practical, skeptical of unsupported claims, and willing to use first person when experience matters.

Avoid consultant language and generic motivation.

Bad:

> AI is revolutionizing every industry and unlocking unprecedented value.

Better:

> A model can write an excellent answer and still be the wrong component for the job. The architecture decides whether the result is useful.

## English Variant

Use **American English** consistently: `behavior`, `organization`, `optimize`, `modeling`.

## Core Vocabulary

Keep these distinctions stable:

```text
MODEL ≠ AI APPLICATION ≠ AGENT ≠ AI SYSTEM
```

Preferred terms:

- **agentic system / agentic AI** for systems with autonomous or semi-autonomous loops;
- **agent** for one software entity inside such a system;
- **open-weight** when weights are available but license/data/training pipeline are not necessarily open source;
- **context engineering** for the full information environment around a model;
- **verification** for evidence-based checks;
- **eval / evaluation** for systematic measurement against a test set;
- **provenance** for origin/version/source information.

Do not use “AI employee,” “digital brain,” or “autonomous coworker” as technical definitions.

## Chapter Rhythm

A strong chapter usually follows:

```text
practical question
↓
mental model
↓
concrete example
↓
architecture / table / decision rule
↓
failure mode
↓
key takeaways
↓
bridge to next question
```

## Technical Depth

Do not remove an engineering detail merely because a beginner may not know the term. Define it, explain why it matters, and preserve the real distinction.

The book should be accessible **without becoming shallow**.

## Mathematics

Use equations only when they provide a practical mental model or sizing rule. Prefer:

```text
required memory ≈ weights + KV cache + runtime + headroom
```

over derivations that do not improve practical decisions.

## Evidence and Claims

Separate:

```text
FACT FROM SOURCE
```

from:

```text
ENGINEERING INFERENCE
```

For fast-moving product facts, use explicit snapshots such as `Snapshot: August 7, 2026.` Prefer primary sources.

## Security Language

Never imply that a system prompt or textual instruction is a security boundary.

Preferred framing:

```text
model proposes
→ host validates
→ policy authorizes
→ tool executes
→ verifier checks
```

Use **least privilege**, **defense in depth**, **approval gate**, **sandbox**, and **audit trail** consistently.

## Internationalization

Do not remove useful European examples merely because the edition is global. Present EU AI Act/GDPR as a concrete jurisdictional case, state that other jurisdictions differ, and keep general security/governance principles jurisdiction-neutral.

Convert Czech-only linguistic observations into multilingual design lessons unless the Czech example itself is instructive.

The analog IC design case study stays. It is a global engineering example and a distinctive signature of the book.

## Personal Voice

Chapter 33 is intentionally personal. Do not homogenize it into corporate prose.

Personal observations must not be converted into universal benchmark claims unless the experiment was designed and recorded as such.

## Visual Language

No decorative robots, glowing brains, generic humanoids, or cyberpunk AI imagery.

A visual earns its place only if it compresses architecture, decision flow, failure path, comparison, hierarchy, or feedback loop.

Visuals must remain understandable in grayscale and should not rely on color alone.

> **WOW comes from compression of a difficult truth, not visual decoration.**

## Endings

Do not end chapters with housekeeping, source URLs, or generic filler. End with the strongest takeaway, a useful question, or a bridge that makes the next chapter feel necessary.

## Final Editorial Test

Before accepting a passage, ask:

1. Is it true or clearly labeled as inference/opinion?
2. Is there a simpler way to say it without losing precision?
3. Does it help the reader build a mental model or make a decision?
4. Is the distinction likely to remain useful after current product names change?
5. Would an engineer trust this paragraph enough to use it as a starting point?

If several answers are no, rewrite or remove the passage.