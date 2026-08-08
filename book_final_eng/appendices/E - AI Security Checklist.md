---
title: "E. AI Security Checklist"
part: "APPENDICES"
status: release-candidate
version: "0.8-eng"
updated: 2026-08-08
---

# E. AI Security Checklist

Use this checklist before a pilot and before production. It does not replace current legal, privacy, security, or jurisdiction-specific review.

## Data and Identity

- [ ] Are data classes defined: PUBLIC / INTERNAL / CONFIDENTIAL / RESTRICTED?
- [ ] Do inputs contain personal data, trade secrets, source code, or customer data?
- [ ] Does every important source have an owner and authoritative version?
- [ ] Is retrieval filtered by user identity/authorization before context assembly?
- [ ] Is data minimized to what the task actually needs?
- [ ] Is long-term memory policy explicit?

## Cloud Policy

- [ ] Is the specific provider and specific product/plan approved?
- [ ] Do we know current training/use-of-data terms?
- [ ] Do we know retention and processing locations?
- [ ] Is the required enterprise/DPA framework in place?
- [ ] Is cloud fallback explicit rather than silent?

## Privacy and Governance

- [ ] Is the processing purpose defined?
- [ ] Are retention/deletion and access rules defined?
- [ ] Are logs and traces included in privacy review?
- [ ] Is the accountable system owner defined?
- [ ] Is the use case risk-classified?
- [ ] Are transparency and human-oversight obligations implemented where applicable?
- [ ] For EU use, have relevant AI Act/GDPR roles and obligations been reviewed?
- [ ] For other jurisdictions, has current local/sector review been performed?

## Model Policy

- [ ] Exact model/version recorded?
- [ ] Source/license/hash recorded for open-weight models where practical?
- [ ] Model approved for the relevant data class?
- [ ] Eval set exists?
- [ ] Upgrade and rollback behavior defined?

## Tool Permissions

For every tool:

- [ ] What may it read?
- [ ] What may it write?
- [ ] Is scope limited to required service/project/directory?
- [ ] Are arguments validated?
- [ ] Does it have timeout and rate/call limits?
- [ ] Is tool output treated as data rather than trusted policy?

## Secrets

- [ ] No credentials directly in prompts?
- [ ] No secrets stored in agent memory?
- [ ] Can tool runtime use credentials without exposing them to the model?
- [ ] Are secrets rotatable?
- [ ] Are logs redacted appropriately?

## Prompt Injection

- [ ] Trusted instructions separated from untrusted content?
- [ ] Direct prompt injection tested?
- [ ] Indirect injection from web/PDF/email/RAG tested?
- [ ] Can document content expand permissions? It should not.
- [ ] Is tool policy enforced outside the model?

## Human Approval

Require appropriate approval especially for:

- [ ] destructive writes,
- [ ] production configuration changes,
- [ ] publish/release actions,
- [ ] external communication,
- [ ] financial transactions,
- [ ] critical engineering artifacts,
- [ ] actions with significant legal or safety impact.

Approval should show what will happen, why, which evidence was used, what data changes, and how to roll back.

## Audit and Observability

- [ ] Every run has an ID?
- [ ] Model/workflow versions recorded?
- [ ] Tool calls and status recorded?
- [ ] Source provenance recoverable?
- [ ] Sensitive content minimized in logs?
- [ ] Audit trail access-controlled?
- [ ] Latency, error rate, success, and cost measured?

## Supply Chain and Production

- [ ] Dependencies pinned and trusted?
- [ ] Container images controlled?
- [ ] Remote custom code reviewed/disabled as appropriate?
- [ ] MCP servers/plugins reviewed like other integrations?
- [ ] Accountable owner and support path?
- [ ] Kill switch and rollback?
- [ ] Cost/rate limits?
- [ ] Incident process?
- [ ] Regression eval before release?

## Ten-Question Threat Model

1. What are we protecting?
2. Who can influence the input?
3. What can the agent read?
4. What can it modify?
5. Where can it send data?
6. Which secrets does the runtime use?
7. What happens under prompt injection?
8. What requires approval?
9. How do we roll back?
10. What appears in the audit trail?

> **Agent security is not one filter. It is the combined design of identity, data authorization, tool policy, sandboxing, verification, approval, and audit.**