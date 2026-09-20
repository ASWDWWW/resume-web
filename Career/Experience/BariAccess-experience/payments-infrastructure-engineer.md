# Payments Infrastructure Engineer

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

Owns payment processing internals: webhooks, reconciliation, idempotency, retries, processor adapters, ledger bindings.

## What you did on TREI that maps here

Stripe work in this repo is infrastructure-shaped even though the product is membership. You persisted intents before calling Stripe, bound session IDs, verified signatures and sandbox flags, rejected connected-account events, serialized with row locks, and made cancellation terminal for a subscription ID.

## How that experience applies to this job

Payments infra interviews are about exactly those properties. You can talk to Stripe's unordered events and dual invoice schemas. You have not built a processor, a money movement network, or a multi-processor router.

## Evidence from this repository

- Migration 054-era checkout intents and normalized event facts
- Retry of lost Checkout responses without double-creating sessions
- Pending_binding vs processed webhook markers
- scripts/stripe-recreate-sandbox-fixtures.mjs and local webhook script

## Strengths you can claim honestly

Replay safety and schema evolution (legacy vs parent.subscription_details).

## Gaps a hiring manager will still probe

Sandbox-only; no settlement, chargebacks, or PCI controls as a job. Volume is clinic-scale.

## How to talk about it

Lead with event custody, not 'I integrated Stripe Checkout in a weekend.'

## Bottom line

Credible junior-to-mid payments infrastructure story. Combine with Fintech SWE.
