# Connected-Device Software Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **4 / 10** ●●●●○○○○○○ |
| **Match band** | Adjacent |
| **Role in one line** | Software for devices that talk to the cloud: apps on hardware, device identity, telemetry. |

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

FITD Kiosk is a connected retail device: iPad/kiosk app, camera capture, outfit builder, virtual try-on via the same Firebase + `virtualTryOn` path as the phone app. Docs specify touchscreen + camera + network.

Phones are also connected devices in a weak sense (FCM, App Check), but that is standard mobile, not IoT.

---

## How that applies to this title

You can talk about a device-shaped product: always-on UI, store environment, shared cloud backend, privacy (camera in public). That overlaps the *application* half of connected-device roles (the app on the box).

It does not overlap device firmware, MQTT fleets, or device certificates.

---

## Gaps (be honest in interviews)

No device management, provisioning, IoT Core, offline store mode designed in depth, or fleet updates. Kiosk catalog API is still future (`stores/{storeId}/products`). Rating stays low-mid.

---

## Evidence in the repo

- `development/apps/FITD-Kiosk/` — SwiftUI iPad kiosk, camera capture, VTO display
- Hardware sourcing docs: touchscreen + camera + network device (no custom firmware)
- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function
- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation

---

## Interview talking points

- Kiosk vs. phone: what must be different in a store (session, privacy, no personal Apple ID).

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
