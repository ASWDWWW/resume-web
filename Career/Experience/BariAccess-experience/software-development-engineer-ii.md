# Software Development Engineer II (SDE II)

**Project-experience rating: 7.2 / 10** (Strong)

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

Amazon SDE II: owns a component, drives design docs, handles on-call, and delivers cross-team features with limited supervision.

## What you did on TREI that maps here

You wrote and implemented design-level behavior: Stripe billing event custody, Spike cloud query foundation, SELECT_MANY custody, handover activation, and TREI first-release patient frame. Those are design-doc problems, not ticket-sized edits.

## How that experience applies to this job

SDE II wants component ownership and operational judgment. You have the former on several TREI components. You have staging operations and TestFlight, but not a long Amazon-style on-call rotation or org-wide influence.

## Evidence from this repository

- docs/STRIPE-BILLING-EVENT-CUSTODY.md aligned with application-package webhook handling
- Connected-health contracts, migrations, API, worker pulls, staff strip, and phone shelf
- trei.care isolated Container App hosting and noindex/public-host hardening

## Strengths you can claim honestly

Written decisions, versioned contracts, refusal to mix environments.

## Gaps a hiring manager will still probe

SDE II bar also includes mentoring, longer production ownership, and scale stories TREI has not yet been forced to live.

## How to talk about it

Use one design: 'Stripe does not promise event order; here is how membership still stays true.' That is an SDE II interview answer.

## Bottom line

Work quality supports SDE II conversations. Tenure and live-production years are the pushback. Target SDE I / SWE II first unless the team values startup intensity.
