# Public Review Control Profile

This profile prevents proposal, candidate, and review work from becoming an
open-ended correction loop. It is a public contribution control, not a Host
runtime policy and not authority to continue work.

## Finding buckets

1. `IN_SCOPE_BLOCKER`: violates the frozen contract and has current
   reachability, a concrete wrong outcome, and a bounded correction.
2. `ADJACENT_FINDING`: credible concern governed by a later gate or outside the
   current frozen scope.
3. `OPERATIONAL_HARDENING`: useful resilience work that is not required for the
   current acceptance claim.

Classify every finding as `FROZEN_CONTRACT_VIOLATION`,
`IMPLEMENTATION_DEFECT`, `EVIDENCE_DEFECT`, `REVIEW_DEFECT`, or
`PROPOSED_NEW_REQUIREMENT`. A proposed new requirement is non-blocking until a
human owner versions it into the contract.

## Budgets

- At most two governed candidates per gate.
- At most one independent whole-surface review per candidate.
- At most three in-scope P1 families in one review.
- Review status at two cumulative engineer-hours.
- Automatic pause at four hours without human continuation.
- Hard stop at ten hours without a written human budget override.

Development iterations before a governed candidate do not consume candidate
identities, but they remain subject to the time budget.

## Verdicts

Report these independently:

- `technical_candidate_verdict`;
- `evidence_readiness_verdict`;
- `governance_landing_verdict`.

Incomplete review coverage cannot produce PASS. For an execution-bearing gate,
preflight must not invoke the effective engine and the effective path must
reach exactly one engine traversal. Static-only gates record zero effective
execution instead.

## Stop conditions

Stop and route to a human Decision when Candidate-02 retains a blocker, a new
root-cause family appears after freeze, the contract grows after freeze, proof
independence is missing, authority or ownership is ambiguous, review coverage
is incomplete, or the candidate cannot be explained with a short causal model.

The assessment output is advisory and must fix `work_authorized=false` and
`automatic_retry=false`.
