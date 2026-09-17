# Forward Deployed Engineer, AI Enablement

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **6 / 10** ●●●●●●○○○○ |
| **Match band** | Solid overlap |
| **Role in one line** | Helps a company adopt AI internally: workflows, guardrails, training, SDLC assistants. |

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

Internal enablement you built: admin prompt packs, Cursor rules, bot platform with approval, handbook, Discord HQ setup, contractor/intern onboarding. You used AI to run marketing and community, not only the consumer app.

That is enablement of FITD-the-company, a single org.

---

## How that applies to this title

AI Enablement FDEs teach and instrument other teams. You have artifacts (prompt packs, rules, runbooks) and have thought about human-in-the-loop (bot approval). Good for roles that want a practitioner who can also write the workshop.

Weaker if they need change management across a 10,000-person company.

---

## Gaps (be honest in interviews)

No enterprise enablement program, no measured adoption across many teams. Agentic SDLC title is the more specific cousin.

---

## Evidence in the repo

- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation
- `development/docs/handbook/` — architecture, handoff, staging, cross-platform plan, file catalog
- Cursor rules, bot runbook, brand product schema
- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding
- `development/apps/react-fitd-website/` — React 19 + Vite + Tailwind marketing site (`fitdai.com`)
- `admin-portal/` — Next.js 14 CRM, RBAC claims, internship review, bot admin, prompt packs

---

## Interview talking points

- Show prompt packs + kill switch as enablement with brakes.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
