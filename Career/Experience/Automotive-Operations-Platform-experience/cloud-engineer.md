# Cloud Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **6.4 / 10** · **Band:** Partial match  
**How to use this in hiring:** Use as transferable evidence, not as proof you already do the job

> This score measures how strongly *this repository* maps to a typical **Cloud Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Cloud engineers design and operate workloads on a public cloud: IAM, compute, data stores, networking, cost, and deployment. They may be app-leaning or infra-leaning.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Cloud Engineer

You used a coherent GCP/Firebase slice: Auth, Firestore, Cloud Functions v2 (HTTPS, callable, scheduler, Firestore triggers), Cloud Storage, Hosting, Secret Manager-style function secrets for Stripe, us-central1, GitHub OIDC-less token deploy. You thought about cost (~$50–150/mo model) and free-tier Auth. That is real cloud application engineering on a managed PaaS.

## Concrete evidence from this project

- Multi-product Firebase architecture with production project id `launchpage-alex-roadservice`.
- Scheduled Cloud Functions (`every 24 hours`).
- Secrets for `STRIPE_SECRET_KEY` / `STRIPE_WEBHOOK_SECRET` (not in client).
- CI deploy of hosting + rules + indexes + storage + functions.
- App Check called out in the threat model for abuse protection.

## Gaps versus a typical hiring bar

Little IAM beyond Firebase Auth custom claims; no GKE, Cloud SQL, VPC-SC, or multi-account landing zone. Cloud Engineer roles that are 80% networking/IAM will not see enough. App-centric Firebase/GCP roles will.

## How to talk about this

- Name the managed services and *why* each exists (Auth for staff, Functions for privileged writes, Hosting for static+SPA-like ops).
- Discuss cost and backup as first-class, not afterthoughts.
- Be ready for “why not Cloud Run + Postgres?” — SMB speed, realtime, auth bundled.

## Repo pointers

- `dev/firebase.json`
- `dev/functions/index.js`
- `dev/docs/FIREBASE_SETUP.md`
- `dev/docs/STRIPE_SETUP.md`
