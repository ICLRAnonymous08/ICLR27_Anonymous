# NAT-057: Intersection queue length

**Domain:** Mobility systems

## Public question

Determine whether the following proposition is true.
Entity: Intersection approach IA-57
Metric: 95th percentile queue length
Condition: fixed approach lane, queue definition and peak window
Time window: 20 valid consecutive signal cycles
Target population: complete queue extending beyond the camera crop boundary
Aggregation: nearest-rank p95 of complete-lane queue counts
Validity rule: counts must cover the full mapped lane and the same cycle sampling instant
Comparison: strict < 10.0 vehicles

## Document store and condition visibility

Both renderings below contain all 19 document records. They are stores for the retrieval runner, not literal C1 or D6 model prompts. See [visibility.json](visibility.json): Among this case's 19 documents, C1 exposes S1 plus H1–H3 and B01–B10; D6 exposes S1–S6 plus the same H and B documents.

| Slot | Document ID | Grouped rendering | Distributed rendering |
|---|---|---|---|
| S1 | `doc-da518efcc8180660` | [HTML](grouped/doc-da518efcc8180660.html) | [HTML](distributed/doc-da518efcc8180660.html) |
| S2 | `doc-711cc9feee4c7b0b` | [HTML](grouped/doc-711cc9feee4c7b0b.html) | [HTML](distributed/doc-711cc9feee4c7b0b.html) |
| S3 | `doc-cb7d1c5239a63511` | [HTML](grouped/doc-cb7d1c5239a63511.html) | [HTML](distributed/doc-cb7d1c5239a63511.html) |
| S4 | `doc-cf11cb7565981e15` | [HTML](grouped/doc-cf11cb7565981e15.html) | [HTML](distributed/doc-cf11cb7565981e15.html) |
| S5 | `doc-86e4d910f8ccb0f5` | [HTML](grouped/doc-86e4d910f8ccb0f5.html) | [HTML](distributed/doc-86e4d910f8ccb0f5.html) |
| S6 | `doc-c2b20339eb9624b4` | [HTML](grouped/doc-c2b20339eb9624b4.html) | [HTML](distributed/doc-c2b20339eb9624b4.html) |
| H1 | `doc-07e8e64ede333726` | [HTML](grouped/doc-07e8e64ede333726.html) | [HTML](distributed/doc-07e8e64ede333726.html) |
| H2 | `doc-daa6d5e210d45e06` | [HTML](grouped/doc-daa6d5e210d45e06.html) | [HTML](distributed/doc-daa6d5e210d45e06.html) |
| H3 | `doc-ca54d77da4640ca9` | [HTML](grouped/doc-ca54d77da4640ca9.html) | [HTML](distributed/doc-ca54d77da4640ca9.html) |
| B01 | `doc-7ac55e19796994a7` | [HTML](grouped/doc-7ac55e19796994a7.html) | [HTML](distributed/doc-7ac55e19796994a7.html) |
| B02 | `doc-8219a3760c727524` | [HTML](grouped/doc-8219a3760c727524.html) | [HTML](distributed/doc-8219a3760c727524.html) |
| B03 | `doc-1815ff541d4fdc6c` | [HTML](grouped/doc-1815ff541d4fdc6c.html) | [HTML](distributed/doc-1815ff541d4fdc6c.html) |
| B04 | `doc-c993b2acb4d42c88` | [HTML](grouped/doc-c993b2acb4d42c88.html) | [HTML](distributed/doc-c993b2acb4d42c88.html) |
| B05 | `doc-771e7b4fc9690863` | [HTML](grouped/doc-771e7b4fc9690863.html) | [HTML](distributed/doc-771e7b4fc9690863.html) |
| B06 | `doc-856643aa1886f338` | [HTML](grouped/doc-856643aa1886f338.html) | [HTML](distributed/doc-856643aa1886f338.html) |
| B07 | `doc-2b75614634683f78` | [HTML](grouped/doc-2b75614634683f78.html) | [HTML](distributed/doc-2b75614634683f78.html) |
| B08 | `doc-4b995cc92a7e6498` | [HTML](grouped/doc-4b995cc92a7e6498.html) | [HTML](distributed/doc-4b995cc92a7e6498.html) |
| B09 | `doc-54abdba87a7ea9ce` | [HTML](grouped/doc-54abdba87a7ea9ce.html) | [HTML](distributed/doc-54abdba87a7ea9ce.html) |
| B10 | `doc-fa7bf7ad29bc84ba` | [HTML](grouped/doc-fa7bf7ad29bc84ba.html) | [HTML](distributed/doc-fa7bf7ad29bc84ba.html) |

Ground truth and arithmetic inputs are stored under `evaluation_only/` and `evaluation.json`. Provenance and slot metadata in `document_map.json` are audit-only metadata and were not supplied to the model.
