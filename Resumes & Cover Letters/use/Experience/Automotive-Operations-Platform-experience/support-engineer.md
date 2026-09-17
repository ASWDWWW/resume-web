# Support Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **6.2 / 10** · **Band:** Partial match  
**How to use this in hiring:** Use as transferable evidence, not as proof you already do the job

> This score measures how strongly *this repository* maps to a typical **Support Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Support engineers diagnose customer issues, reproduce bugs, write clear workarounds, and escalate with good signal. Technical support roles range from tickets-only to L2 that read logs and ship hotfixes.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Support Engineer

You wrote the artifacts a support team needs: runbook (severities, restore, deploy), staff credentials/demo notes, Stripe test cards, training agenda, hypercare window, “what your retainer covers,” and staging-access style docs. You also built admin tools (employee reset, audit log listing) that are how you would actually support a shop.

## Concrete evidence from this project

- `docs/RUNBOOK.md` incident table and backup notes.
- Health check endpoint for “is prod up?”
- Employee password reset callable.
- Launch-and-care packet: go-live checklist, training, retainer, hypercare.
- Demo mode so support can reproduce without production data.

## Gaps versus a typical hiring bar

No ticket volume, SLAs you have lived, or Zendesk/Jira service history. You designed support; you did not necessarily staff a queue.

## How to talk about this

- Good for Support Engineer interviews if you enjoy customer debugging: you already think in runbooks and reproduction sandboxes.
- Bring the Stripe payment-success verification steps as a sample SOP.

## Repo pointers

- `dev/docs/RUNBOOK.md`
- `dev/docs/STRIPE_SETUP.md`
- `business/Closed Sales/10 Launch and Care/`
- `dev/Development Docs/`
