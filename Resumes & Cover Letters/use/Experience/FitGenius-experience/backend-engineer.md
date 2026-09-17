# Backend Engineer

**Experience rating:** 8.3 / 10 — Strong match  
**Application guidance:** Apply now  
**Family:** Core software  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

Backend engineers design APIs, data models, jobs, and server-side correctness (authZ, idempotency, money, abuse). They are evaluated on systems thinking more than pixels.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

You built ~64 Cloud Functions: Gemini AI, workout logs + overload engine, outdoor activity validation, segment leaderboards, IAP verify/restore + Apple/Google notifications, social counters, DMs, clubs/challenges, moderation, admin analytics, account deletion, Places/WeatherKit/MusicKit proxies. Firestore rules (~900 lines) encode authorization. Rate limits, event ledger, security logs.

## How that work applies to **Backend Engineer**

A Backend Engineer hiring manager should see a real service layer, not a BaaS-only CRUD app. You still used a managed platform (Firebase) rather than designing your own service mesh. That is fine for product-backend roles; weaker for 'build the platform' backend roles.

## Strengths a hiring manager can credit

- Callable + trigger + HTTP + Pub/Sub + scheduler mix
- Money-adjacent entitlements as server source of truth
- Abuse controls (rate limit, content filter, strikes)
- Tests on entitlements, deletion, moderation, AI context

## Gaps versus a typical hiring bar

- No independently operated SQL/queue/cache cluster
- Single region, single project, no staging
- App Check enforcement still off

## How to talk about it

Walk `verifyIapPurchase` + webhook expiry, or `saveOutdoorActivity` validation. Those are backend interviews.

## Repo evidence

`functions/src/index.ts`, `iap.ts`, `callableSecurity.ts`, `firestore.rules`

## Rating rationale

Strong product-backend. Not staff-backend/infra.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
