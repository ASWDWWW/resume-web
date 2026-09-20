# Cloud Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **6 / 10** ●●●●●●○○○○ |
| **Match band** | Solid overlap |
| **Role in one line** | Implements and operates cloud services (IAM, functions, storage, networking, cost). |

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

You operated a real GCP/Firebase estate:

- Production and staging projects, Hosting, Functions (Node 20), Firestore, Storage, Auth, FCM, Analytics, App Check
- Vertex AI for try-on and bot media
- Function secrets, admin custom claims
- Website asset CDN via Storage/GCS
- Deploy scripts for app functions, bot, rules, and the marketing site

That is applied cloud engineering for a production consumer+admin product.

---

## How that applies to this title

Cloud Engineer jobs that are “make us successful on GCP/Firebase/serverless” match. You can discuss IAM-adjacent patterns (rules, claims, App Check), environment strategy, and which workloads belong in Functions vs. the client.

Jobs that are AWS landing-zone, VPC, or Terraform-heavy are a weaker match.

---

## Gaps (be honest in interviews)

Limited multi-cloud, little raw GCP (GKE, Cloud SQL, VPC SC). Cost/FinOps and formal IAM reviews are light. No CI-promoted infra. Be precise: Firebase-centric Cloud Engineer, not a cloud network specialist.

---

## Evidence in the repo

- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function
- Firestore/Storage security rules, admin custom claims, App Check
- Function secrets (`GEMINI_API_KEY`), geo sanitization, bot kill switch / audit log
- `development/apps/react-fitd-website/` — React 19 + Vite + Tailwind marketing site (`fitdai.com`)
- `admin-portal/` — Next.js 14 CRM, RBAC claims, internship review, bot admin, prompt packs

---

## Interview talking points

- Prod vs staging project, bundle IDs, and Hosting domains.
- Vertex in Functions vs. Gemini from clients — cloud trust boundaries.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
