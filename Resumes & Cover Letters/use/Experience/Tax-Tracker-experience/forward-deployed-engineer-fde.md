# Forward Deployed Engineer (FDE)

**Project scored:** TaxTacker (this repository only)  
**Score:** 6.5 / 10  
**Band:** Good  
**Application guidance:** Target now

This project is credible evidence; name the gaps in interviews.

---

## What this job title usually means

Forward Deployed Engineers (Palantir-style and startups copying the title) sit with a customer, turn a messy operational problem into working software, and keep it alive in that environment. The skill set is high-agency full-stack plus communication, not a single framework. Baseline FDE roles expect you to code, debug in production, and adapt the product to constraints you did not invent.

## What you actually did in this project

You designed and implemented both clients and the Firebase/Functions backend so one user account, one Firestore model, and one billing state work on web and mobile. App Store Guideline 2.3.10 copy fix (remove Play references on iOS), review accounts that skip email verification and get seeded Diamond demo data, store listing placeholders, EAS submit profiles. OPS.md, RUNNING.md, production-status notes, store metadata, IAP/billing setup, support@taxtacker.app, Privacy/Terms with CCPA/GDPR language, demo mode archived out of production. You repeatedly adapted TaxTacker to *external* systems you do not control: Apple review guidelines, Play/AdMob SDKs, Stripe webhook contracts, Expo/EAS, Firebase App Check. That is the FDE motion (constraint from the environment → working software), even though the 'customer' was stores, reviewers, and end users rather than a Fortune 500 site.

## How that work applies to this title

FDE interviews look for: shipped under ambiguity, talked to a real environment, owned integration pain, wrote enough docs that the system can be operated. You have that. You do not have on-site embedding at a named enterprise.

## Gaps (be ready to say these out loud)

No evidence of deploying *inside a customer VPC*, customizing per-tenant workflows on-site, or managing multiple concurrent customer deployments. Title inflation is common; be honest about 'FDE-like ownership of a product in hostile external platforms' vs 'I was an FDE at Palantir.'

## Interview / resume angle

Tell three constraint stories: (1) entitlements only via Stripe webhooks, (2) App Store review accounts, (3) AdMob/Kotlin EAS break. FDE interviewers hire for that texture.

## Verdict

Credible for FDE roles that accept startup/product backgrounds. Weaker for FDEs that require prior customer-facing consulting.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
