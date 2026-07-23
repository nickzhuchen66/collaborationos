# Public review-control contract

Read `docs/contributing/REVIEW_CONTROL_PROFILE.md` before assessing a review
loop. Its exact public hash is frozen in `source-bindings.json`.

Run the deterministic assessment from the repository root:

```bash
python3 tools/cos_wave1.py assess-review \
  --input REVIEW_FACTS.json \
  --output /ABSOLUTE/BOUNDED/OUTPUT/assessment.json \
  --output-root /ABSOLUTE/BOUNDED/OUTPUT
```

The output recommends routing only. It grants no work, review, retry, merge, or
governance authority.
