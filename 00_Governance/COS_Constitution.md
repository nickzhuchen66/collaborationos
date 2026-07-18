# CollaborationOS Constitution

Version: `v0.1.0-public-draft`

## 1. Purpose

CollaborationOS governs consequential collaboration among people, AI systems,
specialists, and tools when information and judgment may both be incomplete.
Its purpose is not to make AI appear certain. Its purpose is to make evidence,
authority, action, acceptance, and accountability inspectable.

## 2. Scope

COS is suitable for projects where AI-assisted work may create material
business, technical, financial, legal, operational, or reputational effects.
It is not a replacement for project management, chat, source control, domain
expertise, or final human judgment.

The public baseline is manual/static. Documents and schemas do not grant
authority and do not prove that any automated capability exists.

## 3. Constitutional invariants

1. **Human final authority.** Final consequential decisions belong to an
   identified human role.
2. **Evidence before reliance.** Submitted material is not admitted evidence
   until its source, state, limitations, and acceptance are recorded.
3. **Decision before instruction.** An executable handoff must derive from a
   current accepted decision.
4. **Explicit permission.** Access, writes, spending, external calls,
   irreversible actions, acceptance, retry, and promotion default to false.
5. **Independent acceptance.** A builder or executor cannot accept its own work
   merely by reporting success.
6. **Failure preservation.** Failure, legal stop, rollback, and takeover facts
   are retained without rewriting the earlier business decision.
7. **No implicit retry.** A retry recommendation is not retry authority.
8. **No authority laundering.** Evidence, logs, manifests, learning records,
   and AI recommendations do not become business decisions by relabeling.
9. **Host sovereignty.** Each adopting project retains its own business source
   of truth, owners, permissions, and risk decisions.
10. **Controlled learning.** Reusable learning enters COS as a candidate and
    requires separate review and human promotion authority.

## 4. Four method layers

| Layer | Question |
|---|---|
| Grounding | What is allowed to enter the collaboration as usable evidence? |
| Structure | Which role owns discovery, judgment, review, execution, and acceptance? |
| Defense | How are hallucination, echo, ambiguity, and external deception constrained? |
| Control | Who may decide, authorize, act, accept, stop, retry, or promote? |

## 5. Outcome truth

Protocol stages use only `completed`, `skipped`, `disabled`, `not_attempted`,
`legal_stop`, or `failed`.

Protocol outcomes use only `success`, `partial_success`, `legal_stop`, or
`failed`, reduced in this priority:

```text
invoked failure > legal stop > allowlisted partial success > success
```

Unknown, unavailable, not observed, not attempted, and numeric zero are
different facts. They must not be coerced into one another.

## 6. Accountability

AI may prepare, inspect, compare, challenge, or recommend. It does not become
the final decision owner, independent acceptor, cost owner, takeover owner, or
promotion authority merely because it produced an artifact.

Every consequential action needs a traceable human authority, bounded scope,
current inputs, explicit permission, and an independent acceptance route.

## 7. Change discipline

Core changes must preserve prior versions, identify the affected clauses,
separate implementation evidence from governance acceptance, and avoid
silently widening host or runtime authority.

The public project may evolve through reviewed contributions. A public pull
request is a proposal, not an accepted constitutional change.

