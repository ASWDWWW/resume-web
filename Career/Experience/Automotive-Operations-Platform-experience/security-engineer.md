# Security Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **6.8 / 10** · **Band:** Partial match  
**How to use this in hiring:** Use as transferable evidence, not as proof you already do the job

> This score measures how strongly *this repository* maps to a typical **Security Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Security engineers reduce risk: threat models, authz, secure defaults, reviews, detection, and sometimes appsec or cloudsec specialization.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Security Engineer

Security is a first-class theme in this repo, not a checklist afterthought. Deny-by-default Firestore, Storage path ACLs, custom claims, inactive staff lockout, immutable payments, CSP/HSTS, Stripe signature verification, encrypted staff messaging (ECDH P-256 + AES-GCM), rules tests, npm audit in CI, OWASP mapped mitigations, and a written threat model (spam, stuffing, insider invoice tampering, XSS, key leakage). That is applied product security.

## Concrete evidence from this project

- `firestore.rules` and `storage.rules` with role + assignment checks.
- `tests/security-rules.test.cjs` and `security-regressions.test.cjs`.
- E2E messaging crypto module with IndexedDB key storage.
- Hosting security headers including a detailed CSP.
- Implementation plan §8 threat model + SOC 2-foundation audit log.

## Gaps versus a typical hiring bar

Not a Security Engineer career yet: no pentest reports you ran, no detection engineering, no IAM at org scale, no vulnerability management program. AppSec-minded product engineers will recognize this; dedicated SecEng teams will call it “secure development.”

## How to talk about this

- Strongest security story: money and identity cannot be mutated from the browser.
- Second story: participant-only message media + E2E crypto.
- Do not claim you are a full-time Security Engineer; claim you ship security-sensitive product features.

## Repo pointers

- `dev/firestore.rules`
- `dev/storage.rules`
- `dev/public/app/js/messaging-crypto.js`
- `dev/docs/IMPLEMENTATION_PLAN.md` §8
- `dev/tests/security-*.cjs`
