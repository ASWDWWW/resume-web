# Infrastructure Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **4 / 10** ●●●●○○○○○○ |
| **Match band** | Adjacent |
| **Role in one line** | Owns compute, networks, reliability, and the machines/software others deploy onto. |

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

Infrastructure you actually ran: Firebase Hosting, Cloud Functions (us-central1), Firestore, Storage/GCS, FCM, two GCP Firebase projects, domain `fitdai.com` / `staging.fitdai.com`. Manual CLI deploys. No servers you patch.

Kiosk hardware notes cover *buying* a compute+camera device, not racking infrastructure.

---

## How that applies to this title

You understand managed cloud primitives and environment isolation. That helps in infra conversations about “what we don’t want to run ourselves.” You can talk blast radius (prod vs staging, function secrets).

This is cloud-product usage, not infrastructure engineering as a discipline.

---

## Gaps (be honest in interviews)

No IaC estate, no load balancers you configured, no observability stack you own, no capacity planning, no on-prem. A dedicated Infrastructure Engineer role would be a stretch; Cloud Engineer is the more honest nearby title.

---

## Evidence in the repo

- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function
- `development/docs/handbook/` — architecture, handoff, staging, cross-platform plan, file catalog
- Cursor rules, bot runbook, brand product schema

---

## Interview talking points

- What Firebase hides and what you still had to get right (rules, secrets, project split).

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
