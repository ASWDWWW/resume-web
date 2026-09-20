# Application Developer

**Project-experience rating: 8.6 / 10** (Direct match)

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

Builds business applications: forms, workflows, CRUD-plus-rules, integrations with existing systems of record.

## What you did on TREI that maps here

TREI is a clinical-adjacent business application. You built intake questionnaires with follow-ups, confirmation and handover, membership checkout, staff patient workspace, program assignment, daily check-ins, and appointment booking. Rules live on the server; clients render authorized state.

## How that experience applies to this job

Application Developer roles (often hospital IT, enterprise, or ISVs) care that you can model a workflow, persist it, and keep staff and patient views consistent. Clinic visits, roster matching, and Path A membership are exactly that.

## Evidence from this repository

- Website intakes, follow-up persistence, and confirm-on-save including nested follow-ups
- Practice handover codes bound to patient and practice, with retry and redeem races closed
- Staff operating projections: membership, cohort, Action corrections, Beacon readings

## Strengths you can claim honestly

Domain modeling under healthcare caution. You do not let a form become the source of truth.

## Gaps a hiring manager will still probe

Little classic .NET/Java enterprise stack; little SharePoint/Salesforce. Stack is TypeScript/Postgres/Azure.

## How to talk about it

Walk Path A: public review → roster match → intakes → Calendly remotes → Stripe → staff admission → phone Today.

## Bottom line

Very strong fit wherever the job is 'build the application the business actually runs.'
