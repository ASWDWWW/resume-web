# Software Engineer II / SWE II

**Project scored:** TaxTacker (this repository only)  
**Score:** 7.0 / 10  
**Band:** Good  
**Application guidance:** Target now

This project is credible evidence; name the gaps in interviews.

---

## What this job title usually means

SWE II usually means independent ownership of medium-sized features, some design input, production debugging, and mentoring juniors. At large tech companies this is often the first 'fully independent' IC level (e.g. Google L3/L4 depending on ladder).

## What you actually did in this project

Cloud Functions handle authenticated Stripe Checkout and Billing Portal, webhook-driven entitlement updates, IAP activation with replay protection on transaction IDs, recursive account deletion (Firestore + Storage + Auth + Stripe cancel), custom claims for complimentary admin and App Review, and scheduled Expo push reminders (tax calendar + missing items in America/New_York). Email verification before data access; Firestore rules that freeze billing/admin fields from the client; Storage MIME allowlist and 25 MB cap; CSP, X-Frame-Options DENY, Permissions-Policy; App Check scaffolding; redirect allowlists on checkout URLs; secrets kept out of git in ops docs. Live Stripe products (Standard $9.99/$99.99, Diamond $19.99/$199.99), 7-day trial for first-time customers, webhook signature verification, plan mapping from Price IDs, Customer Portal, and a parallel App Store / Play Billing path (`activateIapEntitlement`) that writes `billingProvider: store` and blocks reused transaction IDs. You made design choices that a SWE II is expected to make: entitlements only from webhooks (not the client), custom claims instead of emails in security rules, redirect allowlists, IAP replay protection.

## How that work applies to this title

The *scope* of TaxTacker is SWE II-shaped: multi-platform product, billing correctness, security, CI, store compliance. The *scale* is not: single Firebase project, modest test suite, no high-throughput services, no team lead evidence.

## Gaps (be ready to say these out loud)

SWE II loops often ask about designing for failure, observability at scale, and working through others' code. Your Crashlytics/Analytics/ops docs help. Lack of multi-engineer collaboration and distributed-systems depth is the main gap.

## Interview / resume angle

Frame it as 'I operated at SWE II ownership on a small system.' Be explicit about what you would change at 100x users (indexes, Cloud Tasks instead of naive scheduled fan-out, full App Store Server API verification).

## Verdict

Credible SWE II candidate if you can discuss tradeoffs and scale-up. Do not claim FAANG-scale backend experience from this repo alone.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
