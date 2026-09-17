# AI Product Engineer

**Experience rating:** 8.6 / 10 — Strong match  
**Application guidance:** Apply now  
**Family:** Product / AI product  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

AI Product Engineers put models into a product: UX, evaluation, cost, safety, entitlements, and context — not papers. They care whether the feature works for a user on a subscription tier.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

You productized Gemini via `fitgeniusAi` (coach chat, structured LLM, motivation, food estimate, image fallback), daily content generation, living-profile context allowlists, Pro/Coach server-side gates, rate limits, in-chat medical disclaimer, and a counsel-facing Gemini payload audit. Overload engine numbers override model guesses — a real product-quality decision.

## How that work applies to **AI Product Engineer**

This is applied product AI. You can talk about context minimization, spend control, fallbacks (Unsplash), and not-a-clinician safety. You did not train models. That is exactly what most 2026 AI Product Engineer jobs want.

## Strengths a hiring manager can credit

- Shipped user-facing AI, not a playground
- Safety + legal + entitlement as part of the feature
- Deterministic engines coexisting with LLM

## Gaps versus a typical hiring bar

- Limited offline eval harness / golden-set quality program
- No RAG platform of your own
- Image gen is fallback URLs, not Imagen production

## How to talk about it

Story: 'The model is not allowed to invent loads; the overload engine is source of truth.' That is AI product engineering.

## Repo evidence

`functions/src/aiUserContext.ts`, `entitlements.ts`, `company/legal/protection-suite/md/24_ai-gemini-payload-audit.md`

## Rating rationale

Strong. Deducted for eval/RAG maturity, not for relevance.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
