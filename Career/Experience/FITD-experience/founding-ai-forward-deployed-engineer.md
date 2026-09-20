# Founding AI Forward Deployed Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **9 / 10** ●●●●●●●●●○ |
| **Match band** | Strong match |
| **Role in one line** | First FDE at an AI company: invents the motion, deploys the model, feeds product. |

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

This is the closest named role to what you have already been. You were the founding engineer *and* the person who took AI to users and brands. You created the deployment kit: schema, import, kiosk, CRM, prompts, handbook, internship/GTM.

Founding FDE means zero playbook. FITD had zero playbook.

---

## How that applies to this title

Early AI startups use this title when they need a builder who will sit with the first ten customers and also write product code. You have done both on one company. The “AI” modifier is earned (Gemini, Vertex, bots), not cosmetic.

If you join another founding team, this doc is the one to send.

---

## Gaps (be honest in interviews)

You were founding FDE of *your* company. Doing it again means proving you can deploy someone else’s model/product. That is learnable; interview for curiosity about their stack, not only FITD.

---

## Evidence in the repo

- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation
- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog
- `development/apps/FITD-Kiosk/` — SwiftUI iPad kiosk, camera capture, VTO display
- Hardware sourcing docs: touchscreen + camera + network device (no custom firmware)
- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding
- `development/apps/FITD-App/` — production SwiftUI app (~115 Swift files), App Store
- Auth (email, Google, Apple, anonymous), StoreKit 2, WeatherKit, FCM, App Check / DeviceCheck
- Closet, shop, AI stylist, FITD Room virtual try-on, social feed, brand toolkit
- `development/docs/handbook/` — architecture, handoff, staging, cross-platform plan, file catalog
- Cursor rules, bot runbook, brand product schema

---

## Interview talking points

- What you would copy from FITD’s first-customer motion and what was too founder-specific.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
