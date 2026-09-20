# Connected-Device Software Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **2.1 / 10** · **Band:** Minimal / not a fit  
**How to use this in hiring:** Do not claim this project as experience for this title

> This score measures how strongly *this repository* maps to a typical **Connected-Device Software Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

These engineers connect physical devices to cloud: telemetry ingest, device identity, MQTT/HTTP, OTA, and device-shadow state.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Connected-Device Software Engineer

The business is physically connected (trucks on the road), but the software does not talk to devices. Telematics and GPS dispatch are explicitly future/out of scope. You modeled trucks and PM due dates, which is the *business* side of connected fleet software.

## Concrete evidence from this project

- Truck registry with VIN, PM, customer linkage.
- NHTSA VIN decode integration (cloud API, not a device).
- Roadmap: emergency dispatch map, fleet telematics PM triggers (unimplemented).

## Gaps versus a typical hiring bar

No device identity, IoT Core, MQTT, or onboard software. Weak/minimal.

## How to talk about this

- Position as fleet operations software, not connected-device software.
- If the role is “cloud for devices,” you only have the cloud operations half.

## Repo pointers

- `dev/public/app/js/vin-lookup.js`
- `dev/docs/IMPLEMENTATION_PLAN.md` §15 v3 telematics
