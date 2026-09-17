# Backend Engineer

**Project-experience rating: 8.4 / 10** (Strong)

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

Owns APIs, data models, authz, jobs, and integration reliability. UI is a consumer, not the job.

## What you did on TREI that maps here

You spent serious time in packages/application, packages/data, packages/contracts, apps/api, and webhook/worker-adjacent code. Examples: Spike adapter and live path, Stripe handling kept inside the application package, Calendly event keys, SELECT_ONE vs SELECT_MANY custody, patient admission before intakes complete.

## How that experience applies to this job

Backend interviews care about auth, consistency, and jobs. TREI's durable decisions (server authorization, transactional outbox, idempotent handlers, versioned decision results) are the interview language. You implemented product on top of that spine.

## Evidence from this repository

- Fastify modular API with OIDC verification and use-case authorization
- PostgreSQL migrations (including 075+ connected-health history in tests)
- Webhook signature verification for Stripe and Calendly; Spike HMAC path
- Erasure, disconnect, and fail-closed provider lifecycle events

## Strengths you can claim honestly

Correctness under replay, delayed events, and missing vendor data. Healthcare-safe defaults.

## Gaps a hiring manager will still probe

You also did a large amount of UI, so some teams will want deeper pure-backend (query plans, multi-region, JVM/Go services). Worker file-touch count is smaller than API/data.

## How to talk about it

Do not hide the UI work, but interview as: I own the record, the job, and the contract; clients are projections.

## Bottom line

Strong backend story. Pair it with full-stack rather than pretending you never touched React.
