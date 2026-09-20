# Algorithm Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **5 / 10** ●●●●●○○○○○ |
| **Match band** | Adjacent |
| **Role in one line** | Designs and implements algorithms (ranking, optimization, geometry, signal) as product code. |

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

The main algorithm is client-side recommendation scoring: likes, onboarding tags, implicit interest, collaborative `recStats`. Outfit “random + constraints” and geo-targeting sanitizers are smaller algorithms.

No heavy numerical methods, no published algorithms, no latency-optimized C++.

---

## How that applies to this title

You can discuss ranking as an algorithm with features and failure modes. That is enough for “we need someone who can write the ranking code,” not for a computational-geometry or ads-auction Algorithm Engineer role.

---

## Gaps (be honest in interviews)

Complexity, proofs, and specialized domains are absent. Keep this as a supporting skill on Product/AI titles.

---

## Evidence in the repo

- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation
- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog

---

## Interview talking points

- Write the rec score as a function of signals; say what you would add next (embeddings).

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
