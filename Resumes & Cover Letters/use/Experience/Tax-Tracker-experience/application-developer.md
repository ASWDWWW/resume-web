# Application Developer

**Project scored:** TaxTacker (this repository only)  
**Score:** 8.5 / 10  
**Band:** Strong  
**Application guidance:** Target now

This project is primary evidence for the role.

---

## What this job title usually means

Application developers build business applications — CRUD, workflows, UI, integrations — often against a BaaS or existing platform rather than inventing infrastructure.

## What you actually did in this project

You owned the product loop: tax-year workspaces, income/expense types (W-2, 1099-NEC, 1099-K, cash, rental, etc.), missing-item tracker, preparer notes, dashboard readiness, CSV/ZIP export for a CPA, onboarding, and paid tiers (Free / Standard / Diamond). The web app is a typed React SPA with a design system (Tailwind tokens, shared UI primitives, error boundaries, offline banner, tier guards, analytics route listener). Mobile mirrors the same flows in React Native with navigation stacks/tabs, splash/lock gates, and platform copy splits. Nested Firestore model `users/{uid}/taxYears/{yearId}/{income,expenses,documents,notes,missingItems,exports}` plus user-level subscription, push tokens, and IAP transaction ledger. Aggregates for dashboard totals. CSV/JSON/ZIP packaging with document binaries. Features are real workflows: log income, categorize expenses with business-use %, upload W-2s/receipts, track missing items, export a CPA package.

## How that work applies to this title

This title is almost a 1:1 label for TaxTacker. You built the application layer on Firebase: screens, validation, tier gates, exports, and notifications. That is application development.

## Gaps (be ready to say these out loud)

Some 'application developer' jobs (SAP, Salesforce, .NET enterprise) want those platforms. This evidence is JS/TS + Firebase, not those stacks.

## Interview / resume angle

Demo the tax-year workspace and export ZIP. Application roles hire people who finish user-facing workflows, which you did.

## Verdict

Direct fit for JS/TS application developer roles.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
