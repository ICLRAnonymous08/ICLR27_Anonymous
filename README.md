# SourceSplit Artifact

This repository provides a partial ECHO-WEB dataset release containing ten cases across eight domains, together with saved traces and offline verification scripts.

The artifact supports data inspection and implementation auditing. Quantitative results reported in the paper are computed over the full 100-case benchmark.

## Browse the artifact

- [Artifact documentation](SourceSplit_artifact/README.md)
- [Case manifest](SourceSplit_artifact/case_manifest.json)
- [Cases and documents](SourceSplit_artifact/cases/)
- [Saved baseline traces and prompts](SourceSplit_artifact/traces/)
- [Defense implementation and saved records](SourceSplit_artifact/defense/)
- [Protocol configuration](SourceSplit_artifact/config/main_protocol.json)

## Offline verification

Python 3.9 or later is sufficient; no API key or model call is needed.
After cloning this repository or downloading its source files:

```bash
cd SourceSplit_artifact
python3 verify.py
python3 scripts/replay_selector.py
python3 scripts/audit_model_visibility.py
```

Scope, condition visibility, and saved-run details are documented in the [artifact README](SourceSplit_artifact/README.md).
