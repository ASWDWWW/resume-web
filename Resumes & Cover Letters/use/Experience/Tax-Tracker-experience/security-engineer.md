# Security Engineer

**Project scored:** TaxTacker (this repository only)  
**Score:** 5.5 / 10  
**Band:** Partial  
**Application guidance:** Stretch

Use as supporting evidence, not the whole case.

---

## What this job title usually means

Security engineers specialize in threat modeling, detection, appsec, identity, or infra hardening as their primary job.

## What you actually did in this project

Email verification before data access; Firestore rules that freeze billing/admin fields from the client; Storage MIME allowlist and 25 MB cap; CSP, X-Frame-Options DENY, Permissions-Policy; App Check scaffolding; redirect allowlists on checkout URLs; secrets kept out of git in ops docs. Extra: complimentary admin emails live server-side only; App Review claims; webhook signatures; account deletion; Crashlytics; password policy min 8; legal privacy text. You treated tax documents as sensitive user data.

## How that work applies to this title

This is **application security work done by the product owner**, which many mid-size companies actually need. It is not a security-engineer specialist portfolio (no red team, no SIEM, no formal threat model doc).

## Gaps (be ready to say these out loud)

No dedicated security tests (SAST beyond ESLint, DAST, pen test reports). IAP verification incomplete. App Check called out as still needing Console enablement in production-status notes. Min password 8 is a start, not a modern policy bar.

## Interview / resume angle

Apply to AppSec-leaning SWE or 'security-minded full-stack' postings. For pure Security Engineer, this is a strong *project*, not a career of security.

## Verdict

Partial-to-good as a security story on a SWE resume. Borderline as the job title itself.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
