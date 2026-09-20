# Software Development Engineer I (SDE I)

**Project scored:** TaxTacker (this repository only)  
**Score:** 8.5 / 10  
**Band:** Strong  
**Application guidance:** Target now

This project is primary evidence for the role.

---

## What this job title usually means

Amazon/similar SDE I is an entry IC role: deliver features in an existing service, write tests, follow operational bars (logging, IAM-ish thinking), and grow toward owning a small component.

## What you actually did in this project

Cloud Functions handle authenticated Stripe Checkout and Billing Portal, webhook-driven entitlement updates, IAP activation with replay protection on transaction IDs, recursive account deletion (Firestore + Storage + Auth + Stripe cancel), custom claims for complimentary admin and App Review, and scheduled Expo push reminders (tax calendar + missing items in America/New_York). GitHub Actions: web lint + Vitest + production build, mobile `tsc --noEmit`, functions syntax check; manual workflow to deploy Firestore/Storage rules with a confirm gate. Functions are broken into modules (`planMapping`, `adminAccess`, `iapProducts`, `pushNotifications`, `appReviewSeed`, `ga4Server`) with syntax checks and some tests — an SDE-style service layout even though it is one Functions package.

## How that work applies to this title

Amazon-style interviews care about customer obsession and operational correctness. Your webhook-only billing, App Review path so reviewers can actually use the app, and account-deletion that cancels Stripe then wipes data map well to that culture.

## Gaps (be ready to say these out loud)

No evidence of Amazon-scale distributed systems, leadership principles stories from a team, or Oncall. Coding interview still separate.

## Interview / resume angle

Use STAR: Situation (store would reject unverified email gate) → Task (reviewers must reach Diamond demo) → Action (auth onCreate + claims + seed) → Result (review accounts skip verify and land in-app).

## Verdict

Excellent SDE I portfolio piece. Pair it with interview-drill prep.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
