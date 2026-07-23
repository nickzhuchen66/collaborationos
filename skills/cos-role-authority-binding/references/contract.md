# Canonical contract

Read these repository-relative sources before preparing an A03:

- `02_Protocols/COS_Role_Authority_Binding_Protocol_v0.1.md`
- `03_Schemas_and_Templates/COS_Role_Authority_Map_v0.1.schema.json`
- `03_Schemas_and_Templates/COS_Role_Authority_Map_Template_v0.1.md`

The exact permission registry is `read_context`, `prepare_artifact`, `propose`,
`challenge`, `edit_authorized_scope`, `external_call`, `incur_cost`,
`perform_irreversible_action`, `make_decision`, `accept_result`, `takeover`,
`promote_core`, `canonical_write`, and `release_product`.

Validate from the COS repository root:

```bash
python3 tools/cos_wave1.py validate-artifact \
  --cos-root . --kind A03 --input PATH_TO_A03.json
```

Validation does not accept the map or activate a permission.
