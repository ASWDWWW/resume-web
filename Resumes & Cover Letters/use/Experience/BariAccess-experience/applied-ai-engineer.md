# Applied AI Engineer

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

Takes models into a specific domain: healthcare, legal, finance. Mixes prompt/policy, product, and evaluation against domain rules.

## What you did on TREI that maps here

Aba is applied AI in metabolic/GLP-1 care. Output checks block medical claims, verbatim echo, internal detail, and unaffirmed personal claims. Urgent phrasing routes away from ordinary generation. Voice and text share policy so a spoken question cannot bypass the typed safety path.

## How that experience applies to this job

Applied AI hiring wants domain constraints encoded. You have them. The clinic is the customer, so this is closer to FDE+AI than to a lab.

## Evidence from this repository

- Clinical topic vs product-navigation vs emergency regex routes
- 24-hour retention, six-exchange context, refused replies cannot poison later turns
- Disclosure, microphone, and cost gates in the voice decision record

## Strengths you can claim honestly

Domain-safe application. You can explain why a wellness assistant must not dose-advise.

## Gaps a hiring manager will still probe

Limited offline eval against clinician-labeled transcripts. Physical voice acceptance still open.

## How to talk about it

Bring a concrete forbidden output and the code path that stops it.

## Bottom line

Very good applied-AI story if the team is productizing LLMs in a regulated-ish domain.
