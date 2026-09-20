# Fintech Software Engineer

**Project scored:** TaxTacker (this repository only)  
**Score:** 7.0 / 10  
**Band:** Good  
**Application guidance:** Target now

This project is credible evidence; name the gaps in interviews.

---

## What this job title usually means

Fintech SWEs build products around money, identity, compliance, and ledgers — banking, cards, investing, tax, lending — with extra correctness and audit sensitivity.

## What you actually did in this project

You owned the product loop: tax-year workspaces, income/expense types (W-2, 1099-NEC, 1099-K, cash, rental, etc.), missing-item tracker, preparer notes, dashboard readiness, CSV/ZIP export for a CPA, onboarding, and paid tiers (Free / Standard / Diamond). Live Stripe products (Standard $9.99/$99.99, Diamond $19.99/$199.99), 7-day trial for first-time customers, webhook signature verification, plan mapping from Price IDs, Customer Portal, and a parallel App Store / Play Billing path (`activateIapEntitlement`) that writes `billingProvider: store` and blocks reused transaction IDs. Email verification before data access; Firestore rules that freeze billing/admin fields from the client; Storage MIME allowlist and 25 MB cap; CSP, X-Frame-Options DENY, Permissions-Policy; App Check scaffolding; redirect allowlists on checkout URLs; secrets kept out of git in ops docs. Tax-year records, income types that match IRS forms, expense deductibility fields, CPA export, subscription money path, no-refunds legal clause, account deletion that cancels billing. You explicitly did **not** calculate tax liability or file returns — a compliance-aware product boundary.

## How that work applies to this title

Adjacent fintech: tax-organizer SaaS plus real billing. You treated money and PII (tax docs) as sensitive (verified email, storage MIME/size, CSP, App Check). That mindset is what fintech interviews look for.

## Gaps (be ready to say these out loud)

No ledger, no PCI-DSS scope (Stripe Checkout hosts cards), no KYC/AML, no bank rails, no money movement between users. 'Fintech' at a bank/card network is deeper than this.

## Interview / resume angle

Lead with trust: how entitlements cannot be forged from the client, how documents are gated, how you scoped *out* filing. Fintech interviewers listen for what you refused to DIY.

## Verdict

Good for fintech *application* teams (tax, bookkeeping, SMB finance). Weaker for core banking/payments rails teams (see next title).

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
