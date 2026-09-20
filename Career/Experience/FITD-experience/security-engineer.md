# Security Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **4 / 10** ●●●●○○○○○○ |
| **Match band** | Adjacent |
| **Role in one line** | Threat modeling, controls, detection, secure design — security as the job, not a side task. |

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

Security work you did as the product owner:

- Firestore and Storage rules (owner, admin claims, bot collections locked down)
- App Check (DeviceCheck, Play Integrity)
- Admin RBAC (`admin` / `editor` / `viewer`)
- Function secrets; `geminiProxy` to stop shipping keys
- Geo sanitization on the server
- Bot kill switch, quotas, moderation, audit log
- Documented residual risks (historical client Gemini key, CORS)

This is secure-by-construction product work, not a security program.

---

## How that applies to this title

Application Security / startup “security-minded engineer” conversations can use these controls. You can threat-model the FITD trust boundary (client → rules → functions → Vertex).

A Security Engineer hire (detection, pentest, compliance, identity) is a different job.

---

## Gaps (be honest in interviews)

No security tooling career (SIEM, vuln management), no formal threat models, and known gaps remain in the READMEs. Do not claim you are a Security Engineer; claim you ship with security constraints.

---

## Evidence in the repo

- Firestore/Storage security rules, admin custom claims, App Check
- Function secrets (`GEMINI_API_KEY`), geo sanitization, bot kill switch / audit log
- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function

---

## Interview talking points

- Walk a hostile client against `firestore.rules`.
- What you would do next: remove remaining client secrets, add CI secret scanning, tighten CORS.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
