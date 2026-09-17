# Forward Deployed Engineer (FDE)

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **8 / 10** ●●●●●●●●○○ |
| **Match band** | Strong match |
| **Role in one line** | Embeds with customers, turns their workflow into a working deployment of the product. |

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

You did the FDE loop for your own company: sit with the customer problem (shoppers, brands, stores), configure and extend the product (catalog schema, import, geo ads, kiosk, CRM), and stay until it works.

Concrete deployments: 57-brand catalog pipeline, brand subscription packaging, in-store kiosk design, internship/lead funnels, Instagram growth stack. You wrote talking points and onboarding so a human can run the motion.

---

## How that applies to this title

FDE (Palantir-style and the AI-lab copies) wants: high agency, product fluency, custom glue, comfort with messy data, and customer-facing communication. FITD is a long FDE tour where you were also the platform.

This is one of your best non-core-SWE titles — especially at AI companies that staff FDEs to land design-partner deployments.

---

## Gaps (be honest in interviews)

You have not been staffed onto *other companies’* environments (their VPC, their SSO, their politics) as an external FDE. Enterprise procurement and classified networks are unproven. The skill is there; the logo-on-the-badge context is different.

---

## Evidence in the repo

- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog
- `development/apps/FITD-Kiosk/` — SwiftUI iPad kiosk, camera capture, VTO display
- Hardware sourcing docs: touchscreen + camera + network device (no custom firmware)
- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding
- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation
- `development/apps/react-fitd-website/` — React 19 + Vite + Tailwind marketing site (`fitdai.com`)
- `admin-portal/` — Next.js 14 CRM, RBAC claims, internship review, bot admin, prompt packs

---

## Interview talking points

- Tell one brand as a deployment: raw site → JSON → schema gaps → import → live shop cards.
- Kiosk as a forward deployment into a physical venue.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
