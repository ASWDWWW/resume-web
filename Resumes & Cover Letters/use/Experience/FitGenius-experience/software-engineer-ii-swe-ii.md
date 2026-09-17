# Software Engineer II / SWE II

**Experience rating:** 8.4 / 10 — Strong match  
**Application guidance:** Apply now  
**Family:** Core software  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

SWE II typically owns a problem area end-to-end, designs APIs, handles production incidents, and mentors more junior engineers. Scope is a subsystem, not the whole company, but quality bar is high.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

You owned multiple subsystems at SWE II depth: progressive overload (client + Cloud Functions), outdoor GPS + pace engine + segment matching, IAP entitlement policy, moderation/trust-safety, Gemini callable with rate limits, and HealthKit/Health Connect parity. You wrote audits, QA packets, and security logging rather than only feature code.

## How that work applies to **Software Engineer II / SWE II**

Map FitGenius as several SWE II-sized systems, not as 'I built an app.' Interviewers at this level ask for design tradeoffs (why Firebase, why server-side entitlements, why Gemini context allowlists). You have those answers in repo docs. Weakest SWE II signal is operating a live multi-tenant service with SLOs.

## Strengths a hiring manager can credit

- Subsystem design with tests and written audits
- Cross-layer changes (mobile + functions + rules together)
- Production-minded constraints (age gate, App Check plan, rate limits)

## Gaps versus a typical hiring bar

- No peer review culture or on-call rotation to point to
- Limited evidence of mentoring others
- Scale is startup, not millions of QPS

## How to talk about it

Pick one system (overload engine or IAP webhooks) and walk design, failure modes, and tests. That is the SWE II interview.

## Repo evidence

`functions/src/overload/`, `functions/src/iap.ts`, `docs/development/PROGRESSIVE_OVERLOAD_ENGINE_AUDIT.md`

## Rating rationale

Strong SWE II evidence on ownership and design. Not 9+ because companies want live-at-scale and team influence.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
