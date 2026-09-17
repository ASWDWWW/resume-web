# Analytics Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **5 / 10** ●●●●●○○○○○ |
| **Match band** | Adjacent |
| **Role in one line** | Turns raw events into trusted metrics: modeling, semantic layer, stakeholder-ready tables. |

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

You defined an analytics *tracking* spec (`ANALYTICS-TRACKING.md`): event names, user properties (`user_type`, `subscription_tier`, …), and product funnels. You ingest web analytics to Firestore rollups the admin CRM charts. Brand analytics exist in-app (clicks, reach).

That is analytics instrumentation plus a light semantic layer in docs — not dbt models.

---

## How that applies to this title

You can partner with growth and investors on KPIs because you named them and wired events. Internship/lead funnels in CRM are analytics-shaped.

True Analytics Engineer (Looker + dbt + warehouse) would be a stretch hire based on FITD alone.

---

## Gaps (be honest in interviews)

No warehouse modeling, no metric store, limited experiment analysis. Firebase Analytics is not a modeled mart.

---

## Evidence in the repo

- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog
- `development/apps/react-fitd-website/` — React 19 + Vite + Tailwind marketing site (`fitdai.com`)
- `admin-portal/` — Next.js 14 CRM, RBAC claims, internship review, bot admin, prompt packs

---

## Interview talking points

- Use the event catalog as your analytics-engineer portfolio artifact.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
