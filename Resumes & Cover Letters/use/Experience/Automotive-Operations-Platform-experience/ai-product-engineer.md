# AI Product Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **2.4 / 10** · **Band:** Minimal / not a fit  
**How to use this in hiring:** Do not claim this project as experience for this title

> This score measures how strongly *this repository* maps to a typical **AI Product Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

AI Product Engineers ship user-facing AI features: they pick model/provider, design prompts or tools, handle evals, cost, latency, and failure UX, and keep the feature grounded in a real job-to-be-done.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to AI Product Engineer

The roadmap lists “AI estimate assist (Firebase AI / Gemini — parts suggest from description)” as v3 differentiation. That is product *intent*, not a shipped AI system. There are no prompts, eval sets, model calls, or RAG over work-order history.

## Concrete evidence from this project

- Documented a future AI estimate-assist idea tied to a real workflow (parts from a complaint).
- Built the underlying job/parts data model an AI feature would need.
- No model integration in Cloud Functions or the client.

## Gaps versus a typical hiring bar

No LLM APIs, eval harness, guardrails, embeddings, or human-in-the-loop labeling. This project does not support an AI Product Engineer claim beyond domain context.

## How to talk about this

- Do not list “AI Product Engineer experience” from this repo.
- If targeting those roles, propose how you would add estimate assist *on top of* the existing WO/inventory data — that is a credible take-home.
- Use Product Engineer materials instead.

## Repo pointers

- `dev/docs/IMPLEMENTATION_PLAN.md` §15 v3 — AI estimate assist
