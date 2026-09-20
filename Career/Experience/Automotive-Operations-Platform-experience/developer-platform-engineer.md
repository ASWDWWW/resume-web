# Developer Platform Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **3.2 / 10** · **Band:** Weak match  
**How to use this in hiring:** Thin overlap — mention only if asked, then pivot

> This score measures how strongly *this repository* maps to a typical **Developer Platform Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Developer Platform Engineers build golden paths for many engineering teams: paved CI, environments, service templates, IDP portals, and policy as code.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Developer Platform Engineer

Your “developer platform” is a single-product toolchain: npm scripts, emulator-based tests, seed generators, and a bootstrap admin script. Useful, but the user of the platform is you (and later LaunchPage delivery), not dozens of teams.

## Concrete evidence from this project

- `scripts/check-js.cjs` syntax gate.
- Provision-initial-admin script.
- Demo seed generators.
- README-driven local serve path.

## Gaps versus a typical hiring bar

No Backstage, no reusable service template repo, no org-wide CI library, no ephemeral preview environments per PR (PRs validate only). Weak match.

## How to talk about this

- Do not apply to Developer Platform roles with this as the main example.
- You can mention you care about `npm run check` as a paved path for *this* repo.

## Repo pointers

- `dev/package.json`
- `dev/scripts/`
- `dev/functions/scripts/provision-initial-admin.js`
