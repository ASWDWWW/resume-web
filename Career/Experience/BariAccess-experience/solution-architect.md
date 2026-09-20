# Solution Architect

**Project-experience rating: 6.4 / 10** (Adjacent)

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

Owns the technical design of a customer or enterprise solution: integration map, NFRs, sign-off, sometimes less hands-on code.

## What you did on TREI that maps here

You operated inside a written architecture (modular monolith, outbox, identity, rings) and added decisions (cloud custody SELECT_MANY, Calendly, Stripe custody). You architected slices. You were not a titled architect signing off a 200-person estate.

## How that experience applies to this job

Some SA roles are senior SEs who can draw the diagram and implement. That is closer. Formal solution-architect jobs that want TOGAF, enterprise integration bus, and stakeholder RACI will see tenure as light.

## Evidence from this repository

- docs/ARCHITECTURE.md durable decisions you coded against
- Identity across two clients and one API
- External vendor map: Stripe, Calendly, Spike, Azure OpenAI, APNs, Entra

## Strengths you can claim honestly

Boundary thinking. You can explain why clients cannot calculate Beacon.

## Gaps a hiring manager will still probe

Seniority, multi-account architecture consulting, little non-Azure enterprise estate work.

## How to talk about it

Prefer 'Forward Deployed Engineer / Solution Architect' combined title over pure SA.

## Bottom line

Architect-shaped thinking at IC implementation seniority, not Principal SA.
