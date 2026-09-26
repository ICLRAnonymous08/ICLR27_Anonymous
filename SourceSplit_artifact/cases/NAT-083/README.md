# NAT-083: Outlet flow rate

**Domain:** Buildings/energy

## Public question

Determine whether the following proposition is true.
Entity: Outlet fitting F-9
Metric: steady outlet flow
Condition: specified supply pressure, fully open operating state and stabilized collection
Time window: one timed steady-flow collection per acquisition
Target population: all collected water during the timed interval
Aggregation: imperial gallons per minute × 4.54609 L/imperial gallon
Validity rule: record gallon convention explicitly and use the matching conversion factor
Comparison: strict > 9.0 L/min

## Document store and condition visibility

Both renderings below contain all 19 document records. They are stores for the retrieval runner, not literal C1 or D6 model prompts. See [visibility.json](visibility.json): Among this case's 19 documents, C1 exposes S1 plus H1–H3 and B01–B10; D6 exposes S1–S6 plus the same H and B documents.

| Slot | Document ID | Grouped rendering | Distributed rendering |
|---|---|---|---|
| S1 | `doc-26e9536aab5148ac` | [HTML](grouped/doc-26e9536aab5148ac.html) | [HTML](distributed/doc-26e9536aab5148ac.html) |
| S2 | `doc-12aac58f6736c71d` | [HTML](grouped/doc-12aac58f6736c71d.html) | [HTML](distributed/doc-12aac58f6736c71d.html) |
| S3 | `doc-5c33de4a81ae9f1b` | [HTML](grouped/doc-5c33de4a81ae9f1b.html) | [HTML](distributed/doc-5c33de4a81ae9f1b.html) |
| S4 | `doc-f2264b5da7823073` | [HTML](grouped/doc-f2264b5da7823073.html) | [HTML](distributed/doc-f2264b5da7823073.html) |
| S5 | `doc-ce09b678657129df` | [HTML](grouped/doc-ce09b678657129df.html) | [HTML](distributed/doc-ce09b678657129df.html) |
| S6 | `doc-edfcc06d17d843f3` | [HTML](grouped/doc-edfcc06d17d843f3.html) | [HTML](distributed/doc-edfcc06d17d843f3.html) |
| H1 | `doc-464a079803822578` | [HTML](grouped/doc-464a079803822578.html) | [HTML](distributed/doc-464a079803822578.html) |
| H2 | `doc-0e4f1622a3836d4b` | [HTML](grouped/doc-0e4f1622a3836d4b.html) | [HTML](distributed/doc-0e4f1622a3836d4b.html) |
| H3 | `doc-39b430f4c21921c6` | [HTML](grouped/doc-39b430f4c21921c6.html) | [HTML](distributed/doc-39b430f4c21921c6.html) |
| B01 | `doc-6ee355c1aae4d130` | [HTML](grouped/doc-6ee355c1aae4d130.html) | [HTML](distributed/doc-6ee355c1aae4d130.html) |
| B02 | `doc-750962aaa568ce81` | [HTML](grouped/doc-750962aaa568ce81.html) | [HTML](distributed/doc-750962aaa568ce81.html) |
| B03 | `doc-365efa7ad845996f` | [HTML](grouped/doc-365efa7ad845996f.html) | [HTML](distributed/doc-365efa7ad845996f.html) |
| B04 | `doc-759d3dd440f063a9` | [HTML](grouped/doc-759d3dd440f063a9.html) | [HTML](distributed/doc-759d3dd440f063a9.html) |
| B05 | `doc-64f5ac49cf579a9e` | [HTML](grouped/doc-64f5ac49cf579a9e.html) | [HTML](distributed/doc-64f5ac49cf579a9e.html) |
| B06 | `doc-a54e8e47f34c832d` | [HTML](grouped/doc-a54e8e47f34c832d.html) | [HTML](distributed/doc-a54e8e47f34c832d.html) |
| B07 | `doc-48e37dee392a2bb7` | [HTML](grouped/doc-48e37dee392a2bb7.html) | [HTML](distributed/doc-48e37dee392a2bb7.html) |
| B08 | `doc-3ebf6edfc5e531e2` | [HTML](grouped/doc-3ebf6edfc5e531e2.html) | [HTML](distributed/doc-3ebf6edfc5e531e2.html) |
| B09 | `doc-f33da46192d9cddb` | [HTML](grouped/doc-f33da46192d9cddb.html) | [HTML](distributed/doc-f33da46192d9cddb.html) |
| B10 | `doc-e4f81f8cb93ff340` | [HTML](grouped/doc-e4f81f8cb93ff340.html) | [HTML](distributed/doc-e4f81f8cb93ff340.html) |

Ground truth and arithmetic inputs are stored under `evaluation_only/` and `evaluation.json`. Provenance and slot metadata in `document_map.json` are audit-only metadata and were not supplied to the model.
