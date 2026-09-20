# Job-title experience overview

This folder maps **one production project** — the Insightful Care Solutions LLC telepsychiatry website — onto 54 job titles. Each title has its own document. This file is the index, the rating method, and the honest summary.

**Evidence source:** Insightful Care Solutions LLC — production telepsychiatry website for a New Jersey psychiatric practice  
**Live site:** https://insightfulcare.solutions/  
**Your role on the work:** Solo engineer (Zakiy Manigo), Oct 2025 – Jul 2026  
**What shipped:** React + Vite + Tailwind SPA, Firebase Hosting, Google Apps Script contact backend, ChARM Health booking integration, SEO/AI-crawler assets, accessibility and responsive UX, client-facing ops docs


## How to use these documents

- Treat ratings as **evidence from this repo**, not as a ceiling on your career.
- **Lead** with titles scored 7–8 when this project is the main story.
- **Support** titles scored 5–6 with this project plus other work.
- **Do not** headline titles scored 0–3 from this project.

## Rating scale

| Score | Band | Meaning |
|------:|------|---------|
| 8 | Strong match | This project is credible primary evidence for an entry / early-career version of the role |
| 7 | Good junior match | Complete production story; interviews will still probe depth |
| 6 | Solid adjacent / junior | Real work; claim junior-level only if you are honest about scope |
| 5 | Partial | Relevant skills; typical hiring bar is broader |
| 4 | Thin-to-partial | Supporting evidence only |
| 3 | Adjacent | Habits transfer; craft does not |
| 2 | Weak adjacency | A few related decisions |
| 1 | Minimal | Almost nothing maps |
| 0 | None | Do not claim the title from this project |

Mid-level, senior, staff, lead, and principal titles are scored against **those** bars, not against “did you write code.” A strong SWE I story can still be a 3 for SWE II.

## Snapshot

| Metric | Value |
|--------|------:|
| Titles scored | 54 |
| Mean rating | 2.7 / 10 |
| Strongest score in this set | 8 / 10 (Frontend Engineer) |
| Titles at 7+ (lead with these) | 5 |
| Titles at 6 (honest junior) | 5 |
| Titles at 4–5 (partial) | 7 |
| Titles at 2–3 (adjacent) | 16 |
| Titles at 0–1 (do not claim) | 21 |

## What you actually built (shared facts)

Insightful Care Solutions LLC is a **virtual-only New Jersey telepsychiatry practice**. This repository is **not** an EHR or clinical system. It is the public product that:

1. Explains services, team, insurance, and conditions treated
2. Sends patients to **ChARM Health** public calendar to book
3. Captures inquiries via a **Google Apps Script** `doPost` handler that emails staff and the submitter
4. Surfaces **crisis resources** (911, 988, NJ Hopeline, county hotlines)
5. Is discoverable via **schema.org, sitemap, robots.txt, llms.txt, IndexNow**, and owner playbooks for Search Console / Bing / Google Business Profile

**Stack:** JavaScript, React 18 (production) and React 19 (redesign), Vite, Tailwind CSS, Firebase Hosting, Google Apps Script, documented EmailJS alternative (unused in code).

**Architecture:** Two SPAs in one repo. Production is a large `App.jsx`. The redesign is modular (`components/ui|layout|sections`, hooks, `content.js`). Only the production `dist` is configured in `firebase.json`.

**Not in the repo:** databases, auth, native iOS/Android, payments processors, ML models, CI/CD, Docker, tests, monitoring, firmware, clearance work.

## Lead with these titles

- **8/10** — [Frontend Engineer](frontend-engineer.md)
- **7/10** — [Application Developer](application-developer.md)
- **7/10** — [Associate Forward Deployed Engineer](associate-forward-deployed-engineer.md)
- **7/10** — [Product Engineer](product-engineer.md)
- **7/10** — [Software Engineer I](software-engineer-i.md)

## Honest junior / generalist titles

- **6/10** — [Forward Deployed Engineer (FDE)](forward-deployed-engineer.md)
- **6/10** — [Software Development Engineer I (SDE I)](software-development-engineer-i-sde-i.md)
- **6/10** — [Software Engineer](software-engineer.md)
- **6/10** — [Software Generalist](software-generalist.md)
- **6/10** — [Solutions Engineer](solutions-engineer.md)

## Partial — use as supporting evidence

- **5/10** — [Forward Deployed Engineer / Solution Architect](forward-deployed-engineer-solution-architect.md)
- **5/10** — [Full-Stack Engineer](full-stack-engineer.md)
- **4/10** — [AI/Search Engineer](ai-search-engineer.md)
- **4/10** — [Cloud Engineer](cloud-engineer.md)
- **4/10** — [Developer Tools Engineer](developer-tools-engineer.md)
- **4/10** — [Software Engineer II / SWE II](software-engineer-ii-swe-ii.md)
- **4/10** — [Support Engineer](support-engineer.md)

## Adjacent only

- **3/10** — [AI Product Engineer](ai-product-engineer.md)
- **3/10** — [Backend Engineer](backend-engineer.md)
- **3/10** — [Mobile Engineer](mobile-engineer.md)
- **3/10** — [Senior Forward Deployed Engineer](senior-forward-deployed-engineer.md)
- **3/10** — [Software Development Engineer II (SDE II)](software-development-engineer-ii-sde-ii.md)
- **3/10** — [Solution Architect](solution-architect.md)
- **2/10** — [AI Engineer](ai-engineer.md)
- **2/10** — [Developer Platform Engineer](developer-platform-engineer.md)
- **2/10** — [Field Engineer](field-engineer.md)
- **2/10** — [Forward Deployed AI Engineer](forward-deployed-ai-engineer.md)
- **2/10** — [Forward Deployed Engineer, AI Enablement](forward-deployed-engineer-ai-enablement.md)
- **2/10** — [Infrastructure Engineer](infrastructure-engineer.md)
- **2/10** — [Lead Forward Deployed Engineer](lead-forward-deployed-engineer.md)
- **2/10** — [Platform Engineer](platform-engineer.md)
- **2/10** — [Principal Software Solutions Engineer / Forward Deployed](principal-software-solutions-engineer-forward-deployed.md)
- **2/10** — [Security Engineer](security-engineer.md)

## Do not claim from this project

- **1/10** — [Algorithm Engineer](algorithm-engineer.md)
- **1/10** — [Analytics Engineer](analytics-engineer.md)
- **1/10** — [Android Engineer](android-engineer.md)
- **1/10** — [Applied AI Engineer](applied-ai-engineer.md)
- **1/10** — [Connected-Device Software Engineer](connected-device-software-engineer.md)
- **1/10** — [Data Engineer](data-engineer.md)
- **1/10** — [Fintech Software Engineer](fintech-software-engineer.md)
- **1/10** — [Forward Deployed Engineer, AI & Agentic SDLC](forward-deployed-engineer-ai-agentic-sdlc.md)
- **1/10** — [Founding AI Forward Deployed Engineer](founding-ai-forward-deployed-engineer.md)
- **1/10** — [Generative AI / GenAI Engineer](generative-ai-genai-engineer.md)
- **1/10** — [Lead Forward Deployed Engineer, Hospitality](lead-forward-deployed-engineer-hospitality.md)
- **1/10** — [Networking Engineer](networking-engineer.md)
- **1/10** — [Staff Forward Deployed Engineer](staff-forward-deployed-engineer.md)
- **1/10** — [iOS Engineer](ios-engineer.md)
- **0/10** — [Embedded Software Engineer](embedded-software-engineer.md)
- **0/10** — [Firmware Engineer](firmware-engineer.md)
- **0/10** — [Forward Deployed Engineer — Clearance Required](forward-deployed-engineer-clearance-required.md)
- **0/10** — [Hardware/Software Engineer](hardware-software-engineer.md)
- **0/10** — [Machine Learning Engineer](machine-learning-engineer.md)
- **0/10** — [Payments Infrastructure Engineer](payments-infrastructure-engineer.md)
- **0/10** — [Sensor Algorithm Engineer](sensor-algorithm-engineer.md)

## All titles by rating

| Rating | Band | Title |
|------:|------|-------|
| 8/10 | Strong match | [Frontend Engineer](frontend-engineer.md) |
| 7/10 | Good junior match | [Application Developer](application-developer.md) |
| 7/10 | Good junior match | [Associate Forward Deployed Engineer](associate-forward-deployed-engineer.md) |
| 7/10 | Good junior match | [Product Engineer](product-engineer.md) |
| 7/10 | Good junior match | [Software Engineer I](software-engineer-i.md) |
| 6/10 | Solid adjacent / junior | [Forward Deployed Engineer (FDE)](forward-deployed-engineer.md) |
| 6/10 | Solid adjacent / junior | [Software Development Engineer I (SDE I)](software-development-engineer-i-sde-i.md) |
| 6/10 | Solid adjacent / junior | [Software Engineer](software-engineer.md) |
| 6/10 | Solid adjacent / junior | [Software Generalist](software-generalist.md) |
| 6/10 | Solid adjacent / junior | [Solutions Engineer](solutions-engineer.md) |
| 5/10 | Partial match | [Forward Deployed Engineer / Solution Architect](forward-deployed-engineer-solution-architect.md) |
| 5/10 | Partial match | [Full-Stack Engineer](full-stack-engineer.md) |
| 4/10 | Thin-to-partial | [AI/Search Engineer](ai-search-engineer.md) |
| 4/10 | Thin-to-partial | [Cloud Engineer](cloud-engineer.md) |
| 4/10 | Thin-to-partial | [Developer Tools Engineer](developer-tools-engineer.md) |
| 4/10 | Thin-to-partial | [Software Engineer II / SWE II](software-engineer-ii-swe-ii.md) |
| 4/10 | Thin-to-partial | [Support Engineer](support-engineer.md) |
| 3/10 | Adjacent only | [AI Product Engineer](ai-product-engineer.md) |
| 3/10 | Adjacent only | [Backend Engineer](backend-engineer.md) |
| 3/10 | Adjacent only | [Mobile Engineer](mobile-engineer.md) |
| 3/10 | Adjacent only | [Senior Forward Deployed Engineer](senior-forward-deployed-engineer.md) |
| 3/10 | Adjacent only | [Software Development Engineer II (SDE II)](software-development-engineer-ii-sde-ii.md) |
| 3/10 | Adjacent only | [Solution Architect](solution-architect.md) |
| 2/10 | Weak adjacency | [AI Engineer](ai-engineer.md) |
| 2/10 | Weak adjacency | [Developer Platform Engineer](developer-platform-engineer.md) |
| 2/10 | Weak adjacency | [Field Engineer](field-engineer.md) |
| 2/10 | Weak adjacency | [Forward Deployed AI Engineer](forward-deployed-ai-engineer.md) |
| 2/10 | Weak adjacency | [Forward Deployed Engineer, AI Enablement](forward-deployed-engineer-ai-enablement.md) |
| 2/10 | Weak adjacency | [Infrastructure Engineer](infrastructure-engineer.md) |
| 2/10 | Weak adjacency | [Lead Forward Deployed Engineer](lead-forward-deployed-engineer.md) |
| 2/10 | Weak adjacency | [Platform Engineer](platform-engineer.md) |
| 2/10 | Weak adjacency | [Principal Software Solutions Engineer / Forward Deployed](principal-software-solutions-engineer-forward-deployed.md) |
| 2/10 | Weak adjacency | [Security Engineer](security-engineer.md) |
| 1/10 | Minimal | [Algorithm Engineer](algorithm-engineer.md) |
| 1/10 | Minimal | [Analytics Engineer](analytics-engineer.md) |
| 1/10 | Minimal | [Android Engineer](android-engineer.md) |
| 1/10 | Minimal | [Applied AI Engineer](applied-ai-engineer.md) |
| 1/10 | Minimal | [Connected-Device Software Engineer](connected-device-software-engineer.md) |
| 1/10 | Minimal | [Data Engineer](data-engineer.md) |
| 1/10 | Minimal | [Fintech Software Engineer](fintech-software-engineer.md) |
| 1/10 | Minimal | [Forward Deployed Engineer, AI & Agentic SDLC](forward-deployed-engineer-ai-agentic-sdlc.md) |
| 1/10 | Minimal | [Founding AI Forward Deployed Engineer](founding-ai-forward-deployed-engineer.md) |
| 1/10 | Minimal | [Generative AI / GenAI Engineer](generative-ai-genai-engineer.md) |
| 1/10 | Minimal | [Lead Forward Deployed Engineer, Hospitality](lead-forward-deployed-engineer-hospitality.md) |
| 1/10 | Minimal | [Networking Engineer](networking-engineer.md) |
| 1/10 | Minimal | [Staff Forward Deployed Engineer](staff-forward-deployed-engineer.md) |
| 1/10 | Minimal | [iOS Engineer](ios-engineer.md) |
| 0/10 | No relevant experience | [Embedded Software Engineer](embedded-software-engineer.md) |
| 0/10 | No relevant experience | [Firmware Engineer](firmware-engineer.md) |
| 0/10 | No relevant experience | [Forward Deployed Engineer — Clearance Required](forward-deployed-engineer-clearance-required.md) |
| 0/10 | No relevant experience | [Hardware/Software Engineer](hardware-software-engineer.md) |
| 0/10 | No relevant experience | [Machine Learning Engineer](machine-learning-engineer.md) |
| 0/10 | No relevant experience | [Payments Infrastructure Engineer](payments-infrastructure-engineer.md) |
| 0/10 | No relevant experience | [Sensor Algorithm Engineer](sensor-algorithm-engineer.md) |

## How clusters compare

**Frontend / product / application** is the real center of gravity. You shipped UI, accessibility, conversion UX, a design-system refactor, and a live site.

**FDE / solutions / generalist** is the second cluster. You embedded with a healthcare customer, integrated their EHR calendar, and left operational docs. That is junior FDE/SE shaped work, not Palantir-scale deployment.

**Full-stack / cloud / search** is partial. GAS + Firebase + technical SEO are real, but shallow versus specialists.

**Backend, mobile native, platform, infra, data, ML/AI product, fintech, payments, networking, security, embedded, firmware, sensors, clearance, hospitality, agentic SDLC** are not evidenced at a hiring bar.

## Recommended targeting (if this project is the main story)

1. **Frontend Engineer**, **Application Developer**, **Software Engineer I**, **Product Engineer**, **Associate Forward Deployed Engineer**
2. Then **Software Engineer**, **Software Generalist**, **Solutions Engineer**, **SDE I**, **Full-Stack Engineer** (frontend-heavy)
3. Stretch only with extra evidence: **SWE II**, **Cloud Engineer**, **AI/Search** (SEO-leaning), **FDE / Solution Architect**
4. Skip from this repo: native mobile, ML/AI engineering, payments, embedded, clearance, principal/staff/lead

## Method notes

- Evidence reviewed: production app, redesign app, Firebase config, GAS backend, SEO/public assets, deployment and owner docs, git history (18 commits, Oct 2025 – Jul 2026, Zakiy Manigo).
- Live URLs considered: `https://insightfulcare.solutions/` and Firebase Hosting fallback.
- Each document answers the same three questions: what you did here, how it maps to that title, and how far it is from how that title is usually hired.
