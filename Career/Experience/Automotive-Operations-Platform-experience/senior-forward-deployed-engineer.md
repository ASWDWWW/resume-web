# Senior Forward Deployed Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **7.1 / 10** · **Band:** Solid match  
**How to use this in hiring:** Interview-credible with this as a primary story; expect gap questions

> This score measures how strongly *this repository* maps to a typical **Senior Forward Deployed Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Senior FDEs own difficult deployments, invent repeatable patterns, unblock customers politically and technically, and mentor associates. They are trusted with the company’s reputation on-site.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Senior Forward Deployed Engineer

You invented a repeatable delivery pattern (duplicate, customize, gate money, UAT, retainer) and owned architecture decisions that protect the studio (IP, Stripe on the *shop’s* account, scope checklists). That is senior-shaped *process*. Senior FDE hiring also looks for a track record of multiple thorny customers and influencing the core product roadmap from the field; you have one deep customer/vertical and a roadmap, but not a portfolio of deployments.

## Concrete evidence from this project

- Post-sale playbook as an internal operating standard.
- Risk register and change-control after go-live.
- Packaging (Essentials / Growth / Complete) that maps engineering effort to commercial tiers.
- Technical decisions that survive customer pressure (no manual payment entry).

## Gaps versus a typical hiring bar

No evidence of leading other FDEs, no multi-threaded enterprise stakeholders, no “saved a failing deployment” war story with a named third party. Stretch for Senior; strong for mid FDE.

## How to talk about this

- Argue senior on: you created the methodology, not only executed a playbook.
- Concede: you have not yet run this playbook across many logos.

## Repo pointers

- `business/docs/POST_SALE_DELIVERY_PLAYBOOK.md`
- `business/docs/SALES_PRICING_GUIDE.md`
- `dev/docs/IMPLEMENTATION_PLAN.md` §14 governance
