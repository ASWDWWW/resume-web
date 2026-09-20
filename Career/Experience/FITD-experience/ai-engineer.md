# AI Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **7 / 10** ●●●●●●●○○○ |
| **Match band** | Solid overlap |
| **Role in one line** | Broad AI builder: applications, pipelines, and integrations around modern model APIs. |

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

You integrated multiple model families into one product: Gemini for vision+text styling, Vertex for try-on, planned Imagen/Veo for bots, GPT-4o for social captions. You added a server proxy, admin prompt packs, moderation/quotas, and a data-collection pipeline for future taste models.

“AI Engineer” in 2026 often means exactly this: production LLM/VLM features, not papers.

---

## How that applies to this title

Strong match for AI Engineer postings that list LLM apps, tool use, and productization. You have multi-model orchestration (bots), multimodal input (photos), and safety controls.

Weaker match if they mean research or training.

---

## Gaps (be honest in interviews)

Eval platforms, RAG, agents-in-production beyond scheduled bots, and fine-tuning are thin. Title inflation is common — keep stories concrete (which model, which function, which UX).

---

## Evidence in the repo

- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation
- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function
- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding

---

## Interview talking points

- Inventory every model in FITD and why that model, not a larger one.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
