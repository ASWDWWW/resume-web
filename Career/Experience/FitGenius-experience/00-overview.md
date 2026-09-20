# FitGenius → job-title experience: overview

**Subject:** Founding technical partner work on FitGenius (this repository)  
**Question:** For each requested job title, what did you actually do, how does it apply, and how strong is the experience?  
**Documents:** One file per title in this folder, plus this overview  
**Date of assessment:** 16 September 2026

---

## Method

Ratings are **not** years-of-experience guesses and they are **not** interview predictions. They score how strongly *this repository* demonstrates the work a hiring manager for that title usually wants.

Each score weights:

1. **Directness (40%)** — did you do the job, or an analogy of it?
2. **Depth (30%)** — production-quality systems, tests, failure modes, not a tutorial slice
3. **Transferability (20%)** — would a typical 2026 posting recognize this evidence?
4. **Gaps (10%)** — what a competent interviewer will still poke

| Score | Meaning |
|------:|---------|
| 9.0–10 | Direct, deep match. You could interview as if this *was* the job. |
| 8.0–8.9 | Strong match. Most of the role is in the repo; a few typical requirements are missing. |
| 7.0–7.9 | Solid match. Real production work in the same family; hiring managers will still probe gaps. |
| 6.0–6.9 | Credible adjacent. Transferable, but the title is more specialized than FitGenius. |
| 5.0–5.9 | Partial. Some overlap; do not lead a search with this title. |
| 3.5–4.9 | Weak. Mention only if a posting is unusually broad. |
| 1.0–3.4 | Not demonstrated. Do not apply on FitGenius evidence alone. |

Honest constraints used everywhere:

- FitGenius is **feature-rich and pre-launch**. Store submit and some IAP deploy steps are still open. That caps any 'ran production at scale' claim.
- You were **one engineer**, so collaboration/mentorship evidence is thin.
- **AI work is applied Gemini / Vertex**, not model training.
- **Payments work is App Store / Play IAP**, not Stripe or bank rails.
- **FDE work is founder-embedded**, not multi-customer Palantir-style deployment.
- **No** embedded firmware, hospitality vertical, or security clearance.

---

## What you built (shared evidence)

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

Headline inventory:

| Area | What exists |
|------|-------------|
| Mobile | Expo 54 / React Native 0.81, 65+ screens, iOS + Android native projects, EAS |
| Native integrations | HealthKit, Health Connect, background GPS, StoreKit/Play Billing client, camera, maps, push |
| Backend | ~64 Cloud Functions, Firestore + Storage rules, scheduled jobs, webhooks |
| AI | Gemini on Vertex (`coachChat`, plans, food estimate, daily content) with allowlisted context |
| Algorithms | Progressive overload engine, outdoor pace engine, GPS validation, segment matching, Fit Score |
| Web | Vite/React marketing site; legal/support/admin hosting |
| Quality | Mobile Jest, functions tests, Firebase rules tests, website Vitest, GitHub Actions CI |
| Go-to-market | Store paste sheets, legal protection suite, founder packets, admin ops portal |
| Not in repo | BLE/firmware, watchOS, model training, Stripe, Terraform/k8s, clearance, hospitality |

---

## Scores at a glance (high → low)

| Score | Band | Title | Family | Guidance |
|------:|------|-------|--------|----------|
| 9.5 | Exceptional match | [Software Generalist](./software-generalist.md) | Core software | Apply now |
| 9.4 | Exceptional match | [Mobile Engineer](./mobile-engineer.md) | Mobile | Apply now |
| 9.2 | Exceptional match | [Software Engineer](./software-engineer.md) | Core software | Apply now |
| 9.1 | Exceptional match | [Product Engineer](./product-engineer.md) | Product / AI product | Apply now |
| 9.0 | Exceptional match | [Full-Stack Engineer](./full-stack-engineer.md) | Core software | Apply now |
| 8.8 | Strong match | [Software Development Engineer I (SDE I)](./software-development-engineer-i-sde-i.md) | Core software | Apply now |
| 8.8 | Strong match | [Software Engineer I](./software-engineer-i.md) | Core software | Apply now |
| 8.6 | Strong match | [AI Product Engineer](./ai-product-engineer.md) | Product / AI product | Apply now |
| 8.6 | Strong match | [Application Developer](./application-developer.md) | Core software | Apply now |
| 8.4 | Strong match | [Founding AI Forward Deployed Engineer](./founding-ai-forward-deployed-engineer.md) | Forward deployed | Apply now |
| 8.4 | Strong match | [Software Development Engineer II (SDE II)](./software-development-engineer-ii-sde-ii.md) | Core software | Apply now |
| 8.4 | Strong match | [Software Engineer II / SWE II](./software-engineer-ii-swe-ii.md) | Core software | Apply now |
| 8.3 | Strong match | [Backend Engineer](./backend-engineer.md) | Core software | Apply now |
| 8.2 | Strong match | [Applied AI Engineer](./applied-ai-engineer.md) | Product / AI product | Apply now |
| 8.1 | Strong match | [Generative AI / GenAI Engineer](./generative-ai-genai-engineer.md) | Product / AI product | Apply now |
| 8.0 | Strong match | [Associate Forward Deployed Engineer](./associate-forward-deployed-engineer.md) | Forward deployed | Apply now |
| 8.0 | Strong match | [Solutions Engineer](./solutions-engineer.md) | Customer-facing | Apply now |
| 7.8 | Solid match | [Frontend Engineer](./frontend-engineer.md) | Core software | Apply with framing |
| 7.6 | Solid match | [AI Engineer](./ai-engineer.md) | Product / AI product | Apply with framing |
| 7.6 | Solid match | [Forward Deployed AI Engineer](./forward-deployed-ai-engineer.md) | Forward deployed | Apply with framing |
| 7.5 | Solid match | [Forward Deployed Engineer, AI Enablement](./forward-deployed-engineer-ai-enablement.md) | Forward deployed | Apply with framing |
| 7.4 | Solid match | [Algorithm Engineer](./algorithm-engineer.md) | ML / data | Apply with framing |
| 7.4 | Solid match | [Forward Deployed Engineer / Solution Architect](./forward-deployed-engineer-solution-architect.md) | Forward deployed | Apply with framing |
| 7.2 | Solid match | [Android Engineer](./android-engineer.md) | Mobile | Apply with framing |
| 7.2 | Solid match | [Forward Deployed Engineer (FDE)](./forward-deployed-engineer-fde.md) | Forward deployed | Apply with framing |
| 7.2 | Solid match | [iOS Engineer](./ios-engineer.md) | Mobile | Apply with framing |
| 7.1 | Solid match | [Solution Architect](./solution-architect.md) | Customer-facing | Apply with framing |
| 7.0 | Solid match | [Cloud Engineer](./cloud-engineer.md) | Cloud / platform | Apply with framing |
| 7.0 | Solid match | [Security Engineer](./security-engineer.md) | Cloud / platform | Apply with framing |
| 6.6 | Credible adjacent | [Payments Infrastructure Engineer](./payments-infrastructure-engineer.md) | Payments / fintech | Apply with framing |
| 6.4 | Credible adjacent | [Developer Tools Engineer](./developer-tools-engineer.md) | Cloud / platform | Stretch only |
| 6.4 | Credible adjacent | [Senior Forward Deployed Engineer](./senior-forward-deployed-engineer.md) | Forward deployed | Stretch only |
| 6.4 | Credible adjacent | [Support Engineer](./support-engineer.md) | Customer-facing | Stretch only |
| 6.3 | Credible adjacent | [Analytics Engineer](./analytics-engineer.md) | ML / data | Stretch only |
| 6.2 | Credible adjacent | [Forward Deployed Engineer, AI and Agentic SDLC](./forward-deployed-engineer-ai-and-agentic-sdlc.md) | Forward deployed | Stretch only |
| 6.2 | Credible adjacent | [Platform Engineer](./platform-engineer.md) | Cloud / platform | Stretch only |
| 5.8 | Partial | [Sensor Algorithm Engineer](./sensor-algorithm-engineer.md) | Hardware / devices | Stretch only |
| 5.6 | Partial | [Developer Platform Engineer](./developer-platform-engineer.md) | Cloud / platform | Stretch only |
| 5.4 | Partial | [Infrastructure Engineer](./infrastructure-engineer.md) | Cloud / platform | Stretch only |
| 5.2 | Partial | [Field Engineer](./field-engineer.md) | Customer-facing | Stretch only |
| 5.0 | Partial | [Principal Software Solutions Engineer / Forward Deployed](./principal-software-solutions-engineer-forward-deployed.md) | Forward deployed | Stretch only |
| 4.8 | Weak / stretch | [AI/Search Engineer](./ai-search-engineer.md) | ML / data | Unlikely — only if posting is unusually broad |
| 4.8 | Weak / stretch | [Fintech Software Engineer](./fintech-software-engineer.md) | Payments / fintech | Unlikely — only if posting is unusually broad |
| 4.6 | Weak / stretch | [Data Engineer](./data-engineer.md) | ML / data | Unlikely — only if posting is unusually broad |
| 4.4 | Weak / stretch | [Staff Forward Deployed Engineer](./staff-forward-deployed-engineer.md) | Forward deployed | Unlikely — only if posting is unusually broad |
| 4.2 | Weak / stretch | [Machine Learning Engineer](./machine-learning-engineer.md) | ML / data | Unlikely — only if posting is unusually broad |
| 4.0 | Weak / stretch | [Lead Forward Deployed Engineer](./lead-forward-deployed-engineer.md) | Forward deployed | Unlikely — only if posting is unusually broad |
| 3.6 | Weak / stretch | [Connected-Device Software Engineer](./connected-device-software-engineer.md) | Hardware / devices | Unlikely — only if posting is unusually broad |
| 2.8 | Not demonstrated | [Networking Engineer](./networking-engineer.md) | Hardware / devices | Do not apply on this evidence |
| 2.4 | Not demonstrated | [Hardware/Software Engineer](./hardware-software-engineer.md) | Hardware / devices | Do not apply on this evidence |
| 1.8 | Not demonstrated | [Embedded Software Engineer](./embedded-software-engineer.md) | Hardware / devices | Do not apply on this evidence |
| 1.8 | Not demonstrated | [Lead Forward Deployed Engineer, Hospitality](./lead-forward-deployed-engineer-hospitality.md) | Forward deployed | Do not apply on this evidence |
| 1.6 | Not demonstrated | [Forward Deployed Engineer — Clearance Required](./forward-deployed-engineer-clearance-required.md) | Forward deployed | Do not apply on this evidence |
| 1.4 | Not demonstrated | [Firmware Engineer](./firmware-engineer.md) | Hardware / devices | Do not apply on this evidence |

---

## Where to spend applications

### Apply now (8.0+)

- **9.5** [Software Generalist](./software-generalist.md)
- **9.4** [Mobile Engineer](./mobile-engineer.md)
- **9.2** [Software Engineer](./software-engineer.md)
- **9.1** [Product Engineer](./product-engineer.md)
- **9.0** [Full-Stack Engineer](./full-stack-engineer.md)
- **8.8** [Software Development Engineer I (SDE I)](./software-development-engineer-i-sde-i.md)
- **8.8** [Software Engineer I](./software-engineer-i.md)
- **8.6** [AI Product Engineer](./ai-product-engineer.md)
- **8.6** [Application Developer](./application-developer.md)
- **8.4** [Founding AI Forward Deployed Engineer](./founding-ai-forward-deployed-engineer.md)
- **8.4** [Software Development Engineer II (SDE II)](./software-development-engineer-ii-sde-ii.md)
- **8.4** [Software Engineer II / SWE II](./software-engineer-ii-swe-ii.md)
- **8.3** [Backend Engineer](./backend-engineer.md)
- **8.2** [Applied AI Engineer](./applied-ai-engineer.md)
- **8.1** [Generative AI / GenAI Engineer](./generative-ai-genai-engineer.md)
- **8.0** [Associate Forward Deployed Engineer](./associate-forward-deployed-engineer.md)
- **8.0** [Solutions Engineer](./solutions-engineer.md)

### Apply with framing (6.5–7.9)

- **7.8** [Frontend Engineer](./frontend-engineer.md)
- **7.6** [AI Engineer](./ai-engineer.md)
- **7.6** [Forward Deployed AI Engineer](./forward-deployed-ai-engineer.md)
- **7.5** [Forward Deployed Engineer, AI Enablement](./forward-deployed-engineer-ai-enablement.md)
- **7.4** [Algorithm Engineer](./algorithm-engineer.md)
- **7.4** [Forward Deployed Engineer / Solution Architect](./forward-deployed-engineer-solution-architect.md)
- **7.2** [Android Engineer](./android-engineer.md)
- **7.2** [Forward Deployed Engineer (FDE)](./forward-deployed-engineer-fde.md)
- **7.2** [iOS Engineer](./ios-engineer.md)
- **7.1** [Solution Architect](./solution-architect.md)
- **7.0** [Cloud Engineer](./cloud-engineer.md)
- **7.0** [Security Engineer](./security-engineer.md)
- **6.6** [Payments Infrastructure Engineer](./payments-infrastructure-engineer.md)

### Stretch only (5.0–6.4)

- **6.4** [Developer Tools Engineer](./developer-tools-engineer.md)
- **6.4** [Senior Forward Deployed Engineer](./senior-forward-deployed-engineer.md)
- **6.4** [Support Engineer](./support-engineer.md)
- **6.3** [Analytics Engineer](./analytics-engineer.md)
- **6.2** [Forward Deployed Engineer, AI and Agentic SDLC](./forward-deployed-engineer-ai-and-agentic-sdlc.md)
- **6.2** [Platform Engineer](./platform-engineer.md)
- **5.8** [Sensor Algorithm Engineer](./sensor-algorithm-engineer.md)
- **5.6** [Developer Platform Engineer](./developer-platform-engineer.md)
- **5.4** [Infrastructure Engineer](./infrastructure-engineer.md)
- **5.2** [Field Engineer](./field-engineer.md)
- **5.0** [Principal Software Solutions Engineer / Forward Deployed](./principal-software-solutions-engineer-forward-deployed.md)

### Do not use FitGenius as the case (below 5.0)

- **4.8** [AI/Search Engineer](./ai-search-engineer.md)
- **4.8** [Fintech Software Engineer](./fintech-software-engineer.md)
- **4.6** [Data Engineer](./data-engineer.md)
- **4.4** [Staff Forward Deployed Engineer](./staff-forward-deployed-engineer.md)
- **4.2** [Machine Learning Engineer](./machine-learning-engineer.md)
- **4.0** [Lead Forward Deployed Engineer](./lead-forward-deployed-engineer.md)
- **3.6** [Connected-Device Software Engineer](./connected-device-software-engineer.md)
- **2.8** [Networking Engineer](./networking-engineer.md)
- **2.4** [Hardware/Software Engineer](./hardware-software-engineer.md)
- **1.8** [Embedded Software Engineer](./embedded-software-engineer.md)
- **1.8** [Lead Forward Deployed Engineer, Hospitality](./lead-forward-deployed-engineer-hospitality.md)
- **1.6** [Forward Deployed Engineer — Clearance Required](./forward-deployed-engineer-clearance-required.md)
- **1.4** [Firmware Engineer](./firmware-engineer.md)

---

## By family

### Core software

Family average: **8.7 / 10**

- **9.5** [Software Generalist](./software-generalist.md)
- **9.2** [Software Engineer](./software-engineer.md)
- **9.0** [Full-Stack Engineer](./full-stack-engineer.md)
- **8.8** [Software Engineer I](./software-engineer-i.md)
- **8.8** [Software Development Engineer I (SDE I)](./software-development-engineer-i-sde-i.md)
- **8.6** [Application Developer](./application-developer.md)
- **8.4** [Software Engineer II / SWE II](./software-engineer-ii-swe-ii.md)
- **8.4** [Software Development Engineer II (SDE II)](./software-development-engineer-ii-sde-ii.md)
- **8.3** [Backend Engineer](./backend-engineer.md)
- **7.8** [Frontend Engineer](./frontend-engineer.md)
### Mobile

Family average: **7.9 / 10**

- **9.4** [Mobile Engineer](./mobile-engineer.md)
- **7.2** [iOS Engineer](./ios-engineer.md)
- **7.2** [Android Engineer](./android-engineer.md)
### Product / AI product

Family average: **8.3 / 10**

- **9.1** [Product Engineer](./product-engineer.md)
- **8.6** [AI Product Engineer](./ai-product-engineer.md)
- **8.2** [Applied AI Engineer](./applied-ai-engineer.md)
- **8.1** [Generative AI / GenAI Engineer](./generative-ai-genai-engineer.md)
- **7.6** [AI Engineer](./ai-engineer.md)
### Cloud / platform

Family average: **6.3 / 10**

- **7.0** [Cloud Engineer](./cloud-engineer.md)
- **7.0** [Security Engineer](./security-engineer.md)
- **6.4** [Developer Tools Engineer](./developer-tools-engineer.md)
- **6.2** [Platform Engineer](./platform-engineer.md)
- **5.6** [Developer Platform Engineer](./developer-platform-engineer.md)
- **5.4** [Infrastructure Engineer](./infrastructure-engineer.md)
### ML / data

Family average: **5.5 / 10**

- **7.4** [Algorithm Engineer](./algorithm-engineer.md)
- **6.3** [Analytics Engineer](./analytics-engineer.md)
- **4.8** [AI/Search Engineer](./ai-search-engineer.md)
- **4.6** [Data Engineer](./data-engineer.md)
- **4.2** [Machine Learning Engineer](./machine-learning-engineer.md)
### Payments / fintech

Family average: **5.7 / 10**

- **6.6** [Payments Infrastructure Engineer](./payments-infrastructure-engineer.md)
- **4.8** [Fintech Software Engineer](./fintech-software-engineer.md)
### Customer-facing

Family average: **6.7 / 10**

- **8.0** [Solutions Engineer](./solutions-engineer.md)
- **7.1** [Solution Architect](./solution-architect.md)
- **6.4** [Support Engineer](./support-engineer.md)
- **5.2** [Field Engineer](./field-engineer.md)
### Forward deployed

Family average: **5.8 / 10**

- **8.4** [Founding AI Forward Deployed Engineer](./founding-ai-forward-deployed-engineer.md)
- **8.0** [Associate Forward Deployed Engineer](./associate-forward-deployed-engineer.md)
- **7.6** [Forward Deployed AI Engineer](./forward-deployed-ai-engineer.md)
- **7.5** [Forward Deployed Engineer, AI Enablement](./forward-deployed-engineer-ai-enablement.md)
- **7.4** [Forward Deployed Engineer / Solution Architect](./forward-deployed-engineer-solution-architect.md)
- **7.2** [Forward Deployed Engineer (FDE)](./forward-deployed-engineer-fde.md)
- **6.4** [Senior Forward Deployed Engineer](./senior-forward-deployed-engineer.md)
- **6.2** [Forward Deployed Engineer, AI and Agentic SDLC](./forward-deployed-engineer-ai-and-agentic-sdlc.md)
- **5.0** [Principal Software Solutions Engineer / Forward Deployed](./principal-software-solutions-engineer-forward-deployed.md)
- **4.4** [Staff Forward Deployed Engineer](./staff-forward-deployed-engineer.md)
- **4.0** [Lead Forward Deployed Engineer](./lead-forward-deployed-engineer.md)
- **1.8** [Lead Forward Deployed Engineer, Hospitality](./lead-forward-deployed-engineer-hospitality.md)
- **1.6** [Forward Deployed Engineer — Clearance Required](./forward-deployed-engineer-clearance-required.md)
### Hardware / devices

Family average: **3.0 / 10**

- **5.8** [Sensor Algorithm Engineer](./sensor-algorithm-engineer.md)
- **3.6** [Connected-Device Software Engineer](./connected-device-software-engineer.md)
- **2.8** [Networking Engineer](./networking-engineer.md)
- **2.4** [Hardware/Software Engineer](./hardware-software-engineer.md)
- **1.8** [Embedded Software Engineer](./embedded-software-engineer.md)
- **1.4** [Firmware Engineer](./firmware-engineer.md)

---

## How to use these documents

1. Pick the title you are applying to and open its file in this folder.
2. Copy **what you did** and **how it applies** into resume bullets — keep the gaps so you do not overclaim.
3. Use **how to talk about it** as the interview outline.
4. If two titles are close (SWE II vs SDE II, FDE vs Solutions Engineer), read both; the difference is vocabulary and hiring culture, not a different career.

Related visual: a filterable ratings canvas lives beside chat as `fitgenius-role-experience-ratings.canvas.tsx` (same scores as this folder).

---

## Files in this folder

- [Software Generalist](./software-generalist.md) — 9.5/10
- [Mobile Engineer](./mobile-engineer.md) — 9.4/10
- [Software Engineer](./software-engineer.md) — 9.2/10
- [Product Engineer](./product-engineer.md) — 9.1/10
- [Full-Stack Engineer](./full-stack-engineer.md) — 9.0/10
- [Software Development Engineer I (SDE I)](./software-development-engineer-i-sde-i.md) — 8.8/10
- [Software Engineer I](./software-engineer-i.md) — 8.8/10
- [AI Product Engineer](./ai-product-engineer.md) — 8.6/10
- [Application Developer](./application-developer.md) — 8.6/10
- [Founding AI Forward Deployed Engineer](./founding-ai-forward-deployed-engineer.md) — 8.4/10
- [Software Development Engineer II (SDE II)](./software-development-engineer-ii-sde-ii.md) — 8.4/10
- [Software Engineer II / SWE II](./software-engineer-ii-swe-ii.md) — 8.4/10
- [Backend Engineer](./backend-engineer.md) — 8.3/10
- [Applied AI Engineer](./applied-ai-engineer.md) — 8.2/10
- [Generative AI / GenAI Engineer](./generative-ai-genai-engineer.md) — 8.1/10
- [Associate Forward Deployed Engineer](./associate-forward-deployed-engineer.md) — 8.0/10
- [Solutions Engineer](./solutions-engineer.md) — 8.0/10
- [Frontend Engineer](./frontend-engineer.md) — 7.8/10
- [AI Engineer](./ai-engineer.md) — 7.6/10
- [Forward Deployed AI Engineer](./forward-deployed-ai-engineer.md) — 7.6/10
- [Forward Deployed Engineer, AI Enablement](./forward-deployed-engineer-ai-enablement.md) — 7.5/10
- [Algorithm Engineer](./algorithm-engineer.md) — 7.4/10
- [Forward Deployed Engineer / Solution Architect](./forward-deployed-engineer-solution-architect.md) — 7.4/10
- [Android Engineer](./android-engineer.md) — 7.2/10
- [Forward Deployed Engineer (FDE)](./forward-deployed-engineer-fde.md) — 7.2/10
- [iOS Engineer](./ios-engineer.md) — 7.2/10
- [Solution Architect](./solution-architect.md) — 7.1/10
- [Cloud Engineer](./cloud-engineer.md) — 7.0/10
- [Security Engineer](./security-engineer.md) — 7.0/10
- [Payments Infrastructure Engineer](./payments-infrastructure-engineer.md) — 6.6/10
- [Developer Tools Engineer](./developer-tools-engineer.md) — 6.4/10
- [Senior Forward Deployed Engineer](./senior-forward-deployed-engineer.md) — 6.4/10
- [Support Engineer](./support-engineer.md) — 6.4/10
- [Analytics Engineer](./analytics-engineer.md) — 6.3/10
- [Forward Deployed Engineer, AI and Agentic SDLC](./forward-deployed-engineer-ai-and-agentic-sdlc.md) — 6.2/10
- [Platform Engineer](./platform-engineer.md) — 6.2/10
- [Sensor Algorithm Engineer](./sensor-algorithm-engineer.md) — 5.8/10
- [Developer Platform Engineer](./developer-platform-engineer.md) — 5.6/10
- [Infrastructure Engineer](./infrastructure-engineer.md) — 5.4/10
- [Field Engineer](./field-engineer.md) — 5.2/10
- [Principal Software Solutions Engineer / Forward Deployed](./principal-software-solutions-engineer-forward-deployed.md) — 5.0/10
- [AI/Search Engineer](./ai-search-engineer.md) — 4.8/10
- [Fintech Software Engineer](./fintech-software-engineer.md) — 4.8/10
- [Data Engineer](./data-engineer.md) — 4.6/10
- [Staff Forward Deployed Engineer](./staff-forward-deployed-engineer.md) — 4.4/10
- [Machine Learning Engineer](./machine-learning-engineer.md) — 4.2/10
- [Lead Forward Deployed Engineer](./lead-forward-deployed-engineer.md) — 4.0/10
- [Connected-Device Software Engineer](./connected-device-software-engineer.md) — 3.6/10
- [Networking Engineer](./networking-engineer.md) — 2.8/10
- [Hardware/Software Engineer](./hardware-software-engineer.md) — 2.4/10
- [Embedded Software Engineer](./embedded-software-engineer.md) — 1.8/10
- [Lead Forward Deployed Engineer, Hospitality](./lead-forward-deployed-engineer-hospitality.md) — 1.8/10
- [Forward Deployed Engineer — Clearance Required](./forward-deployed-engineer-clearance-required.md) — 1.6/10
- [Firmware Engineer](./firmware-engineer.md) — 1.4/10

---

*Assessment is based on the FitGenius repository as of September 2026. It does not include work outside this repo. Update scores if you later ship store launch, Stripe, a second customer deployment, or hardware/firmware.*
