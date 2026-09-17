# AI/Search Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **3 / 10** ●●●○○○○○○○ |
| **Match band** | Thin transfer |
| **Role in one line** | Information retrieval + ML: indexing, ranking, query understanding, embeddings. |

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

The shop has search UI and heuristic product ranking (`ProductRecommendationEngine`, `recStats`, implicit interest). Brand schema notes future `search.*` / `ai.visual.*` embedding fields — not implemented.

No inverted index you built, no vector database, no query rewriting, no learning-to-rank model.

---

## How that applies to this title

You understand why search/recs matter in a catalog of 16.5k+ SKUs and you started feature plumbing (implicit signals). That is product ranking, not search engineering.

A Search Engineer team would consider this a head start on the problem statement only.

---

## Gaps (be honest in interviews)

Core IR stack missing. Do not target this title until you have built retrieval.

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

- Describe current recs honestly as heuristics; describe the embedding fields you reserved in schema.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
