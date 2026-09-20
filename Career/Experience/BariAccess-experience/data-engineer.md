# Data Engineer

**Project-experience rating: 7.0 / 10** (Strong)

## How to read the rating

The score is **experience this project gave you for this title**, not a career-total grade.

| Band | Score | Meaning |
| --- | --- | --- |
| Direct match | 8.5–10 | You already did this job on TREI. Interviews should lead with this work. |
| Strong | 7.0–8.4 | Substantial overlapping ownership. Name the gaps; do not overclaim seniority. |
| Adjacent | 5.5–6.9 | Real transferable work, but it is not the center of this title. |
| Partial | 4.0–5.4 | Some relevant pieces. Use as supporting evidence, not the headline. |
| Thin | 2.5–3.9 | Indirect overlap only. |
| Minimal | 0–2.4 | This project barely touches the role. |

Scope of evidence: 17 July 2026 – 16 September 2026. You are one of two primary engineers on TREI (BariAccess), with about 203 commits, ~99k lines added, and 658 files touched. Andrei remains the other primary author and owns more of the domain-engine and production-estate volume. Do not claim sole authorship of the whole platform.



## Project in one paragraph

**TREI** is the patient and care-team product in this repository. It is a wellness-first GLP-1 and metabolic-care platform for Bariatric Associates. You helped build a TypeScript monorepo with a Fastify API, PostgreSQL as system of record, a worker plus transactional outbox, an Expo iPhone app, a React staff console, and the public/patient site at trei.care. Staging runs on Azure Container Apps with Entra/External ID, Key Vault, Service Bus, Stripe sandbox, Calendly, Spike wearable adapters, and a guarded Azure OpenAI assistant named Aba.


## What this role typically owns

Pipelines, warehouses, ingestion, quality, orchestration, idempotent ETL/ELT.

## What you did on TREI that maps here

You built operational data paths rather than a warehouse: Spike pulls into PostgreSQL, webhook intake, outbox-to-worker, projections for Today/staff, erasure ledger, and normalized Stripe/Calendly facts without storing raw secrets. Migrations are versioned and tested against Postgres 17.

## How that experience applies to this job

Many Data Engineer jobs in product companies are 'get events into the system of record correctly.' That is TREI. Classic DE jobs that mean dbt + Snowflake + Airflow are only partly matched.

## Evidence from this repository

- packages/data repositories and migrations (connected-health, bookings, billing intents)
- Transactional outbox; idempotent handlers
- Spike cloud query foundation: native units, omit nulls, do not zero-fill
- scripts/reconcile-external-health-erasure-ledger.ts

## Strengths you can claim honestly

Idempotency, late-arriving events, PII/PHI minimization.

## Gaps a hiring manager will still probe

No analytics warehouse modeling, no Spark, no CDC-to-lake, limited orchestration beyond the worker.

## How to talk about it

Call it operational data engineering / event ingestion. Ask if they mean warehouse DE.

## Bottom line

Strong for product-data/ingestion roles. Medium for analytics-warehouse DE.
