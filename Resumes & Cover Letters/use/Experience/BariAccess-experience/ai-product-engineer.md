# AI Product Engineer

**Project-experience rating: 8.0 / 10** (Strong)

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

Ships AI-backed product features with UX, evals/safety, cost, and a clear job-to-be-done. Models are a dependency, not the identity of the role.

## What you did on TREI that maps here

You helped make Aba a product, not a chatbot demo. Typed and voice conversation share a guarded backend. Voice transcribes, checks echo, sends the transcript through the same policy as text, and only then asks Realtime to speak the checked body. Rate limits, 24-hour retention, start-fresh, and medical-claim output checks are product decisions in code.

## How that experience applies to this job

AI Product Engineer interviews ask: what must never happen, who is the authority, and how does the UI stay honest when the model is wrong. TREI's answer is: the backend is the authority; Realtime is a renderer; urgent/clinical/injection routes are classified before generation.

## Evidence from this repository

- TREI-05 one ABA text and voice conversation
- packages/domain/src/ai/generated.ts route and output checks (urgent, injection, medical claims)
- docs/OLLIE-VOICE-AND-COST.md: ephemeral client secrets, no patient record in the Realtime session
- Recovery, pause, and restricted-conversation client fixes

## Strengths you can claim honestly

Safety and product constraints first. Cost and session lifetime are designed, not hoped.

## Gaps a hiring manager will still probe

No large eval harness, no prompt-ops team, no fine-tuning. Physical iOS voice proof is still called out as open in the voice doc.

## How to talk about it

Never say 'we added ChatGPT.' Say 'we added a bounded assistant that cannot become the record.'

## Bottom line

Strong AI-product story for healthcare and other high-stakes UX.
