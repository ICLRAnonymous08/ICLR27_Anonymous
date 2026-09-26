"""Visible-evidence dependency estimate used in the saved defense traces.

The selector receives the public target, SERP title, and page text. It never
uses document slot, case answer, condition, or hidden provenance. Structural
record cues are treated as evidence that a page may describe its own
acquisition; the rule does not judge whether a reported claim is correct.
"""

from __future__ import annotations

import re

COMPARISON_RE = re.compile(
    r"\b(?:below|above|under|over|exceed(?:s|ed)?|satisf(?:y|ied|ies)|met|failed|passes|reference|threshold|criterion|benchmark|comparison|target|limit|accepted)\b",
    re.I,
)
PRIMARY_RECORD_RE = re.compile(
    r"\b(?:acquisition record|instrument / setup|observed values|raw record|validity controls|sample plan|recorded observations|post-processed solid depths)\b"
    r"|\bmeasurement entry\s+[^.]{0,50}samples\b"
    r"|\b\d+(?:\.\d+)?\s*[,;]\s*\d+(?:\.\d+)?\s*[,;]\s*\d+(?:\.\d+)?\b"
    r"|\b\d+(?:\.\d+)?\s*[×*/]\s*\d+(?:\.\d+)?(?:\s*[×*/]\s*\d+(?:\.\d+)?)?",
    re.I,
)
# A visible accession for a run is useful without interpreting its value.
RUN_ACCESSION_RE = re.compile(r"\b[A-Z][A-Z0-9-]*-RUN-[A-Z0-9-]+\b", re.I)
EARLY_ACQUISITION_RE = re.compile(r"\bacquisition\b", re.I)
ENTITY_PART_RE = re.compile(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*")
METRIC_WORD_RE = re.compile(r"[a-z]{3,}")
METRIC_STOPWORDS = {"the", "and", "for", "from", "per", "under", "with", "after", "mean", "time", "rate"}
ACTIVE_ACQUISITION_RE = re.compile(
    r"\b(?:evaluated|examined|operated|deployed|used|ran|replayed|measured|collected|acquired|tested|logged|captured|scored|counted|derived|calculated|recorded|monitored|calibrated|measures|records|acquires|integrates|counts)\b",
    re.I,
)
APPARATUS_RE = re.compile(
    r"\b(?:instrument|sensor|meter|analyzer|logger|harness|fixture|rig|trace|counter|samples|readings|test crew|laboratory|field team|bench|photoelectric|calorimetry|flow cell|workstation|camera|transducer|waveform)\b",
    re.I,
)
ATTRIBUTION_RE = re.compile(
    r"\b(?:according to|reported by|vendor reports?|supplier reports?|documentation describes|reported evaluation|source:|operating record|retained.entry|release documentation)\b",
    re.I,
)


def is_target_claim_relay(target: dict, title: str, page_text: str) -> bool:
    """Return whether the visible page is a target-claim relay candidate."""
    entity = target["entity"]
    parts = ENTITY_PART_RE.findall(entity)
    codes = [part for part in parts if len(part) >= 4 and any(char.isdigit() for char in part) and any(char.isalpha() for char in part)]
    visible = f"{title}\n{page_text}"
    threshold_pattern = re.compile(r"(?<![0-9])" + re.escape(str(target["threshold"])) + r"(?![0-9])")
    has_threshold = bool(threshold_pattern.search(page_text))
    aliases = [entity, *codes]
    if len(parts) >= 2:
        aliases.append(" ".join(parts[:2]))
    if parts and len(parts[0]) >= 5 and has_threshold:
        aliases.append(parts[0])
    target_match = any(
        re.search(r"(?<![\w-])" + re.escape(alias) + r"(?![\w-])", visible, re.I)
        for alias in aliases
    )
    metric_words = set(METRIC_WORD_RE.findall(target["metric"].casefold())) - METRIC_STOPWORDS
    metric_overlap = len(metric_words & set(METRIC_WORD_RE.findall(visible.casefold())))
    comparison_match = metric_overlap >= 2 and bool(COMPARISON_RE.search(visible))
    own_acquisition = bool(
        PRIMARY_RECORD_RE.search(page_text)
        or RUN_ACCESSION_RE.search(page_text)
        or EARLY_ACQUISITION_RE.search(page_text[:200])
        or (
            has_threshold
            and ACTIVE_ACQUISITION_RE.search(page_text[:250])
            and APPARATUS_RE.search(page_text[:250])
            and not ATTRIBUTION_RE.search(page_text)
        )
    )
    return target_match and comparison_match and not own_acquisition
