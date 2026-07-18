# COS Gate Pack Artifact Register v0.1

Status: `PUBLIC_MANUAL_STATIC_BASELINE`

| ID | Artifact | Primary owner | Authority boundary |
|---|---|---|---|
| A01 | Context Packet | Context Owner | records accepted context; does not admit evidence |
| A02 | Evidence Record | Evidence Acceptor | records evidence disposition; does not make a decision |
| A03 | Role/Authority Map | Final Human Authority | binds roles and permissions; participation grants nothing |
| A04 | Decision Packet | Decision Owner | records bounded human decision; does not prove execution |
| A05 | Cost Decision Packet | Cost Owner | approves/rejects bounded cost; does not override A04 |
| A06 | Execution Handoff | Handoff Owner | authorizes exact operations; does not accept results |
| A07 | Change Acceptance Packet | Independent Acceptor | accepts/rejects exact result; does not rewrite evidence |
| A08 | Failure/Manual Takeover Record | Takeover Owner | preserves failure and takeover truth; does not authorize retry |
| A09 | Learning Candidate Record | Learning Registrar | records reusable candidate; does not promote core material |

## Required pair rule

Each artifact has one strict JSON schema and one human-readable template. The
schema owns machine-valid shape; the template helps a person prepare content.
The template cannot add fields or authority that the schema does not permit.

## Selection rule

- A01-A04 are required before an executable handoff.
- A05 is required when the cost trigger is true or required cost is unknown.
- A06 is required for bounded execution.
- A07 is required for independent acceptance.
- A08 is required when failure, ambiguous rollback, or manual takeover occurs.
- A09 is optional and cannot authorize promotion.

## Canonical files

All schema and template files are in this directory. Their names share the
artifact type and version. See the
[Protocol System Map](../02_Protocols/COS_Protocol_System_Map_v0.1.md) for the
ordered protocol dependencies.

## Public limitation

The register is a manual/static artifact map. It grants no host access,
execution, spending, acceptance, retry, promotion, or production authority.

