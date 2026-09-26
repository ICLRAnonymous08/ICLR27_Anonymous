# NAT-034: Drying energy use

**Domain:** Industrial systems

## Public question

Determine whether the following proposition is true.
Entity: Dryer DR-6
Metric: specific energy per kilogram of water removed
Condition: locked wet feed, inlet condition and terminal moisture criterion
Time window: one complete batch from loading to endpoint
Target population: all valid batches of the defined material and load
Aggregation: total process electricity divided by measured water mass removed
Validity rule: measure starting and final water mass on the same dry-solids basis
Comparison: strict > 2.5 kWh/kg water

## Document store and condition visibility

Both renderings below contain all 19 document records. They are stores for the retrieval runner, not literal C1 or D6 model prompts. See [visibility.json](visibility.json): Among this case's 19 documents, C1 exposes S1 plus H1–H3 and B01–B10; D6 exposes S1–S6 plus the same H and B documents.

| Slot | Document ID | Grouped rendering | Distributed rendering |
|---|---|---|---|
| S1 | `doc-ac0de21951b2ff09` | [HTML](grouped/doc-ac0de21951b2ff09.html) | [HTML](distributed/doc-ac0de21951b2ff09.html) |
| S2 | `doc-b2387183adecdc8f` | [HTML](grouped/doc-b2387183adecdc8f.html) | [HTML](distributed/doc-b2387183adecdc8f.html) |
| S3 | `doc-b0e5032bdb25e033` | [HTML](grouped/doc-b0e5032bdb25e033.html) | [HTML](distributed/doc-b0e5032bdb25e033.html) |
| S4 | `doc-6e6e54890790dd44` | [HTML](grouped/doc-6e6e54890790dd44.html) | [HTML](distributed/doc-6e6e54890790dd44.html) |
| S5 | `doc-a96562880f461c0c` | [HTML](grouped/doc-a96562880f461c0c.html) | [HTML](distributed/doc-a96562880f461c0c.html) |
| S6 | `doc-dbef69dcef06ef5e` | [HTML](grouped/doc-dbef69dcef06ef5e.html) | [HTML](distributed/doc-dbef69dcef06ef5e.html) |
| H1 | `doc-f11cf9cd31aa6a55` | [HTML](grouped/doc-f11cf9cd31aa6a55.html) | [HTML](distributed/doc-f11cf9cd31aa6a55.html) |
| H2 | `doc-38f622bce6678997` | [HTML](grouped/doc-38f622bce6678997.html) | [HTML](distributed/doc-38f622bce6678997.html) |
| H3 | `doc-346e5bcc2a697a71` | [HTML](grouped/doc-346e5bcc2a697a71.html) | [HTML](distributed/doc-346e5bcc2a697a71.html) |
| B01 | `doc-62d734370c1c786b` | [HTML](grouped/doc-62d734370c1c786b.html) | [HTML](distributed/doc-62d734370c1c786b.html) |
| B02 | `doc-70d778bec7c5ce84` | [HTML](grouped/doc-70d778bec7c5ce84.html) | [HTML](distributed/doc-70d778bec7c5ce84.html) |
| B03 | `doc-2a14664c8a2b033b` | [HTML](grouped/doc-2a14664c8a2b033b.html) | [HTML](distributed/doc-2a14664c8a2b033b.html) |
| B04 | `doc-47805497631118f7` | [HTML](grouped/doc-47805497631118f7.html) | [HTML](distributed/doc-47805497631118f7.html) |
| B05 | `doc-e70e05e47e45595b` | [HTML](grouped/doc-e70e05e47e45595b.html) | [HTML](distributed/doc-e70e05e47e45595b.html) |
| B06 | `doc-3de832891f973114` | [HTML](grouped/doc-3de832891f973114.html) | [HTML](distributed/doc-3de832891f973114.html) |
| B07 | `doc-00640559554f9956` | [HTML](grouped/doc-00640559554f9956.html) | [HTML](distributed/doc-00640559554f9956.html) |
| B08 | `doc-3b02a3e708642735` | [HTML](grouped/doc-3b02a3e708642735.html) | [HTML](distributed/doc-3b02a3e708642735.html) |
| B09 | `doc-a34af23393b37ef0` | [HTML](grouped/doc-a34af23393b37ef0.html) | [HTML](distributed/doc-a34af23393b37ef0.html) |
| B10 | `doc-6078c6c1ee04c289` | [HTML](grouped/doc-6078c6c1ee04c289.html) | [HTML](distributed/doc-6078c6c1ee04c289.html) |

Ground truth and arithmetic inputs are stored under `evaluation_only/` and `evaluation.json`. Provenance and slot metadata in `document_map.json` are audit-only metadata and were not supplied to the model.
