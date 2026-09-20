# Security Engineer

**Evidence source:** Insightful Care Solutions LLC — production telepsychiatry website for a New Jersey psychiatric practice  
**Live site:** https://insightfulcare.solutions/  
**Your role on the work:** Solo engineer (Zakiy Manigo), Oct 2025 – Jul 2026  
**What shipped:** React + Vite + Tailwind SPA, Firebase Hosting, Google Apps Script contact backend, ChARM Health booking integration, SEO/AI-crawler assets, accessibility and responsive UX, client-facing ops docs


## Experience rating (this project only)

**2 / 10 — Weak adjacency**

A few related decisions, not role-shaped experience.

Ratings are not a prediction of whether you can *learn* the job. They measure how much **this repository** already looks like the work that title is hired to do.

## What this role typically requires

Threat modeling, appsec, IAM, detection, vuln management, sometimes compliance programs (SOC2, HIPAA technical safeguards).

## What you have done in this project

HTTPS by default, `noopener` on external booking (with a conscious referrer exception for ChARM’s allowlist), client and GAS validation, no secrets committed, crisis disclaimers, HIPAA mentioned as Zoom/telehealth property of the vendor. Healthcare PII in contact emails is an implicit security/privacy design (and a risk).

## How that work applies to Security Engineer

You made a few security-aware product choices and worked in a HIPAA-adjacent business. The ChARM referrer tradeoff is a real security-vs-function discussion. A security engineer would still criticize emailing PII and the lack of CAPTCHA/rate limits/CSP.

## Gaps versus a typical hiring bar

No authz, no threat model doc, no SAST/DAST, no CSP/headers beyond cache, no secrets manager, no audit logs. Not security engineering.

## How to talk about it

You can discuss healthcare privacy constraints and one integration tradeoff. Do not claim Security Engineer.

## Bottom line

Security awareness only.
