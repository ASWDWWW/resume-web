# Security Engineer

**Project-experience rating: 6.6 / 10** (Adjacent)

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

Threat modeling, appsec, identity, secrets, vulnerability management, sometimes detection.

## What you did on TREI that maps here

Security is woven through TREI and through your commits: OIDC verification, public-client Apple redemption, token-free first-cohort contacts, deletion retaining only allowed confirmations, fail-closed Spike lifecycle, webhook signatures, Key Vault, noindex public host, fast-uri host-confusion bump, rate limits on public review, privacy/legal pages. You are not a dedicated red-teamer.

## How that experience applies to this job

AppSec-minded product engineer is the honest label. Security Engineer jobs that want pentest certs, SIEM, or vulnerability research are a stretch. Healthcare data minimization is a plus.

## Evidence from this repository

- OIDC issuer/audience/expiry/signature/scope checks in architecture you coded against
- Stripe/Calendly/Spike signature fail-closed
- Account deletion boundary and identity removal tests
- Public site isolation and unindexed host rules
- Aba session: no patient record, no secrets in logs

## Strengths you can claim honestly

Threat models encoded as tests. Least privilege between platform admin and clinical access.

## Gaps a hiring manager will still probe

No security team role, no pentest ownership, no detection engineering, HIPAA program not yours alone.

## How to talk about it

Apply to product-security-adjacent SWE or healthcare appsec if they want builders. For pure Security Engineer, this is supporting evidence.

## Bottom line

Strong secure-by-construction SWE. Medium dedicated Security Engineer.
