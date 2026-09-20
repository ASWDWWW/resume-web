# Platform Engineer

**Project scored:** TaxTacker (this repository only)  
**Score:** 5.0 / 10  
**Band:** Partial  
**Application guidance:** Adjacent only

Use as supporting evidence, not the whole case.

---

## What this job title usually means

Platform engineers build internal platforms: CI, paved-road deploys, golden paths, multi-tenant infra, developer self-service.

## What you actually did in this project

GitHub Actions: web lint + Vitest + production build, mobile `tsc --noEmit`, functions syntax check; manual workflow to deploy Firestore/Storage rules with a confirm gate. Firebase Hosting + Functions + rules-as-code, EAS build profiles (development/preview/production), Expo config plugins, documented secrets/staging split. You paved *your own* road.

## How that work applies to this title

You practiced platform *thinking* for a single product: reproducible builds, manual gated rules deploy, env var contracts. That is a seed of platform work.

## Gaps (be ready to say these out loud)

Platform jobs want you to serve other engineers as customers (IDP, clusters, golden templates). Here you were the only customer. No Kubernetes, no service mesh, no internal developer portal.

## Interview / resume angle

Use this as 'I care about paved paths' evidence inside a broader SWE story, not as a Platform Engineer headline.

## Verdict

Partial. Supporting story only.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
