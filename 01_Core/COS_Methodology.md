# CollaborationOS Methodology

Version: `v0.1.0-public-draft`

This document turns the Constitution into an operating method. It is deliberately
domain-neutral and uses synthetic role names.

## 1. Grounding layer

### 1.1 Define before relying

Before a term, claim, dataset, or recommendation becomes a decision input,
record what it means, where it came from, its current state, and what would
disprove or limit it.

### 1.2 Separate source, fact, interpretation, and decision

COS keeps four truths distinct:

1. source-local claim;
2. observed or reproducible fact;
3. interpretation or recommendation;
4. human decision.

Identity equality between a submitter and an authorized owner grants nothing.
Missing or unavailable required evidence normally produces a legal stop;
invalid or contradictory evidence normally produces failure.

### 1.3 Grounding is not final judgment

Grounding establishes eligibility for consideration. It does not make a claim
true, complete, current, or sufficient for a consequential decision.

## 2. Structure layer

### 2.1 Functional roles

| Role | Primary responsibility |
|---|---|
| Vision Owner | final direction and consequential decision |
| Domain Evidence Owner | first-hand or authoritative domain facts |
| Reviewer | challenge, conformance review, and boundary detection |
| Builder | bounded implementation or artifact construction |
| Executor | authorized action within an exact scope |
| Independent Acceptor | acceptance or rejection independent of execution |
| Takeover Owner | human resolution after ambiguous or unsafe failure |

One person may hold multiple roles only when the relevant protocol permits it
and independence is not required. Role participation is not role authority.

### 2.2 Persist four kinds of state

Projects should keep decisions, current progress, deferred work, and reusable
learning in distinct durable locations. Material changes should update every
affected location rather than relying on conversational memory.

### 2.3 Handoff is a contract

An execution handoff identifies accepted inputs, exact operations, permissions,
preconditions, expected postconditions, stop rules, rollback ownership, and the
independent acceptance route. A summary or chat instruction is not equivalent.

## 3. Defense layer

### 3.1 Mechanize honesty where possible

Facts that can be computed, parsed, hashed, enumerated, or compared should be
handled by deterministic mechanisms. AI may interpret results, but should not
invent values that a mechanism can derive.

### 3.2 Prevent echo from becoming validation

Repeated agreement from dependent agents or shared sources is not independent
confirmation. Record source dependence, reviewer independence, and the limits
of consensus.

### 3.3 Preserve uncertainty

Use explicit states for unknown, unavailable, not observed, not applicable,
stale, rejected, and superseded. Do not use `0`, `false`, or an empty string as
a substitute unless the schema defines that exact meaning.

### 3.4 Treat external capability as a lifecycle cost

Before adopting a paid tool, model, service, or locked platform, compare total
cost, alternatives, exit path, data exposure, retry amplification, and who owns
the consequence. Unknown required cost means no buy, call, or integration.

## 4. Control layer

### 4.1 Scale autonomy to consequence

Low-impact reversible preparation may be delegated. Consequential, paid,
external, irreversible, or authority-changing action requires explicit human
confirmation. Autonomy is scoped per action, not granted as a broad identity
property.

### 4.2 Decision precedes instruction

The sequence is:

```text
context -> evidence -> authority -> human decision -> cost gate when needed
-> execution handoff -> execution evidence -> independent acceptance
-> failure/takeover when needed -> learning candidate
```

Later artifacts cannot retroactively authorize earlier action.

### 4.3 Failure is an outcome, not an embarrassment

A failure record preserves the primary error, ordered secondary errors, last
safe checkpoint, observed side effects, rollback truth, manual takeover need,
and retryability. Cleanup must not erase evidence or claim ownership of foreign
state.

### 4.4 Learning is gated

Reusable observations are de-identified, source-bound, reviewed, and assigned
an evidence maturity. Recommendation does not modify canonical COS material.

## 5. Eight common failure modes

1. fabricated or weakly grounded content;
2. AI decision overreach;
3. dependent agreement presented as validation;
4. external deception or source ambiguity;
5. inflated, coerced, or context-free data;
6. context and decision loss across time;
7. responsibility transferred to a system;
8. hidden lifecycle cost and tool lock-in.

## 6. Manual/static operating rule

The public baseline is usable by people without runtime software. Operators
prepare the A01-A09 artifacts, follow P01-P07, and inspect fixtures and matrices
manually. Passing a manual check does not claim automated enforcement.

