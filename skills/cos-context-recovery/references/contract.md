# Canonical contract

Read these repository-relative sources before preparing an A01:

- `02_Protocols/COS_Context_Recovery_Protocol_v0.1.md`
- `03_Schemas_and_Templates/COS_Context_Packet_v0.1.schema.json`
- `03_Schemas_and_Templates/COS_Context_Packet_Template_v0.1.md`

Their exact hashes are frozen in `source-bindings.json`. Missing or mismatched
sources fail closed; do not use a nearby version or copied fallback.

Validate a prepared artifact from the COS repository root:

```bash
python3 tools/cos_wave1.py validate-artifact \
  --cos-root . --kind A01 --input PATH_TO_A01.json
```

Validation does not accept the artifact.
