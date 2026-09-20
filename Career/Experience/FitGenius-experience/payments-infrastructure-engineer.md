# Payments Infrastructure Engineer

**Experience rating:** 6.6 / 10 — Credible adjacent  
**Application guidance:** Apply with framing  
**Family:** Payments / fintech  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

Owns payment processing internals: processors, webhooks, retries, idempotency, reconciliation, payouts. Often Stripe/Adyen platform depth.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

You built a small but real payments plane: `verifyIapPurchase`, `restoreIapPurchases`, Apple Server Notifications v2 with root CAs, Google Play RTDN Pub/Sub, scheduled expiry sweep, `iap_purchase_owners` dedup, entitlement fields client-write-blocked. No Stripe/Connect.

## How that work applies to **Payments Infrastructure Engineer**

Credible for mobile-payments / IAP infrastructure. Stretch for Stripe-platform jobs. You can talk webhook authenticity, entitlement state machines, and replay/idempotency at startup scale.

## Strengths a hiring manager can credit

- Dual-store verification
- Webhook + sweep architecture
- Entitlements isolated from the client
- QA checklist for purchases

## Gaps versus a typical hiring bar

- Not deployed fully (audit still lists IAP functions as a launch blocker)
- No card-network / ACH
- No reconciliation at processor-scale

## How to talk about it

Walk Apple JWS verify → Firestore entitlement → client ProGate. Mention the launch-blocker honestly if asked about production.

## Repo evidence

`functions/src/iap.ts`, `iapEntitlementPolicy.ts`, certs under `functions/src/certs/`

## Rating rationale

Real payments plumbing on IAP; not processor infra. Launch-blocker honesty caps the score.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
