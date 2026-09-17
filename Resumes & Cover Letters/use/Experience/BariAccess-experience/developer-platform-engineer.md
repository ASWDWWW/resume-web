# Developer Platform Engineer

**Project-experience rating: 5.1 / 10** (Partial)

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

Builds tools, paved paths, and self-service so other developers ship faster: golden templates, IDP, internal CLIs, preview environments.

## What you did on TREI that maps here

You improved the developer path for this one repo: npm workspaces, CI lanes (docs vs full), seed/migrate scripts, local Stripe/Calendly webhook scripts, and Metro/EAS development client flow. That is developer experience for a two-person team, not a platform used by many teams.

## How that experience applies to this job

DX work transfers, but Developer Platform Engineer at a mid-size company usually means productizing those paths. TREI did not require an internal developer portal.

## Evidence from this repository

- Root package.json scripts for db, smoke, webhooks, identity configure
- CI proof-lane classification
- Local preview:mobile with synthetic display data

## Strengths you can claim honestly

You feel friction and script it. You keep secrets out of Git.

## Gaps a hiring manager will still probe

No Backstage/IDP, no multi-repo golden path, no self-service preview apps for many squads.

## How to talk about it

Position as 'I care about the paved path' inside a product-engineer story.

## Bottom line

Partial. Do not apply as a specialist unless you have other DX work.
