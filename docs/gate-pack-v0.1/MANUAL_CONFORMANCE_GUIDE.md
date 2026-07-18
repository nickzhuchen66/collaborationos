# Manual Conformance Guide

Status: `PUBLIC_MANUAL_STATIC_BASELINE / NO_AUTOMATED_VALIDATOR`

## Available matrices

| Wave | Matrix | Coverage |
|---|---|---|
| M5-A | [`COS_M5A_Manual_Conformance_Matrix_v0.1.md`](../../05_Conformance/M5A/COS_M5A_Manual_Conformance_Matrix_v0.1.md) | 26 fixtures; context and authority |
| M5-B | [`COS_M5B_Manual_Conformance_Matrix_v0.1.md`](../../05_Conformance/M5B/COS_M5B_Manual_Conformance_Matrix_v0.1.md) | 32 fixtures; evidence, decision, and cost |
| M5-C | [`COS_M5C_Manual_Conformance_Matrix_v0.1.md`](../../05_Conformance/M5C/COS_M5C_Manual_Conformance_Matrix_v0.1.md) | 36 fixtures; handoff, acceptance, and takeover |
| M5-D | [`COS_M5D_Manual_Conformance_Matrix_v0.1.md`](../../05_Conformance/M5D/COS_M5D_Manual_Conformance_Matrix_v0.1.md) | 32 fixtures; learning and promotion boundaries |

## Manual review method

For each fixture:

1. confirm the fixture is synthetic and contains no host payload;
2. identify the target protocol, artifact, stage, and expected outcome;
3. validate the JSON instance against the relevant public schema;
4. follow the matrix predicates in order;
5. confirm the first failure or legal stop occurs at the expected stage;
6. confirm downstream stages remain `not_attempted` when required;
7. confirm permissions, side effects, rollback, takeover, retry, and promotion
   are not widened by the result;
8. record disagreements as review findings rather than editing expected truth
   during the review.

## Claim boundary

The fixtures document expected behavior. They are not proof of an executable
validator. A manual reviewer may report schema or matrix conformance, but may
not report runtime enforcement or production readiness.

## Extending fixtures

New fixtures should use synthetic identities, stable IDs, one primary negative
per case, explicit expected stage/outcome, and no secrets. A proposed fixture
does not change a protocol until the protocol and matrix change are separately
reviewed.

