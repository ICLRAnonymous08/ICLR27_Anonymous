# NAT-025: Complete handling success rate

**Domain:** Industrial systems

## Public question

Determine whether the following proposition is true.
Entity: VG-4 vacuum handling cell
Metric: complete pick-transfer-place success proportion
Condition: same rigid workpiece set, initial pose distribution, vacuum setting, transfer path, speed, and final placement tolerance
Time window: one locked 50–75-trial commissioning session per acquisition
Target population: all initiated handling trials under the locked recipe
Aggregation: successful complete placements / all initiated trials × 100
Validity rule: a success requires pick-up, uninterrupted transfer, and placement within tolerance; aborted trials and in-transit drops remain in the denominator
Comparison: strict < 92.0 %

## Document store and condition visibility

Both renderings below contain all 19 document records. They are stores for the retrieval runner, not literal C1 or D6 model prompts. See [visibility.json](visibility.json): Among this case's 19 documents, C1 exposes S1 plus H1–H3 and B01–B10; D6 exposes S1–S6 plus the same H and B documents.

| Slot | Document ID | Grouped rendering | Distributed rendering |
|---|---|---|---|
| S1 | `doc-0d318daf7858b49c` | [HTML](grouped/doc-0d318daf7858b49c.html) | [HTML](distributed/doc-0d318daf7858b49c.html) |
| S2 | `doc-972435e1ea8bd6be` | [HTML](grouped/doc-972435e1ea8bd6be.html) | [HTML](distributed/doc-972435e1ea8bd6be.html) |
| S3 | `doc-0a326c8d545ede1f` | [HTML](grouped/doc-0a326c8d545ede1f.html) | [HTML](distributed/doc-0a326c8d545ede1f.html) |
| S4 | `doc-d0fb37f39a9b58f6` | [HTML](grouped/doc-d0fb37f39a9b58f6.html) | [HTML](distributed/doc-d0fb37f39a9b58f6.html) |
| S5 | `doc-11acc5eb1d763c80` | [HTML](grouped/doc-11acc5eb1d763c80.html) | [HTML](distributed/doc-11acc5eb1d763c80.html) |
| S6 | `doc-77fddb5aa56906c0` | [HTML](grouped/doc-77fddb5aa56906c0.html) | [HTML](distributed/doc-77fddb5aa56906c0.html) |
| H1 | `doc-f34819b7caee6d4e` | [HTML](grouped/doc-f34819b7caee6d4e.html) | [HTML](distributed/doc-f34819b7caee6d4e.html) |
| H2 | `doc-6511896b62b41ac8` | [HTML](grouped/doc-6511896b62b41ac8.html) | [HTML](distributed/doc-6511896b62b41ac8.html) |
| H3 | `doc-e91461882882ce31` | [HTML](grouped/doc-e91461882882ce31.html) | [HTML](distributed/doc-e91461882882ce31.html) |
| B01 | `doc-d8e986daa86161d8` | [HTML](grouped/doc-d8e986daa86161d8.html) | [HTML](distributed/doc-d8e986daa86161d8.html) |
| B02 | `doc-a2f16f21f8c08f5b` | [HTML](grouped/doc-a2f16f21f8c08f5b.html) | [HTML](distributed/doc-a2f16f21f8c08f5b.html) |
| B03 | `doc-b39a08d30cd2ac2a` | [HTML](grouped/doc-b39a08d30cd2ac2a.html) | [HTML](distributed/doc-b39a08d30cd2ac2a.html) |
| B04 | `doc-9332ee1c144e36bf` | [HTML](grouped/doc-9332ee1c144e36bf.html) | [HTML](distributed/doc-9332ee1c144e36bf.html) |
| B05 | `doc-8ff71a71677f6b47` | [HTML](grouped/doc-8ff71a71677f6b47.html) | [HTML](distributed/doc-8ff71a71677f6b47.html) |
| B06 | `doc-6bb2c5f516d76353` | [HTML](grouped/doc-6bb2c5f516d76353.html) | [HTML](distributed/doc-6bb2c5f516d76353.html) |
| B07 | `doc-dc3259dcf8bc46fc` | [HTML](grouped/doc-dc3259dcf8bc46fc.html) | [HTML](distributed/doc-dc3259dcf8bc46fc.html) |
| B08 | `doc-b73daa78885c45e0` | [HTML](grouped/doc-b73daa78885c45e0.html) | [HTML](distributed/doc-b73daa78885c45e0.html) |
| B09 | `doc-0701bb145f2b99a3` | [HTML](grouped/doc-0701bb145f2b99a3.html) | [HTML](distributed/doc-0701bb145f2b99a3.html) |
| B10 | `doc-3921147a9a5bb431` | [HTML](grouped/doc-3921147a9a5bb431.html) | [HTML](distributed/doc-3921147a9a5bb431.html) |

Ground truth and arithmetic inputs are stored under `evaluation_only/` and `evaluation.json`. Provenance and slot metadata in `document_map.json` are audit-only metadata and were not supplied to the model.
