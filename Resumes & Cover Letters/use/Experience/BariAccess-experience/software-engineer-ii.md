# Software Engineer II / SWE II

**Project-experience rating: 7.6 / 10** (Strong)

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

Independent owner of multi-week features. Anticipates edge cases, designs interfaces, mentors juniors, and is trusted with ambiguous product work.

## What you did on TREI that maps here

Several of your slices are SWE II in difficulty: Stripe event custody, Calendly webhook ordering, Spike SELECT_MANY cloud custody, ABA voice using backend-checked speech rather than raw model audio, and staff operating projections that must not go stale. You designed fail-closed behavior instead of happy-path UI.

## How that experience applies to this job

SWE II interviews ask whether you can own a system, not a function. You can talk about webhook idempotency, projection refresh, public-client OIDC, and multi-source wearable shelves. The gap is calendar time and org leverage: SWE II often implies 2+ years of independent production ownership and some mentoring.

## Evidence from this repository

- Stripe sandbox checkout intents, signature verification, and membership binding without storing raw card payloads
- Calendly create/cancel/reschedule races with invitee timestamps and webhook keys
- Whoop / Withings / Samsung offer-connect-callback-disconnect-erase path through Spike
- Staff TREI-07 operating cards, membership recording, and cohort refresh honesty

## Strengths you can claim honestly

Ambiguous product work, integration hardness, refusal to invent Beacon or membership from a late event.

## Gaps a hiring manager will still probe

Short tenure; no documented mentoring of other engineers; production remains dark, so live-incident seniority is limited.

## How to talk about it

Frame as SWE II-shaped ownership on a small team. Be explicit that production cohort is not yet live so you do not oversell on-call years.

## Bottom line

Credible SWE II candidate on work quality. Expect companies to still ask about time-in-role and production incidents.
