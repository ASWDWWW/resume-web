# Senior Forward Deployed Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **7 / 10** ●●●●●●●○○○ |
| **Match band** | Solid overlap |
| **Role in one line** | Owns a customer (or a few) end-to-end: technical success, expansion, difficult integrations. |

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

You owned every FITD “customer” class: consumers, brands, and a hypothetical store (kiosk). You made architecture calls when the product was missing a piece (import function, geo sanitize, admin CRM).

Senior FDE means less “I need a spec” and more “I will create the spec with the customer.” That matches how you work.

---

## How that applies to this title

At an early AI company, Senior FDE is often “founding technical deployer.” Your mix of build + GTM + AI features is the profile.

At a mature FDE org, Senior also means repeatable playbooks across many accounts and mentoring associates. You have playbooks (schema, onboarding packet) but not a dozen enterprise accounts.

---

## Gaps (be honest in interviews)

Multi-account enterprise complexity, delivery management, and political navigation inside a Fortune 500 are unproven. Rating is “can do the work, must learn the theater.”

---

## Evidence in the repo

- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog
- `development/apps/FITD-Kiosk/` — SwiftUI iPad kiosk, camera capture, VTO display
- Hardware sourcing docs: touchscreen + camera + network device (no custom firmware)
- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation
- `development/docs/handbook/` — architecture, handoff, staging, cross-platform plan, file catalog
- Cursor rules, bot runbook, brand product schema
- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding

---

## Interview talking points

- How you would run the first 30 days in a design-partner retailer.
- What you would refuse to custom-build vs. take back to product (classic senior FDE judgment).

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
