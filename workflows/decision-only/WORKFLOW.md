# COS-WF02 Decision-Only Workflow

Status: `PUBLIC EXPERIMENTAL / MANUAL STATIC / NO EXECUTION`

## Purpose

Coordinate accepted A01, A02, and A03 with an accepted A04 record, then stop.
The Workflow can report the human disposition and observed P05-evaluation
eligibility. It cannot create A05/A06, instructions, execution permission, or
Host access.

## Inputs

Provide one strict JSON run specification:

```json
{
  "workflow_run_id": "wf02-example",
  "as_of": "2026-07-23T00:00:00Z",
  "artifacts": {
    "A01": "repo-relative/path/to/a01.json",
    "A02": "repo-relative/path/to/a02.json",
    "A03": "repo-relative/path/to/a03.json",
    "A04": "repo-relative/path/to/a04.json"
  }
}
```

All paths must remain inside the supplied COS checkout. Verify the exact hashes
in `source-bindings.json` before use.

## Ordered stages

1. `context_recovery`: validate accepted A01.
2. `evidence_admission_external_prerequisite`: validate accepted A02.
3. `authority_binding`: validate accepted A03 and the permission registry.
4. `decision_record`: validate accepted A04 and cross-artifact relations.
5. `execution_handoff`: fixed `not_attempted`.

Any schema, lifecycle, lineage, or authority mismatch fails closed.

## Run

```bash
python3 tools/cos_wave1.py decision-only \
  --cos-root . \
  --input /ABSOLUTE/PATH/run.json \
  --output /ABSOLUTE/BOUNDED/OUTPUT/state.json \
  --output-root /ABSOLUTE/BOUNDED/OUTPUT
```

The output always fixes `p05_started=false`, `execution_authorized=false`,
`host_access=false`, `external_calls=0`, and `automatic_retry=false`.

## Terminal branches

- Accepted A04: `decision_recorded_no_execution`.
- Invalid or mismatched prerequisite: `failed_closed`; downstream remains
  `not_attempted`.
