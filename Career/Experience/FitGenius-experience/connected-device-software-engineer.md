# Connected-Device Software Engineer

**Experience rating:** 3.6 / 10 — Weak / stretch  
**Application guidance:** Unlikely — only if posting is unusually broad  
**Family:** Hardware / devices  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

Builds software that pairs and talks to hardware: BLE, Wi-Fi devices, companion apps, device identity, firmware-adjacent protocols.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

You integrated *OS health platforms* that already aggregate watches and bands. You did not implement BLE pairing, GATT, or a proprietary wearable SDK. Camera is used for barcodes/photos, not a connected accessory.

## How that work applies to **Connected-Device Software Engineer**

Very thin. You can say you shipped a phone app that *consumes* connected-device data via HealthKit/Health Connect. That is companion-app adjacent, not connected-device engineering.

## Strengths a hiring manager can credit

- Health platform as a device data bus
- Background location as a device capability
- Permission/consent UX for sensors

## Gaps versus a typical hiring bar

- No BLE/Wi-Fi device protocol work
- No pairing UX for a specific hardware SKU
- No firmware handshake

## How to talk about it

Only mention if a posting is 'mobile app for our wearable' and they accept HealthKit-first. Skip IoT/BLE roles.

## Repo evidence

`src/services/healthKitService.ts`, `androidHealthBiometrics.ts`

## Rating rationale

OS-mediated sensors ≠ connected-device stack.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
