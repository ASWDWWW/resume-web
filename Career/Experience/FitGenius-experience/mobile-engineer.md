# Mobile Engineer

**Experience rating:** 9.4 / 10 — Exceptional match  
**Application guidance:** Apply now  
**Family:** Mobile  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

Mobile engineers ship native or cross-platform apps that use device capabilities, app-store constraints, and OS integrations. They own performance, permissions, and release.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

This *is* the core of FitGenius. Expo 54 / RN 0.81 New Architecture, committed `ios/` and `android/` projects, custom config plugins (HealthKit, Health Connect, no advertising ID), EAS Build/Submit, background GPS, IAP, HealthKit/Health Connect, camera/barcode, maps, push, App Check, Crashlytics, Remote Config, 21 locales, 52 Jest tests.

## How that work applies to **Mobile Engineer**

Almost every Mobile Engineer interview can be answered from this repo. Be precise: you are a cross-platform mobile engineer with real native *integration*, not a Swift/Kotlin UI specialist. Many product companies hire exactly that.

## Strengths a hiring manager can credit

- Store-oriented mobile (permissions, privacy manifest, Health Connect, background location)
- Native modules via plugins + Kotlin/Swift app entry
- Offline-ish encrypted local storage for GPS routes
- Release engineering (EAS profiles, OTA)

## Gaps versus a typical hiring bar

- No standalone watchOS/Wear OS
- Custom native modules beyond config plugins are limited
- App not publicly in stores yet

## How to talk about it

Open with 'I shipped a dual-platform fitness client with HealthKit, Health Connect, background GPS, and store IAP.' That sentence is the job.

## Repo evidence

`mobile/`, `mobile/app.config.js`, `mobile/plugins/`, `mobile/eas.json`

## Rating rationale

Highest core-engineering score. Tiny deduction for not-in-store and RN-not-pure-native.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
