# Forward Deployed AI Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **8 / 10** ●●●●●●●●○○ |
| **Match band** | Strong match |
| **Role in one line** | FDE whose payload is models: eval in the customer’s domain, RAG/tools, safety, workflow change. |

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

You deployed AI into real workflows: shoppers (stylist, VTO, closet labels), brands (Gemini tagging), marketing (GPT-4o, n8n), and community (bots with approval). You constrained models with domain data (wardrobe, weather, catalog) and added safety (moderation, kill switch, proxy).

That is Forward Deployed AI: the model only counts if the workflow changes.

---

## How that applies to this title

AI labs hiring FDEs for design partners want people who have already put Gemini-class models in front of users and dealt with quality variance (you listed this as a business risk). Fashion is a credible multimodal domain (garments, photos, try-on).

Strong title for you — pair with AI Product Engineer.

---

## Gaps (be honest in interviews)

Customer-premise model deployment (VPC, private endpoints, their data residency) is unproven. Evals are informal. Still a strong match for startup/lab FDE-AI.

---

## Evidence in the repo

- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation
- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding
- `development/apps/FITD-Kiosk/` — SwiftUI iPad kiosk, camera capture, VTO display
- Hardware sourcing docs: touchscreen + camera + network device (no custom firmware)
- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog

---

## Interview talking points

- A design-partner story: we will not chat — we will label closet photos and only then generate outfits.
- What you measure (saves, VTO completion) vs. what you do not (BLEU on captions).

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
