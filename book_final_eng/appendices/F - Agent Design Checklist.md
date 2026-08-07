---
title: "F. Agent Design Checklist"
part: "APPENDICES"
status: international-draft
version: "0.8-eng"
updated: 2026-08-08
---

# F. Agent Design Checklist

Use this checklist before a prototype becomes an agentic system with real permissions.

## Task

- [ ] What is the exact goal?
- [ ] What is the non-AI baseline?
- [ ] What counts as success?
- [ ] Which cases must return `UNKNOWN`, refuse, or escalate?

```text
INPUT → PROCESS → OUTPUT → SUCCESS CRITERIA
```

## Inputs and Context

- [ ] What information is required?
- [ ] Which sources are authoritative?
- [ ] How is the current revision resolved?
- [ ] What happens when input is missing or sources conflict?
- [ ] Is context limited intentionally?

## Model

- [ ] Which capabilities are actually required?
- [ ] Have at least two candidates been benchmarked?
- [ ] Is a smaller/cheaper/local model sufficient?
- [ ] Does structured output work reliably?
- [ ] Is tool calling good enough on our eval set?
- [ ] Is exact model/version recorded?

## Tools

For every tool:

- [ ] Why is it needed?
- [ ] Is the schema narrow?
- [ ] Are arguments validated?
- [ ] Is retry safe/idempotent?
- [ ] Is the error contract explicit?
- [ ] Is there a timeout?
- [ ] Can it be tested outside production?

## Permissions

- [ ] What may be read?
- [ ] What may be written?
- [ ] Is write scope narrow?
- [ ] Are read/write credentials separated?
- [ ] Is internet access necessary?
- [ ] Can it send external communication?
- [ ] Is admin/root access truly necessary?

> **Give the agent the smallest action space in which it can still achieve the goal.**

## State and Memory

- [ ] Does the run need persistent state?
- [ ] Is long-term memory actually necessary?
- [ ] What is stored and for how long?
- [ ] Does memory include provenance/time?
- [ ] How are stale facts superseded?
- [ ] How do we avoid turning one model mistake into permanent memory?

## Loop and Stop Conditions

- [ ] How does the agent know it is done?
- [ ] Maximum steps?
- [ ] Time limit?
- [ ] Token/cost budget?
- [ ] Repeated-state/loop detection?
- [ ] Human escalation condition?

## Verification

- [ ] What can be checked deterministically?
- [ ] Schema validation?
- [ ] Unit/rule checks?
- [ ] External test/simulator?
- [ ] LLM judge only where deterministic checks are insufficient?
- [ ] Human review where required?

Preferred order:

```text
schema → rules → external verifier → LLM review → human review
```

## Approval

- [ ] Which actions require approval?
- [ ] Does the approver see action, rationale, evidence, and diff?
- [ ] Can the action be rejected or modified?
- [ ] Is approval recorded?

## Observability and Evals

- [ ] Every run has an ID?
- [ ] Model/workflow versions recorded?
- [ ] Retrieval and tool calls inspectable?
- [ ] Representative test set?
- [ ] Edge, missing-data, conflicting-data, and injection cases included?
- [ ] End-to-end success, cost, and latency measured?

## Failure Handling

- [ ] What happens when the model fails?
- [ ] What happens when a tool times out?
- [ ] Is retry safe?
- [ ] Is there a fallback or `UNKNOWN` state?
- [ ] Can the system terminate safely without producing an answer?

## Production Readiness

Before production I want **yes** on at least:

1. [ ] Use case precisely defined.
2. [ ] Baseline measured.
3. [ ] Eval set exists.
4. [ ] Permissions are minimal.
5. [ ] Output is verified.
6. [ ] Critical actions require approval.
7. [ ] Every run is auditable.
8. [ ] Failure behavior is safe.
9. [ ] Rollback / kill switch exists.
10. [ ] Operating cost is understood.

“I don’t know” is not automatically a reason to cancel the project. It is a blocker to resolve before increasing autonomy.