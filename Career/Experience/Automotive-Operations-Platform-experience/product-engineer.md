# Product Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **8.9 / 10** · **Band:** Strong match  
**How to use this in hiring:** Ready to use this as a flagship example

> This score measures how strongly *this repository* maps to a typical **Product Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Product engineers sit on the boundary of product and engineering: they discover what to build with users, ship the slice, measure whether it works, and iterate. They are valued for taste, scope control, and business outcome, not only code volume.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Product Engineer

You behaved as a product engineer. You wrote success criteria (staff run the shop without spreadsheets; auditable money; role separation). You sequenced an MVP vs v1.1 vs v2 against Fullbay/Shop-Ware. You built sales, delivery, training, and hypercare artifacts so the software is a *product* LaunchPage can sell, not a one-off site. Feature checklists, UAT scripts, and a 50%/100% review process are product operations.

## Concrete evidence from this project

- PRD-like implementation plan with epics, acceptance criteria, and competitive roadmap.
- Demo environment and staff walkthrough accounts for sales.
- Closed-sales packet: MSA, SOW, feature scope checklist, UAT, go-live, retainer.
- Configurable modules/settings so the same system can be duplicated per client.
- Explicit out-of-scope list (GPS dispatch, multi-location, native apps) to prevent scope creep.

## Gaps versus a typical hiring bar

You do not have product analytics instrumentation as a shipped loop (funnels, experiments). Firebase Analytics is planned more than proven. No multi-customer usage metrics. Product Engineer at a consumer company will still ask about experiment design.

## How to talk about this

- Story: “I turned a repair shop’s daily work into a licensed product with gates so we do not give away the platform.”
- Show the lead → paid invoice journey from the sales brief.
- Talk about saying no: v1 without telematics, with Stripe Checkout instead of storing PAN.

## Repo pointers

- `dev/docs/IMPLEMENTATION_PLAN.md`
- `business/docs/SALES_MARKETING_PLATFORM_BRIEF.md`
- `business/docs/POST_SALE_DELIVERY_PLAYBOOK.md`
- `business/Closed Sales/`
