# <Host Project> COS Host Adapter v0.1

Status: `<PROPOSED / ACCEPTED / PAUSED / SUPERSEDED>`

Host: `<stable host ID>`

Adopted COS level: `<L0 / L1 / L2 / L3>`

Host adoption Decision: `<reference>`

## 1. Purpose and non-goals

Purpose: `<How this Adapter translates COS into the host.>`

Non-goals:

- does not modify COS Core;
- does not replace host business authority;
- does not authorize execution, cost, retry, acceptance or promotion;
- does not create M6 or cross-host evidence by itself.

## 2. Authority ownership

| Surface | Owner | Adapter ruling |
|---|---|---|
| COS protocols/schemas/maturity | CollaborationOS | read-only dependency |
| Host business truth | `<host authority>` | host-owned |
| Host implementation | `<host authority>` | host-owned |
| Final Decision | `<human role>` | never delegated to AI/runtime |
| COS learning submission | `<host submitter + COS reviewer>` | redacted, no automatic promotion |

Conflict rule: `<How conflicting COS and host facts are routed without silent override.>`

## 3. Role binding

| COS function | Host role | Authority | Prohibited |
|---|---|---|---|
| project/final owner | `<role>` | `<scope>` | `<boundary>` |
| context preparer/reviewer | `<role>` | `<scope>` | `<boundary>` |
| evidence submitter/admission reviewer | `<role>` | `<scope>` | `<boundary>` |
| decision owner | `<role>` | `<scope>` | `<boundary>` |
| cost owner | `<role>` | `<scope>` | `<boundary>` |
| executor/builder | `<role>` | `<scope>` | `<boundary>` |
| independent acceptor | `<role>` | `<scope>` | `<boundary>` |
| takeover owner | `<role>` | `<scope>` | `<boundary>` |
| learning/promotion owner | `<role>` | `<scope>` | `<boundary>` |

## 4. Artifact crosswalk

| COS artifact | Host source/output | Precedence and use |
|---|---|---|
| A01 Context Packet | `<paths>` | `<rule>` |
| A02 Evidence Record | `<paths>` | `<rule>` |
| A03 Role/Authority Map | `<paths>` | `<rule>` |
| A04 Decision Packet | `<paths>` | `<rule>` |
| A05 Cost Decision | `<paths>` | `<rule>` |
| A06 Execution Handoff | `<paths>` | `<rule>` |
| A07 Change/Acceptance | `<paths>` | `<rule>` |
| A08 Failure/Takeover | `<paths>` | `<rule>` |
| A09 Learning Candidate | `<paths>` | `<rule>` |

## 5. Protocol applicability

| Protocol | Host mechanism | Disposition | Limitation |
|---|---|---|---|
| P01 Context Recovery | `<mechanism>` | `<APPLICABLE / PARTIAL / NOT_APPLICABLE>` | `<text>` |
| P02 Evidence Admission | `<mechanism>` | `<value>` | `<text>` |
| P03 Authority Binding | `<mechanism>` | `<value>` | `<text>` |
| P04 Decision Before Instruction | `<mechanism>` | `<value>` | `<text>` |
| P05 Execution Handoff | `<mechanism>` | `<value>` | `<text>` |
| P06 Acceptance/Failure | `<mechanism>` | `<value>` | `<text>` |
| P07 Learning/Promotion | `<mechanism>` | `<value>` | `<text>` |

## 6. Domain Extension boundary

Host-specific ontology, business schema and project rules that must remain outside COS Core:

- `<item>`

## 7. Failure and takeover route

- Failure evidence root: `<path>`
- Stable public error owner: `<role>`
- Takeover owner: `<role>`
- Retry rule: `no implicit retry; separate Decision required`
- Sensitive-data handling: `<rule>`

## 8. Learning bridge

- Full host evidence stays at: `<path>`
- Redaction owner: `<role>`
- Submission path: `<path or not adopted>`
- COS route options: `CORE_CANDIDATE / DOMAIN_EXTENSION / AI_NATIVE_CAPABILITY / MIXED_SPLIT / REJECT`
- Automatic promotion: `false`

## 9. Permission envelope

```text
automatic_apply=false
automatic_acceptance=false
automatic_retry=false
automatic_promotion=false
automatic_canonical_write=false
automatic_external_call=false
automatic_cost_approval=false
```

Additional host-specific false permissions:

- `<permission>=false`

## 10. Acceptance and limitations

- Adapter reviewer: `<role>`
- Human acceptance reference: `<Decision>`
- Known limitations: `<text>`
- Next permitted adoption gate: `<value>`
