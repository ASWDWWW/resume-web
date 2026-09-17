# Associate Forward Deployed Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **9 / 10** ●●●●●●●●●○ |
| **Match band** | Exceeds the bar |
| **Role in one line** | Early-career FDE: supports deployments, learns the product, executes well-scoped customer work. |

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

Associate FDE is scoped customer tasks under a lead. You have already led the motion yourself (catalogs, kiosk, CRM, AI features). The associate bar — SQL/JSON wrangling, demos, tickets, light app config — is well below what FITD required.

---

## How that applies to this title

You would clear an Associate FDE screen on technical range and communication (handbook, investor overview, brand emails). The risk is overqualification / impatience with shadowing.

Apply if you want the FDE career path and accept the level; use FITD to skip “can this person write a script and talk to a customer?”

---

## Gaps (be honest in interviews)

None on capability. Process gap: you have not been an associate on a team. Show you can take notes in someone else’s account plan.

---

## Evidence in the repo

- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog
- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding
- `development/apps/react-fitd-website/` — React 19 + Vite + Tailwind marketing site (`fitdai.com`)
- `admin-portal/` — Next.js 14 CRM, RBAC claims, internship review, bot admin, prompt packs
- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation

---

## Interview talking points

- Bring a 10-minute product demo and a catalog-cleaning story.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
