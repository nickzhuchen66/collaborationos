---
name: cos-decision-packet-preparation
description: Prepare or inspect a COS A04 Decision Packet that separates accepted evidence, human authority, business disposition, cost gating, record acceptance, and downstream eligibility. Use when a material project fork needs an explicit human Decision before any instruction or execution handoff.
---

# COS Decision Packet Preparation

Prepare an A04 draft. A recommendation is not a Decision, and an accepted
Decision record is not execution permission.

## Procedure

1. Read `references/contract.md` and verify its source bindings.
2. Verify accepted/current A01, A02, and A03 share exact A01 identity, checksum, and cutoff lineage.
3. Resolve the Decision owner through A03 to a human `decision_owner` binding in the exact scope.
4. Freeze the question, alternatives, baseline, scope, non-scope, and deadline.
5. Include only eligible A02 evidence; preserve counterevidence, unknowns, and accepted limitations.
6. Record one disposition: approved, rejected, deferred, needs-information, or not-decided.
7. If a cost trigger exists, require a separately accepted A05. This Skill does not create A05.
8. Record reversal, expiry, supersede, consequences, and non-goals.
9. Derive P05 evaluation eligibility without starting P05.
10. Produce a JSON A04 draft, run the public validator, and stop for independent record acceptance.

## Output boundary

Return the A04 draft or findings, the human Decision gate, and any missing A05
prerequisite. State `p05_started=false`, `instruction_generated=false`,
`execution_authorized=false`, and `external_calls=0` unless separately
observed outside this Skill.

Never choose for the human, fabricate acceptance, start execution, or turn
eligibility into permission.
