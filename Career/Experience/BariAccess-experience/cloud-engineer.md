# Cloud Engineer

**Project-experience rating: 6.6 / 10** (Adjacent)

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

Designs and operates cloud services: IAM, containers, managed databases, networking, cost, and environment promotion.

## What you did on TREI that maps here

TREI's runtime is Azure-native. You shipped a site onto Container Apps, dealt with ACR pull permissions, used managed identity for worker/API patterns, and kept staging/production separate. You configured OIDC against Microsoft External ID and workforce Entra.

## How that experience applies to this job

Cloud Engineer interviews want you to reason about identity, secrets, and promotion. You have those stories. You do not have a deep networking/landing-zone specialty or multi-cloud.

## Evidence from this repository

- rg-bariaccess-staging mental model: API, worker, Postgres, Service Bus, Blob, Key Vault, ACR, telemetry, External ID
- trellis-web Azure deploy workflow
- Apple/Google/email customer identity plus staff workforce tenant

## Strengths you can claim honestly

Identity and environment isolation, which is the hard part of cloud for a health product.

## Gaps a hiring manager will still probe

Limited VNet/Private Endpoint/front-door depth in your personal commits. Cost optimization and reserved-capacity work not evidenced.

## How to talk about it

Map the architecture diagram. Mention managed identity instead of long-lived keys.

## Bottom line

Solid cloud-product engineer. Borderline as a dedicated Cloud Engineer vs a full-stack engineer who deploys to Azure.
