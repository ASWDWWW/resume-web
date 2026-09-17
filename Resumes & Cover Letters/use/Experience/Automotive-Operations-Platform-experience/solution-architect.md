# Solution Architect

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **6.9 / 10** · **Band:** Partial match  
**How to use this in hiring:** Use as transferable evidence, not as proof you already do the job

> This score measures how strongly *this repository* maps to a typical **Solution Architect** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Solution Architects design how a product (or several products) lands in a customer’s landscape: integration, security, data, identity, and non-functionals. They produce diagrams and decision records more than they write all the code.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Solution Architect

You authored a real architecture: layers, collections, RBAC matrix, threat model, PCI SAQ A decision, NFRs, vendor failure handling, and environment strategy (emulators vs prod, no hosted staging). That is solution architecture for an SMB shop on Firebase. It is not multi-cloud enterprise architecture spanning SAP, SSO, and data residency regimes.

## Concrete evidence from this project

- Architecture diagram and key technical decisions table.
- RBAC matrix that drives both UI and rules.
- Integrations section: email, SMS, Stripe, VIN, accounting — with failure behavior.
- Security/compliance: OWASP, audit log, secrets, DOT record retention notes.

## Gaps versus a typical hiring bar

No TOGAF-style enterprise portfolio, no customer-specific integration architecture for 5 systems of record. Title “Solution Architect” at a large SI will expect more client-landscape mapping. For SMB SaaS architecture, you are closer.

## How to talk about this

- Walk the “card data never touches us” architecture as a PCI decision.
- Walk deny-by-default + Functions writers as a security architecture.
- Be modest on “enterprise architect.”

## Repo pointers

- `dev/docs/IMPLEMENTATION_PLAN.md` §3, §7, §8, §12, §13
- `dev/firestore.rules`
- `dev/firebase.json`
