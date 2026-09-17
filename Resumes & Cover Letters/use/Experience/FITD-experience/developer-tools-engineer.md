# Developer Tools Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **5 / 10** ●●●●●○○○○○ |
| **Match band** | Adjacent |
| **Role in one line** | Builds compilers, CLIs, debuggers, IDE integrations, or internal engineering tools. |

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

Tools you built are product-ops tools, not language tools: firestore-scripts (seed, export emails, claims, geo, VTO presets), admin CRM, bot kill-switch UI, prompt packs, IG CRM, n8n workflows, scraper dashboard.

Cursor rules and PDF branding automation (`_generate_pdfs.mjs`) are lightweight developer tooling.

---

## How that applies to this title

If the role means “internal tools for the company,” you have a portfolio. If it means LLVM, Buildkite, or `kubectl` plugins, you do not.

Position FITD admin + scripts as the first version of an internal toolbelt you would grow.

---

## Gaps (be honest in interviews)

No compiler/toolchain, no widely used CLI, no IDE plugin. Title is easy to over-claim — keep the rating modest.

---

## Evidence in the repo

- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding
- `development/apps/react-fitd-website/` — React 19 + Vite + Tailwind marketing site (`fitdai.com`)
- `admin-portal/` — Next.js 14 CRM, RBAC claims, internship review, bot admin, prompt packs
- `development/docs/handbook/` — architecture, handoff, staging, cross-platform plan, file catalog
- Cursor rules, bot runbook, brand product schema

---

## Interview talking points

- Show one script that saved repeated Firebase console work (admin claims or catalog).

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
