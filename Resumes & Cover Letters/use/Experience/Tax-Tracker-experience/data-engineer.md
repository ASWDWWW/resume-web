# Data Engineer

**Project scored:** TaxTacker (this repository only)  
**Score:** 3.5 / 10  
**Band:** Adjacent  
**Application guidance:** Adjacent only

Only transferable habits; the role’s core craft is missing.

---

## What this job title usually means

Data engineers build reliable data movement: warehouses, ETL/ELT, orchestration, quality, lakehouse.

## What you actually did in this project

Nested Firestore model `users/{uid}/taxYears/{yearId}/{income,expenses,documents,notes,missingItems,exports}` plus user-level subscription, push tokens, and IAP transaction ledger. Aggregates for dashboard totals. CSV/JSON/ZIP packaging with document binaries. Exports produce CSV/JSON/ZIP. Firestore indexes are declared. Push jobs scan users for due items. That is operational data, not a warehouse.

## How that work applies to this title

You modeled a real-world schema and thought about ownership paths and aggregation fields. Junior data roles sometimes accept strong application data modeling as a start.

## Gaps (be ready to say these out loud)

No Airflow/dbt/Spark/BigQuery pipelines, no CDC, no dimensional modeling, no SLAs on data freshness for analytics consumers.

## Interview / resume angle

Do not apply to DE-II warehouse jobs on this evidence. Fine as a side story.

## Verdict

Adjacent only.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
