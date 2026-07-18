# COS Decision-Before-Instruction Protocol v0.1

Repository role: `M5-B IMPLEMENTATION ARTIFACT`  
Conformance mode: `MANUAL / STATIC ONLY`  
Release status: `PUBLIC_MANUAL_STATIC_BASELINE`  
Protocol ID: `COS-P04`  
Canonical artifacts: `COS-A04 Decision Packet`; conditional `COS-A05 Cost Decision Packet`  
Depends on: accepted/current A01, A02 and A03 with common A01 lineage  
Runtime / production: `NOT IMPLEMENTED`

## 1. Purpose

P04 records an explicit human Decision before any instruction or execution handoff. It separates accepted record, approved business Decision, downstream eligibility and future execution permission.

## 2. Prerequisites and authority

At protocol start and before A04 acceptance, verify accepted/current A01, A02 and A03 plus common A01 ID/checksum/cutoff. Decision owner and acceptor resolve to authorized humans through accepted A03. AI, CPO, builder, validator and runtime cannot be final Decision authority.

## 3. Exact clauses

`P04-C01 Common accepted lineage`  
Missing, stale, superseded or mismatched prerequisite is a legal stop. Downstream never fabricates acceptance.

`P04-C02 Frozen decision frame`  
Freeze decision_frame_id/checksum over question, alternatives, baseline, scope and deadline before cost evaluation. It excludes A05 result, final chosen option, disposition and acceptance to prevent checksum cycles.

`P04-C03 Qualified evidence basis`  
Basis references only A02 items with derived eligibility true and lists counterevidence, unknowns and accepted limitations. Excluded, unresolved-conflict or ungrounded evidence in basis fails.

`P04-C04 Human authority`  
Decision owner is one A03-bound human in exact scope. Authority mismatch legal-stops; no role name implies permission.

`P04-C05 Lifecycle and disposition separation`  
Artifact lifecycle, acceptance result, business disposition, protocol outcome and technical failure are distinct. Accepted rejected/deferred/needs-information records are valid records but never approved Decisions.

`P04-C06 Consequences and reversal`  
Record rationale, non-goals, consequences, reversal/expiry/supersede conditions. Irreversible Decisions require explicit human reconfirmation.

`P04-C07 A05 cost specialization`  
Cost-triggered frames require A05. A05 references frame ID/checksum and expresses only cost_gate_result. Final A04 references accepted A05 ID/checksum. A05 cannot choose or override the business option.

`P04-C08 Unknown-cost deny-to-act`  
Unknown required price, usage, retry amplification, TCO, migration or exit cost forces effective_cost_allow=false and no buy/no call/no integration. Unknown is not zero or not_applicable.

`P04-C09 Independent acceptance`  
A02/A04/A05 acceptance events bind accepted artifact checksum, acceptor, accepted A03 facts, authority source, time, scope, assertions and result. Preparer, Decision owner and acceptor facts remain separable; exceptions cannot self-approve.

`P04-C10 Decision before instruction and eligibility`  
P04 only computes eligible_for_p05_evaluation. True requires accepted/current/non-expired A04, business approved, valid chosen option, current common lineage and authority, plus accepted A05 approved_within_ceiling/effective allow/no required unknown cost when triggered. Rejected, deferred, needs_information, not_decided, missing/invalid A05 or unknown cost yields false. A04/A05 never creates P05, grants execution or invokes downstream work.

`P04-C11 No partial success`  
P04 outcome is success, legal_stop or failed. Partial success is schema-invalid.

`P04-C12 Supersede and recovery`  
Current selection follows explicit supersede/expiry lineage, never latest filename. Re-open requires new attempt identity, human owner and changed-fact delta. No implicit retry.

## 4. Ordered stages

1. prerequisite_common_lineage;
2. decision_frame;
3. qualified_evidence_basis;
4. authority_separation;
5. cost_gate;
6. human_decision;
7. independent_record_review;
8. a04_a05_acceptance;
9. downstream_eligibility_archive;
10. automated_instruction_generation, fixed disabled.

## 5. Outcome and failure

Reduction is invoked failed > required legal stop > success. Blank/not-decided, missing authority and unknown required cost legal-stop; schema, lineage or authority forgery and unauthorized downstream-start claims fail. Stable secret-safe failure envelope and human takeover apply. Runtime, P05 execution, external calls and production are not implemented.

## 6. Acceptance scope policy reference

Policy owner path: `02_Protocols/COS_Evidence_Admission_Grounding_Protocol_v0.1.md`  
Policy owner SHA-256: `e57dfaeae2bff00377a09058b8e9b7efb696ccec72824eb9b623ac46bb310d9d`  

P04 consumes the P02-owned closed policy by exact path and checksum. It does not carry a second policy table. A missing owner, checksum mismatch or unknown tuple legal-stops acceptance; an artifact scope outside the exact allowed set fails acceptance integrity and forces P05 eligibility false.
