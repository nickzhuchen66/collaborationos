# COS A04 Decision Packet Template v0.1

Repository role: `M5-B IMPLEMENTATION ARTIFACT`  
Schema: `COS_Decision_Packet_v0.1.schema.json`  
Owner protocol: `COS-P04`  
Conformance: `MANUAL / STATIC ONLY`

## Identity and Common Lineage
- Artifact ID / lifecycle / created at:
- Accepted/current A01, A02 and A03 IDs/checksums/cutoffs:
- Shared A01 lineage verification at start and pre-accept:

## Frozen Decision Frame
- Frame ID/checksum:
- Question / alternatives / baseline:
- In/out scope / deadline:

## Qualified Basis
- Eligible A02 evidence item IDs:
- Counterevidence / unknowns / accepted limitations:
- Confirm excluded, conflicted-unresolved and ungrounded items are absent:

## Authority and Decision
- Human Decision owner and accepted A03 binding:
- Business disposition: approved / rejected / deferred / needs_information / not_decided:
- Chosen option or not_applicable:
- Rationale / non-goals / consequences:
- Reversal / expiry / supersede / current state:

## Cost Gate
- Triggered? A05 ID/checksum or explicit not_applicable:
- Cost-gate result / effective allow / required unknown count:

## Acceptance and Downstream Eligibility
- Acceptance event with artifact checksum, human/A03/authority/time/scope/assertions:
- Derived eligible_for_p05_evaluation:
- Confirm eligibility is not permission or invocation and p05_started remains false:

## Protocol Run
Record all ten stages; automated_instruction_generation is disabled. P04 has no partial success. Include secret-safe failure envelope and takeover for non-success.


## Retry-02 mechanical integrity

- Record `preparer_actor_id`; it must differ from the authorized human acceptance actor.
- Accepted lifecycle requires an explicit business disposition. Eligibility is recomputed from chosen-option membership, current common lineage, accepted human authority and the complete cost-gate truth table.
- Acceptance binds the exact A04 artifact ID and canonical body checksum. Eligibility never creates P05 or execution authority.


## Retry-03 real A05 binding

- When cost-triggered, qualification must receive the referenced A05 object and verify its exact canonical body checksum.
- A05 must be accepted, pass schema/acceptance/A03 cost-authority checks, bind the same decision-frame ID/checksum, approve within ceiling, allow effectively and contain no required unknown cost.
- A syntactically valid A05 ID/checksum without the verified object never creates eligibility.


## Retry-04 exact authority and registry binding

Cost eligibility consumes A05 only after exact cost-owner actor, kind, role, binding, governed scope, authority source and current validity match a frozen accepted A03 fact. Duplicate related-artifact identity fails before registry construction.

## Architecture-baseline acceptance scope

Acceptance uses the P02-owned policy at `02_Protocols/COS_Evidence_Admission_Grounding_Protocol_v0.1.md`. A03 remains the sole authority source; the policy only narrows the allowed acceptance action. Missing policy or tuple legal-stops; broader or self-asserted scope fails and keeps P05 eligibility false.
