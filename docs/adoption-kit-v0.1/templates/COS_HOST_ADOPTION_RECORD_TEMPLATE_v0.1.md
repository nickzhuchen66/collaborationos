# <Host Project> COS Adoption Record

Record ID: `<stable ID>`

Status: `<PROPOSED / ACCEPTED / PAUSED / SUPERSEDED / RETIRED>`

Decision owner: `<human name or stable role>`

Effective time: `<RFC3339>`

## 1. Purpose

`<Why this host is adopting COS and what problem it should solve.>`

## 2. Adoption level

Selected level: `<L0 / L1 / L2 / L3>`

Included surfaces:

- `<surface>`

Excluded surfaces:

- `<surface>`

## 3. Canonical COS binding

| Item | Path | SHA-256 | Version/Decision |
|---|---|---|---|
| Gate Pack manifest | `<path>` | `<hash>` | `<value>` |
| Manual Operator Flow | `<path>` | `<hash>` | `<value>` |
| Artifact ownership | `<path>` | `<hash>` | `<value>` |
| Required schemas | `<path or inventory>` | `<hash>` | `<value>` |
| Review controls, if adopted | `<path>` | `<hash>` | `<value>` |

## 4. Host authority

- Host source of truth: `<paths and precedence>`
- Final project owner: `<role>`
- Decision owner: `<role>`
- Cost owner: `<role>`
- Executor/builder: `<role>`
- Independent acceptor: `<role>`
- Takeover owner: `<role>`
- Promotion/adoption owner: `<role>`

Role overlap explicitly allowed: `<none or exact pairs and conditions>`

## 5. Permission defaults

```text
execution_authorized=false
host_access_authorized=false
external_call_authorized=false
cost_authorized=false
automatic_retry=false
automatic_acceptance=false
automatic_promotion=false
automatic_canonical_write=false
runtime_authorized=false
production_authorized=false
```

Any separately granted permission must reference an exact host Decision and scope.

## 6. Artifact ownership

- Entry Pointer: `<path>`
- Host Adapter: `<path>`
- A01-A09 instances: `<path>`
- Full evidence: `<path>`
- Sensitive evidence owner: `<role>`
- Learning submission root: `<path or not adopted>`

## 7. Initial rehearsal

- Historical case: `<reference>`
- Rehearsal scope: `<A01-A04/A05>`
- Reviewer: `<independent role>`
- Result: `<PASS / LIMITATION / LEGAL_STOP / FAILED / NOT_YET_RUN>`
- Limitations: `<text>`

## 8. Claim ceiling

Allowed claim:

`<Exact host adoption claim.>`

Forbidden claims:

- COS product/runtime adoption unless separately released;
- cross-host validation or M6 completion;
- automatic authority, acceptance, retry or promotion;
- modification of COS Core from the host.

## 9. Upgrade and exit

- Upgrade owner: `<role>`
- Version review trigger: `<condition>`
- Pause trigger: `<condition>`
- Exit/retention rule: `<rule>`

## 10. Decision

Disposition: `<ADOPT / ADAPT / DEFER / REJECT>`

Conditions: `<text>`

Decision reference: `<host Decision ID/path/hash>`
