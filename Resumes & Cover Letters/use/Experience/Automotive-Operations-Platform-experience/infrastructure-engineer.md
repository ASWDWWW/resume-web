# Infrastructure Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **3.8 / 10** · **Band:** Weak match  
**How to use this in hiring:** Thin overlap — mention only if asked, then pivot

> This score measures how strongly *this repository* maps to a typical **Infrastructure Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Infrastructure engineers own servers, networks, OS images, capacity, and often IaC for the metal/VMs/cloud accounts underneath applications.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Infrastructure Engineer

You consumed managed infrastructure (Firebase Hosting, Cloud Functions region `us-central1`, Firestore, Storage) and configured it (rules, indexes, headers, secrets, artifact retention). That is application-infra, not infrastructure engineering as a discipline.

## Concrete evidence from this project

- Firebase project wiring: hosting, functions, rules, indexes, storage, emulators.
- HSTS, CSP, cache headers.
- Documented PITR and daily export as backup strategy (enablement still a go-live checkbox).
- Functions artifact cleanup policy script.

## Gaps versus a typical hiring bar

No Terraform/Pulumi/Ansible, no VPC design, no load balancers you operate, no OS hardening, no on-prem. Weak match.

## How to talk about this

- Call it cloud application operations, not infra engineering.
- If a role is “infra for a product team,” mention deploy + backup + health check only as adjacent.

## Repo pointers

- `dev/firebase.json`
- `dev/docs/RUNBOOK.md`
- `dev/docs/FIREBASE_SETUP.md`
