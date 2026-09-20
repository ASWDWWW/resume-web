# Mobile Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **3.4 / 10** · **Band:** Weak match  
**How to use this in hiring:** Thin overlap — mention only if asked, then pivot

> This score measures how strongly *this repository* maps to a typical **Mobile Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Mobile engineers ship iOS/Android (or serious React Native/Flutter) apps: navigation, offline, device APIs, store release, and platform-specific UX.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Mobile Engineer

The plan calls out field technicians on phones and responsive WO detail, and you designed for spotty-connection future work (Firestore persistence / write queue as later phases). That is mobile-*aware* web, not mobile engineering. Native apps are explicitly out of scope for v1.

## Concrete evidence from this project

- Responsive ops UI intended for technicians updating job status in the field.
- Photo/video capture-friendly media uploads on work orders.
- NFR-O1/O2 documenting offline cache and queued writes as future work.
- Touch-target / WCAG notes in the plan.

## Gaps versus a typical hiring bar

No Swift, Kotlin, React Native, Flutter, App Store/Play pipelines, push notifications as a mobile OS feature, or true offline sync. Do not list Mobile Engineer as a title you have already performed based on this repo alone.

## How to talk about this

- Honest line: “I built a mobile-usable web ops app for technicians; I have not shipped a native client.”
- If applying anyway: emphasize field workflow research and media upload constraints.
- Pivot to Full-Stack / Product Engineer unless the role is hybrid web+mobile.

## Repo pointers

- `dev/docs/IMPLEMENTATION_PLAN.md` §7.5 Offline & Field Use
- `dev/public/app/work-order-detail.html`
- `dev/public/app/js/media-service.js`
