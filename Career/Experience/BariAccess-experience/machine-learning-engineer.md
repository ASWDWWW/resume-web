# Machine Learning Engineer

**Project-experience rating: 4.1 / 10** (Partial)

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

Trains, evaluates, deploys ML models: data pipelines, features, training jobs, model registry, monitoring.

## What you did on TREI that maps here

TREI's 'intelligence' is mostly deterministic, versioned evaluators (R&R, Beacon, ISE, governors) plus a generated-language gateway. You worked on product surfaces and some decision/presentation wiring. You did not train models, label datasets, or run GPU jobs.

## How that experience applies to this job

You understand why ML must not own authorization or evidence. That is valuable around ML teams. It is not MLE experience.

## Evidence from this repository

- packages/domain decision owners with algorithmId/algorithmVersion
- Beacon mapper and R&R registry exist; scheduled live R&R publication is not active
- Azure OpenAI as a bounded vendor, not a trained in-house model

## Strengths you can claim honestly

Feature/evidence discipline; you will not silently fill missing labs with a model guess.

## Gaps a hiring manager will still probe

No training, no eval datasets of your own, no model serving infra, no feature store.

## How to talk about it

Apply to Applied AI / AI Product, not classic MLE, unless you have other ML work.

## Bottom line

Partial literacy, not MLE qualification.
