# Backend Engineer

**Project scored:** TaxTacker (this repository only)  
**Score:** 7.0 / 10  
**Band:** Good  
**Application guidance:** Target now

This project is credible evidence; name the gaps in interviews.

---

## What this job title usually means

Backend engineers own APIs, data integrity, authz, jobs, and integrations. They think in contracts, idempotency, and failure modes more than pixels.

## What you actually did in this project

Cloud Functions handle authenticated Stripe Checkout and Billing Portal, webhook-driven entitlement updates, IAP activation with replay protection on transaction IDs, recursive account deletion (Firestore + Storage + Auth + Stripe cancel), custom claims for complimentary admin and App Review, and scheduled Expo push reminders (tax calendar + missing items in America/New_York). Email verification before data access; Firestore rules that freeze billing/admin fields from the client; Storage MIME allowlist and 25 MB cap; CSP, X-Frame-Options DENY, Permissions-Policy; App Check scaffolding; redirect allowlists on checkout URLs; secrets kept out of git in ops docs. Nested Firestore model `users/{uid}/taxYears/{yearId}/{income,expenses,documents,notes,missingItems,exports}` plus user-level subscription, push tokens, and IAP transaction ledger. Aggregates for dashboard totals. CSV/JSON/ZIP packaging with document binaries. Notable backend details: Bearer ID-token verification, email-verified gate, Stripe customer reuse, webhook event handling (`checkout.session.completed`, subscription created/updated/deleted), `iapTransactions` uniqueness, `recursiveDelete` on account close, Cloud Scheduler-style `onSchedule` push fan-out.

## How that work applies to this title

A backend interviewer can grill you on billing correctness and security rules and you have real answers. That is more backend than a CRUD tutorial.

## Gaps (be ready to say these out loud)

No independently scaled HTTP service, no SQL schema migrations, no message queue, limited automated tests on Functions (plan mapping / admin access, not full webhook integration tests). Language is JavaScript, not Go/Java/Kotlin often used in backend teams.

## Interview / resume angle

Offer to whiteboard the entitlement state machine: free → trial → active → past_due → inactive, plus complimentary and store IAP overlays.

## Verdict

Good backend evidence for Node/Firebase shops. For JVM/Go backend teams, this is adjacent unless you translate the designs.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
