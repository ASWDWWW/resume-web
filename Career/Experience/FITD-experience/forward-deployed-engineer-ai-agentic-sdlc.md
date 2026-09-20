# Forward Deployed Engineer, AI & Agentic SDLC

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **6 / 10** ●●●●●●○○○○ |
| **Match band** | Solid overlap |
| **Role in one line** | Deploys AI into how software is built: agents, code assistants, evals, SDLC guardrails. |

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

You already work in an agentic SDLC: Cursor rules, handbook-as-context, prompt packs in admin, AI bots that post/comment with human gates, and a repo organized so agents can find architecture. You specified bot orchestrators, quotas, and idempotency — agent-ops patterns.

You have not built a commercial agentic-SDLC product (PR agents, repo evaluators) for other engineering orgs.

---

## How that applies to this title

Companies selling coding agents need FDEs who have felt agent-assisted development and can install it safely. Your kill-switch/approval mindset is the correct instinct for SDLC (you do not auto-merge the bot).

Your consumer fashion AI is a parallel story: agents need tools + data + brakes.

---

## Gaps (be honest in interviews)

No deployment of Copilot/Cursor Enterprise/internal agents across a customer’s GitHub, no SDLC metrics (PR cycle time) you own for others. Fashion-bot orchestration ≠ enterprise SDLC platform, but the control-plane ideas transfer.

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

---

## Interview talking points

- How you would introduce an agent to a repo like FITD-Bible: rules, handbook, required human approval on deploys.
- Idempotency and audit logs on bots as the seed of agent observability.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
