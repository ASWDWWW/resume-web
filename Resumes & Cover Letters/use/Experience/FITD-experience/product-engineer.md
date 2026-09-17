# Product Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **9 / 10** ●●●●●●●●●○ |
| **Match band** | Strong match |
| **Role in one line** | Engineer who owns user outcomes: discovery, build, ship, measure, iterate. |

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

You defined the product and built it. Shopper loops (closet → outfit → try-on → post), brand loops (register → subscribe → upload → analytics), and web loops (quiz → lead → CRM) were designed as outcomes, not only screens.

You wrote investor/client overviews, marketing feature guides, kiosk PRD, analytics event catalog, and intern/contractor briefs. You treated VTO as beta, froze Android for a better cross-platform bet, and instrumented implicit interest for recommendations.

That is Product Engineer work: sit with the user problem, ship the thinnest real solution, measure.

---

## How that applies to this title

Product Engineer roles (often at startups) want people who will not wait for a perfect spec. FITD is the case study. You can talk KPIs you defined (activation, outfit saves, brand placement) and the features that serve them.

Pair this title with AI Product Engineer when the team is AI-first.

---

## Gaps (be honest in interviews)

Less formal product process (PRDs for every feature, A/B platforms, growth experiments with stats). You are founder-PM + engineer; some Product Engineer teams still have a separate PM. Show you can partner, not only decide alone.

---

## Evidence in the repo

- `development/apps/FITD-App/` — production SwiftUI app (~115 Swift files), App Store
- Auth (email, Google, Apple, anonymous), StoreKit 2, WeatherKit, FCM, App Check / DeviceCheck
- Closet, shop, AI stylist, FITD Room virtual try-on, social feed, brand toolkit
- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation
- `development/apps/react-fitd-website/` — React 19 + Vite + Tailwind marketing site (`fitdai.com`)
- `admin-portal/` — Next.js 14 CRM, RBAC claims, internship review, bot admin, prompt packs
- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog
- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding

---

## Interview talking points

- Tell the closet→Gemini→outfit→VTO loop as a product narrative with the metric each step should move.
- Use brand Starter/Growth/Pro as a packaging + engineering story.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
