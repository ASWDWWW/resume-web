# Analytics Engineer

**Project-experience rating: 4.8 / 10** (Partial)

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

dbt models, semantic layers, BI-ready tables, metric definitions for business users.

## What you did on TREI that maps here

You implemented product metrics as deterministic domain owners (Beacon display bands, R&R components) and staff/patient projections. Telemetry policy explicitly forbids health values in product analytics. There is no dbt project or Looker layer.

## How that experience applies to this job

You can define metrics carefully, which analytics engineers need. You did not build an analytics platform.

## Evidence from this repository

- Architecture: analytics uses a separate typed event vocabulary; no health values in telemetry
- Beacon/R&R as versioned evaluators, not a warehouse mart

## Strengths you can claim honestly

Metric honesty and privacy.

## Gaps a hiring manager will still probe

dbt, BI tools, stakeholder metric catalogs, dimensional modeling as a job.

## How to talk about it

Use as a supporting story about metric governance, not as the target title.

## Bottom line

Partial. Better as Data Engineer (operational) or Algorithm Engineer.
