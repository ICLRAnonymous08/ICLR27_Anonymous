"""Self-contained Top-50 to Top-8 relay quota used for offline trace replay."""

from __future__ import annotations

import hashlib

AGENTS = ("A", "B", "C")
DISPLAY_BUDGET = 8


def owner(case_id: str, repeat: int) -> str:
    digest = hashlib.sha256(f"relay-quota-v1|{case_id}|{repeat}".encode()).digest()
    return AGENTS[int.from_bytes(digest[:8], "big") % len(AGENTS)]


def choose(case_id: str, repeat: int, agent_id: str, rows: list[dict], relay_labels: dict[str, bool]) -> list[dict]:
    """Select eight candidates using only visible-evidence detector flags.

    The repeated relay group is allowed only for the deterministic owner
    Agent. For that Agent, at most one relay candidate is retained per search.
    All other candidates are distinct by document ID. Group state resets on
    each call.
    """
    if agent_id not in AGENTS:
        raise ValueError(agent_id)
    if len(rows) != 50:
        raise ValueError("expected a saved BM25 Top-50 candidate list")

    selected: list[dict] = []
    seen: set[tuple[str, str]] = set()
    owner_agent = owner(case_id, repeat)
    for row in rows:
        document_id = row["document_id"]
        is_relay = relay_labels[document_id]
        if is_relay and agent_id != owner_agent:
            continue
        group = ("relay", case_id) if is_relay else ("singleton", document_id)
        if group in seen:
            continue
        seen.add(group)
        selected.append(row)
        if len(selected) == DISPLAY_BUDGET:
            break
    if len(selected) != DISPLAY_BUDGET:
        raise RuntimeError("could not fill Top-8 from saved Top-50")
    return selected
