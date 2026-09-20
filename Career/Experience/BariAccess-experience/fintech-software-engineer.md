# Fintech Software Engineer

**Project-experience rating: 6.5 / 10** (Adjacent)

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

Software for money movement, accounts, ledgers, compliance, banking/fintech products.

## What you did on TREI that maps here

You built membership billing: Stripe Checkout in sandbox, signed webhooks, checkout intents, subscription binding, invoice normalization across Stripe's evolving objects, cancellation terminality, and no complimentary grants from unpaid invoices. Path A prices are encoded. Production live charges remain unauthorized.

## How that experience applies to this job

Fintech SWE is broader than Stripe Checkout, but payment-state machines, idempotency, and 'never infer a grant from a weird event' are the same muscles. You do not have KYC, card issuing, or ledger products.

## Evidence from this repository

- docs/STRIPE-BILLING-EVENT-CUSTODY.md
- Website checkout + legal URL routing
- Application-package webhook handling; no raw PAN storage
- Customer portal / cancellation path in sandbox

## Strengths you can claim honestly

Money-adjacent conservatism. You treated billing as a custody problem.

## Gaps a hiring manager will still probe

Not a bank, not PCI SAQ owner, sandbox only, no multi-currency or payouts.

## How to talk about it

Good for fintech teams that need product engineers who respect ledgers. Weak for core-banking.

## Bottom line

Adjacent-to-strong payments-product experience inside a health company.
