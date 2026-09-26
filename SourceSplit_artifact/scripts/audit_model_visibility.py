#!/usr/bin/env python3
"""Check saved baseline API payloads for evaluation-only fields and origins."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_FIELD_NAMES = (
    "origin_id", "oracle", "slot_id", "ground_truth", "raw_values",
    "wrong_reduction", "human_review_status", "evaluation_only/",
)


def main() -> None:
    hidden_origins = set()
    for path in (ROOT / "cases").glob("NAT-*/document_map.json"):
        for doc in json.loads(path.read_text()):
            if doc.get("origin_id"):
                hidden_origins.add(doc["origin_id"])

    stages: Counter[str] = Counter()
    checked = 0
    for line in (ROOT / "traces/api_requests.jsonl").read_text().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        payload = json.dumps(row["payload"], ensure_ascii=False)
        folded = payload.casefold()
        assert not any(name in folded for name in FORBIDDEN_FIELD_NAMES), (row["case_id"], row["stage"])
        assert not any(origin in payload for origin in hidden_origins), (row["case_id"], row["stage"])
        stages[row["stage"]] += 1
        checked += 1

    print(json.dumps({"status": "PASS", "saved_baseline_api_requests_checked": checked,
                      "hidden_origin_ids_checked": len(hidden_origins),
                      "request_stages": dict(stages)}, indent=2))


if __name__ == "__main__":
    main()
