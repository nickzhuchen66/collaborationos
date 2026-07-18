# Artifact Selection and Ownership

Status: `PUBLIC_MANUAL_STATIC_BASELINE / NO_EXECUTION_AUTHORITY`

## Selection table

| ID | Use when | Prepared by | Required authority or independent role | Does not authorize |
|---|---|---|---|---|
| A01 Context Packet | work needs a recoverable current-state baseline | context preparer | context reviewer | a new business Decision |
| A02 Evidence Record | information must be admitted, limited or rejected for a claim | evidence submitter | admission reviewer | ground truth or business authority |
| A03 Role & Authority Map | roles, permissions and takeover ownership must be explicit | authority mapper | human authority owner | execution merely because a role is named |
| A04 Decision Packet | a material fork has been decided | decision preparer | authorized human decision owner | action outside the recorded scope |
| A05 Cost Decision Packet | a tool, external call, purchase or cost-bearing capability is considered | cost analyst/preparer | cost owner and required human approver | purchase, call or integration before acceptance |
| A06 Execution Handoff | an accepted Decision is ready for bounded implementation | architect/reviewer | authorized handoff owner; references A03/A04 | acceptance or broader permissions |
| A07 Change & Acceptance Packet | observed results must be separated from formal acceptance | builder for result evidence | independent acceptor for acceptance event | self-acceptance by the executor |
| A08 Failure & Manual Takeover Record | failure, side effects or takeover must remain inspectable | failure recorder | failure owner and takeover owner | retry or a second business Decision |
| A09 Learning Candidate Record | bounded learning may be reviewed for retention or promotion | host submitter/intake registrar | COS reviewer; human promotion owner remains separate | automatic promotion, canonical release or host adoption |

Canonical definitions are in the [Artifact Register](../../03_Schemas_and_Templates/COS_Gate_Pack_Artifact_Register_v0.1.md).

## Schema and template use

Each A01-A09 artifact has:

- a strict JSON Schema for machine-inspectable structure;
- a Markdown template for human preparation and review.

The template helps a person prepare an instance. It does not weaken schema constraints or create authority. The schema validates structure; it does not decide whether an actor is genuinely authorized or whether evidence is true.

## Ownership invariants

1. A03 is the sole role/permission artifact authority. Other artifacts reference it.
2. A04 is the sole business Decision artifact authority. A05 specializes cost decisions without creating a parallel authority system.
3. A06 carries accepted permission; it cannot create a missing Decision.
4. A07 separates result facts from independent acceptance.
5. A08 records failure and takeover without erasing A04 or changing the business outcome.
6. A09 records learning and recommendations; promotion remains separately decided by a human owner.

## Minimum separation of duties

At minimum, distinguish these functions even when one person holds more than one role:

| Function | Responsibility |
|---|---|
| preparer | assembles context, evidence or a draft artifact |
| decision owner | makes the material business/governance choice |
| executor/builder | performs only the accepted handoff scope |
| independent acceptor | judges result acceptance independently of execution self-report |
| takeover owner | owns the next safe action after failure or ambiguity |
| promotion owner | decides whether bounded learning changes canonical COS assets |

Role overlap must be explicitly allowed by accepted authority. Identity equality alone grants nothing.

## Canonical schema/template pairs

| ID | Schema | Human template |
|---|---|---|
| A01 | [`COS_Context_Packet_v0.1.schema.json`](../../03_Schemas_and_Templates/COS_Context_Packet_v0.1.schema.json) | [`COS_Context_Packet_Template_v0.1.md`](../../03_Schemas_and_Templates/COS_Context_Packet_Template_v0.1.md) |
| A02 | [`COS_Evidence_Record_v0.1.schema.json`](../../03_Schemas_and_Templates/COS_Evidence_Record_v0.1.schema.json) | [`COS_Evidence_Record_Template_v0.1.md`](../../03_Schemas_and_Templates/COS_Evidence_Record_Template_v0.1.md) |
| A03 | [`COS_Role_Authority_Map_v0.1.schema.json`](../../03_Schemas_and_Templates/COS_Role_Authority_Map_v0.1.schema.json) | [`COS_Role_Authority_Map_Template_v0.1.md`](../../03_Schemas_and_Templates/COS_Role_Authority_Map_Template_v0.1.md) |
| A04 | [`COS_Decision_Packet_v0.1.schema.json`](../../03_Schemas_and_Templates/COS_Decision_Packet_v0.1.schema.json) | [`COS_Decision_Packet_Template_v0.1.md`](../../03_Schemas_and_Templates/COS_Decision_Packet_Template_v0.1.md) |
| A05 | [`COS_Cost_Decision_Packet_v0.1.schema.json`](../../03_Schemas_and_Templates/COS_Cost_Decision_Packet_v0.1.schema.json) | [`COS_Cost_Decision_Packet_Template_v0.1.md`](../../03_Schemas_and_Templates/COS_Cost_Decision_Packet_Template_v0.1.md) |
| A06 | [`COS_Execution_Handoff_v0.1.schema.json`](../../03_Schemas_and_Templates/COS_Execution_Handoff_v0.1.schema.json) | [`COS_Execution_Handoff_Template_v0.1.md`](../../03_Schemas_and_Templates/COS_Execution_Handoff_Template_v0.1.md) |
| A07 | [`COS_Change_Acceptance_Packet_v0.1.schema.json`](../../03_Schemas_and_Templates/COS_Change_Acceptance_Packet_v0.1.schema.json) | [`COS_Change_Acceptance_Packet_Template_v0.1.md`](../../03_Schemas_and_Templates/COS_Change_Acceptance_Packet_Template_v0.1.md) |
| A08 | [`COS_Failure_Manual_Takeover_Record_v0.1.schema.json`](../../03_Schemas_and_Templates/COS_Failure_Manual_Takeover_Record_v0.1.schema.json) | [`COS_Failure_Manual_Takeover_Record_Template_v0.1.md`](../../03_Schemas_and_Templates/COS_Failure_Manual_Takeover_Record_Template_v0.1.md) |
| A09 | [`COS_Learning_Candidate_Record_v0.1.schema.json`](../../03_Schemas_and_Templates/COS_Learning_Candidate_Record_v0.1.schema.json) | [`COS_Learning_Candidate_Record_Template_v0.1.md`](../../03_Schemas_and_Templates/COS_Learning_Candidate_Record_Template_v0.1.md) |
