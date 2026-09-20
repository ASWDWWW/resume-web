# Infrastructure Engineer

**Project-experience rating: 5.9 / 10** (Adjacent)

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

Owns networks, compute, databases, backups, IAM at the estate level. Often closer to SRE/sysadmin than product features.

## What you did on TREI that maps here

You contributed to Bicep app/access modules, staging website hosting, Containerfile awareness, and scripts that assume Key Vault and managed identity. Dark production and database privilege proof exist in the repo; Andrei's volume is larger on that estate.

## How that experience applies to this job

You can speak to Azure resource topology (Container Apps, Postgres Flexible Server, Service Bus, Blob, Key Vault, Monitor) and why local adapters cannot start as staging. That is infrastructure literacy. It is not years of running the estate.

## Evidence from this repository

- infra/apps.bicep, access.bicep, trellis-web.bicep file history
- Staging Container App for the public site
- docs/RUNBOOK.md and deploy workflow familiarity

## Strengths you can claim honestly

Respect for environment boundaries and secrets. You did not treat localhost as production.

## Gaps a hiring manager will still probe

No evidence you are the primary owner of Postgres HA, VNet, WAF, backup drills, or capacity planning. Recovery exercises are documented as organizational, not as your personal completed drills.

## How to talk about it

Be precise: I helped define and deploy app infrastructure; I am not the lone infra owner.

## Bottom line

Enough to pair with Cloud Engineer. Not enough to be a dedicated Infra hire.
