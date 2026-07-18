# COS New Host Project Adoption Manual v0.1

Status: `PUBLIC_ADOPTION_GUIDE / MANUAL_STATIC / NO_AUTOMATIC_AUTHORITY`

Applies to: new or existing projects that want to use the CollaborationOS manual/static Gate Pack.

Does not imply: M6 evidence, cross-host validation, Skill/runtime installation, public release or production readiness.

## 1. Intended result

After completing this manual, a host project should have:

1. one stable pointer to the canonical CollaborationOS project;
2. one human-approved adoption record defining scope and limits;
3. one Host Adapter mapping host roles and files to COS functions;
4. one initial Context Packet and Role/Authority Map;
5. a location for host-owned A01-A09 instances and evidence;
6. a rehearsed Decision-Only path;
7. explicit failure, takeover, learning and version-upgrade routes.

The host does not receive permission to act merely by completing these documents.

## 2. Adoption principles

### 2.1 Reference, do not fork

CollaborationOS remains the canonical owner of COS protocols, schemas, templates and maturity rules. A host project references a pinned COS baseline. It does not copy the COS Core and start editing a private fork.

### 2.2 Host owns host truth

The host project continues to own its business state, source of truth, Roadmap, data, secrets and Decisions. COS provides collaboration contracts and artifacts, not business authority.

### 2.3 Adapter, do not contaminate Core

Host-specific roles, ontology, lifecycle and business rules belong in the Host Adapter or a Domain Extension. They do not enter COS Core merely because one project uses them.

### 2.4 Prepare, then decide

AI may prepare or challenge Context, Evidence, Authority, Decision and Handoff artifacts. Final Decision, acceptance, takeover and promotion remain human actions.

### 2.5 Start with no execution

A new host first rehearses `Decision-Only`. Governed Change is adopted only after context and authority mappings have been checked. No host should begin by automating P05/P06.

## 3. Adoption levels

| Level | Name | Use | Required host artifacts | Does not include |
|---|---|---|---|---|
| `L0` | Reference | use COS principles during discussion | entry pointer | formal COS artifact lifecycle |
| `L1` | Decision Governance | recover context, admit evidence, bind authority and record Decisions | pointer, adoption record, Host Adapter, A01-A05 area | execution handoff or acceptance claims |
| `L2` | Governed Change | use P01-P06 for bounded project changes | all L1 artifacts plus A06-A08 and independent acceptor | automatic execution, retry or promotion |
| `L3` | Learning Bridge | return redacted learning to independent COS | all L2 artifacts plus learning submission route and A09 | automatic Core promotion |

Recommended default for a new project: adopt `L1`, complete one historical rehearsal, then separately decide whether to advance to `L2`.

## 4. Preconditions

Do not begin adoption until these facts are available:

- named human project owner;
- known host source-of-truth files;
- known location for Decisions and execution evidence;
- named authority owner for permissions and costs;
- a candidate independent acceptor distinct from implementation self-report;
- a takeover owner for failure or ambiguity;
- permission to create host-local governance documentation;
- no requirement to expose secrets or restricted business payloads to COS.

Missing required authority is a `legal_stop`, not a reason to invent a role.

## 5. Canonical COS baseline to pin

At adoption time, record exact paths and SHA-256 values for at least:

- `docs/gate-pack-v0.1/README.md`;
- `docs/gate-pack-v0.1/PACKAGE_MANIFEST.json`;
- `docs/gate-pack-v0.1/MANUAL_OPERATOR_FLOW.md`;
- `docs/gate-pack-v0.1/ARTIFACT_SELECTION_AND_OWNERSHIP.md`;
- `02_Protocols/COS_Protocol_System_Map_v0.1.md`;
- the A01-A09 schemas used by the adopted level;
- `05_Conformance/COS_Evidence_Maturity_Model.md`;
- `UNAVAILABLE_IN_PUBLIC_V0.1`: governed-candidate review control requires a separately supplied public contract and is not part of this release. It is optional and must not block the manual/static adoption path documented here.

Same-workspace hosts should reference canonical paths directly. A host on another machine may use an internally distributed read-only snapshot with a manifest and checksums. That snapshot is a pinned dependency, not a new COS authority.

## 6. Suggested host layout

Folder names may follow the host's conventions, but ownership must remain explicit. A simple layout is:

```text
<host-project>/
  governance/
    cos/
      COS_HOST_ENTRY_POINTER.md
      COS_HOST_ADOPTION_RECORD.md
      COS_HOST_ADAPTER.md
      artifacts/
        A01_context/
        A02_evidence/
        A03_authority/
        A04_decisions/
        A05_cost/
        A06_handoffs/
        A07_acceptance/
        A08_failure_takeover/
        A09_learning/
      evidence/
      rehearsals/
      learning_submissions/
```

Do not force this layout onto a project with established governance directories. The Host Adapter must instead map the established locations to A01-A09 roles.

## 7. Phase A: establish the entry pointer

1. Copy and fill [Host Entry Pointer Template](templates/COS_HOST_ENTRY_POINTER_TEMPLATE_v0.1.md).
2. Add a short reference in the host's agent instructions and context handoff.
3. State that COS is read-only from the host's perspective.
4. Record adopted level and pinned package identity.
5. State that host business truth remains host-owned.

The entry pointer should be short. It routes operators to the adoption record and Host Adapter; it does not duplicate the entire COS manual.

## 8. Phase B: approve the adoption record

Use [Host Adoption Record Template](templates/COS_HOST_ADOPTION_RECORD_TEMPLATE_v0.1.md).

The record must define:

- adoption level and purpose;
- included and excluded project surfaces;
- human adoption owner;
- source-of-truth precedence;
- allowed artifact locations;
- whether external calls, spending or execution are in scope;
- independent acceptance and takeover ownership;
- claim ceiling;
- exit and version-upgrade rules.

For initial `L1` adoption, set all execution, external-call, spending, retry, promotion and canonical-write permissions to false.

## 9. Phase C: recover context and bind authority

### 9.1 Prepare A01

Use P01 and the canonical A01 template to record:

- current phase and objective;
- authoritative project files;
- prior Decisions and superseded history;
- known blockers and unknowns;
- protected surfaces;
- current external-call and cost truth.

Do not use A01 to create a new business Decision.

### 9.2 Prepare A03

Use P03 and the canonical A03 template. Map at least:

- project owner;
- context preparer/reviewer;
- evidence submitter/admission reviewer;
- decision owner;
- cost owner;
- executor/builder;
- independent acceptor;
- takeover owner;
- learning/promotion owner.

One person may hold multiple functions only when the accepted authority map explicitly allows it. Identity equality grants no additional permission.

## 10. Phase D: create the Host Adapter

Use [Host Adapter Template](templates/COS_HOST_ADAPTER_TEMPLATE_v0.1.md).

The Adapter must answer:

1. Which host files carry context, formal truth, Decisions, roadmap state and execution evidence?
2. Which host role maps to each COS function?
3. Which COS protocols are applicable, not applicable or already supported by an existing host mechanism?
4. Which host-specific rules remain Domain Extension material?
5. How are conflicts between COS and host authority resolved?
6. Where do failure evidence, manual takeover and learning submissions go?
7. Which permissions are explicitly false?

The Adapter translates. It cannot alter COS Core or host business facts.

## 11. Phase E: perform a historical Decision-Only rehearsal

Choose one completed, low-sensitivity host Decision. Do not reopen or rewrite it.

Reconstruct, using historical facts only:

1. A01 context as known at that time;
2. A02 admitted and excluded evidence;
3. A03 authority map;
4. A04 Decision and optional A05 cost branch;
5. expected legal-stop and failed variants.

Check whether COS would have:

- identified the same decision owner;
- excluded unavailable or ungrounded evidence;
- prevented instruction before Decision;
- preserved unknown cost as no-call/no-buy;
- avoided rewriting historical truth.

Label the result `HISTORICAL_MANUAL_REHEARSAL`. It is not live execution, cross-host validation or M6 evidence.

## 12. Phase F: authorize the first live Decision-Only use

The project owner separately decides whether to use COS on one current Decision.

Allowed sequence:

```text
A01 Context
  -> A02 Evidence + A03 Authority
  -> human A04 Decision
  -> optional A05 Cost Decision
  -> stop
```

Do not produce A06 or begin implementation as part of the first Decision-Only exercise. Record friction, missing mappings and unnecessary ceremony as host-local observations.

## 13. Phase G: optional L2 governed-change adoption

Advance to L2 only through a separate host Decision after L1 has worked in practice.

For each governed change:

1. refresh or reference accepted A01-A05;
2. create A06 with exact target scope, permission, protected surfaces, evidence, rollback and takeover owner;
3. execute only through the host project's separately authorized implementation mechanism;
4. preserve observed result evidence;
5. route to an independent acceptor;
6. create A07 for result and acceptance truth, or A08 for failure/legal-stop/takeover truth;
7. do not retry without a separate Decision.

COS artifacts do not replace the host's Change Packet, pull request, test suite, deployment system or business approval. The Adapter links them.

## 14. Failure handling

When a stage fails or reaches a legal stop:

- stop downstream dispatch;
- preserve the first failure and last safe checkpoint;
- record side effects and affected surfaces;
- distinguish business outcome from technical error;
- identify the takeover owner;
- record whether retry is allowed, prohibited or not yet decided;
- never convert a failure to partial success because a later summary completed.

If ownership, source truth or rollback state is ambiguous, require manual takeover.

## 15. Learning return path

At L3, full evidence remains in the host. Only a minimum redacted submission enters CollaborationOS.

```text
host event
  -> host-owned full evidence
  -> redaction and source/hash binding
  -> COS Learning Submission
  -> independent COS triage
  -> candidate, domain extension, AI-Native capability or reject
  -> explicit human Decision
```

Use the canonical Learning Submission schema/template. A submission, A09 or reviewer recommendation never promotes itself.

## 16. Agent instruction block

A host may adapt this short block in its agent instructions:

```text
CollaborationOS is an independent, read-only collaboration-governance dependency.
Use the host COS Entry Pointer, Adoption Record and Host Adapter before preparing COS artifacts.
Host business truth and final Decisions remain host-owned.
AI may prepare or inspect A01-A09 but may not self-authorize execution, cost, acceptance, retry, promotion or canonical writes.
Unknown authority, evidence, cost or scope fails closed as the applicable legal stop.
Do not edit COS Core from this host; submit redacted learning through the adopted bridge.
```

## 17. Validation checklist

### Entry and identity

- canonical COS release, commit, or approved local snapshot is pinned;
- package manifest and required schemas have recorded hashes;
- entry pointer, adoption record and Host Adapter agree on adoption level;
- no private editable COS Core copy exists in the host.

### Authority

- final Decision owner is human and named;
- cost, execution, acceptance, takeover and promotion functions are explicit;
- role overlap is explicitly allowed rather than inferred;
- AI and runtime permissions default false.

### Artifacts

- instances use the matching schema/template version;
- unknown/not-observed/not-applicable/zero are not conflated;
- A04 remains Decision authority;
- A06 does not invent missing authority;
- A07 separates observed result from acceptance;
- A08 does not imply retry;
- A09 does not imply promotion.

### Operations

- first use is Decision-Only;
- historical rehearsal is labeled historical;
- external calls and costs are recorded;
- failure and takeover route is known;
- no cross-host or product claim is made.

## 18. Version upgrade

When COS publishes a new public baseline:

1. freeze old and new package identities;
2. inspect semantic and schema changes;
3. classify each host mapping as `ALREADY_CONFORMANT`, `ADAPT`, `NOT_APPLICABLE`, `CONFLICT` or `DEFER`;
4. create a separate host adoption Decision for any change;
5. update the Adapter and pointer only after acceptance;
6. preserve prior instances with their original schema versions.

Never silently point historical artifacts to a newer schema.

## 19. Pause or remove adoption

A host may pause or stop using COS. The exit record should state:

- effective time and owner;
- reason and residual obligations;
- treatment of open Decisions/handoffs/failures;
- retained evidence and deletion restrictions;
- whether learning submissions remain valid;
- that historical records are not rewritten.

Removing an entry pointer does not erase accepted Decisions or failure evidence.

## 20. Completion definition

Initial host adoption is complete only when:

- pointer, adoption record and Adapter are human-accepted;
- A01 and A03 exist for the adopted scope;
- one historical Decision-Only rehearsal is reviewed;
- one explicit next-use Decision is recorded;
- no execution or cross-host claim was inferred;
- open limitations and upgrade owner are named.

At that point the accurate claim is:

> This host has adopted the CollaborationOS manual/static decision-governance baseline at the recorded level and version. Host business authority remains local, and no runtime, cross-host or product capability is implied.

## 21. Quick-start sequence

1. Choose `L1`.
2. Fill the Entry Pointer.
3. Pin COS package and schema hashes.
4. Approve the Adoption Record with all execution permissions false.
5. Prepare A01 and A03.
6. Complete the Host Adapter.
7. Rehearse one historical Decision through A01-A05.
8. Review limitations.
9. Separately decide whether to use Decision-Only on one live project fork.
10. Consider L2 only after L1 is useful and stable.
