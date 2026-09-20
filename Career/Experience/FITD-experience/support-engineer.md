# Support Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **5 / 10** ●●●●●○○○○○ |
| **Match band** | Adjacent |
| **Role in one line** | Debugs customer issues, writes repros, improves product/docs from tickets. |

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

You built the tools support would use (admin CRM, bot audit, kill switch) and wrote handbooks. You have not run a ticket queue, SLA, or knowledge base for external users at volume.

Founder support (brands, internships, contractor) is real but informal.

---

## How that applies to this title

You can debug across client, rules, and functions — the skill support engineers need. Docs are better than average. The job itself (queues, empathy at scale, reproduction harnesses) is not evidenced as a practice.

---

## Gaps (be honest in interviews)

No Zendesk/Jira support process, no on-call customer rotation. Overqualified technically for many Support Engineer I seats; under-evidenced for Support Engineering as a career.

---

## Evidence in the repo

- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding
- `development/docs/handbook/` — architecture, handoff, staging, cross-platform plan, file catalog
- Cursor rules, bot runbook, brand product schema
- `development/apps/react-fitd-website/` — React 19 + Vite + Tailwind marketing site (`fitdai.com`)
- `admin-portal/` — Next.js 14 CRM, RBAC claims, internship review, bot admin, prompt packs

---

## Interview talking points

- Pick a production risk from the iOS README (client Gemini key, CORS) and how you would debug a user report.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
