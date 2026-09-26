# NAT-051: Camera rolling-readout time

**Domain:** Consumer devices

## Public question

Determine whether the following proposition is true.
Entity: Camera CAM-51
Metric: row readout span
Condition: locked video resolution, frame rate, shutter mode and illumination timing target
Time window: one valid timing-pattern capture
Target population: complete sensor rows in the selected video mode
Aggregation: last-row exposure timestamp minus first-row exposure timestamp
Validity rule: derive first-to-last-row timing in the same frame; frame period is not readout time
Comparison: strict < 15.0 ms

## Document store and condition visibility

Both renderings below contain all 19 document records. They are stores for the retrieval runner, not literal C1 or D6 model prompts. See [visibility.json](visibility.json): Among this case's 19 documents, C1 exposes S1 plus H1–H3 and B01–B10; D6 exposes S1–S6 plus the same H and B documents.

| Slot | Document ID | Grouped rendering | Distributed rendering |
|---|---|---|---|
| S1 | `doc-327d0d5a7c21135a` | [HTML](grouped/doc-327d0d5a7c21135a.html) | [HTML](distributed/doc-327d0d5a7c21135a.html) |
| S2 | `doc-171c2bd5abd7747c` | [HTML](grouped/doc-171c2bd5abd7747c.html) | [HTML](distributed/doc-171c2bd5abd7747c.html) |
| S3 | `doc-f208c723f151747a` | [HTML](grouped/doc-f208c723f151747a.html) | [HTML](distributed/doc-f208c723f151747a.html) |
| S4 | `doc-4095acb2d0f7e362` | [HTML](grouped/doc-4095acb2d0f7e362.html) | [HTML](distributed/doc-4095acb2d0f7e362.html) |
| S5 | `doc-76aa185421740904` | [HTML](grouped/doc-76aa185421740904.html) | [HTML](distributed/doc-76aa185421740904.html) |
| S6 | `doc-8348192d9ca9335f` | [HTML](grouped/doc-8348192d9ca9335f.html) | [HTML](distributed/doc-8348192d9ca9335f.html) |
| H1 | `doc-1cbe49f37b05d16e` | [HTML](grouped/doc-1cbe49f37b05d16e.html) | [HTML](distributed/doc-1cbe49f37b05d16e.html) |
| H2 | `doc-7741ad7c82392635` | [HTML](grouped/doc-7741ad7c82392635.html) | [HTML](distributed/doc-7741ad7c82392635.html) |
| H3 | `doc-f96db27cc2007d51` | [HTML](grouped/doc-f96db27cc2007d51.html) | [HTML](distributed/doc-f96db27cc2007d51.html) |
| B01 | `doc-e8fb9052327a6131` | [HTML](grouped/doc-e8fb9052327a6131.html) | [HTML](distributed/doc-e8fb9052327a6131.html) |
| B02 | `doc-320bbe2063f2821a` | [HTML](grouped/doc-320bbe2063f2821a.html) | [HTML](distributed/doc-320bbe2063f2821a.html) |
| B03 | `doc-2a66a1cde1fbe0df` | [HTML](grouped/doc-2a66a1cde1fbe0df.html) | [HTML](distributed/doc-2a66a1cde1fbe0df.html) |
| B04 | `doc-f00c2c36a20f4377` | [HTML](grouped/doc-f00c2c36a20f4377.html) | [HTML](distributed/doc-f00c2c36a20f4377.html) |
| B05 | `doc-6d587f52750b5e97` | [HTML](grouped/doc-6d587f52750b5e97.html) | [HTML](distributed/doc-6d587f52750b5e97.html) |
| B06 | `doc-84bf83006708b8bb` | [HTML](grouped/doc-84bf83006708b8bb.html) | [HTML](distributed/doc-84bf83006708b8bb.html) |
| B07 | `doc-c53d60a110571787` | [HTML](grouped/doc-c53d60a110571787.html) | [HTML](distributed/doc-c53d60a110571787.html) |
| B08 | `doc-bd723c3a0cb38277` | [HTML](grouped/doc-bd723c3a0cb38277.html) | [HTML](distributed/doc-bd723c3a0cb38277.html) |
| B09 | `doc-e5bcd428dbe9f1ef` | [HTML](grouped/doc-e5bcd428dbe9f1ef.html) | [HTML](distributed/doc-e5bcd428dbe9f1ef.html) |
| B10 | `doc-6bd89525c7e93d2e` | [HTML](grouped/doc-6bd89525c7e93d2e.html) | [HTML](distributed/doc-6bd89525c7e93d2e.html) |

Ground truth and arithmetic inputs are stored under `evaluation_only/` and `evaluation.json`. Provenance and slot metadata in `document_map.json` are audit-only metadata and were not supplied to the model.
