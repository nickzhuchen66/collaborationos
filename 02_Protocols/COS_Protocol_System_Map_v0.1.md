# COS Protocol System Map v0.1

Status: `PUBLIC_MANUAL_STATIC_BASELINE`

## 1. Protocol inventory

| ID | Protocol | Primary output |
|---|---|---|
| P01 | Context Recovery | A01 Context Packet |
| P02 | Evidence Admission and Grounding | A02 Evidence Record |
| P03 | Role and Authority Binding | A03 Role/Authority Map |
| P04 | Decision Before Instruction | A04 Decision Packet and optional A05 cost packet |
| P05 | Execution Handoff and Permission | A06 Execution Handoff |
| P06 | Independent Acceptance, Failure, and Takeover | A07 acceptance and optional A08 failure record |
| P07 | Learning, Pattern, and Promotion | A09 Learning Candidate Record |

## 2. Dependency order

```text
P01 -> P02 -> P03 -> P04 -> P05 -> P06 -> P07
```

P02 and P03 may inspect the same accepted A01, but neither may fabricate the
other's result. P05 requires accepted decision and authority inputs. P06 does
not accept an implementation merely because P05 completed. P07 cannot promote
its own recommendation.

## 3. Shared stage vocabulary

- `completed`
- `skipped`
- `disabled`
- `not_attempted`
- `legal_stop`
- `failed`

Top-level outcomes are `success`, `partial_success`, `legal_stop`, or `failed`.
The reduction priority is invoked failure, then legal stop, then explicitly
allowed partial success, then success.

## 4. Shared failure envelope

A failure or legal stop records a machine-readable code, safe public message,
retryability, side-effect truth, last safe checkpoint, takeover requirement,
owner role, and evidence references. Business disposition remains separate
from technical error.

## 5. Cross-protocol invariants

1. final consequential authority remains human;
2. instruction follows a current accepted decision;
3. permissions default to false;
4. acceptance is independent of execution;
5. missing information is not coerced to zero;
6. failure history and supersession remain append-only;
7. host business payload remains outside COS core;
8. retry and promotion require separate authority;
9. manual conformance does not imply executable enforcement.

## 6. Manual use

Use the [Manual Operator Flow](../docs/gate-pack-v0.1/MANUAL_OPERATOR_FLOW.md)
and select artifacts from the
[Gate Pack Artifact Register](../03_Schemas_and_Templates/COS_Gate_Pack_Artifact_Register_v0.1.md).

