# Software Engineer

**Project scored:** TaxTacker (this repository only)  
**Score:** 8.0 / 10  
**Band:** Strong  
**Application guidance:** Target now

This project is primary evidence for the role.

---

## What this job title usually means

A general software engineer designs, builds, tests, and ships features across a codebase. The exact stack varies; the job is owning working software in production.

## What you actually did in this project

You designed and implemented both clients and the Firebase/Functions backend so one user account, one Firestore model, and one billing state work on web and mobile. You owned the product loop: tax-year workspaces, income/expense types (W-2, 1099-NEC, 1099-K, cash, rental, etc.), missing-item tracker, preparer notes, dashboard readiness, CSV/ZIP export for a CPA, onboarding, and paid tiers (Free / Standard / Diamond). GitHub Actions: web lint + Vitest + production build, mobile `tsc --noEmit`, functions syntax check; manual workflow to deploy Firestore/Storage rules with a confirm gate. OPS.md, RUNNING.md, production-status notes, store metadata, IAP/billing setup, support@taxtacker.app, Privacy/Terms with CCPA/GDPR language, demo mode archived out of production.

## How that work applies to this title

This is the cleanest umbrella. You did not just implement screens — you shipped auth, data, billing, security rules, CI, store constraints, and production hardening. That is the software engineer job: take an ambiguous product (tax-season organizer) and make it real, maintainable, and deployable.

## Gaps (be ready to say these out loud)

No evidence here of large team process (code review culture, on-call rotations, multi-service architecture at scale). Interviewers at large companies will still probe algorithms, system design at higher QPS, and collaboration. Bring TaxTacker as the product story, then be ready for those extra drills.

## Interview / resume angle

Walk a hiring manager from user problem → data model → clients → Functions → rules → Stripe/IAP → store review. Emphasize that you owned the whole path, including the unglamorous parts (AdMob Kotlin mismatch, App Store copy, webhook-only entitlements).

## Verdict

Use TaxTacker as a flagship project for Software Engineer applications. It proves you can ship.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
