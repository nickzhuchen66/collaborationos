# CollaborationOS Host Adoption Checklist

Use this checklist before claiming that a host has adopted COS. A checked box
records an observed fact; it does not create authority.

## 1. Baseline Identity

- [ ] A stable COS release is pinned; `main` is not the governed dependency.
- [ ] Exact release URL or approved snapshot path is recorded.
- [ ] Commit identity is recorded.
- [ ] Root package manifest SHA-256 is verified.
- [ ] Gate Pack manifest SHA-256 is verified.
- [ ] Upgrade owner and version-review trigger are named.

## 2. Host Ownership

- [ ] Host business source of truth is named with precedence.
- [ ] COS is read-only from the host.
- [ ] Host evidence and payload locations remain outside COS Core.
- [ ] Entry Pointer, Adoption Record, and Host Adapter are host-owned.
- [ ] No private editable COS fork is presented as canonical COS.

## 3. Adoption Scope

- [ ] Adoption level is exactly one of L0, L1, L2, or L3.
- [ ] Included surfaces are explicit.
- [ ] Excluded surfaces are explicit.
- [ ] Initial live use is Decision-Only.
- [ ] Claim ceiling excludes runtime, production, and cross-host validation.

## 4. Human Authority

- [ ] Final project owner is a named human role.
- [ ] Decision owner is explicit.
- [ ] Cost owner is explicit or cost is outside the adopted scope.
- [ ] Executor/builder is distinct from final authority.
- [ ] Independent acceptor is explicit for any future L2 use.
- [ ] Takeover owner is explicit.
- [ ] Role overlap is documented rather than inferred from identity.

## 5. Permission Defaults

- [ ] Execution is false for the initial L1 adoption.
- [ ] Host access is false.
- [ ] External calls are false.
- [ ] Cost authority is false.
- [ ] Automatic retry is false.
- [ ] Automatic acceptance is false.
- [ ] Automatic promotion is false.
- [ ] Automatic canonical write is false.
- [ ] Runtime and production authority are false.

## 6. Artifact Routing

- [ ] A01 Context location is mapped.
- [ ] A02 Evidence location and exclusion route are mapped.
- [ ] A03 Role/Authority location is mapped.
- [ ] A04 Decision location is mapped.
- [ ] A05 Cost route is mapped or explicitly not applicable.
- [ ] A06-A08 are marked outside scope for L1, or mapped for a separately accepted L2.
- [ ] A09 learning route is outside scope or explicitly mapped without auto-promotion.

## 7. Rehearsal and Review

- [ ] One completed, low-sensitivity historical Decision is selected.
- [ ] Historical facts are not rewritten.
- [ ] A01-A04 and optional A05 are reconstructed manually.
- [ ] At least one legal-stop variant is reviewed.
- [ ] At least one failure or missing-authority variant is reviewed.
- [ ] Limitations and unnecessary ceremony are recorded.
- [ ] Reviewer is not relying only on implementation self-report.

## 8. Failure, Pause, and Exit

- [ ] Failure evidence location is known.
- [ ] First failure and last safe checkpoint will be preserved.
- [ ] Ownership ambiguity routes to manual takeover.
- [ ] Retry requires a separate decision.
- [ ] Pause triggers are explicit.
- [ ] Exit and retention rules are explicit.
- [ ] Historical decisions and failure evidence will not be rewritten on exit.

## 9. Final Adoption Decision

- [ ] Draft documents contain no unresolved `REPLACE_BEFORE_USE` markers.
- [ ] Unknown facts remain visibly unknown rather than coerced.
- [ ] Human decision owner reviewed the Entry Pointer, Adoption Record, and Adapter.
- [ ] Disposition is recorded as ADOPT, ADAPT, DEFER, or REJECT.
- [ ] Effective time and decision reference are recorded.
- [ ] Any later L2/L3 expansion requires a separate decision.

## Stop Conditions

Do not claim adoption when any required item above is false or unknown. The
accurate disposition is `ADAPT`, `DEFER`, or `LEGAL_STOP`, depending on the host
contract. Documentation completion alone never grants access or execution.

