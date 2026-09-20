# Software Engineer

**Project-experience rating: 8.7 / 10** (Direct match)

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

Design, implement, test, and ship software across a product surface. Own bugs through production. Work in a team with reviews, CI, and release discipline.

## What you did on TREI that maps here

You were a working software engineer on a real product, not a tutorial repo. You wrote production TypeScript across the API, worker callers, website, staff console, and iPhone client. You landed features behind tests, CI checkpoints, and fail-closed release gates. Day-to-day work included schema migrations, webhook races, identity, patient copy, staff operating views, and wearable custody.

## How that experience applies to this job

A general Software Engineer interview is looking for: can you take an unclear product need, turn it into contracts and code, prove it, and keep it honest when vendors, clocks, and users misbehave. That is the shape of TREI. Calendly delayed creates, Stripe event ordering, Spike disconnect vs outage, and overlapping Home refreshes are ordinary SWE problems at production difficulty.

## Evidence from this repository

- Full-stack TypeScript monorepo: apps/api, apps/worker, apps/staff-web, apps/patient-mobile, apps/trellis-web, packages/*
- CI proof (`npm run check`), PostgreSQL integration tests, Bugbot follow-ups, Prettier/ESLint gates
- Feature slices with contracts, migrations, application use cases, and client rendering of server-owned state
- Staging Azure deployment path and TestFlight-oriented iOS builds

## Strengths you can claim honestly

Breadth plus correctness habits: fail-closed auth, idempotent webhooks, stale-load guards, versioned evidence. You ship with product language, not only code.

## Gaps a hiring manager will still probe

Two intense months, not years of independent on-call. You worked beside a stronger-volume co-author. Some infrastructure and domain-formula depth is shared rather than solely yours.

## How to talk about it

Pick one vertical slice (membership checkout, Calendly remotes, or connected-health shelf) and walk issuer → API → Postgres → worker → both UIs. Emphasize what you refused to fake.

## Bottom line

This is the cleanest generic label for the work. Use it unless a more specific title is a better match.
