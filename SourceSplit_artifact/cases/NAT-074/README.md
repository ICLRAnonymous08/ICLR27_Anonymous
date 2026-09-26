# NAT-074: Peak process memory

**Domain:** Cloud/network systems

## Public question

Determine whether the following proposition is true.
Entity: Service process P-6
Metric: stable-window peak resident memory
Condition: fixed workload, process tree boundary, warm-up and six-sample steady window
Time window: one fresh process run per acquisition
Target population: all RSS samples in the steady window
Aggregation: maximum process RSS in valid samples
Validity rule: measure operating-system resident set for the full target process, not runtime heap only
Comparison: strict < 500.0 MiB RSS

## Document store and condition visibility

Both renderings below contain all 19 document records. They are stores for the retrieval runner, not literal C1 or D6 model prompts. See [visibility.json](visibility.json): Among this case's 19 documents, C1 exposes S1 plus H1–H3 and B01–B10; D6 exposes S1–S6 plus the same H and B documents.

| Slot | Document ID | Grouped rendering | Distributed rendering |
|---|---|---|---|
| S1 | `doc-945039b694c16d9d` | [HTML](grouped/doc-945039b694c16d9d.html) | [HTML](distributed/doc-945039b694c16d9d.html) |
| S2 | `doc-da408783a715eef8` | [HTML](grouped/doc-da408783a715eef8.html) | [HTML](distributed/doc-da408783a715eef8.html) |
| S3 | `doc-f8a5c30f072084f0` | [HTML](grouped/doc-f8a5c30f072084f0.html) | [HTML](distributed/doc-f8a5c30f072084f0.html) |
| S4 | `doc-c808bd1dd34c3f6b` | [HTML](grouped/doc-c808bd1dd34c3f6b.html) | [HTML](distributed/doc-c808bd1dd34c3f6b.html) |
| S5 | `doc-c163adf7db851ff2` | [HTML](grouped/doc-c163adf7db851ff2.html) | [HTML](distributed/doc-c163adf7db851ff2.html) |
| S6 | `doc-2af4a7a70c701970` | [HTML](grouped/doc-2af4a7a70c701970.html) | [HTML](distributed/doc-2af4a7a70c701970.html) |
| H1 | `doc-365082de64c26514` | [HTML](grouped/doc-365082de64c26514.html) | [HTML](distributed/doc-365082de64c26514.html) |
| H2 | `doc-c7a17d2bf8f76162` | [HTML](grouped/doc-c7a17d2bf8f76162.html) | [HTML](distributed/doc-c7a17d2bf8f76162.html) |
| H3 | `doc-06467b6d1a21abaf` | [HTML](grouped/doc-06467b6d1a21abaf.html) | [HTML](distributed/doc-06467b6d1a21abaf.html) |
| B01 | `doc-45b50c598a82585e` | [HTML](grouped/doc-45b50c598a82585e.html) | [HTML](distributed/doc-45b50c598a82585e.html) |
| B02 | `doc-df68286a7c797502` | [HTML](grouped/doc-df68286a7c797502.html) | [HTML](distributed/doc-df68286a7c797502.html) |
| B03 | `doc-59d375cfc2ee55b3` | [HTML](grouped/doc-59d375cfc2ee55b3.html) | [HTML](distributed/doc-59d375cfc2ee55b3.html) |
| B04 | `doc-aa796ae4a60be615` | [HTML](grouped/doc-aa796ae4a60be615.html) | [HTML](distributed/doc-aa796ae4a60be615.html) |
| B05 | `doc-d5b47da083d4d365` | [HTML](grouped/doc-d5b47da083d4d365.html) | [HTML](distributed/doc-d5b47da083d4d365.html) |
| B06 | `doc-ce8a79585af7fbb1` | [HTML](grouped/doc-ce8a79585af7fbb1.html) | [HTML](distributed/doc-ce8a79585af7fbb1.html) |
| B07 | `doc-990cf54674119a29` | [HTML](grouped/doc-990cf54674119a29.html) | [HTML](distributed/doc-990cf54674119a29.html) |
| B08 | `doc-4c8f302475b3ff5d` | [HTML](grouped/doc-4c8f302475b3ff5d.html) | [HTML](distributed/doc-4c8f302475b3ff5d.html) |
| B09 | `doc-fa2b393025d526be` | [HTML](grouped/doc-fa2b393025d526be.html) | [HTML](distributed/doc-fa2b393025d526be.html) |
| B10 | `doc-b507edc2234909fa` | [HTML](grouped/doc-b507edc2234909fa.html) | [HTML](distributed/doc-b507edc2234909fa.html) |

Ground truth and arithmetic inputs are stored under `evaluation_only/` and `evaluation.json`. Provenance and slot metadata in `document_map.json` are audit-only metadata and were not supplied to the model.
