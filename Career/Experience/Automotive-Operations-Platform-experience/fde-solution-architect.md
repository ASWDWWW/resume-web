# Forward Deployed Engineer / Solution Architect

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **8.1 / 10** · **Band:** Solid match  
**How to use this in hiring:** Interview-credible with this as a primary story; expect gap questions

> This score measures how strongly *this repository* maps to a typical **Forward Deployed Engineer / Solution Architect** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Hybrid roles that expect FDE customer embedding *and* architecture artifacts: you can sit with the customer and also own the technical design of the deployment.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Forward Deployed Engineer / Solution Architect

This hybrid is a very accurate description of what you did. You architected Firebase/Stripe/RBAC *and* packaged discovery, UAT, and go-live. Few candidates have both the code and the closed-sales architecture.

## Concrete evidence from this project

- Technical architecture (implementation plan) plus delivery architecture (playbook + flowchart).
- Security and PCI decisions made in the context of a real shop, not a vacuum.
- Feature-scope checklist as the contract between architecture and what gets deployed.

## Gaps versus a typical hiring bar

Enterprise integration architecture (IdP, data lakes, existing CMMS) is lighter. For Palantir/SI hybrids that expect huge customer landscapes, still tell the truth about scale.

## How to talk about this

- Best dual-title to put near the top of a resume targeting FDE-like companies.
- Walk one diagram from each world: data model, and the 10-stage delivery flow.

## Repo pointers

- `dev/docs/IMPLEMENTATION_PLAN.md`
- `business/docs/POST_SALE_DELIVERY_PLAYBOOK.md`
- `business/docs/POST_SALE_FLOWCHART.html`
- `business/Closed Sales/02 Contract Packet/04-Feature-Scope-Checklist.md`
