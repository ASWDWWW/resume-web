# Frontend Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **7 / 10** ●●●●●●●○○○ |
| **Match band** | Solid overlap |
| **Role in one line** | Specializes in web UI: components, accessibility, performance, design systems. |

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

Web frontend: React 19 + Vite + Tailwind + Framer Motion marketing site; Next.js 14 App Router admin CRM (stats, leads, internships, bots, prompts). Mobile UI is SwiftUI/Compose — related craft, different title.

You shipped public pages (home, brands, collabs, contact, internships, quiz/lead capture) and a privileged operator UI with role claims. Brand design tokens (Times-style Tinos, brown accent) show you implement a system, not only pages.

---

## How that applies to this title

Frontend Engineer roles that include “the website and the admin tool” match well. You have routing, forms, file upload, charts, and auth-gated dashboards. FITD’s consumer experience is mostly native, so your strongest FE artifacts are `react-fitd-website` and `admin-portal`.

Product-minded frontend teams will like that you also defined the data the UI reads.

---

## Gaps (be honest in interviews)

You are not a dedicated frontend specialist: limited evidence of accessibility audits, design-system libraries, SSR/performance budgets, or complex CSS architecture. No Storybook-level component library. Native SwiftUI should not be sold as “frontend engineering” unless they mean client UI broadly.

---

## Evidence in the repo

- `development/apps/react-fitd-website/` — React 19 + Vite + Tailwind marketing site (`fitdai.com`)
- `admin-portal/` — Next.js 14 CRM, RBAC claims, internship review, bot admin, prompt packs
- `development/docs/handbook/` — architecture, handoff, staging, cross-platform plan, file catalog
- Cursor rules, bot runbook, brand product schema

---

## Interview talking points

- Walk the admin portal information architecture: CRM vs. bots vs. prompts vs. internships.
- Discuss Hosting + Next SSR rewrite as a frontend deploy problem.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
