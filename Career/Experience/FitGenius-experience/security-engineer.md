# Security Engineer

**Experience rating:** 7.0 / 10 — Solid match  
**Application guidance:** Apply with framing  
**Family:** Cloud / platform  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

Security engineers reduce risk: authN/Z, secrets, logging, threat modeling, appsec, sometimes detection. Product-security vs. corporate-security vs. red-team are different jobs.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

Firestore/storage rules, App Check (wired, not enforced), rate limits, structured `fgSecurity` logs, content filter + strike auto-suspend, age gate, consent tests, no-advertising-ID plugin, encrypted local GPS cache, account deletion, incident-contact doc, Gemini payload minimization, admin lookup that avoids sensitive collections.

## How that work applies to **Security Engineer**

Strong for product-security / appsec at a small company. Weak for detection-engineering, pentest, or corporate IAM. You practiced secure-by-construction in a consumer app with health and location data.

## Strengths a hiring manager can credit

- Authorization model in rules, not only UI
- Abuse and UGC safety
- Privacy engineering (consent, minimization, no ads)
- Incident documentation without fake HIPAA claims

## Gaps versus a typical hiring bar

- App Check enforcement still false
- No pentest report / bug bounty operation
- No SIEM beyond Cloud Logging queries

## How to talk about it

Lead with health+location threat model and rules. Be honest App Check is not enforced yet.

## Repo evidence

`firestore.rules`, `securityLog.ts`, `callableSecurity.ts`, `plugins/withNoAdvertisingTracking.js`, legal suite security docs

## Rating rationale

Real product security. Not a dedicated security org.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
