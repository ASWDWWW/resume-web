# AI/Search Engineer

**Project-experience rating: 3.6 / 10** (Thin)

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

Retrieval, ranking, embeddings, query understanding, search quality, sometimes RAG.

## What you did on TREI that maps here

Architecture mentions bounded retrieval for provider-authored content in later specs. The work you actually shipped is not a search stack: no inverted index, no embeddings pipeline, no ranking experiments. Learning content is assigned Program readings, not search.

## How that experience applies to this job

Only weakly: you understand that generated answers must not retrieve unauthorized patient facts. That is access control, not search.

## Evidence from this repository

- Program Learning as reviewed content, not a search corpus
- No vector database or query-understanding service in the runtime map

## Strengths you can claim honestly

Access-control instincts that search/RAG teams need.

## Gaps a hiring manager will still probe

The search discipline itself.

## How to talk about it

Do not target this title from TREI alone.

## Bottom line

Not qualified as AI/Search from this project.
