# Machine Learning Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **3 / 10** ●●●○○○○○○○ |
| **Match band** | Thin transfer |
| **Role in one line** | Trains, evaluates, and serves models; owns data → model → production ML systems. |

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

You consume models as APIs (Gemini, Vertex VTO, Imagen/Veo, GPT-4o). You built a scrape → SQLite → image analysis pipeline toward outfit training, and a heuristic recommender (`ProductRecommendationEngine`). Schema comments mention future embeddings.

You did not train, evaluate, or host a custom model in production.

---

## How that applies to this title

Transfer is “I know how models show up in a product and what data I would need to train.” The curator pipeline is the closest MLE-shaped artifact (data collection, image processing). Rec stats are ranking features, not a learned model.

This is not MLE experience in the industry sense.

---

## Gaps (be honest in interviews)

No PyTorch/TF training loops, feature stores, model registry, offline/online metrics, GPU serving, or MLOps. Applied AI / GenAI Engineer is the honest title.

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

- Be precise: API integration + data collection, not model training.
- If they want MLE growth, talk about what you would train (garment attributes) and why you have not yet.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
