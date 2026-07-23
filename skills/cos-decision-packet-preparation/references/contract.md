# Canonical contract

Read these repository-relative sources before preparing an A04:

- `02_Protocols/COS_Decision_Before_Instruction_Protocol_v0.1.md`
- `03_Schemas_and_Templates/COS_Decision_Packet_v0.1.schema.json`
- `03_Schemas_and_Templates/COS_Decision_Packet_Template_v0.1.md`
- `03_Schemas_and_Templates/COS_Cost_Decision_Packet_v0.1.schema.json` when cost is triggered

Validate from the COS repository root:

```bash
python3 tools/cos_wave1.py validate-artifact \
  --cos-root . --kind A04 --input PATH_TO_A04.json
```

This Skill consumes accepted A02 and optional A05 records as prerequisites. It
does not create either record and never starts P05.
