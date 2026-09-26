#!/usr/bin/env python3
"""Replay saved cross-Agent relay quota searches without model/API calls.

The frozen relay flags were computed from model-visible title and page text.
For documents in this partial release, the detector is independently checked
against DOCUMENT_RECORDS.jsonl. Other flags cannot be recomputed without the
unreleased cross-case pages of the full retrieval corpus.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "defense/paper_methods"))
from relay_detector import is_target_claim_relay  # noqa: E402
from relay_quota import choose  # noqa: E402


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def main() -> None:
    labels = {
        (row["case_id"], row["condition"], row["document_id"]): row
        for row in read_jsonl(ROOT / "defense/paper_methods/relay_labels.jsonl")
    }
    targets = {}
    documents = {}
    for case_dir in sorted((ROOT / "cases").glob("NAT-*")):
        case_id = case_dir.name
        targets[case_id] = json.loads((case_dir / "public_task.json").read_text())
        for view in ("grouped", "distributed"):
            path = case_dir / view / "DOCUMENT_RECORDS.jsonl"
            for row in read_jsonl(path):
                title, page = row["serp_title"], row["open_page_text"]
                fingerprint = (hashlib.sha256(title.encode()).hexdigest(),
                               hashlib.sha256(page.encode()).hexdigest())
                documents.setdefault(row["document_key"], set()).add((fingerprint, title, page))

    local_labels_checked = 0
    for (case_id, condition, doc_id), label in labels.items():
        if doc_id not in documents:
            continue
        expected = (label["title_sha256"], label["page_text_sha256"])
        matches = [(title, page) for fingerprint, title, page in documents[doc_id]
                   if fingerprint == expected]
        assert len(matches) == 1, (case_id, condition, doc_id)
        title, page = matches[0]
        assert is_target_claim_relay(targets[case_id], title, page) == label["is_relay"]
        local_labels_checked += 1

    traces = read_jsonl(ROOT / "defense/paper_methods/cross_agent_relay_quota/agent_traces.jsonl")
    search_events = 0
    for trace in traces:
        case_id, condition, repeat = trace["case_id"], trace["condition"], trace["repeat"]
        for event in trace["events"]:
            if event["type"] != "search":
                continue
            search_events += 1
            flags = {row["document_id"]: labels[case_id, condition, row["document_id"]]["is_relay"] for row in event["raw_candidates"]}
            selected = choose(case_id, repeat, trace["agent_id"], event["raw_candidates"], flags)
            displayed = [
                {key: ({**candidate, "rank": rank})[key] for key in ("rank", "title", "snippet", "publisher", "domain", "url")}
                for rank, candidate in enumerate(selected, 1)
            ]
            assert displayed == event["displayed_candidates"], (case_id, condition, repeat, trace["agent_id"])

    print(json.dumps({"status": "PASS", "search_events_replayed": search_events,
                      "local_detector_labels_checked": local_labels_checked,
                      "frozen_labels": len(labels)}, indent=2))


if __name__ == "__main__":
    main()
