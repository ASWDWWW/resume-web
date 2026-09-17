# Fintech Software Engineer

**Experience rating:** 4.8 / 10 — Weak / stretch  
**Application guidance:** Unlikely — only if posting is unusually broad  
**Family:** Payments / fintech  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

Builds financial products: ledgers, KYC, cards, bank rails, money movement, audit, PCI. Compliance is the product.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

You implemented store IAP (Apple/Google), entitlements, purchase ownership dedup, ambassador grants, and drafted Stripe as future work. You did not build a ledger, KYC, or card processing. Investor site is conversations-only, not a brokerage.

## How that work applies to **Fintech Software Engineer**

Payments-adjacent, not fintech. Apply only to consumer-app teams inside fintech that need mobile/IAP, or to 'fintech' postings that are actually product SWE. Skip core banking.

## Strengths a hiring manager can credit

- Money-adjacent correctness (server source of truth)
- Idempotency/ownership collection for purchases
- Legal/billing copy awareness

## Gaps versus a typical hiring bar

- No PCI, no ledger, no bank APIs
- Stripe not implemented
- No financial reporting systems

## How to talk about it

Say 'I built subscription billing on store IAP,' not 'I am a fintech engineer.'

## Repo evidence

`functions/src/iap.ts`, `iapEntitlementPolicy.ts`, `FEATURES.md` Stripe = not started

## Rating rationale

IAP ≠ fintech. Partial credit for money correctness.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
