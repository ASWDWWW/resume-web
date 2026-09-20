# Platform Engineer

**Experience rating:** 6.2 / 10 — Credible adjacent  
**Application guidance:** Stretch only  
**Family:** Cloud / platform  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

Platform engineers build the paved road other engineers use: clusters, CI templates, golden paths, internal developer platforms. Sometimes the title means 'product platform APIs' inside an app company.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

You built a *product* platform: Firebase project, dual Hosting targets, EAS profiles, CI matrix, emulators, seed scripts, locale pipelines, legal HTML generator. You did not build a multi-team Kubernetes platform.

## How that work applies to **Platform Engineer**

Apply only when the posting is 'platform' as in shared product APIs / app platform on GCP/Firebase. Skip IDP/Backstage/k8s platform roles. Your 'users' of the platform were mostly you plus a founder.

## Strengths a hiring manager can credit

- Reproducible build/test/deploy
- Shared types and API factory (Firebase/REST/mock)
- Tooling that keeps store declarations aligned with the binary

## Gaps versus a typical hiring bar

- No multi-tenant internal platform
- No k8s, service mesh, or golden-path onboarding for 50 engineers
- Single production project, no staging

## How to talk about it

If you apply, reframe as 'I built the application platform for a mobile product on Firebase,' not 'I am a platform SRE.'

## Repo evidence

`firebase.json`, `.github/workflows/ci.yml`, `scripts/`, `mobile/eas.json`

## Rating rationale

Adjacent app-platform work, not classic Platform Engineering.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
