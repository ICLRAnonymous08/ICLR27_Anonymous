# SourceSplit Artifact

This partial ECHO-WEB release contains ten cases across eight domains, document renderings, saved baseline and Cross-Agent Relay Quota runs, and offline verification scripts. It supports trace inspection and implementation auditing. Quantitative results reported in the paper are computed over the full 100-case benchmark.

The original runs searched a 1,900-page corpus; this release contains the ten cases' 190 unique documents. Saved traces may therefore refer to cross-case pages outside this release. Offline selector replay uses the saved Top-50 candidate lists and frozen detector flags for unreleased pages, while recomputing flags from visible title and page text for released pages. The partial release does not reconstruct the full retrieval corpus or rerun the complete experiment.

## Quick start

Python 3.9 or later is sufficient; no API key or model call is needed.

```bash
python3 verify.py
python3 scripts/replay_selector.py
python3 scripts/audit_model_visibility.py
```

`verify.py` checks file hashes, case arithmetic, protocol settings, condition visibility, paired logs, and run-level records. `replay_selector.py` reconstructs saved Cross-Agent Relay Quota Top-8 lists from saved Top-50 lists and visible-evidence detector flags. `audit_model_visibility.py` checks saved baseline API payloads for evaluation-only fields and hidden origin identifiers. The [sanitization record](SANITIZATION.md) documents model-identifier normalization for anonymous review.

The baseline contains 100 Coordinator outcome records but only 96 Coordinator API calls. Four runs had an invalid Local-Agent report and were recorded as `INVALID` before the Coordinator was invoked; these runs count as non-target outcomes under the evaluation protocol.

## Files

- [Case manifest](case_manifest.json): identifiers, domains, and topics. Each case's `README.md` links to its question and documents. `public_task.json` contains the public fields used by selector replay.
- `cases/NAT-*/grouped/` and `cases/NAT-*/distributed/`: document renderings. `DOCUMENT_RECORDS.jsonl` is a document store, not a literal model prompt; `visibility.json` specifies the case's document visibility under C1 and D6.
- [Baseline traces](traces/): queries, Agent interactions, Coordinator outcomes, prompt templates, and API request/response records.
- [Defense](defense/README.md): selector code, saved quota traces, detector flags, and run-level checks.
- `evaluation_only/` and each case's `evaluation.json`: synthetic source records and ground truth for offline verification. Provenance and slot fields in `document_map.json` are also audit-only metadata; these fields were not supplied to the model.
- [Protocol](config/main_protocol.json): condition definitions, rendering policy, Agent budgets, retrieval settings, and run count.

C1 is Single-Surface, exposing only S1 in its grouped rendering. D6 is SourceSplit (B=6), exposing the distributed renderings of S1-S6. Both conditions contain one independent target origin. H and B documents are identical across the two renderings. The folder names `grouped` and `distributed` describe document renderings, not separate experimental conditions.
