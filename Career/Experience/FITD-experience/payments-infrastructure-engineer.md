# Payments Infrastructure Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **3 / 10** ●●●○○○○○○○ |
| **Match band** | Thin transfer |
| **Role in one line** | Builds payment rails: processors, ledgers, retries, reconciliation, PCI boundaries. |

**Rating scale (this project only):** 10 = you already do the core of this job in production;
8–9 = strong match, hire-ready with normal ramp; 6–7 = real overlap, notable gaps;
4–5 = adjacent experience only; 2–3 = thin transfer; 0–1 = not evidenced here.


---

## Project context

FITD is a fashion AI product you designed, built, and operate: a production iOS app,
a native Android port, an Expo cross-platform scaffold, a marketing site and admin CRM,
Firebase/GCP backend (Auth, Firestore, Storage, Cloud Functions, FCM, Analytics, App Check,
Vertex AI), brand catalog ops (~57 brands / ~16.5k product records), Instagram CRM and
n8n growth automations, AI community bots, and an in-store kiosk concept. This write-up
maps **only work evidenced in FITD-Bible**, not other jobs or coursework.


---

## What you have done in this project

You implemented StoreKit 2 and Play Billing for three brand tiers, plus `validateAppleReceipt` and a website `validateSubscription` via App Store Connect. That is store-billing integration, a real but narrow payments problem (receipt trust, entitlements).

No PSP integrations, no idempotent capture/refund rails, no reconciliation warehouse.

---

## How that applies to this title

You understand why payment state cannot be trusted from the client and you put validation on the server. That is the kernel of payments infra thinking.

The rest of the discipline (card networks, webhooks at scale, money correctness) is absent.

---

## Gaps (be honest in interviews)

No Stripe/Adyen, no ledger, no PCI, no payouts. Keep this as a story inside Backend/SWE, not a target specialty.

---

## Evidence in the repo

- StoreKit 2 brand plans (Starter / Growth / Pro) and Play Billing 7.x
- Apple receipt validation + App Store Connect subscription status function
- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function

---

## Interview talking points

- Receipt validation as a security/payments boundary, then stop.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
