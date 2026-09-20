# Local AI — job-title experience overview

This folder maps **only this repository** (Local AI desktop app) onto common job titles. It is not a résumé of your whole career. If you have other jobs, internships, or clearance, add those separately.

## The project in one paragraph

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

## How to read the scores

Ratings are **0–10 for this repository only**, not a full career score.

| Score | Meaning |
| --- | --- |
| 9–10 | This project is a primary hiring signal for the role |
| 7–8 | Strong transferable evidence; interviewable as I/II on this stack |
| 5–6 | Partial overlap; you can tell a credible story with gaps named |
| 3–4 | Adjacent skills only |
| 0–2 | Essentially no evidence from this work |

A high score means “this repo is a credible work sample for that hiring loop.” A low score means “do not stretch this repo onto that title.”

## Ranked findings

| Score | Job title | Level |
| ---: | --- | --- |
| 9.0 | [AI Product Engineer](./ai-product-engineer.md) | Primary match |
| 9.0 | [Application Developer](./application-developer.md) | Primary match |
| 8.5 | [Full-Stack Engineer](./full-stack-engineer.md) | Strong (desktop full stack, not typical web SaaS) |
| 8.5 | [Generative AI / GenAI Engineer](./generative-ai-engineer.md) | Strong |
| 8.5 | [Product Engineer](./product-engineer.md) | Primary match |
| 8.5 | [Software Development Engineer I (SDE I)](./sde-i.md) | Very strong for SDE I |
| 8.5 | [Software Engineer I](./software-engineer-i.md) | Very strong for SWE I |
| 8.5 | [Software Generalist](./software-generalist.md) | Primary match |
| 8.0 | [Applied AI Engineer](./applied-ai-engineer.md) | Strong |
| 8.0 | [Backend Engineer](./backend-engineer.md) | Strong for native/backend; not HTTP services |
| 8.0 | [Software Engineer](./software-engineer.md) | Strong — general SWE I/early II from one product |
| 7.5 | [AI Engineer](./ai-engineer.md) | Strong applied AI engineering |
| 7.5 | [Frontend Engineer](./frontend-engineer.md) | Solid product UI; not a design-system specialist |
| 7.0 | [Associate Forward Deployed Engineer](./associate-forward-deployed-engineer.md) | Reasonable associate FDE signal |
| 7.0 | [Software Development Engineer II (SDE II)](./sde-ii.md) | Partial SDE II — design yes, org scale no |
| 7.0 | [Software Engineer II / SWE II](./software-engineer-ii.md) | Credible early SWE II; thin on scale |
| 6.5 | [AI/Search Engineer](./ai-search-engineer.md) | Partial — local RAG, not search ranking |
| 6.5 | [Forward Deployed AI Engineer](./forward-deployed-ai-engineer.md) | Builder match for AI-flavored FDE |
| 6.5 | [Forward Deployed Engineer, AI & Agentic SDLC](./forward-deployed-engineer-ai-agentic-sdlc.md) | Partial — agent tools + coding-oriented routing, not an SDLC platform |
| 6.0 | [Forward Deployed Engineer (FDE)](./forward-deployed-engineer.md) | Builder-heavy FDE; light on customer deployment |
| 6.0 | [Forward Deployed Engineer, AI Enablement](./forward-deployed-engineer-ai-enablement.md) | Partial — you enabled yourself, not an enterprise workforce |
| 6.0 | [Solutions Engineer](./solutions-engineer.md) | Partial — you built the solution, little customer-facing SE motion |
| 5.5 | [Forward Deployed Engineer / Solution Architect](./forward-deployed-engineer-solution-architect.md) | Hybrid title: stronger engineer than architect-for-hire |
| 5.5 | [Security Engineer](./security-engineer.md) | Solid application-security instincts; not a SecEng career yet |
| 5.0 | [Developer Tools Engineer](./developer-tools-engineer.md) | Partial — tools inside an AI coding-adjacent app |
| 5.0 | [Founding AI Forward Deployed Engineer](./founding-ai-forward-deployed-engineer.md) | 0→1 builder yes; founding FDE also needs GTM/customer zero |
| 5.0 | [Platform Engineer](./platform-engineer.md) | Partial — app platform, not org platform |
| 5.0 | [Solution Architect](./solution-architect.md) | Light architecture of one product, not enterprise SA |
| 5.0 | [Support Engineer](./support-engineer.md) | You wrote support-shaped docs and fail-closed errors, not a support rotation |
| 4.0 | [Algorithm Engineer](./algorithm-engineer.md) | Light — heuristics, not published algorithms |
| 4.0 | [Data Engineer](./data-engineer.md) | Weak — app data, not data platform |
| 4.0 | [Developer Platform Engineer](./developer-platform-engineer.md) | Weak — one product’s DX, not a platform org |
| 4.0 | [Field Engineer](./field-engineer.md) | Lab/self-install only |
| 4.0 | [Hardware/Software Engineer](./hardware-software-engineer.md) | Software side of PC hardware awareness |
| 4.0 | [Infrastructure Engineer](./infrastructure-engineer.md) | Adjacent OS/runtime packaging only |
| 4.0 | [Machine Learning Engineer](./machine-learning-engineer.md) | Inference productization, not ML training |
| 4.0 | [Senior Forward Deployed Engineer](./senior-forward-deployed-engineer.md) | Below senior FDE without customer outcomes |
| 3.0 | [Connected-Device Software Engineer](./connected-device-software-engineer.md) | Weak — local device, not IoT fleet |
| 3.0 | [Lead Forward Deployed Engineer](./lead-forward-deployed-engineer.md) | Not a Lead signal |
| 3.0 | [Principal Software Solutions Engineer / Forward Deployed](./principal-software-solutions-engineer-forward-deployed.md) | Not a Principal signal |
| 3.0 | [Staff Forward Deployed Engineer](./staff-forward-deployed-engineer.md) | Not a Staff signal |
| 2.0 | [Analytics Engineer](./analytics-engineer.md) | No evidence |
| 2.0 | [Cloud Engineer](./cloud-engineer.md) | No cloud delivery |
| 2.0 | [Embedded Software Engineer](./embedded-software-engineer.md) | No embedded targets |
| 2.0 | [Mobile Engineer](./mobile-engineer.md) | Almost no evidence |
| 2.0 | [Networking Engineer](./networking-engineer.md) | No network engineering |
| 1.0 | [Android Engineer](./android-engineer.md) | No evidence |
| 1.0 | [Fintech Software Engineer](./fintech-software-engineer.md) | No evidence |
| 1.0 | [Firmware Engineer](./firmware-engineer.md) | No evidence |
| 1.0 | [Forward Deployed Engineer — Clearance Required](./forward-deployed-engineer-clearance-required.md) | No clearance or classified delivery in this repo |
| 1.0 | [Lead Forward Deployed Engineer, Hospitality](./lead-forward-deployed-engineer-hospitality.md) | No hospitality domain |
| 1.0 | [Payments Infrastructure Engineer](./payments-infrastructure-engineer.md) | No evidence |
| 1.0 | [Sensor Algorithm Engineer](./sensor-algorithm-engineer.md) | No evidence |
| 1.0 | [iOS Engineer](./ios-engineer.md) | No evidence |

## Banded findings

### Primary matches (8.0+)

- **AI Product Engineer** (9.0) — Primary match
- **Application Developer** (9.0) — Primary match
- **Full-Stack Engineer** (8.5) — Strong (desktop full stack, not typical web SaaS)
- **Generative AI / GenAI Engineer** (8.5) — Strong
- **Product Engineer** (8.5) — Primary match
- **Software Development Engineer I (SDE I)** (8.5) — Very strong for SDE I
- **Software Engineer I** (8.5) — Very strong for SWE I
- **Software Generalist** (8.5) — Primary match
- **Applied AI Engineer** (8.0) — Strong
- **Backend Engineer** (8.0) — Strong for native/backend; not HTTP services
- **Software Engineer** (8.0) — Strong — general SWE I/early II from one product

### Strong / interviewable (7.0–7.9)

- **AI Engineer** (7.5) — Strong applied AI engineering
- **Frontend Engineer** (7.5) — Solid product UI; not a design-system specialist
- **Associate Forward Deployed Engineer** (7.0) — Reasonable associate FDE signal
- **Software Development Engineer II (SDE II)** (7.0) — Partial SDE II — design yes, org scale no
- **Software Engineer II / SWE II** (7.0) — Credible early SWE II; thin on scale

### Partial (5.0–6.9)

- **AI/Search Engineer** (6.5) — Partial — local RAG, not search ranking
- **Forward Deployed AI Engineer** (6.5) — Builder match for AI-flavored FDE
- **Forward Deployed Engineer, AI & Agentic SDLC** (6.5) — Partial — agent tools + coding-oriented routing, not an SDLC platform
- **Forward Deployed Engineer (FDE)** (6.0) — Builder-heavy FDE; light on customer deployment
- **Forward Deployed Engineer, AI Enablement** (6.0) — Partial — you enabled yourself, not an enterprise workforce
- **Solutions Engineer** (6.0) — Partial — you built the solution, little customer-facing SE motion
- **Forward Deployed Engineer / Solution Architect** (5.5) — Hybrid title: stronger engineer than architect-for-hire
- **Security Engineer** (5.5) — Solid application-security instincts; not a SecEng career yet
- **Developer Tools Engineer** (5.0) — Partial — tools inside an AI coding-adjacent app
- **Founding AI Forward Deployed Engineer** (5.0) — 0→1 builder yes; founding FDE also needs GTM/customer zero
- **Platform Engineer** (5.0) — Partial — app platform, not org platform
- **Solution Architect** (5.0) — Light architecture of one product, not enterprise SA
- **Support Engineer** (5.0) — You wrote support-shaped docs and fail-closed errors, not a support rotation

### Adjacent (3.0–4.9)

- **Algorithm Engineer** (4.0) — Light — heuristics, not published algorithms
- **Data Engineer** (4.0) — Weak — app data, not data platform
- **Developer Platform Engineer** (4.0) — Weak — one product’s DX, not a platform org
- **Field Engineer** (4.0) — Lab/self-install only
- **Hardware/Software Engineer** (4.0) — Software side of PC hardware awareness
- **Infrastructure Engineer** (4.0) — Adjacent OS/runtime packaging only
- **Machine Learning Engineer** (4.0) — Inference productization, not ML training
- **Senior Forward Deployed Engineer** (4.0) — Below senior FDE without customer outcomes
- **Connected-Device Software Engineer** (3.0) — Weak — local device, not IoT fleet
- **Lead Forward Deployed Engineer** (3.0) — Not a Lead signal
- **Principal Software Solutions Engineer / Forward Deployed** (3.0) — Not a Principal signal
- **Staff Forward Deployed Engineer** (3.0) — Not a Staff signal

### Do not use this project as evidence (0–2.9)

- **Analytics Engineer** (2.0) — No evidence
- **Cloud Engineer** (2.0) — No cloud delivery
- **Embedded Software Engineer** (2.0) — No embedded targets
- **Mobile Engineer** (2.0) — Almost no evidence
- **Networking Engineer** (2.0) — No network engineering
- **Android Engineer** (1.0) — No evidence
- **Fintech Software Engineer** (1.0) — No evidence
- **Firmware Engineer** (1.0) — No evidence
- **Forward Deployed Engineer — Clearance Required** (1.0) — No clearance or classified delivery in this repo
- **Lead Forward Deployed Engineer, Hospitality** (1.0) — No hospitality domain
- **Payments Infrastructure Engineer** (1.0) — No evidence
- **Sensor Algorithm Engineer** (1.0) — No evidence
- **iOS Engineer** (1.0) — No evidence


## What you can honestly claim from this repo

You designed and shipped a **Windows desktop AI product** with a **React/TypeScript UI** and a **Rust native backend**:

- Offline GGUF inference via pinned llama.cpp (`llama-cli` child process, streaming, cancel, GPU/CPU/Vulkan/CUDA runtime selection)
- SQLite persistence (chats, models, settings, documents, projects/prompts)
- Local RAG pipeline (chunk, hash, embed, query/citations — retrieval still failed in the recorded manual run)
- Constrained agent tools (JSON tool calls, path roots, destructive/shell denied by default)
- Prompt templates in Rust (ChatML / Llama 3 / Mistral, Qwen3 thinking flags, context budget)
- Application UX (onboarding, command palette, themes, help, hardware size warnings)
- Packaging (NSIS current-user installer, portable USB layout, unsigned-cert honesty)
- Engineering hygiene (Vitest, Cargo fixture tests, CSP, path canonicalization, secret redaction, capability-locked webview)

## What you should not claim from this repo

- Mobile/iOS/Android, embedded/firmware, fintech/payments, hospitality domain, warehouse/analytics engineering
- Cloud infrastructure, networking engineering, or a cleared deployment
- Staff/Principal/Lead FDE (scope and people leadership)
- Production RAG quality (MAN26/MAN27 failed)
- Native in-process llama.cpp (Stage B still `NativeUnavailable`)
- Authenticode-signed installer

## Suggested application strategy

1. **Lead with:** AI Product Engineer, Application Developer, Software Generalist, Full-Stack Engineer, SWE I / SDE I, Applied/GenAI Engineer, Product Engineer.
2. **Use as a work sample plus other experience:** SWE II / SDE II, Backend, Frontend, AI Engineer, Associate FDE, Forward Deployed AI Engineer.
3. **Supporting anecdote only:** Security (product), Solutions Engineer (demo), Platform/DevTools, Hardware-aware desktop, AI/Search (RAG design).
4. **Skip unless you have outside evidence:** titles scored under 3, plus Senior+ FDE leadership titles.

## Files in this folder

Each job title has its own markdown file with role-specific mapping, gaps, and a talk track. This overview is the index.

| File | Title |
| --- | --- |
| [`ai-engineer.md`](./ai-engineer.md) | AI Engineer |
| [`ai-product-engineer.md`](./ai-product-engineer.md) | AI Product Engineer |
| [`ai-search-engineer.md`](./ai-search-engineer.md) | AI/Search Engineer |
| [`algorithm-engineer.md`](./algorithm-engineer.md) | Algorithm Engineer |
| [`analytics-engineer.md`](./analytics-engineer.md) | Analytics Engineer |
| [`android-engineer.md`](./android-engineer.md) | Android Engineer |
| [`application-developer.md`](./application-developer.md) | Application Developer |
| [`applied-ai-engineer.md`](./applied-ai-engineer.md) | Applied AI Engineer |
| [`associate-forward-deployed-engineer.md`](./associate-forward-deployed-engineer.md) | Associate Forward Deployed Engineer |
| [`backend-engineer.md`](./backend-engineer.md) | Backend Engineer |
| [`cloud-engineer.md`](./cloud-engineer.md) | Cloud Engineer |
| [`connected-device-software-engineer.md`](./connected-device-software-engineer.md) | Connected-Device Software Engineer |
| [`data-engineer.md`](./data-engineer.md) | Data Engineer |
| [`developer-platform-engineer.md`](./developer-platform-engineer.md) | Developer Platform Engineer |
| [`developer-tools-engineer.md`](./developer-tools-engineer.md) | Developer Tools Engineer |
| [`embedded-software-engineer.md`](./embedded-software-engineer.md) | Embedded Software Engineer |
| [`field-engineer.md`](./field-engineer.md) | Field Engineer |
| [`fintech-software-engineer.md`](./fintech-software-engineer.md) | Fintech Software Engineer |
| [`firmware-engineer.md`](./firmware-engineer.md) | Firmware Engineer |
| [`forward-deployed-ai-engineer.md`](./forward-deployed-ai-engineer.md) | Forward Deployed AI Engineer |
| [`forward-deployed-engineer.md`](./forward-deployed-engineer.md) | Forward Deployed Engineer (FDE) |
| [`forward-deployed-engineer-solution-architect.md`](./forward-deployed-engineer-solution-architect.md) | Forward Deployed Engineer / Solution Architect |
| [`forward-deployed-engineer-clearance-required.md`](./forward-deployed-engineer-clearance-required.md) | Forward Deployed Engineer — Clearance Required |
| [`forward-deployed-engineer-ai-agentic-sdlc.md`](./forward-deployed-engineer-ai-agentic-sdlc.md) | Forward Deployed Engineer, AI & Agentic SDLC |
| [`forward-deployed-engineer-ai-enablement.md`](./forward-deployed-engineer-ai-enablement.md) | Forward Deployed Engineer, AI Enablement |
| [`founding-ai-forward-deployed-engineer.md`](./founding-ai-forward-deployed-engineer.md) | Founding AI Forward Deployed Engineer |
| [`frontend-engineer.md`](./frontend-engineer.md) | Frontend Engineer |
| [`full-stack-engineer.md`](./full-stack-engineer.md) | Full-Stack Engineer |
| [`generative-ai-engineer.md`](./generative-ai-engineer.md) | Generative AI / GenAI Engineer |
| [`hardware-software-engineer.md`](./hardware-software-engineer.md) | Hardware/Software Engineer |
| [`infrastructure-engineer.md`](./infrastructure-engineer.md) | Infrastructure Engineer |
| [`lead-forward-deployed-engineer.md`](./lead-forward-deployed-engineer.md) | Lead Forward Deployed Engineer |
| [`lead-forward-deployed-engineer-hospitality.md`](./lead-forward-deployed-engineer-hospitality.md) | Lead Forward Deployed Engineer, Hospitality |
| [`machine-learning-engineer.md`](./machine-learning-engineer.md) | Machine Learning Engineer |
| [`mobile-engineer.md`](./mobile-engineer.md) | Mobile Engineer |
| [`networking-engineer.md`](./networking-engineer.md) | Networking Engineer |
| [`payments-infrastructure-engineer.md`](./payments-infrastructure-engineer.md) | Payments Infrastructure Engineer |
| [`platform-engineer.md`](./platform-engineer.md) | Platform Engineer |
| [`principal-software-solutions-engineer-forward-deployed.md`](./principal-software-solutions-engineer-forward-deployed.md) | Principal Software Solutions Engineer / Forward Deployed |
| [`product-engineer.md`](./product-engineer.md) | Product Engineer |
| [`security-engineer.md`](./security-engineer.md) | Security Engineer |
| [`senior-forward-deployed-engineer.md`](./senior-forward-deployed-engineer.md) | Senior Forward Deployed Engineer |
| [`sensor-algorithm-engineer.md`](./sensor-algorithm-engineer.md) | Sensor Algorithm Engineer |
| [`sde-i.md`](./sde-i.md) | Software Development Engineer I (SDE I) |
| [`sde-ii.md`](./sde-ii.md) | Software Development Engineer II (SDE II) |
| [`software-engineer.md`](./software-engineer.md) | Software Engineer |
| [`software-engineer-i.md`](./software-engineer-i.md) | Software Engineer I |
| [`software-engineer-ii.md`](./software-engineer-ii.md) | Software Engineer II / SWE II |
| [`software-generalist.md`](./software-generalist.md) | Software Generalist |
| [`solution-architect.md`](./solution-architect.md) | Solution Architect |
| [`solutions-engineer.md`](./solutions-engineer.md) | Solutions Engineer |
| [`staff-forward-deployed-engineer.md`](./staff-forward-deployed-engineer.md) | Staff Forward Deployed Engineer |
| [`support-engineer.md`](./support-engineer.md) | Support Engineer |
| [`ios-engineer.md`](./ios-engineer.md) | iOS Engineer |

---

*Evidence sources: `README.md`, `docs/ARCHITECTURE.md`, `docs/TESTING.md`, `docs/SECURITY.md`, `docs/PACKAGING.md`, `src-tauri/src/**`, `src/**`.*
