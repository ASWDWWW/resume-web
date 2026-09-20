# Platform Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **5 / 10** ●●●●●○○○○○ |
| **Match band** | Adjacent |
| **Role in one line** | Builds internal platforms: paved roads, golden paths, shared runtime for other engineers. |

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

You built a *product* platform (Firebase projects, functions, rules, staging, handbook) that other people (interns, contractor) are meant to use. Firestore scripts, admin claims, bot admin UI, and Cursor rules are internal enablement.

That is proto-platform work at a 1–3 person company. It is not a platform engineering org (Kubernetes, IDP, golden CI, service catalog).

---

## How that applies to this title

Sell the parts that transfer: multi-environment Firebase (`fitd-app-203cb` vs `fitd-app-staging`), documented deploy scripts, shared schema, and admin tooling so non-engineers can operate bots/CRM. You think about “how the next person ships.”

Good fit for startup “platform” meaning shared backend + tooling. Weak fit for Big Tech Platform Engineering.

---

## Gaps (be honest in interviews)

No Kubernetes, Terraform/Pulumi at scale, service mesh, paved CI, developer portal (Backstage), or multi-tenant compute. Do not apply as a k8s Platform Engineer on FITD evidence alone.

---

## Evidence in the repo

- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function
- `development/docs/handbook/` — architecture, handoff, staging, cross-platform plan, file catalog
- Cursor rules, bot runbook, brand product schema
- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding

---

## Interview talking points

- Staging remaining-setup doc as your platform backlog.
- What a real paved road would look like if a second app team joined.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
