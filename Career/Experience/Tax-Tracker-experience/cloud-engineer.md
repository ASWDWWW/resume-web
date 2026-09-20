# Cloud Engineer

**Project scored:** TaxTacker (this repository only)  
**Score:** 5.5 / 10  
**Band:** Partial  
**Application guidance:** Stretch

Use as supporting evidence, not the whole case.

---

## What this job title usually means

Cloud engineers design and operate workloads on AWS/GCP/Azure: IAM, networking, serverless, cost, landing zones.

## What you actually did in this project

You operated a GCP-adjacent Firebase project: Auth, Firestore, Storage, Hosting, Functions v1+v2, Analytics, Crashlytics, App Check, Cloud Scheduler-style jobs, FCM. Email verification before data access; Firestore rules that freeze billing/admin fields from the client; Storage MIME allowlist and 25 MB cap; CSP, X-Frame-Options DENY, Permissions-Policy; App Check scaffolding; redirect allowlists on checkout URLs; secrets kept out of git in ops docs. CSP connect-src includes Google and Stripe endpoints you had to get right.

## How that work applies to this title

Firebase is a GCP product surface. A cloud engineer interview that accepts serverless/BaaS will count this. You also thought about staging vs production projects in OPS.md.

## Gaps (be ready to say these out loud)

No VPC, no GKE, no Cloud SQL, no IAM org hierarchy, no cost dashboards. 'Cloud Engineer' at enterprises often means that lower-level GCP/AWS work.

## Interview / resume angle

Name the Firebase/GCP services and *why* you chose BaaS (speed, security rules, mobile clients) versus rolling ECS/GKE.

## Verdict

Partial-to-good for serverless/Firebase cloud roles; thin for classic cloud infra roles.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
