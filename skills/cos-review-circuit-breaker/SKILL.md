---
name: cos-review-circuit-breaker
description: Classify review findings, separate technical/evidence/governance verdicts, enforce candidate and time budgets, and recommend stop, reset, defer, or next-gate routing under COS review controls. Use when proposal, candidate, review, retry, or development work risks becoming an open-ended correction loop.
---

# COS Review Circuit Breaker

Assess process state. Do not authorize work or manufacture the subject's
expected oracle.

## Procedure

1. Read `references/contract.md`, verify its public source binding, and identify the exact current gate and frozen matrix version.
2. Record development status, governed candidate number, review count, and cumulative elapsed engineer-hours.
3. Separate findings into in-scope blockers, adjacent findings, and operational hardening.
4. Classify each finding as contract violation, implementation defect, evidence defect, review defect, or proposed new requirement.
5. Admit a blocker only when it names the frozen row, current reachability, wrong outcome, and bounded correction.
6. Keep technical, evidence-readiness, and governance-landing verdicts separate.
7. Run the deterministic circuit assessment with observed facts. A renamed packet cannot reset budgets.
8. If tripped, recommend only the returned stop, reset, or defer route.
9. Report reviewed and unreviewed surfaces, remaining uncertainty, and correction-log references.
10. Stop for a human continuation Decision.

## Output boundary

Return an assessment with reasons, one recommended next action, allowed and
forbidden actions, `work_authorized=false`, and `automatic_retry=false`.

Never construct a candidate, change the frozen contract, convert hardening into
a blocker, or grant a reduced-assurance exception.
