# Forward Deployed Engineer / Solution Architect

**Project scored:** TaxTacker (this repository only)  
**Score:** 6.0 / 10  
**Band:** Good  
**Application guidance:** Target now

This project is credible evidence; name the gaps in interviews.

---

## What this job title usually means

Hybrid posting: do FDE implementation *and* own the architecture conversation with the customer (integrations, security, rollout).

## What you actually did in this project

You both architected and implemented the solution: You designed and implemented both clients and the Firebase/Functions backend so one user account, one Firestore model, and one billing state work on web and mobile. Email verification before data access; Firestore rules that freeze billing/admin fields from the client; Storage MIME allowlist and 25 MB cap; CSP, X-Frame-Options DENY, Permissions-Policy; App Check scaffolding; redirect allowlists on checkout URLs; secrets kept out of git in ops docs. Live Stripe products (Standard $9.99/$99.99, Diamond $19.99/$199.99), 7-day trial for first-time customers, webhook signature verification, plan mapping from Price IDs, Customer Portal, and a parallel App Store / Play Billing path (`activateIapEntitlement`) that writes `billingProvider: store` and blocks reused transaction IDs. You can explain *and* build the system — the hybrid this title wants — at product scale.

## How that work applies to this title

Stronger than pure SA because you implemented. Stronger than pure coder because you designed billing/security/store constraints as a system. Matches startup FDE/SA postings better than enterprise SA.

## Gaps (be ready to say these out loud)

Same as FDE + SA: no external enterprise customer landscape. Architecture is of your SaaS, not of a bank’s 40-system estate.

## Interview / resume angle

Lead with a diagram, then drop into code-level stories. That combination is the job.

## Verdict

Good target among the hybrid FDE titles.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
