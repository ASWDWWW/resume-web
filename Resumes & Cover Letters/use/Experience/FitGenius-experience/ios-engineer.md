# iOS Engineer

**Experience rating:** 7.2 / 10 — Solid match  
**Application guidance:** Apply with framing  
**Family:** Mobile  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

iOS Engineer postings usually want Swift, UIKit/SwiftUI, Combine, and Apple framework depth (HealthKit, StoreKit, background modes) written in native UI.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

You shipped a real iOS binary: Swift AppDelegate, HealthKit entitlement, Apple Sign-In, MusicKit token via backend, WeatherKit via backend, StoreKit via react-native-iap, background location, privacy manifest, CocoaPods, EAS iOS build. HealthKit read/write and live HR observer are production concerns, even if called from TypeScript.

## How that work applies to **iOS Engineer**

Apply if the team accepts React Native or wants Health/fitness iOS product work. Skip UIKit-only or 'rewrite in SwiftUI' roles. You can speak HealthKit types, entitlements, and App Store privacy; you cannot show large SwiftUI code.

## Strengths a hiring manager can credit

- HealthKit integration surface
- StoreKit IAP path
- iOS privacy/entitlements hygiene
- Sign in with Apple token lifecycle on the server

## Gaps versus a typical hiring bar

- Little Swift UI code
- No watchOS
- Debugging is often at the RN bridge, not Instruments-first

## How to talk about it

Never pretend you are a SwiftUI engineer. Say 'cross-platform iOS with native HealthKit and StoreKit integrations.'

## Repo evidence

`mobile/ios/FitGenius/AppDelegate.swift`, `plugins/withHealthKit.js`, `src/services/healthKitService.ts`

## Rating rationale

Real iOS product shipping, not native-UI seniority.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
