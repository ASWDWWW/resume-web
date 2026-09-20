# Generative AI / GenAI Engineer

**Project-experience rating: 7.5 / 10** (Strong)

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

Owns LLM/voice/image generation features: prompting, safety, latency, cost, multimodal UX.

## What you did on TREI that maps here

Generative work in TREI is text plus speech. You wired Realtime as TTS-of-checked-text rather than letting the model improvise aloud. That is a GenAI engineering choice with latency, interruption, and echo consequences you then had to debug (ABA recovery, pause, duplicate history).

## How that experience applies to this job

GenAI roles love multimodal demos. You have a more mature variant: generation is allowed only after policy. Cost and rate limits are explicit.

## Evidence from this repository

- Native WebRTC session, semantic VAD, echo filter, manual interruption
- Out-of-band checked speech payload; automatic responses disabled
- Rate limits 12/5 minutes and 60/day

## Strengths you can claim honestly

Multimodal without surrendering authority. Debugging conversational state is real GenAI work.

## Gaps a hiring manager will still probe

No image/video generation. No agent swarms. No fine-tuned voice clone as a product.

## How to talk about it

Contrast naive Realtime conversation vs TREI's checked-speech design. That is the interview.

## Bottom line

Strong GenAI application engineer for voice+text products.
