# Double-blind model-identifier normalization

Backend-specific and repository-internal model identifiers in the saved review-facing records were normalized to the paper's public name, **DeepSeek v4 Flash**. This affects `model` fields in trace metadata and the saved API request/response envelopes. In the 1,192 saved requests, the `model` routing field and linked `request_sha256` values in request and response records were updated together, so the published request hashes remain internally consistent.

Only model-identifier fields and those linked hashes changed. Prompt messages, queries, retrieved candidates, opened pages, Agent reports, Coordinator decisions, and model-generated response content were not modified. The first normalization covered 30 backend-specific aliases; the second covered 3,148 repository-internal aliases in the retained files. Per-file before/after hashes and counts are in `sanitization_manifest.json`.

These are anonymized review-facing records, not byte-for-byte copies of the original API envelopes. Unmodified source records remain outside the artifact.
