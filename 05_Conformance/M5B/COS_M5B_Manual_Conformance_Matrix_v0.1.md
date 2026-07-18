# COS M5-B Manual Conformance Matrix v0.1

Repository role: `M5-B IMPLEMENTATION EVIDENCE`  
Conformance mode: `MANUAL / STATIC ONLY`  
Protocols: `COS-P02`, `COS-P04`  
Artifacts: `COS-A02`, `COS-A04`, `COS-A05`  
Runtime / production / cross-host claim: `NONE`

## 1. Qualification contract

Each fixture freezes target schema, expected schema validity, protocol outcome, lifecycle and named assertions. Semantic scenarios must reach their named predicate; unrelated schema failure does not count. The packet-local validator covers only the Draft 2020-12 subset exercised by these schemas and is not a general runtime validator.

## 2. Exact fixture matrix

| Scenario | Fixture | Assertion ID(s) | Schema valid | Expected result |
|---|---|---|---|---|
| `M5B-P02-POS-01` | `M5B-P02-POS-01-evidence-admitted.json` | `M5B-AST-P02-POS-01` | `true` | `success / accepted` |
| `M5B-P02-POS-02` | `M5B-P02-POS-02-evidence-limited-partial.json` | `M5B-AST-P02-POS-02` | `true` | `partial_success / accepted` |
| `M5B-P04-POS-01` | `M5B-P04-POS-01-human-decision-approved.json` | `M5B-AST-P04-POS-01` | `true` | `success / accepted` |
| `M5B-P04-POS-02` | `M5B-P04-POS-02-human-decision-rejected.json` | `M5B-AST-P04-POS-02` | `true` | `success / accepted` |
| `M5B-P04-POS-03` | `M5B-P04-POS-03-human-decision-deferred.json` | `M5B-AST-P04-POS-03` | `true` | `success / accepted` |
| `M5B-P04-POS-04` | `M5B-P04-POS-04-human-decision-needs-information.json` | `M5B-AST-P04-POS-04` | `true` | `success / accepted` |
| `M5B-A05-POS-01` | `M5B-A05-POS-01-known-cost-approved.json` | `M5B-AST-A05-POS-01` | `true` | `success / accepted` |
| `M5B-A05-POS-02` | `M5B-A05-POS-02-known-cost-rejected.json` | `M5B-AST-A05-POS-02` | `true` | `success / accepted` |
| `M5B-A05-POS-03` | `M5B-A05-POS-03-cost-not-applicable-with-analysis.json` | `M5B-AST-A05-POS-03` | `true` | `success / accepted` |
| `M5B-A05-STOP-01` | `M5B-A05-STOP-01-unknown-cost-legal-stop.json` | `M5B-AST-A05-STOP-01` | `true` | `legal_stop / rejected` |
| `M5B-N01` | `M5B-N01-p02-context-not-accepted.json` | `M5B-AST-N01` | `true` | `legal_stop / rejected` |
| `M5B-N02` | `M5B-N02-source-checksum-mismatch.json` | `M5B-AST-N02` | `true` | `failed / rejected` |
| `M5B-N03` | `M5B-N03-evidence-interpretation-conflation.json` | `M5B-AST-N03` | `false` | `failed / rejected` |
| `M5B-N04` | `M5B-N04-ungrounded-item-admitted.json` | `M5B-AST-N04` | `true` | `failed / rejected` |
| `M5B-N05` | `M5B-N05-optional-evidence-limited.json` | `M5B-AST-N05` | `true` | `partial_success / accepted` |
| `M5B-N06` | `M5B-N06-required-evidence-unavailable.json` | `M5B-AST-N06` | `true` | `legal_stop / rejected` |
| `M5B-N07` | `M5B-N07-submitter-self-acceptance.json` | `M5B-AST-N07A, M5B-AST-N07B` | `true` | `legal_stop / rejected` |
| `M5B-N08` | `M5B-N08-excluded-evidence-in-decision-basis.json` | `M5B-AST-N08` | `true` | `failed / rejected` |
| `M5B-N09` | `M5B-N09-context-lineage-mismatch.json` | `M5B-AST-N09` | `true` | `legal_stop / rejected` |
| `M5B-N10` | `M5B-N10-blank-decision-coerced.json` | `M5B-AST-N10` | `true` | `legal_stop / under_review` |
| `M5B-N11` | `M5B-N11-ai-final-decision-owner.json` | `M5B-AST-N11` | `true` | `legal_stop / rejected` |
| `M5B-N12` | `M5B-N12-approved-without-chosen-option.json` | `M5B-AST-N12` | `false` | `failed / rejected` |
| `M5B-N13` | `M5B-N13-decision-boundaries-incomplete.json` | `M5B-AST-N13` | `false` | `failed / rejected` |
| `M5B-N14` | `M5B-N14-decision-authority-mismatch.json` | `M5B-AST-N14` | `true` | `legal_stop / rejected` |
| `M5B-N15` | `M5B-N15-cost-trigger-without-a05.json` | `M5B-AST-N15` | `true` | `legal_stop / rejected` |
| `M5B-N16` | `M5B-N16-unknown-cost-coerced.json` | `M5B-AST-N16` | `false` | `failed / rejected` |
| `M5B-N17` | `M5B-N17-a05-overrides-a04.json` | `M5B-AST-N17` | `false` | `failed / rejected` |
| `M5B-N18` | `M5B-N18-cost-not-applicable-without-analysis.json` | `M5B-AST-N18` | `false` | `failed / rejected` |
| `M5B-N19` | `M5B-N19-unauthorized-downstream-start.json` | `M5B-AST-N19` | `false` | `failed / rejected` |
| `M5B-N20` | `M5B-N20-p04-partial-success.json` | `M5B-AST-N20` | `false` | `partial_success / rejected` |
| `M5B-N21` | `M5B-N21-superseded-decision-used.json` | `M5B-AST-N21` | `true` | `legal_stop / superseded` |
| `M5B-N22` | `M5B-N22-unknown-state-collision.json` | `M5B-AST-N22A, M5B-AST-N22B` | `true` | `failed / rejected` |

## 3. Aggregate reachability

- Stage statuses: completed, skipped, disabled, not_attempted, legal_stop, failed.
- Outcomes: success, partial_success, legal_stop, failed; P04 partial_success is rejected.
- Accepted rejected/deferred/needs_information A04 records have eligibility false.
- Approved A04 is eligible only with current lineage, human authority and a satisfied required cost gate.
- P05 invocation count is always zero; fixture N19 is an invalid attempted-start claim, not a side effect.
- Required P02 gaps cannot reduce to partial success.
- Admission current state derives only from append-only event lineage; N07/N22 cover reviewer/A03 and identity/overwrite failures.

## 4. Candidate-only gate

Qualification requires exact 32 fixture identities/paths, exact 41 ADD + 2 MODIFY + 0 REMOVE, two README preimages, all formal ADD targets absent, protected parity, schema/assertion reachability, candidate hashes and frozen checkpoint. PASS does not authorize repo copy or M5-B start.


## 5. Retry-02 mutation closure

Qualification must reject cross-type identity reuse, acceptance self/mis-binding, accepted-plus-not-decided A04, cost-denied eligibility, reordered or duplicate stages, broken admission lineage and false execution-observation claims. N07 and N22 keep their formal fixture paths and carry bounded variants. The zero-P05 claim is derived from a closed 43-file non-executable candidate inventory and const-false protocol fields; actual runtime invocation remains `not_observed_packet_static`.


## 6. Retry-03 relational and A05 closure

The existing N22 wrapper carries dangling-reference, duplicate/missing projection and basis-derivation variants. The existing approved P04 wrapper now exercises a positive cost-triggered A04 to a supplied accepted A05 plus fabricated, checksum-mismatched, unaccepted, wrong-frame, acceptance-misbound and authority-misbound variants. Formal fixture paths and assertion IDs remain unchanged.


## 7. Retry-04 final bounded closure

N22 additionally rejects cross-claim interpretation and support-link pairing. The approved P04 wrapper additionally rejects decision/evidence role laundering, same-actor wrong binding, authority-source mismatch, expired cost authority and duplicate A05 registry identity. The positive A05 cost-owner tuple remains reachable. Formal fixture paths and assertion IDs remain unchanged. Retry-04 is the final bounded retry under the current proposal.

## 8. Architecture-baseline graph and scope closure

N22 carries empty-union, three overlap, three relation-kind mismatch and duplicate semantic-edge variants; existing cross-claim variants remain. N07 carries missing-policy and missing-tuple legal stops. P02/A04/A05 positive wrappers prove exact allowlisted scopes, while A04/A05 variants reject broader scope, artifact self-allowlist and checksum fraud. Source binding is a pre-freeze packet gate, not an artifact result. Fixture paths remain 32 and assertion IDs remain 36.
