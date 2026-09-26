# Defense implementation and saved runs

This partial release includes an exact document/URL deduplication audit and the Cross-Agent Relay Quota selector with saved execution records. The full defense comparison is reported in the manuscript.

## Implementation and replay

- `paper_methods/relay_detector.py` estimates claim-relay dependence from public target fields and visible title/page text. It does not use ground truth, hidden origin labels, or document roles.
- `paper_methods/relay_quota.py` applies a within-search group limit and a deterministic Agent owner across searches in one case-repeat run.
- `paper_methods/relay_labels.jsonl` stores detector flags derived from public target fields and visible page content, with hashes identifying the corresponding rendering.
- `../scripts/replay_selector.py` reconstructs saved Top-50 to Top-8 selections without model calls. Detector flags for released pages are recomputed from the included document records; flags for unreleased cross-case pages are retained as frozen inputs.

## Saved records

`paper_methods/cross_agent_relay_quota/` contains Agent and Coordinator records for the ten cases. The Agent records combine 50 baseline traces, 60 within-search relay traces, and 190 newly run quota traces. The Coordinator records reuse 5 baseline cells and contain 95 quota cells. Saved outputs are reused only for cells whose model-visible candidate lists are unchanged by the selector; changed cells were rerun.

`exact_dedup_audit.json` summarizes the document/URL uniqueness checks for the saved baseline searches. `paper_methods/run_metrics.csv` retains run-level checks for the baseline and quota traces in this release; it is not a full-benchmark result table.
