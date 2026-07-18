# Synthetic Manual/Static Walkthrough

This example uses a fictional project, `Northstar Docs`, to show the COS
sequence without exposing a real host or claiming executable enforcement.

## Scenario

Northstar Docs wants an AI builder to update a public documentation index. The
change is local, reversible, and has no external call or paid capability. A
human Vision Owner makes the decision; a separate human reviewer accepts or
rejects the result.

## Actors

| Functional role | Synthetic actor |
|---|---|
| Vision Owner / Decision Owner | `human-owner-01` |
| Context Owner | `human-owner-01` |
| Evidence Submitter | `ai-researcher-01` |
| Evidence Acceptor | `human-reviewer-01` |
| Builder | `ai-builder-01` |
| Independent Acceptor | `human-reviewer-01` |
| Takeover Owner | `human-owner-01` |

Identity equality is not authority. The role map is the authority source.

## Positive branch

1. **P01/A01:** record the repository version, requested index, current files,
   exclusions, and cutoff time.
2. **P02/A02:** admit the current index and target document as local evidence;
   exclude unrelated drafts.
3. **P03/A03:** bind the builder to one file modification; all external calls,
   spending, host access, promotion, retry, and irreversible action remain
   false.
4. **P04/A04:** the Vision Owner chooses “update one index entry.”
5. **P04/A05:** mark cost as not applicable only after recording that no cost
   trigger exists.
6. **P05/A06:** hand off the exact preimage, postcondition, allowed path, stop
   rules, and rollback owner.
7. **P06/A07:** the independent acceptor compares the result with the accepted
   decision and either accepts or rejects it.
8. **P07/A09:** optionally record a de-identified learning candidate such as
   “index changes should bind the target document hash.” This does not modify
   COS core.

Expected protocol outcome: `success` only if all invoked stages pass and A07 is
accepted by the independent human role.

## Legal-stop branch

Immediately before handoff, the target preimage no longer matches A01.

- P05 outcome: `legal_stop`;
- execution: `not_attempted`;
- A07: not fabricated;
- retry: false until a new human decision authorizes a new attempt.

## Failure/takeover branch

The builder starts an authorized local write, then reports an ambiguous
replacement owned by another process.

- protocol outcome: `failed`;
- A08 records the primary error, observed side effect, last safe checkpoint,
  rollback ambiguity, and takeover owner;
- destructive rollback is prohibited without ownership proof;
- manual takeover is required;
- the original business decision is not rewritten as rejected merely because
  execution failed.

## Related public fixtures

- Context/authority: `05_Conformance/M5A/fixtures/`
- Evidence/decision/cost: `05_Conformance/M5B/fixtures/`
- Handoff/acceptance/takeover: `05_Conformance/M5C/fixtures/`
- Learning/promotion: `05_Conformance/M5D/fixtures/`

The fixture directories contain machine-readable synthetic cases. The matrices
describe their expected manual outcomes.

