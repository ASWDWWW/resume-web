# Applied AI Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **8 / 10** ●●●●●●●●○○ |
| **Match band** | Strong match |
| **Role in one line** | Applies existing models to a domain: prompts, tools, data constraints, product eval. |

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

Fashion is your domain. You applied vision-language models to garment labeling, outfit assembly with weather context, virtual try-on, and marketing/community generation. Constraints come from real inventory (closet + brand catalog), not open chat.

The recommendation engine applies classical ranking to implicit signals — applied, not theoretical.

---

## How that applies to this title

Applied AI Engineer is the academic/industry name for what you did with Gemini and Vertex. Domain adaptation, prompt design (admin packs), and “make it work on user photos” are the job.

This title is more accurate than Machine Learning Engineer.

---

## Gaps (be honest in interviews)

Formal eval sets for “good outfit” and human-rating pipelines are early. Search/RAG over the 16.5k catalog is not built. Still a strong applied profile.

---

## Evidence in the repo

- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation
- `development/apps/FITD-App/` — production SwiftUI app (~115 Swift files), App Store
- Auth (email, Google, Apple, anonymous), StoreKit 2, WeatherKit, FCM, App Check / DeviceCheck
- Closet, shop, AI stylist, FITD Room virtual try-on, social feed, brand toolkit
- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog

---

## Interview talking points

- How a bad Gemini label would poison the closet and what you do about it.
- Why try-on is a different model class than the stylist.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
