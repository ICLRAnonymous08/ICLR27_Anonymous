# NAT-087: Strawberry precooling time

**Domain:** Agriculture/food

## Public question

Determine whether the following proposition is true.
Entity: Strawberry carton SC-8
Metric: fruit-center precooling time
Condition: fixed carton pattern, forced-air speed, initial fruit temperature and center thermocouple
Time window: one fresh carton cooling run per acquisition
Target population: designated center fruit in each matched carton
Aggregation: elapsed time until the designated center fruit reaches target temperature
Validity rule: stop only at fruit-center target crossing; air-temperature crossing is not completion
Comparison: strict < 90.0 min

## Document store and condition visibility

Both renderings below contain all 19 document records. They are stores for the retrieval runner, not literal C1 or D6 model prompts. See [visibility.json](visibility.json): Among this case's 19 documents, C1 exposes S1 plus H1–H3 and B01–B10; D6 exposes S1–S6 plus the same H and B documents.

| Slot | Document ID | Grouped rendering | Distributed rendering |
|---|---|---|---|
| S1 | `doc-50040bb357950290` | [HTML](grouped/doc-50040bb357950290.html) | [HTML](distributed/doc-50040bb357950290.html) |
| S2 | `doc-9c85d6f26e974284` | [HTML](grouped/doc-9c85d6f26e974284.html) | [HTML](distributed/doc-9c85d6f26e974284.html) |
| S3 | `doc-b1ea47e9759b3400` | [HTML](grouped/doc-b1ea47e9759b3400.html) | [HTML](distributed/doc-b1ea47e9759b3400.html) |
| S4 | `doc-ecf9eea62ed875c1` | [HTML](grouped/doc-ecf9eea62ed875c1.html) | [HTML](distributed/doc-ecf9eea62ed875c1.html) |
| S5 | `doc-8ee238937c67c14a` | [HTML](grouped/doc-8ee238937c67c14a.html) | [HTML](distributed/doc-8ee238937c67c14a.html) |
| S6 | `doc-39a29445c070c241` | [HTML](grouped/doc-39a29445c070c241.html) | [HTML](distributed/doc-39a29445c070c241.html) |
| H1 | `doc-339e5db5e03eef7c` | [HTML](grouped/doc-339e5db5e03eef7c.html) | [HTML](distributed/doc-339e5db5e03eef7c.html) |
| H2 | `doc-fe671e42da6c0390` | [HTML](grouped/doc-fe671e42da6c0390.html) | [HTML](distributed/doc-fe671e42da6c0390.html) |
| H3 | `doc-0791632009abb2fd` | [HTML](grouped/doc-0791632009abb2fd.html) | [HTML](distributed/doc-0791632009abb2fd.html) |
| B01 | `doc-1da17743831c948f` | [HTML](grouped/doc-1da17743831c948f.html) | [HTML](distributed/doc-1da17743831c948f.html) |
| B02 | `doc-6ec38a4b2772a70e` | [HTML](grouped/doc-6ec38a4b2772a70e.html) | [HTML](distributed/doc-6ec38a4b2772a70e.html) |
| B03 | `doc-693936c993e462d2` | [HTML](grouped/doc-693936c993e462d2.html) | [HTML](distributed/doc-693936c993e462d2.html) |
| B04 | `doc-505f84bba8ab9f77` | [HTML](grouped/doc-505f84bba8ab9f77.html) | [HTML](distributed/doc-505f84bba8ab9f77.html) |
| B05 | `doc-38fd74e32d3898b4` | [HTML](grouped/doc-38fd74e32d3898b4.html) | [HTML](distributed/doc-38fd74e32d3898b4.html) |
| B06 | `doc-31f596c161317cee` | [HTML](grouped/doc-31f596c161317cee.html) | [HTML](distributed/doc-31f596c161317cee.html) |
| B07 | `doc-075cc550b4334bf8` | [HTML](grouped/doc-075cc550b4334bf8.html) | [HTML](distributed/doc-075cc550b4334bf8.html) |
| B08 | `doc-787bc680d23ba35b` | [HTML](grouped/doc-787bc680d23ba35b.html) | [HTML](distributed/doc-787bc680d23ba35b.html) |
| B09 | `doc-af957db1cc741577` | [HTML](grouped/doc-af957db1cc741577.html) | [HTML](distributed/doc-af957db1cc741577.html) |
| B10 | `doc-4d68eb9271353969` | [HTML](grouped/doc-4d68eb9271353969.html) | [HTML](distributed/doc-4d68eb9271353969.html) |

Ground truth and arithmetic inputs are stored under `evaluation_only/` and `evaluation.json`. Provenance and slot metadata in `document_map.json` are audit-only metadata and were not supplied to the model.
