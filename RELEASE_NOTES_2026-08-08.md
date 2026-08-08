# Release Notes — 2026-08-08

## AI od základů k agentním systémům / AI: From First Principles to Agentic Systems

This repository now contains two independently edited release-candidate editions of the book.

## Editions

### Czech edition

**Title:** *AI od základů k agentním systémům*  
**Subtitle:** *Jak AI skutečně funguje, jak ji používat a jak z modelů stavět spolehlivé systémy*  
**Version:** `0.7`  
**Status:** release candidate

Current manuscript structure:

- introduction;
- 36 numbered chapters;
- 7 appendices;
- 43 diagrams plus print variants;
- approximately 53,000 words;
- current proof format: 170 × 240 mm;
- current PDF proof: approximately 600 pages.

### English edition

**Title:** *AI: From First Principles to Agentic Systems*  
**Subtitle:** *How AI Actually Works — From LLMs and RAG to Tools, Agents, Evals, and Reliable Systems*  
**Positioning:** *Understand the model. Engineer the context. Connect the tools. Verify the result.*  
**Version:** `0.8-eng`  
**Status:** release candidate

Current manuscript structure:

- introduction;
- 36 numbered chapters;
- 7 appendices;
- 43 diagrams plus print variants;
- approximately 52,000 words;
- current proof format: 170 × 240 mm;
- current PDF proof: approximately 471 pages.

The English edition is intentionally a native-English adaptation rather than a sentence-by-sentence translation.

---

## What changed in the final editorial cycle

### Content and structure

- Both editions were normalized into the same high-level architecture: foundations → models → context → RAG → tools → MCP → agents → agentic systems → enterprise adoption → evaluation → economics → future direction → practical projects.
- The core system thesis was sharpened throughout the manuscript:

> **MODEL ≠ AI APPLICATION ≠ AGENT ≠ AI SYSTEM**

- The reliability principle was made explicit throughout:

> **Generation is powerful. Generation is not a truth guarantee.**

- Agent chapters were aligned around the idea that the model may propose an action, but host software controls whether that action is allowed.
- The analog IC case study was retained as a distinctive engineering example rather than generalized away.

### English content-parity patch

A chapter-by-chapter Czech ↔ English audit found no systemic translation failure. Most of the large page-count difference came from denser English structure, not missing content.

A surgical patch was therefore limited to six chapters:

- Chapter 13 — Second Brain: three-layer `RAW ARCHIVE → KNOWLEDGE → WORKING` model;
- Chapter 15 — MCP: constrained analog-design MCP example and host-side permission boundary;
- Chapter 18 — Multi-Agent Systems: analog-block example and single-agent-first principle;
- Chapter 24 — AI Security: AI literacy as an operating capability;
- Chapter 33 — personal lessons: “What I Would Do Differently” and seven first-page rules;
- Chapter 36 — practical projects: stronger procedures, human-approval triggers, and difficulty progression.

No bulk expansion was applied to the other chapters merely to make the page counts look similar.

### Editorial and mechanical QA

Both editions passed the final manuscript gate for:

- chapter numbering and completeness;
- appendix count;
- index links;
- diagram references;
- placeholder / draft-marker scans;
- long duplicate-paragraph detection;
- current snapshot date consistency;
- PDF page-size consistency;
- extractable text;
- replacement-glyph checks.

### Visual / diagram QA

The diagram set received an explicit visual pass focused on:

- text fitting inside boxes;
- line wrapping;
- collision avoidance with arrows and connectors;
- readable labels;
- consistent visual hierarchy;
- figure placement and captions in the manuscript proofs.

The remaining mandatory production gate is the physical proof on the exact printer / paper / binding combination.

---

## Current publication state

The books should now be treated as **content-locked release candidates**, not as finished commercial print editions.

Still intentionally outside the manuscript content lock:

- final cover / back cover;
- spine width;
- author display / bio decisions;
- title / copyright / ISBN pages;
- Czech tiráž and English imprint layer;
- printer-specific bleed / gutter / binding setup;
- physical proof approval;
- last-minute fact check of fast-moving AI snapshot material.

The release gate and physical-proof procedure are tracked in [`RELEASE_PACKAGE_CHECKLIST.md`](RELEASE_PACKAGE_CHECKLIST.md).

---

## Repository paths

- Czech master: `book_final/`
- English edition: `book_final_eng/`
- Czech proof: `book_final/proof/AI-od-zakladu-k-agentnim-systemum-final-cz.pdf`
- English proof: `book_final_eng/proof/AI-From-First-Principles-to-Agentic-Systems-final-en.pdf`

## Release principle

> **Do not publish a PDF merely because it renders correctly. Publish the exact artifact that passed content QA, visual QA, printer preflight, and physical proof — and record the commit and checksum that produced it.**
