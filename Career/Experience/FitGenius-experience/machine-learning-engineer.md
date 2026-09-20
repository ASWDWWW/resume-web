# Machine Learning Engineer

**Experience rating:** 4.2 / 10 — Weak / stretch  
**Application guidance:** Unlikely — only if posting is unusually broad  
**Family:** ML / data  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

MLEs train, evaluate, deploy, and monitor models. They own data pipelines into training, feature stores, and serving latency. Calling a third-party LLM API is usually *not* this job.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

You integrated Gemini via Vertex and wrote deterministic scoring (Fit Score, overload, pace bands, living-profile inference). No training loop, no custom model, no eval dataset platform, no GPU serving.

## How that work applies to **Machine Learning Engineer**

Do not apply to classic MLE roles. If a posting says MLE but the description is 'ship LLM features,' redirect them to Applied AI / AI Engineer. The algorithms you wrote are software, not ML.

## Strengths a hiring manager can credit

- Feature engineering-ish signals for a model (living profile)
- Vertex AI production call path
- Heuristic models with tests

## Gaps versus a typical hiring bar

- No training, fine-tuning, or MLOps
- No experiment tracking
- No custom model metrics

## How to talk about it

Refuse the MLE label unless the company clearly means LLM app engineering.

## Repo evidence

`functions/src/index.ts` (Gemini), `overloadEngine.ts`, `fitScoreService.ts`

## Rating rationale

LLM integration is not MLE. Partial only because of Vertex + heuristics.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
