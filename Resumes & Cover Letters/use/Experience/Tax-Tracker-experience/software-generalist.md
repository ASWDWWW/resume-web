# Software Generalist

**Project scored:** TaxTacker (this repository only)  
**Score:** 9.0 / 10  
**Band:** Strong  
**Application guidance:** Target now

This project is primary evidence for the role.

---

## What this job title usually means

A software generalist is hired to do whatever the product needs: UI, API, data, build, store, a bit of ops. Startups and small teams use this explicitly.

## What you actually did in this project

You designed and implemented both clients and the Firebase/Functions backend so one user account, one Firestore model, and one billing state work on web and mobile. Expo 57 app with EAS profiles, iOS/Android Firebase apps, App Attest / Play Integrity App Check notes, Face ID/Touch ID lock, expo-iap subscriptions, AdMob banners for free users, Crashlytics config plugins, image/document pickers, and store-review seed accounts. Live Stripe products (Standard $9.99/$99.99, Diamond $19.99/$199.99), 7-day trial for first-time customers, webhook signature verification, plan mapping from Price IDs, Customer Portal, and a parallel App Store / Play Billing path (`activateIapEntitlement`) that writes `billingProvider: store` and blocks reused transaction IDs. Email verification before data access; Firestore rules that freeze billing/admin fields from the client; Storage MIME allowlist and 25 MB cap; CSP, X-Frame-Options DENY, Permissions-Policy; App Check scaffolding; redirect allowlists on checkout URLs; secrets kept out of git in ops docs. GitHub Actions: web lint + Vitest + production build, mobile `tsc --noEmit`, functions syntax check; manual workflow to deploy Firestore/Storage rules with a confirm gate. OPS.md, RUNNING.md, production-status notes, store metadata, IAP/billing setup, support@taxtacker.app, Privacy/Terms with CCPA/GDPR language, demo mode archived out of production. App Store Guideline 2.3.10 copy fix (remove Play references on iOS), review accounts that skip email verification and get seeded Diamond demo data, store listing placeholders, EAS submit profiles. Breadth is the point of this repo.

## How that work applies to this title

This is the single most accurate description of what you did. You crossed web, mobile, backend, billing, security, CI, and store compliance without staying in one silo.

## Gaps (be ready to say these out loud)

Generalists get questioned on depth. Pick one or two deep stories (billing entitlements, security rules, native build plugins) so you are not 'a mile wide and an inch deep' in the interview.

## Interview / resume angle

Say: 'I am a generalist who shipped a production tax product across three surfaces.' Then go deep on one subsystem.

## Verdict

Highest-confidence label. Lean into it for startups and small product teams.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
