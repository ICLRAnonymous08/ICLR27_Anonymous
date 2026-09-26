# NAT-048: Headphone battery life

**Domain:** Consumer devices

## Public question

Determine whether the following proposition is true.
Entity: Earbuds EB-48
Metric: continuous playback time
Condition: 50% volume, fixed 256-kbps playlist, ANC enabled, fully charged pair, no pause
Time window: one uninterrupted discharge run per acquisition
Target population: matched EB-48 pairs under the locked firmware/configuration
Aggregation: elapsed active-playback time from full charge to first-earbud playback stop
Validity rule: exclude any paused interval and stop when the first earbud ceases playback
Comparison: strict < 6.0 h

## Document store and condition visibility

Both renderings below contain all 19 document records. They are stores for the retrieval runner, not literal C1 or D6 model prompts. See [visibility.json](visibility.json): Among this case's 19 documents, C1 exposes S1 plus H1–H3 and B01–B10; D6 exposes S1–S6 plus the same H and B documents.

| Slot | Document ID | Grouped rendering | Distributed rendering |
|---|---|---|---|
| S1 | `doc-a2f00bb4e7bf8f72` | [HTML](grouped/doc-a2f00bb4e7bf8f72.html) | [HTML](distributed/doc-a2f00bb4e7bf8f72.html) |
| S2 | `doc-59cf0d5694fc4007` | [HTML](grouped/doc-59cf0d5694fc4007.html) | [HTML](distributed/doc-59cf0d5694fc4007.html) |
| S3 | `doc-f4ae44f66c169423` | [HTML](grouped/doc-f4ae44f66c169423.html) | [HTML](distributed/doc-f4ae44f66c169423.html) |
| S4 | `doc-ff7cc7d1941161e9` | [HTML](grouped/doc-ff7cc7d1941161e9.html) | [HTML](distributed/doc-ff7cc7d1941161e9.html) |
| S5 | `doc-c1903c4b5635ea33` | [HTML](grouped/doc-c1903c4b5635ea33.html) | [HTML](distributed/doc-c1903c4b5635ea33.html) |
| S6 | `doc-1bf5d379b567d713` | [HTML](grouped/doc-1bf5d379b567d713.html) | [HTML](distributed/doc-1bf5d379b567d713.html) |
| H1 | `doc-1da28ce8b1790abf` | [HTML](grouped/doc-1da28ce8b1790abf.html) | [HTML](distributed/doc-1da28ce8b1790abf.html) |
| H2 | `doc-a3a1bc59ac2bf469` | [HTML](grouped/doc-a3a1bc59ac2bf469.html) | [HTML](distributed/doc-a3a1bc59ac2bf469.html) |
| H3 | `doc-48d5ffe623964e23` | [HTML](grouped/doc-48d5ffe623964e23.html) | [HTML](distributed/doc-48d5ffe623964e23.html) |
| B01 | `doc-ce2bc3d90947d1b8` | [HTML](grouped/doc-ce2bc3d90947d1b8.html) | [HTML](distributed/doc-ce2bc3d90947d1b8.html) |
| B02 | `doc-ebcdbe96d56e0d1c` | [HTML](grouped/doc-ebcdbe96d56e0d1c.html) | [HTML](distributed/doc-ebcdbe96d56e0d1c.html) |
| B03 | `doc-f608b317e3f53204` | [HTML](grouped/doc-f608b317e3f53204.html) | [HTML](distributed/doc-f608b317e3f53204.html) |
| B04 | `doc-b52537cc7b69d2cd` | [HTML](grouped/doc-b52537cc7b69d2cd.html) | [HTML](distributed/doc-b52537cc7b69d2cd.html) |
| B05 | `doc-348551fd900feeec` | [HTML](grouped/doc-348551fd900feeec.html) | [HTML](distributed/doc-348551fd900feeec.html) |
| B06 | `doc-a32674f07fda7aa0` | [HTML](grouped/doc-a32674f07fda7aa0.html) | [HTML](distributed/doc-a32674f07fda7aa0.html) |
| B07 | `doc-331ab4290406fa07` | [HTML](grouped/doc-331ab4290406fa07.html) | [HTML](distributed/doc-331ab4290406fa07.html) |
| B08 | `doc-63dfceed5d6699df` | [HTML](grouped/doc-63dfceed5d6699df.html) | [HTML](distributed/doc-63dfceed5d6699df.html) |
| B09 | `doc-15548ffb26fe16ca` | [HTML](grouped/doc-15548ffb26fe16ca.html) | [HTML](distributed/doc-15548ffb26fe16ca.html) |
| B10 | `doc-428b31783446ed12` | [HTML](grouped/doc-428b31783446ed12.html) | [HTML](distributed/doc-428b31783446ed12.html) |

Ground truth and arithmetic inputs are stored under `evaluation_only/` and `evaluation.json`. Provenance and slot metadata in `document_map.json` are audit-only metadata and were not supplied to the model.
