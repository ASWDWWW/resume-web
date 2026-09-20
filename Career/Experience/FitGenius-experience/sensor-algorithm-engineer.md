# Sensor Algorithm Engineer

**Experience rating:** 5.8 / 10 — Partial  
**Application guidance:** Stretch only  
**Family:** Hardware / devices  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

Designs algorithms on raw sensor streams: IMU, PPG, GNSS, camera. Filtering, sensor fusion, on-device inference.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

You processed GPS points (distance, pace, elevation, splits, background task latch), HR zone time-in-zone from health-platform samples, and composite readiness/Fit Score. You did not run on raw IMU/PPG; the OS already fused much of that.

## How that work applies to **Sensor Algorithm Engineer**

Partial. Strongest slice is GNSS activity processing and HR zone aggregation. Weak for 'build the VO2 algorithm from PPG.'

## Strengths a hiring manager can credit

- GPS validation against physically implausible speeds
- Background location session latch (orphan-update problem)
- HR zones and live HR during workouts

## Gaps versus a typical hiring bar

- No raw IMU/PPG pipeline
- VO2 comes from the health platform, not your model
- No sensor fusion paper-level work

## How to talk about it

Frame as 'activity-sensor algorithms on phone GNSS + health samples,' not 'wearable DSP.'

## Repo evidence

`gpsTrackingService.ts`, `backgroundGpsService.ts`, `heartRateZonesService.ts`, `BACKGROUND_GPS_QA.md`

## Rating rationale

GNSS/HR product algorithms, not sensor-research.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
