# Software Development Engineer I (SDE I)

**Project-experience rating: 9.1 / 10** (Direct match)

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

Amazon-style SDE I: implements designs, writes tests, understands operational basics, and owns small-to-medium features.

## What you did on TREI that maps here

Your work maps cleanly onto SDE I bar: typed contracts, migrations, IAM-style identity mapping, and operational scripts (webhook proofs, Calendly designated-slot pass, Stripe sandbox fixtures). You treated CI as a gate, not a suggestion.

## How that experience applies to this job

SDE I loops reward candidates who can write correct code, explain tradeoffs, and show operational awareness. TREI gives you Service Bus vs local worker, Key Vault, Container Apps, and fail-closed identity stories without claiming you invented AWS.

## Evidence from this repository

- OIDC token verification and public-client Apple code redemption without sending Origin
- Outbox/worker path and Spike webhook live-path staging proof
- Dependency audit script and security patch chores

## Strengths you can claim honestly

Bias to measurable proof. Comfort with cloud identity and queues.

## Gaps a hiring manager will still probe

Little classic distributed-systems interview drill (leader election, large-scale partitioning). Pilot scale is 1–2k users by design.

## How to talk about it

Translate Azure Container Apps / Service Bus / Key Vault into SDE language: compute, queue, secrets, identity. Keep the customer (clinic) in the story.

## Bottom line

Excellent SDE I evidence. Stronger than a typical new-grad project because the product is clinic-real and gated.
