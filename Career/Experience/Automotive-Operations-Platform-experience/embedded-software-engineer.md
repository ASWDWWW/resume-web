# Embedded Software Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **0.4 / 10** · **Band:** Minimal / not a fit  
**How to use this in hiring:** Do not claim this project as experience for this title

> This score measures how strongly *this repository* maps to a typical **Embedded Software Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Embedded software engineers write C/C++/Rust on microcontrollers or RTOS: peripherals, timing, memory constraints, and hardware bring-up.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Embedded Software Engineer

This repository is cloud and web software for a shop that *services* vehicles. There is no firmware, no MCU, no CAN bus stack, no RTOS.

## Concrete evidence from this project

- Domain proximity only: commercial trucks, VIN metadata, PM dates as data fields.

## Gaps versus a typical hiring bar

Total stack mismatch. Do not claim embedded experience.

## How to talk about this

- Do not use this project for embedded applications except as “I understand the shop’s operational data about trucks.”

## Repo pointers

- `dev/public/app/js/vin-lookup.js` (vehicle metadata, not firmware)
