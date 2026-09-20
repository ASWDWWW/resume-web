# Generative AI / GenAI Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **8 / 10** ●●●●●●●●○○ |
| **Match band** | Strong match |
| **Role in one line** | Specializes in generative models: text, image, video — prompts, safety, productization. |

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

Generative surfaces in FITD:

- Text/vision: Gemini stylist, labels, daily colors, bot captions
- Image: Vertex virtual try-on; bot spec for Imagen
- Video: bot spec for Veo
- Marketing: GPT-4o captions; n8n OpenAI → Reddit/LinkedIn

Safety/productization: `geminiProxy`, bot moderation, quotas, idempotency, admin approval, kill switch.

---

## How that applies to this title

GenAI Engineer postings that want “we use frontier APIs in production” are a direct fit. You have more than a chatbot: structured generation into product objects (category, colors, outfits) and image generation for try-on.

Community bots are a GenAI ops story (scheduled generation + human gate).

---

## Gaps (be honest in interviews)

No LoRA/fine-tune, no advanced agent graphs in the SDLC product sense, limited eval. Image/video bot generation may be spec-ahead of fully proven production quality — say what is shipped vs. specified.

---

## Evidence in the repo

- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation
- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding
- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function

---

## Interview talking points

- Structured output for closet labels vs. freeform captions — two GenAI modes.
- Kill switch as the GenAI production control plane.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
