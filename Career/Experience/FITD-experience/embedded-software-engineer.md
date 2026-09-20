# Embedded Software Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **1 / 10** ●○○○○○○○○○ |
| **Match band** | Not evidenced |
| **Role in one line** | Writes software close to hardware: RTOS, drivers, MCUs, constrained C/C++. |

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

FITD has no embedded codebase. The kiosk is an iPad/SwiftUI app on a purchased touchscreen+camera device. Hardware docs are sourcing and RFQ notes, not board support packages.

There is no C/C++, RTOS, HAL, or device driver work in this repo.

---

## How that applies to this title

Almost nothing applies directly. The only thin transfer is thinking about a device that has a camera, display, and network in a store — still application software.

Do not use FITD as embedded evidence.

---

## Gaps (be honest in interviews)

The entire embedded stack is missing. This title is not a fit from this project.

---

## Evidence in the repo

- `development/apps/FITD-Kiosk/` — SwiftUI iPad kiosk, camera capture, VTO display
- Hardware sourcing docs: touchscreen + camera + network device (no custom firmware)

---

## Interview talking points

- If asked, be explicit: kiosk is application software on COTS hardware.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
