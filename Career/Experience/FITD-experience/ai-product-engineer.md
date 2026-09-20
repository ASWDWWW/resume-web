# AI Product Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **9 / 10** ●●●●●●●●●○ |
| **Match band** | Strong match |
| **Role in one line** | Ships AI-backed user features: models as APIs, UX for uncertainty, evals-lite, product metrics. |

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

AI is in the product, not a slide:

- Closet and brand-image auto-labeling (Gemini 2.0 Flash)
- AI stylist combining wardrobe + weather + Gemini
- Daily colors/styles generation
- FITD Room virtual try-on (Vertex `virtual-try-on-001`, beta)
- Recommendation scoring from likes, onboarding, implicit signals
- Community bots (Gemini captions, Imagen/Veo media) with human approval and kill switches
- GPT-4o captions in Instagram CRM; admin prompt packs
- `geminiProxy` so mobile does not embed the key

You also started an outfit-curator training scrape/pipeline — research toward better styling, not a production trainer.

---

## How that applies to this title

AI Product Engineer is the cleanest “AI + shipped UX” title for you. You handled the real problems of the job: latency and cost (Flash, proxy), failure UX (VTO beta), safety (moderation, approval, kill switch), and grounding (closet inventory + weather, not unconstrained chat).

You can contrast client-side Gemini vs. server-side Vertex — a product-engineering distinction, not a research one.

---

## Gaps (be honest in interviews)

Limited offline eval harness, no systematic prompt/version A/B, no fine-tunes in production, no RAG/search stack. Companies that want “AI product + evals platform” will want you to grow that muscle. Do not claim you trained foundation models.

---

## Evidence in the repo

- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation
- `development/apps/FITD-App/` — production SwiftUI app (~115 Swift files), App Store
- Auth (email, Google, Apple, anonymous), StoreKit 2, WeatherKit, FCM, App Check / DeviceCheck
- Closet, shop, AI stylist, FITD Room virtual try-on, social feed, brand toolkit
- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function
- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding

---

## Interview talking points

- How the stylist is constrained by closet + weather so it is useful, not a generic chatbot.
- Bot kill switch and admin approval as product safety, not an afterthought.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
