# Algorithm Engineer

**Experience rating:** 7.4 / 10 — Solid match  
**Application guidance:** Apply with framing  
**Family:** ML / data  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

Implements non-trivial algorithms with correctness requirements: optimization, geometry, signal processing, or domain engines with tests and versioned policy.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

Progressive overload engine (versioned policy, load/rep decisions, deload, nutrition signal) on both client and server; outdoor pace engine (bands, weekly volume caps); GPS route validation (speed caps, monotonic timestamps, distance cross-check); segment matching; Fit Score / readiness composites; plate calculator.

## How that work applies to **Algorithm Engineer**

Apply when 'algorithm' means domain engines with tests, not when it means published DSP/CV research. Fitness progression is a real algorithmic product. Interviewers who want LeetCode++ plus production algorithms will like the overload audit.

## Strengths a hiring manager can credit

- Versioned policy (`1.0.0`) and audits
- Client/server parity for overload
- Tests including e2e overload

## Gaps versus a typical hiring bar

- Not numerically heavy (no Kalman, no convex optimization library)
- Not a research algorithms team

## How to talk about it

Bring the overload audit. Explain why the engine overrides the LLM.

## Repo evidence

`functions/src/overload/`, `mobile/src/services/overload/`, `paceEngine.ts`, `PROGRESSIVE_OVERLOAD_ENGINE_AUDIT.md`

## Rating rationale

Real domain algorithms. Not a research Algorithm Engineer bar.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
