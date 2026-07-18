# Manual Operator Flow

Status: `PUBLIC_MANUAL_STATIC_BASELINE / NO_EXECUTION_AUTHORITY`

## Before starting

Confirm all of the following:

- an explicit human owner exists for the task and final decision;
- the current project source of truth is known;
- the operation is manual/static unless a separate execution Decision says otherwise;
- unknown authority, cost or scope remains a stop, not an inferred permission;
- protocol artifacts will be versioned and retained rather than silently overwritten.

## End-to-end sequence

```text
P01 Context Recovery -> A01 Context Packet
          |                    |
          +-> P02 Evidence Admission -> A02 Evidence Record(s)
          |
          +-> P03 Authority Binding -> A03 Role & Authority Map
                                      |
P04 Decision Before Instruction -> A04 Decision Packet
                                  -> A05 Cost Decision Packet when triggered
                                      |
P05 Execution Handoff -> A06 Execution Handoff
                                      |
P06 Independent Acceptance -> A07 Change & Acceptance Packet
                         or -> A08 Failure & Manual Takeover Record
                                      |
P07 Learning / Promotion -> A09 Learning Candidate Record
```

P02 and P03 may be prepared in parallel after P01. P04 requires accepted inputs from both. A downstream stage must not fabricate a missing upstream acceptance.

## Step 1: recover context

Use [P01](../../02_Protocols/COS_Context_Recovery_Protocol_v0.1.md) and the [A01 template](../../03_Schemas_and_Templates/COS_Context_Packet_Template_v0.1.md).

Record current state, prior Decisions, trusted sources, superseded history, blockers and open questions. Do not create a new Decision in A01.

Stop when required context cannot be recovered without guessing. That is a `legal_stop`, not a failure and not permission to continue.

## Step 2: admit evidence and bind authority

Use [P02](../../02_Protocols/COS_Evidence_Admission_Grounding_Protocol_v0.1.md) with A02 and [P03](../../02_Protocols/COS_Role_Authority_Binding_Protocol_v0.1.md) with A03.

- A02 records what evidence may influence which claim and with what limitation.
- A03 identifies who may propose, decide, execute, accept and take over.
- Identity equality between roles does not automatically grant broader authority.
- Self-review or missing authority must follow the protocol's rejection or stop rules.

## Step 3: decide before instruction

Use [P04](../../02_Protocols/COS_Decision_Before_Instruction_Protocol_v0.1.md) and A04. Use A05 when cost or external capability is triggered.

The authorized human decision owner selects the branch and records scope, rationale, conditions and rejected alternatives. Unknown cost means `no buy / no call / no integration` until resolved.

Do not prepare an executable handoff from a proposal, discussion or AI recommendation alone.

## Step 4: prepare the execution handoff

Use [P05](../../02_Protocols/COS_Execution_Handoff_Permission_Protocol_v0.1.md) and A06.

Bind the accepted Decision, exact target scope, permissions, protected surfaces, cost ceiling, expected evidence, rollback boundary and takeover owner. Every permission not explicitly granted remains false.

This package does not itself authorize an execution. A06 authorizes only the exact scope in its accepted instance.

## Step 5: accept, stop or take over

Use [P06](../../02_Protocols/COS_Independent_Acceptance_Failure_Takeover_Protocol_v0.1.md).

- Use A07 for observed change/result facts and independent acceptance.
- Use A08 for failure, legal-stop consequences, side effects and manual takeover.
- The executor supplies evidence but cannot self-accept solely by assertion.
- A failed invoked stage remains failed; a summary cannot rewrite it as success.
- Retry is never implied by failure. It requires separate authority when allowed.

## Step 6: retain learning without automatic promotion

Use [P07](../../02_Protocols/COS_Learning_Pattern_Promotion_Protocol_v0.1.md) and A09.

Record provenance, limitations, supersession and recommended disposition. A09 is a candidate record, not promotion authority. Promotion or canonical release requires a separate human Decision and Build Log lineage.

## Branch meanings

| Branch | Meaning | Required operator response |
|---|---|---|
| `success` | all invoked required stages satisfy their contracts | preserve evidence and request independent acceptance where applicable |
| `partial_success` | only an explicitly allowed limitation remains | record the limitation; do not generalize the result |
| `legal_stop` | required authority/input/capability is honestly unavailable | stop safely; do not fabricate failure or permission |
| `failed` | an invoked stage violates its contract or encounters a technical/integrity failure | preserve failure facts and route to the named takeover owner |

## Completion checklist

- All artifact IDs and source refs are stable and versioned.
- A03 and A04 remain the sole authority and Decision sources.
- Execution evidence and acceptance are separate.
- Failure, side effects and manual takeover are not hidden.
- Cost and external-call authority are explicit.
- A09 does not claim promotion.
- The final claim does not exceed the accepted evidence scope.
