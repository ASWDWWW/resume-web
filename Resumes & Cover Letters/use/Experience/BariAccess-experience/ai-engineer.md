# AI Engineer

**Project-experience rating: 7.1 / 10** (Strong)

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

Builds systems that use foundation models in production: RAG, tools, gateways, safety, observability, cost.

## What you did on TREI that maps here

You implemented and hardened a production-shaped AI gateway path: classified input routes, output checks, bounded context, rate limits, managed-identity session minting, and a voice renderer that is not allowed to see the patient record. Aba is the patient-facing name.

## How that experience applies to this job

AI Engineer (2025–2026 sense) often means LLM application engineering. That is this, in a stricter domain than most chatbots. You also live in a repo that forbids AI from changing deterministic state.

## Evidence from this repository

- AI gateway module in architecture: approved context, persona, structured output, safety, cost
- generated.ts: GENERATE / BOUNDARY / URGENT / PROMPT_INJECTION
- Realtime: 60-second client secret, echo discard, interaction-id join
- Staff/patient copy never lets Aba become clinical authority

## Strengths you can claim honestly

High-stakes LLM app design. Clear authority boundary.

## Gaps a hiring manager will still probe

Little RAG corpus engineering, tool-calling agents, or model-routing platforms. No published eval numbers.

## How to talk about it

Title the work 'guarded LLM application in healthcare,' not 'AI researcher.'

## Bottom line

Strong LLM-app AI Engineer. Weak classical ML AI Engineer.
