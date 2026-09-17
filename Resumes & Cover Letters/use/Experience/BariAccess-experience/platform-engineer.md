# Platform Engineer

**Project-experience rating: 6.3 / 10** (Adjacent)

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

Builds internal platforms: paved roads for deploy, identity, observability, golden paths other teams consume.

## What you did on TREI that maps here

You worked on the *product's* platform spine: Container Apps, Bicep touches (apps.bicep, access.bicep, trellis-web.bicep), GitHub Actions deploys, identity configuration scripts, and a modular monolith other features reuse. You hosted trei.care as an isolated staging Container App.

## How that experience applies to this job

Some Platform Engineer interviews will accept 'I helped stand up the runtime other features run on.' Others mean Kubernetes platform teams, IDP portals, and golden-path modules used by dozens of squads. You have the first, not the second.

## Evidence from this repository

- infra/trellis-web.bicep and isolated ACR token until Owner granted AcrPull
- Identity configure scripts for staging External ID
- CI classify/full_verify with Postgres service
- Architecture of swappable adapters behind stable boundaries

## Strengths you can claim honestly

Environment separation, managed identity, fail-closed config.

## Gaps a hiring manager will still probe

Not a multi-tenant internal developer platform. Limited Terraform/K8s/service-mesh depth. Observability package touches are light in your file histogram.

## How to talk about it

Apply if the 'platform' job is cloud runtime + identity + CI for a product team. Skip if it is a 50-person developer-platform org.

## Bottom line

Adjacent. Use as supporting evidence for Cloud/Infra, not as the headline.
