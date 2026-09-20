# Software Development Engineer II (SDE II)

**Project scored:** TaxTacker (this repository only)  
**Score:** 6.5 / 10  
**Band:** Good  
**Application guidance:** Stretch

This project is credible evidence; name the gaps in interviews.

---

## What this job title usually means

SDE II is expected to own a component or problem space, raise the operational bar, influence design, and deliver with limited oversight. Bar is higher than SDE I on ambiguity and production quality.

## What you actually did in this project

Live Stripe products (Standard $9.99/$99.99, Diamond $19.99/$199.99), 7-day trial for first-time customers, webhook signature verification, plan mapping from Price IDs, Customer Portal, and a parallel App Store / Play Billing path (`activateIapEntitlement`) that writes `billingProvider: store` and blocks reused transaction IDs. Email verification before data access; Firestore rules that freeze billing/admin fields from the client; Storage MIME allowlist and 25 MB cap; CSP, X-Frame-Options DENY, Permissions-Policy; App Check scaffolding; redirect allowlists on checkout URLs; secrets kept out of git in ops docs. You treated billing as a correctness problem (trial once, complimentary Diamond never downgraded by webhooks, client cannot write `subscriptionTier`). That is SDE II judgment.

## How that work applies to this title

You can argue SDE II *behaviors* (ownership, security, customer/store constraints). You cannot yet show SDE II *environment* (large service, high traffic, org influence).

## Gaps (be ready to say these out loud)

Typical SDE II system-design: partitioned data, queues, multi-region, IAM across many accounts. TaxTacker is a well-built Firebase app, not that. Test coverage is still thin for an Amazon bar.

## Interview / resume angle

Be honest: 'This is a production SaaS I owned end-to-end. At SDE II I would add server-side receipt verification, idempotent webhook processing with event IDs, and richer tests.' That honesty reads as SDE II more than overselling.

## Verdict

Possible SDE II at smaller companies or if you have other experience. At Big Tech, treat this as strong supporting evidence, not the whole case.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
