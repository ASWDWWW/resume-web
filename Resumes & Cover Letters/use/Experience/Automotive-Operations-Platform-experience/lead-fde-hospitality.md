# Lead Forward Deployed Engineer, Hospitality

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **3.1 / 10** · **Band:** Weak match  
**How to use this in hiring:** Thin overlap — mention only if asked, then pivot

> This score measures how strongly *this repository* maps to a typical **Lead Forward Deployed Engineer, Hospitality** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

A hospitality-specialized FDE lead deploys software into hotels, restaurants, or venues: shift labor, PMS/POS integrations, guest experience, franchise operations.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Lead Forward Deployed Engineer, Hospitality

Your domain is commercial vehicle repair and roadside service, not hospitality. Transferable pieces: shift-like scheduling, role-separated staff, payments, location-based emergency work, training desk staff vs field staff. The industry knowledge (PMS, STR, F&B, brand standards) is absent.

## Concrete evidence from this project

- Staff schedule blocks (shift, lunch, time off, training, shop duty).
- Front-of-house (office) vs field (technician) permission split.
- Local business operations + public web presence.

## Gaps versus a typical hiring bar

Hospitality domain expertise not evidenced. Lead + hospitality together is a weak match. A hospitality company might still like the FDE motion if they train you on hotels.

## How to talk about this

- Do not claim hospitality experience.
- Analogies you *may* use carefully: front desk vs housekeepers ≈ office vs technicians; folio/settlement ≈ invoice/Stripe.

## Repo pointers

- `dev/public/app/js/schedule-service.js`
- `dev/docs/IMPLEMENTATION_PLAN.md` §12 RBAC
