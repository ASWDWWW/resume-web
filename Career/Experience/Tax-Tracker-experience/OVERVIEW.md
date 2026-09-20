# TaxTacker → job-title experience map

**Date of analysis:** 16 September 2026  
**Source:** this GitHub repository only (`Tax-Tracker-App`)  
**Method:** map shipped work (clients, backend, billing, security, mobile/store, CI/ops) onto each requested title; score 0–10 for *role-fit evidenced here*.

This folder is a job-search artifact. It is not a claim that you held these titles, and it does not include work from other jobs or private repos.

---

## How to use this packet

1. Read this overview for the ranking and the honest gaps.
2. Open the matching file in [`job-titles/`](job-titles/) before you apply or write a resume bullet.
3. Lead applications with titles in **Target now**. Use **Stretch** only with extra prep. Do not use this project as the headline for **Do not target** roles.

There is one markdown file per distinct title you listed (54 files). Similar titles (SWE I vs SDE I, FDE vs Associate FDE) are scored separately because hiring bars differ.

---

## Project snapshot

TaxTacker (branded TaxTacker / TaxTrack) is a production tax-record organizer for freelancers, contractors, and small businesses. It is not a tax-filing engine. You shipped a real product with:

- **Web client:** React 18, TypeScript, Vite, Tailwind, React Router — landing, auth, onboarding, tax-year workspaces, income/expense tracking, documents, notes, missing items, reports, ZIP export, settings, legal/support pages.
- **Mobile client:** Expo / React Native with full feature parity on iOS and Android — navigation, biometric lock, push notifications, AdMob (free tier), store IAP, Crashlytics, App Check, camera/document pickers, share sheets.
- **Backend:** Firebase Auth, Firestore, Storage, Hosting, Cloud Functions (Node 20) — Stripe Checkout/Portal/webhooks, IAP entitlement activation, account deletion, custom claims, App Review seeding, scheduled push reminders, GA4 Measurement Protocol.
- **Production ops:** Firestore/Storage security rules with tier gating, CSP and security headers, GitHub Actions CI, EAS production/preview/dev profiles, App Store review-account bypass, store listing and billing setup docs, Privacy/Terms (CCPA/GDPR).
- **Repo scale (this git history):** ~300 tracked files, ~60k insertions, web + mobile + functions + rules + CI, live hosting at launchpage-tax-tracker.web.app.

All ratings below measure **evidence from this repository only**, not other jobs, courses, or uncommitted work. One strong product does not equal years of team-scale or domain-specialist experience.


### Evidence checklist (what the repo actually contains)

| Area | Present in TaxTacker? | Where it shows up |
| --- | --- | --- |
| Production web app | Yes | React 18 + TS + Vite, Firebase Hosting, landing + authenticated app |
| Production mobile app | Yes | Expo/RN iOS+Android, EAS, store/IAP/ads/biometrics/push |
| Backend APIs / jobs | Yes | Cloud Functions: Stripe, IAP, claims, delete, pushes, GA4 |
| Data modeling | Yes | Firestore tax-year graph, indexes, export packages |
| AuthN / AuthZ | Yes | Email/password, verify gate, custom claims, security rules |
| Payments | Yes | Stripe Checkout/Portal/webhooks + store IAP entitlements |
| Security hardening | Partial–yes | Rules, CSP, App Check scaffolding, MIME/size, secrets hygiene |
| CI / release | Yes | GitHub Actions, EAS profiles, rules deploy workflow |
| Analytics / crash | Yes | Firebase Analytics, GA4 MP, Crashlytics |
| Tests | Partial | Vitest + some Functions tests; not deep integration coverage |
| Native iOS/Android languages | No | Zero Swift/Kotlin app code; Expo config plugins only |
| ML / GenAI product | No | Unused transitive Vertex dependency only |
| Embedded / hardware | No | — |
| Cleared / gov / hospitality | No | — |

---

### Rating scale (0–10)

Scores are **role-fit from this project**, not a claim about years of employment.

| Score | Band | Meaning |
| --- | --- | --- |
| 8.0–10 | Strong | You can interview this role using TaxTacker as the primary proof. Day-to-day work maps closely. |
| 6.0–7.9 | Good | Solid overlapping work. You should still name gaps (scale, language, team, or domain). |
| 4.0–5.9 | Partial | Adjacent skills exist. This project is supporting evidence, not the core case. |
| 2.0–3.9 | Adjacent | Transferable habits (shipping, debugging, docs) but the job’s core craft is missing. |
| 0.0–1.9 | Weak / none | Do not lead with this project for that title. |

### What was *not* found in this repo

No native Swift/Kotlin app modules, no ML training or inference product, no GenAI feature, no search ranking, no embedded/firmware/hardware, no hospitality domain, no government clearance workflow, no Kubernetes/Terraform-style infra, no data warehouse/dbt, no dedicated security pentest program, no on-site multi-customer FDE deployments.


---

## Ratings — all titles (high to low)

| Score | Band | Apply? | Job title | Document |
| ---: | --- | --- | --- | --- |
| 9.0 | Strong | Target now | Software Generalist | [doc](job-titles/software-generalist.md) |
| 8.5 | Strong | Target now | Application Developer | [doc](job-titles/application-developer.md) |
| 8.5 | Strong | Target now | Full-Stack Engineer | [doc](job-titles/full-stack-engineer.md) |
| 8.5 | Strong | Target now | Product Engineer | [doc](job-titles/product-engineer.md) |
| 8.5 | Strong | Target now | Software Development Engineer I (SDE I) | [doc](job-titles/software-development-engineer-i-sde-i.md) |
| 8.5 | Strong | Target now | Software Engineer I | [doc](job-titles/software-engineer-i.md) |
| 8.0 | Strong | Target now | Frontend Engineer | [doc](job-titles/frontend-engineer.md) |
| 8.0 | Strong | Target now | Mobile Engineer | [doc](job-titles/mobile-engineer.md) |
| 8.0 | Strong | Target now | Software Engineer | [doc](job-titles/software-engineer.md) |
| 7.5 | Strong | Target now | Associate Forward Deployed Engineer | [doc](job-titles/associate-forward-deployed-engineer.md) |
| 7.0 | Good | Target now | Backend Engineer | [doc](job-titles/backend-engineer.md) |
| 7.0 | Good | Target now | Fintech Software Engineer | [doc](job-titles/fintech-software-engineer.md) |
| 7.0 | Good | Target now | Software Engineer II / SWE II | [doc](job-titles/software-engineer-ii-swe-ii.md) |
| 6.5 | Good | Target now | Forward Deployed Engineer (FDE) | [doc](job-titles/forward-deployed-engineer-fde.md) |
| 6.5 | Good | Stretch | Software Development Engineer II (SDE II) | [doc](job-titles/software-development-engineer-ii-sde-ii.md) |
| 6.5 | Good | Target now | Solutions Engineer | [doc](job-titles/solutions-engineer.md) |
| 6.0 | Good | Stretch | Android Engineer | [doc](job-titles/android-engineer.md) |
| 6.0 | Good | Target now | Forward Deployed Engineer / Solution Architect | [doc](job-titles/forward-deployed-engineer-solution-architect.md) |
| 6.0 | Good | Stretch | Payments Infrastructure Engineer | [doc](job-titles/payments-infrastructure-engineer.md) |
| 5.5 | Partial | Stretch | Cloud Engineer | [doc](job-titles/cloud-engineer.md) |
| 5.5 | Partial | Stretch | Security Engineer | [doc](job-titles/security-engineer.md) |
| 5.5 | Partial | Stretch | iOS Engineer | [doc](job-titles/ios-engineer.md) |
| 5.0 | Partial | Adjacent only | Platform Engineer | [doc](job-titles/platform-engineer.md) |
| 5.0 | Partial | Stretch | Solution Architect | [doc](job-titles/solution-architect.md) |
| 5.0 | Partial | Stretch | Support Engineer | [doc](job-titles/support-engineer.md) |
| 4.5 | Partial | Adjacent only | Analytics Engineer | [doc](job-titles/analytics-engineer.md) |
| 4.5 | Partial | Stretch | Senior Forward Deployed Engineer | [doc](job-titles/senior-forward-deployed-engineer.md) |
| 4.0 | Partial | Adjacent only | Infrastructure Engineer | [doc](job-titles/infrastructure-engineer.md) |
| 3.5 | Adjacent | Adjacent only | Data Engineer | [doc](job-titles/data-engineer.md) |
| 3.5 | Adjacent | Do not target from this project | Developer Platform Engineer | [doc](job-titles/developer-platform-engineer.md) |
| 3.5 | Adjacent | Adjacent only | Field Engineer | [doc](job-titles/field-engineer.md) |
| 3.5 | Adjacent | Do not target from this project | Principal Software Solutions Engineer / Forward Deployed | [doc](job-titles/principal-software-solutions-engineer-forward-deployed.md) |
| 3.0 | Adjacent | Do not target from this project | Developer Tools Engineer | [doc](job-titles/developer-tools-engineer.md) |
| 3.0 | Adjacent | Do not target from this project | Lead Forward Deployed Engineer | [doc](job-titles/lead-forward-deployed-engineer.md) |
| 3.0 | Adjacent | Do not target from this project | Staff Forward Deployed Engineer | [doc](job-titles/staff-forward-deployed-engineer.md) |
| 2.0 | Adjacent | Do not target from this project | AI Product Engineer | [doc](job-titles/ai-product-engineer.md) |
| 2.0 | Adjacent | Do not target from this project | Forward Deployed Engineer, AI & Agentic SDLC | [doc](job-titles/forward-deployed-engineer-ai-agentic-sdlc.md) |
| 2.0 | Adjacent | Do not target from this project | Founding AI Forward Deployed Engineer | [doc](job-titles/founding-ai-forward-deployed-engineer.md) |
| 1.5 | Weak / none | Do not target from this project | Algorithm Engineer | [doc](job-titles/algorithm-engineer.md) |
| 1.5 | Weak / none | Do not target from this project | Connected-Device Software Engineer | [doc](job-titles/connected-device-software-engineer.md) |
| 1.5 | Weak / none | Do not target from this project | Forward Deployed AI Engineer | [doc](job-titles/forward-deployed-ai-engineer.md) |
| 1.5 | Weak / none | Do not target from this project | Forward Deployed Engineer, AI Enablement | [doc](job-titles/forward-deployed-engineer-ai-enablement.md) |
| 1.5 | Weak / none | Do not target from this project | Lead Forward Deployed Engineer, Hospitality | [doc](job-titles/lead-forward-deployed-engineer-hospitality.md) |
| 1.5 | Weak / none | Do not target from this project | Networking Engineer | [doc](job-titles/networking-engineer.md) |
| 1.0 | Weak / none | Do not target from this project | AI/Search Engineer | [doc](job-titles/ai-search-engineer.md) |
| 1.0 | Weak / none | Do not target from this project | Forward Deployed Engineer — Clearance Required | [doc](job-titles/forward-deployed-engineer-clearance-required.md) |
| 0.5 | Weak / none | Do not target from this project | AI Engineer | [doc](job-titles/ai-engineer.md) |
| 0.5 | Weak / none | Do not target from this project | Applied AI Engineer | [doc](job-titles/applied-ai-engineer.md) |
| 0.5 | Weak / none | Do not target from this project | Embedded Software Engineer | [doc](job-titles/embedded-software-engineer.md) |
| 0.5 | Weak / none | Do not target from this project | Firmware Engineer | [doc](job-titles/firmware-engineer.md) |
| 0.5 | Weak / none | Do not target from this project | Generative AI / GenAI Engineer | [doc](job-titles/generative-ai-genai-engineer.md) |
| 0.5 | Weak / none | Do not target from this project | Hardware/Software Engineer | [doc](job-titles/hardware-software-engineer.md) |
| 0.5 | Weak / none | Do not target from this project | Machine Learning Engineer | [doc](job-titles/machine-learning-engineer.md) |
| 0.5 | Weak / none | Do not target from this project | Sensor Algorithm Engineer | [doc](job-titles/sensor-algorithm-engineer.md) |

---

## Findings by band

### Strong (8.0+) — lead with these

- **Software Generalist** (9.0/10) — Highest-confidence label. Lean into it for startups and small product teams.
- **Application Developer** (8.5/10) — Direct fit for JS/TS application developer roles.
- **Full-Stack Engineer** (8.5/10) — Lead with this title. TaxTacker is a full-stack product.
- **Product Engineer** (8.5/10) — One of the two best labels for this work (with Full-Stack).
- **Software Development Engineer I (SDE I)** (8.5/10) — Excellent SDE I portfolio piece. Pair it with interview-drill prep.
- **Software Engineer I** (8.5/10) — Very strong fit. This project is more than enough evidence for SWE I if coding screens are passed.
- **Frontend Engineer** (8.0/10) — Strong frontend fit, especially product/React roles. Pair with a live demo.
- **Mobile Engineer** (8.0/10) — Strong for React Native / Expo mobile roles. Good supporting evidence for 'mobile' on a full-stack team.
- **Software Engineer** (8.0/10) — Use TaxTacker as a flagship project for Software Engineer applications. It proves you can ship.

### Good (6.0–7.9) — apply with a clear gap sentence

- **Associate Forward Deployed Engineer** (7.5/10) — Strong target if you want the FDE path.
- **Backend Engineer** (7.0/10) — Good backend evidence for Node/Firebase shops. For JVM/Go backend teams, this is adjacent unless you translate the designs.
- **Fintech Software Engineer** (7.0/10) — Good for fintech *application* teams (tax, bookkeeping, SMB finance). Weaker for core banking/payments rails teams (see next title).
- **Software Engineer II / SWE II** (7.0/10) — Credible SWE II candidate if you can discuss tradeoffs and scale-up. Do not claim FAANG-scale backend experience from this repo alone.
- **Forward Deployed Engineer (FDE)** (6.5/10) — Credible for FDE roles that accept startup/product backgrounds. Weaker for FDEs that require prior customer-facing consulting.
- **Software Development Engineer II (SDE II)** (6.5/10) — Possible SDE II at smaller companies or if you have other experience. At Big Tech, treat this as strong supporting evidence, not the whole case.
- **Solutions Engineer** (6.5/10) — Good fit especially for technical SE / sales-engineer roles on SaaS. Stronger if you add live demo fluency.
- **Android Engineer** (6.0/10) — Better Android evidence than iOS evidence, still not a native Android IC portfolio.
- **Forward Deployed Engineer / Solution Architect** (6.0/10) — Good target among the hybrid FDE titles.
- **Payments Infrastructure Engineer** (6.0/10) — Good supporting evidence for payments-adjacent SWE. Stretch for a dedicated payments-infra team unless you have more.

### Stretch titles (apply only if the rest of your background helps)

- **Software Development Engineer II (SDE II)** (6.5/10) — Possible SDE II at smaller companies or if you have other experience. At Big Tech, treat this as strong supporting evidence, not the whole case.
- **Android Engineer** (6.0/10) — Better Android evidence than iOS evidence, still not a native Android IC portfolio.
- **Payments Infrastructure Engineer** (6.0/10) — Good supporting evidence for payments-adjacent SWE. Stretch for a dedicated payments-infra team unless you have more.
- **Cloud Engineer** (5.5/10) — Partial-to-good for serverless/Firebase cloud roles; thin for classic cloud infra roles.
- **Security Engineer** (5.5/10) — Partial-to-good as a security story on a SWE resume. Borderline as the job title itself.
- **iOS Engineer** (5.5/10) — Partial. Do not title your resume 'iOS Engineer' from this repo alone unless the job is RN.
- **Solution Architect** (5.0/10) — Partial. Better as Solutions Engineer or Product Engineer than SA unless the SA job is startup-sized.
- **Support Engineer** (5.0/10) — Partial. Better as a plus on a SWE resume than a Support Engineer headline unless you want that path.
- **Senior Forward Deployed Engineer** (4.5/10) — This project does not by itself justify Senior FDE.

### Do not use this project as the headline

These roles need craft that TaxTacker does not contain (AI/ML, embedded, clearance, staff/principal scope, hospitality, etc.):

- **Developer Platform Engineer** (3.5/10) — Not a fit as a headline.
- **Principal Software Solutions Engineer / Forward Deployed** (3.5/10) — Not a fit.
- **Developer Tools Engineer** (3.0/10) — Not evidenced as a career target from this repo.
- **Lead Forward Deployed Engineer** (3.0/10) — Not a fit.
- **Staff Forward Deployed Engineer** (3.0/10) — Not a fit.
- **AI Product Engineer** (2.0/10) — Not evidenced. Product Engineer yes; AI Product Engineer no.
- **Forward Deployed Engineer, AI & Agentic SDLC** (2.0/10) — Not a fit.
- **Founding AI Forward Deployed Engineer** (2.0/10) — Founding energy yes; AI FDE no.
- **Algorithm Engineer** (1.5/10) — Not a fit.
- **Connected-Device Software Engineer** (1.5/10) — Not a fit.
- **Forward Deployed AI Engineer** (1.5/10) — Not a fit until you ship an AI deployment.
- **Forward Deployed Engineer, AI Enablement** (1.5/10) — Not a fit.
- **Lead Forward Deployed Engineer, Hospitality** (1.5/10) — Not a fit.
- **Networking Engineer** (1.5/10) — No evidence.
- **AI/Search Engineer** (1.0/10) — No evidence.
- **Forward Deployed Engineer — Clearance Required** (1.0/10) — This project does not satisfy the clearance requirement or the gov domain. It can still be a coding sample *if* you are clearance-eligible.
- **AI Engineer** (0.5/10) — No evidence.
- **Applied AI Engineer** (0.5/10) — No evidence.
- **Embedded Software Engineer** (0.5/10) — No evidence.
- **Firmware Engineer** (0.5/10) — No evidence.
- **Generative AI / GenAI Engineer** (0.5/10) — No evidence.
- **Hardware/Software Engineer** (0.5/10) — No evidence.
- **Machine Learning Engineer** (0.5/10) — No evidence.
- **Sensor Algorithm Engineer** (0.5/10) — No evidence.

---

## Cross-cutting findings

### 1. You look like a founding product generalist, not a specialist IC at staff level

The strongest cluster is **Software Generalist / Full-Stack / Product Engineer / Application Developer / SWE I / SDE I / Mobile (RN)**. That cluster is people who *ship a product*. Weakest cluster is anything that requires a missing domain (AI, firmware, networking, hospitality, clearance) or a missing *level* (Staff/Lead/Principal FDE).

### 2. Web + mobile + billing is your depth, not a side quest

The stories that will survive a hard interview are:

1. **Entitlements:** client cannot grant Standard/Diamond; Stripe webhooks and IAP transaction ledger can.
2. **Trust for tax documents:** verified email, Storage allowlist + 25 MB, Firestore field locks, CSP, App Check path.
3. **Hostile external platforms:** App Store review accounts and Guideline 2.3.10; AdMob Kotlin/Gradle pin; dual Stripe vs store billing.
4. **Parity:** one Firebase project, two clients, same product rules.

Memorize those four. They cover Full-Stack, Backend, Mobile, Fintech, FDE, and Security-minded SWE interviews.

### 3. FDE is a reasonable adjacent path, not a Palantir clone story

Associate FDE / FDE / FDE+Solution Architect score **6.0–7.5** because you shipped into constraints you do not control. Senior/Staff/Lead/Principal FDE score **3.0–4.5** because there is no customer portfolio or team leverage. AI-flavored FDE titles score **~1.5–2.0** because the product has no AI.

### 4. Fintech is “SMB tax + subscriptions,” not “core payments rails”

You can talk to bookkeeping/tax/SMB finance teams with a straight face. You should not claim you built a card network, ledger, or in-house processor. IAP server verification is still explicitly incomplete in code comments.

### 5. iOS vs Android vs Mobile

**Mobile Engineer (Expo)** is 8.0. **Android** 6.0 because of Gradle/Play/Ads scars. **iOS** 5.5 because the App Store work is real but Swift is absent. Title your resume to the posting’s actual stack.

---

## Suggested resume bullets (true to this repo)

Use only if you actually did the work (you did, in-repo):

- Shipped a production tax-record product on **web (React/TypeScript)** and **iOS/Android (Expo)**, sharing one Firebase backend (Auth, Firestore, Storage, Functions).
- Implemented **subscription entitlements** via Stripe Checkout, Customer Portal, and signed webhooks, with a parallel **App Store / Play Billing** activation path and replay protection on transaction IDs.
- Enforced **tiered access** in Firestore/Storage rules (client cannot mint paid tiers), including MIME/size limits on tax document uploads.
- Built **CPA-ready export** (CSV/JSON/ZIP with document binaries) and tax-deadline / missing-item **push reminders**.
- Took the mobile app through **store-reality work**: EAS profiles, App Check notes, Crashlytics, AdMob, biometric lock, and App Store review-account seeding.

Avoid bullets that claim AI, native Swift/Kotlin apps, Kubernetes, or cleared deployments.

---

## Recommended application order

1. **Software Generalist, Full-Stack Engineer, Product Engineer, Application Developer**
2. **Software Engineer / SWE I / SDE I**, then **SWE II** at mid-size companies
3. **Mobile Engineer (React Native/Expo)**, Frontend, Backend (Node/Firebase)
4. **Fintech application SWE**, **Associate FDE**, **Solutions Engineer**, **FDE / Solution Architect**
5. Stretch: SWE II at large tech, SDE II, Cloud/serverless, Payments integration, Security-minded SWE, iOS/Android *if the team is RN-friendly*

Stop the list before AI/ML, embedded, networking, hospitality FDE, and Staff+ FDE unless other experience fills those holes.

---

## Per-title documents

All 54 titles:

| Score | Band | Apply? | Job title | Document |
| ---: | --- | --- | --- | --- |
| 9.0 | Strong | Target now | Software Generalist | [doc](job-titles/software-generalist.md) |
| 8.5 | Strong | Target now | Application Developer | [doc](job-titles/application-developer.md) |
| 8.5 | Strong | Target now | Full-Stack Engineer | [doc](job-titles/full-stack-engineer.md) |
| 8.5 | Strong | Target now | Product Engineer | [doc](job-titles/product-engineer.md) |
| 8.5 | Strong | Target now | Software Development Engineer I (SDE I) | [doc](job-titles/software-development-engineer-i-sde-i.md) |
| 8.5 | Strong | Target now | Software Engineer I | [doc](job-titles/software-engineer-i.md) |
| 8.0 | Strong | Target now | Frontend Engineer | [doc](job-titles/frontend-engineer.md) |
| 8.0 | Strong | Target now | Mobile Engineer | [doc](job-titles/mobile-engineer.md) |
| 8.0 | Strong | Target now | Software Engineer | [doc](job-titles/software-engineer.md) |
| 7.5 | Strong | Target now | Associate Forward Deployed Engineer | [doc](job-titles/associate-forward-deployed-engineer.md) |
| 7.0 | Good | Target now | Backend Engineer | [doc](job-titles/backend-engineer.md) |
| 7.0 | Good | Target now | Fintech Software Engineer | [doc](job-titles/fintech-software-engineer.md) |
| 7.0 | Good | Target now | Software Engineer II / SWE II | [doc](job-titles/software-engineer-ii-swe-ii.md) |
| 6.5 | Good | Target now | Forward Deployed Engineer (FDE) | [doc](job-titles/forward-deployed-engineer-fde.md) |
| 6.5 | Good | Stretch | Software Development Engineer II (SDE II) | [doc](job-titles/software-development-engineer-ii-sde-ii.md) |
| 6.5 | Good | Target now | Solutions Engineer | [doc](job-titles/solutions-engineer.md) |
| 6.0 | Good | Stretch | Android Engineer | [doc](job-titles/android-engineer.md) |
| 6.0 | Good | Target now | Forward Deployed Engineer / Solution Architect | [doc](job-titles/forward-deployed-engineer-solution-architect.md) |
| 6.0 | Good | Stretch | Payments Infrastructure Engineer | [doc](job-titles/payments-infrastructure-engineer.md) |
| 5.5 | Partial | Stretch | Cloud Engineer | [doc](job-titles/cloud-engineer.md) |
| 5.5 | Partial | Stretch | Security Engineer | [doc](job-titles/security-engineer.md) |
| 5.5 | Partial | Stretch | iOS Engineer | [doc](job-titles/ios-engineer.md) |
| 5.0 | Partial | Adjacent only | Platform Engineer | [doc](job-titles/platform-engineer.md) |
| 5.0 | Partial | Stretch | Solution Architect | [doc](job-titles/solution-architect.md) |
| 5.0 | Partial | Stretch | Support Engineer | [doc](job-titles/support-engineer.md) |
| 4.5 | Partial | Adjacent only | Analytics Engineer | [doc](job-titles/analytics-engineer.md) |
| 4.5 | Partial | Stretch | Senior Forward Deployed Engineer | [doc](job-titles/senior-forward-deployed-engineer.md) |
| 4.0 | Partial | Adjacent only | Infrastructure Engineer | [doc](job-titles/infrastructure-engineer.md) |
| 3.5 | Adjacent | Adjacent only | Data Engineer | [doc](job-titles/data-engineer.md) |
| 3.5 | Adjacent | Do not target from this project | Developer Platform Engineer | [doc](job-titles/developer-platform-engineer.md) |
| 3.5 | Adjacent | Adjacent only | Field Engineer | [doc](job-titles/field-engineer.md) |
| 3.5 | Adjacent | Do not target from this project | Principal Software Solutions Engineer / Forward Deployed | [doc](job-titles/principal-software-solutions-engineer-forward-deployed.md) |
| 3.0 | Adjacent | Do not target from this project | Developer Tools Engineer | [doc](job-titles/developer-tools-engineer.md) |
| 3.0 | Adjacent | Do not target from this project | Lead Forward Deployed Engineer | [doc](job-titles/lead-forward-deployed-engineer.md) |
| 3.0 | Adjacent | Do not target from this project | Staff Forward Deployed Engineer | [doc](job-titles/staff-forward-deployed-engineer.md) |
| 2.0 | Adjacent | Do not target from this project | AI Product Engineer | [doc](job-titles/ai-product-engineer.md) |
| 2.0 | Adjacent | Do not target from this project | Forward Deployed Engineer, AI & Agentic SDLC | [doc](job-titles/forward-deployed-engineer-ai-agentic-sdlc.md) |
| 2.0 | Adjacent | Do not target from this project | Founding AI Forward Deployed Engineer | [doc](job-titles/founding-ai-forward-deployed-engineer.md) |
| 1.5 | Weak / none | Do not target from this project | Algorithm Engineer | [doc](job-titles/algorithm-engineer.md) |
| 1.5 | Weak / none | Do not target from this project | Connected-Device Software Engineer | [doc](job-titles/connected-device-software-engineer.md) |
| 1.5 | Weak / none | Do not target from this project | Forward Deployed AI Engineer | [doc](job-titles/forward-deployed-ai-engineer.md) |
| 1.5 | Weak / none | Do not target from this project | Forward Deployed Engineer, AI Enablement | [doc](job-titles/forward-deployed-engineer-ai-enablement.md) |
| 1.5 | Weak / none | Do not target from this project | Lead Forward Deployed Engineer, Hospitality | [doc](job-titles/lead-forward-deployed-engineer-hospitality.md) |
| 1.5 | Weak / none | Do not target from this project | Networking Engineer | [doc](job-titles/networking-engineer.md) |
| 1.0 | Weak / none | Do not target from this project | AI/Search Engineer | [doc](job-titles/ai-search-engineer.md) |
| 1.0 | Weak / none | Do not target from this project | Forward Deployed Engineer — Clearance Required | [doc](job-titles/forward-deployed-engineer-clearance-required.md) |
| 0.5 | Weak / none | Do not target from this project | AI Engineer | [doc](job-titles/ai-engineer.md) |
| 0.5 | Weak / none | Do not target from this project | Applied AI Engineer | [doc](job-titles/applied-ai-engineer.md) |
| 0.5 | Weak / none | Do not target from this project | Embedded Software Engineer | [doc](job-titles/embedded-software-engineer.md) |
| 0.5 | Weak / none | Do not target from this project | Firmware Engineer | [doc](job-titles/firmware-engineer.md) |
| 0.5 | Weak / none | Do not target from this project | Generative AI / GenAI Engineer | [doc](job-titles/generative-ai-genai-engineer.md) |
| 0.5 | Weak / none | Do not target from this project | Hardware/Software Engineer | [doc](job-titles/hardware-software-engineer.md) |
| 0.5 | Weak / none | Do not target from this project | Machine Learning Engineer | [doc](job-titles/machine-learning-engineer.md) |
| 0.5 | Weak / none | Do not target from this project | Sensor Algorithm Engineer | [doc](job-titles/sensor-algorithm-engineer.md) |

---

*If you later add OCR/LLM on documents, native modules, a warehouse, or real customer deployments, re-score AI, iOS/Android, Data, and Senior FDE — those are the ratings most likely to move.*
