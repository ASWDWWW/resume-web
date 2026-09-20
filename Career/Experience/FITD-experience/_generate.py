#!/usr/bin/env python3
"""Generate per-role experience docs from FITD-Bible work."""

from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parent

SCALE = """\
**Rating scale (this project only):** 10 = you already do the core of this job in production;
8–9 = strong match, hire-ready with normal ramp; 6–7 = real overlap, notable gaps;
4–5 = adjacent experience only; 2–3 = thin transfer; 0–1 = not evidenced here.
"""

PROJECT_CONTEXT = """\
FITD is a fashion AI product you designed, built, and operate: a production iOS app,
a native Android port, an Expo cross-platform scaffold, a marketing site and admin CRM,
Firebase/GCP backend (Auth, Firestore, Storage, Cloud Functions, FCM, Analytics, App Check,
Vertex AI), brand catalog ops (~57 brands / ~16.5k product records), Instagram CRM and
n8n growth automations, AI community bots, and an in-store kiosk concept. This write-up
maps **only work evidenced in FITD-Bible**, not other jobs or coursework.
"""

# Shared evidence blocks
EV = {
    "ios": [
        "`development/apps/FITD-App/` — production SwiftUI app (~115 Swift files), App Store",
        "Auth (email, Google, Apple, anonymous), StoreKit 2, WeatherKit, FCM, App Check / DeviceCheck",
        "Closet, shop, AI stylist, FITD Room virtual try-on, social feed, brand toolkit",
    ],
    "android": [
        "`development/apps/FITD-App/android/` — Kotlin + Jetpack Compose (~56 files), Hilt, Coil, Ktor",
        "Play Billing, Play Integrity, Open-Meteo; frozen 2026-09-13 after Expo decision",
    ],
    "expo": [
        "`development/apps/fitd-mobile/` — Expo 57 / React Native scaffold, Expo Router, `geminiProxy`",
    ],
    "web": [
        "`development/apps/react-fitd-website/` — React 19 + Vite + Tailwind marketing site (`fitdai.com`)",
        "`admin-portal/` — Next.js 14 CRM, RBAC claims, internship review, bot admin, prompt packs",
    ],
    "backend": [
        "`development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)",
        "`firestore.rules` / `storage.rules`, staging project `fitd-app-staging`",
        "`geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function",
    ],
    "ai": [
        "Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles",
        "Vertex AI `virtual-try-on-001` via Cloud Function proxy",
        "AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval",
        "Heuristic `ProductRecommendationEngine` + implicit interest aggregation",
    ],
    "data": [
        "`business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function",
        "IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups",
        "`development/docs/handbook/ANALYTICS-TRACKING.md` event catalog",
    ],
    "kiosk": [
        "`development/apps/FITD-Kiosk/` — SwiftUI iPad kiosk, camera capture, VTO display",
        "Hardware sourcing docs: touchscreen + camera + network device (no custom firmware)",
    ],
    "ops": [
        "Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)",
        "Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows",
        "Internship funnel, lead capture, investor/client overview, contractor onboarding",
    ],
    "payments": [
        "StoreKit 2 brand plans (Starter / Growth / Pro) and Play Billing 7.x",
        "Apple receipt validation + App Store Connect subscription status function",
    ],
    "security": [
        "Firestore/Storage security rules, admin custom claims, App Check",
        "Function secrets (`GEMINI_API_KEY`), geo sanitization, bot kill switch / audit log",
    ],
    "docs": [
        "`development/docs/handbook/` — architecture, handoff, staging, cross-platform plan, file catalog",
        "Cursor rules, bot runbook, brand product schema",
    ],
}


def bullets(keys: list[str]) -> str:
    seen: list[str] = []
    for k in keys:
        for line in EV[k]:
            if line not in seen:
                seen.append(line)
    return "\n".join(f"- {x}" for x in seen)


# slug, title, rating, band, one_liner, what_you_did, how_it_applies, gaps, evidence_keys, talking
ROLES: list[dict] = [
    {
        "slug": "software-engineer",
        "title": "Software Engineer",
        "rating": 9,
        "band": "Strong match",
        "one_liner": "General software engineer who designs, ships, and operates production systems.",
        "what": """You were the engineer of record for a multi-surface product, not a single ticket stream.

You wrote and shipped a production iOS client, a native Android port, a React marketing site, a Next.js admin portal, and a Node 20 Firebase backend. You designed the Firestore data model, security rules, Cloud Functions (virtual try-on, receipt validation, catalog import, social fan-out, scheduled engagement, AI bots), and a staging environment. You also built growth automations and an in-store kiosk scaffold.

That is the full software-engineering loop: product definition, implementation, data modeling, integrations, release, and ongoing operation.""",
        "applies": """A Software Engineer is expected to take ambiguous problems, choose an architecture, write working code, and own quality. FITD is that job at company scale: you chose Firebase as the application platform, split client vs. function responsibilities, integrated third-party AI and billing, and documented the system so others can join.

You can speak to shipping user-facing features (closet, shop, social, subscriptions) and platform work (rules, functions, analytics, staging) in the same breath — the combination most SWE interviews actually test.""",
        "gaps": """Typical SWE interviews at large companies also probe algorithms under time pressure, code-review culture on a large team, and CI/CD. This repo shows little automated test/CI infrastructure and no large-team review process. Depth in any one language is high (especially Swift), but the role title is general — you should lead with product impact, then pick the stack the interviewer cares about.""",
        "talking": [
            "Walk through the FITD architecture diagram: clients → Firebase → Vertex/Gemini → store billing.",
            "Pick one hard feature (virtual try-on or catalog import) and explain client vs. function vs. rules.",
            "Be ready to discuss tradeoffs of a serverless backend vs. a dedicated API server.",
        ],
        "ev": ["ios", "android", "web", "backend", "ai", "docs"],
    },
    {
        "slug": "software-engineer-i",
        "title": "Software Engineer I",
        "rating": 10,
        "band": "Exceeds the bar",
        "one_liner": "Entry / early-career SWE: ships features with guidance, learns the stack, writes production code.",
        "what": """SWE I work is scoped tickets, mentored PRs, and first production features. You instead owned the entire FITD stack: SwiftUI production app, Android Compose port, web + admin, Cloud Functions, security rules, AI integrations, and brand/catalog operations.

You have already done the work SWE I is hired to start learning — independently.""",
        "applies": """Every SWE I competency maps cleanly: writing application code, using a cloud backend, reading docs, shipping UI, handling auth, and fixing production issues. Your intern-hiring materials and handbook show you can also explain the system to someone at this level.

For this title, FITD is overqualified evidence. Use it to skip junior-screening doubt, then show you can still take direction and work in a team process.""",
        "gaps": """The only gap is cultural, not skill: SWE I roles assume you will be mentored. Interviewers may worry a founder will reject narrow tickets. Frame FITD as proof you can finish work, not as a reason you cannot take a smaller scope.""",
        "talking": [
            "Show one end-to-end feature (e.g. closet upload → Gemini label → Firestore → closet grid).",
            "Emphasize you can work inside someone else’s architecture, not only your own.",
        ],
        "ev": ["ios", "backend", "web"],
    },
    {
        "slug": "software-engineer-ii",
        "title": "Software Engineer II / SWE II",
        "rating": 8,
        "band": "Strong match",
        "one_liner": "Mid-level SWE: owns features end-to-end, designs small systems, mentors juniors, ships independently.",
        "what": """SWE II is the first title that expects independent ownership of a problem area. You owned several: mobile clients, Firebase backend, AI features, brand subscriptions, admin CRM, and a cross-platform migration plan (native Android freeze → Expo).

You wrote the engineering handbook, handoff contracts, product schema, and staging notes — the written design work SWE II interviews look for. You also scoped contractor onboarding (Andreea) and internship programs, which is informal mentorship.""",
        "applies": """Map FITD work to SWE II expectations:

- **Feature ownership:** Get FITD, FITD Room, brand plans, catalog import, notifications.
- **System design (small/medium):** Firestore collections, function triggers, App Check, geo sanitization.
- **Cross-stack delivery:** iOS + Functions + rules + analytics for the same feature.
- **Operational judgment:** kill switches on bots, VTO treated as beta, Android freeze vs. rewrite.

That is a mid-level profile, not a junior one.""",
        "gaps": """SWE II at a large product org also means working in a shared codebase with CI, on-call, and design review. You have less evidence of collaborative process, automated tests, and high-QPS systems design. Some companies will still slot you SWE II and grow you; others will probe algorithms and distributed systems harder than FITD required.""",
        "talking": [
            "Use the Expo migration as a SWE II story: why freeze Android, what Phase 0–8 covers, what you would not rewrite.",
            "Design a feature on a whiteboard the way you designed `implicitProductInterest` + `recStats`.",
        ],
        "ev": ["ios", "android", "expo", "backend", "ai", "docs"],
    },
    {
        "slug": "sde-i",
        "title": "Software Development Engineer I (SDE I)",
        "rating": 10,
        "band": "Exceeds the bar",
        "one_liner": "Amazon-style new-grad / early SDE: writes production code, learns operational bar, delivers with a mentor.",
        "what": """SDE I is scoped implementation on an existing service. You built FITD’s services and clients yourself: Cloud Functions, Firestore rules, iOS/Android apps, and web. You operated staging vs. production Firebase projects and store billing.

That is above the SDE I delivery bar. The Amazon-flavored title adds an expectation that you can follow a well-specified design and write maintainable code — your handbook and schema docs show you can specify as well as implement.""",
        "applies": """Translate FITD into SDE language: you owned a customer-facing application on a managed AWS-like platform (GCP/Firebase), wrote backend functions with explicit IAM-style access (security rules + admin claims), and integrated external APIs (Gemini, Vertex, WeatherKit, App Store).

Leadership principles you can evidence: Ownership (whole product), Bias for Action (ship VTO as beta), Dive Deep (catalog schema, geo sanitize), Invent and Simplify (Firebase instead of a custom server).""",
        "gaps": """Amazon SDE I interviews still require data structures and coding under time. This repo does not prove leetcode fluency. Operational excellence (alarms, tickets, weekly metrics reviews) is lighter than a typical AWS team. Do not claim Amazon-scale distributed systems experience.""",
        "talking": [
            "Describe `validateAppleReceipt` as a trust-boundary function: why it cannot live only on device.",
            "Walk security rules as your authorization service.",
        ],
        "ev": ["ios", "backend", "security", "payments"],
    },
    {
        "slug": "sde-ii",
        "title": "Software Development Engineer II (SDE II)",
        "rating": 8,
        "band": "Strong match",
        "one_liner": "Amazon mid-level SDE: designs components, delivers independently, raises the operational bar.",
        "what": """You designed multi-component systems: mobile clients + Cloud Functions + Firestore + Vertex + store billing. You introduced a Gemini proxy so keys leave the client, built bot orchestration with quotas and kill switches, and planned a cross-platform rewrite.

SDE II is “I can take a fuzzy problem and return a design plus working software.” FITD Room, catalog import, brand geo-targeting, and the admin CRM are that shape of work.""",
        "applies": """SDE II loops you already ran:

- Write a design (handbook architecture, brand schema, kiosk PRD).
- Implement across client and service.
- Handle failure modes (VTO beta, OpenWeather fallback, bot moderation).
- Instrument (Firebase Analytics event catalog, CRM growth charts).

You can interview as someone who has been the tech lead of a small product, which is how many SDE IIs actually spend their time.""",
        "gaps": """Amazon SDE II bar includes stronger CS fundamentals, code quality at team scale, and often on-call for a high-availability service. FITD’s backend is serverless and low-ops; you have not run large fleets, queues at scale, or formal design reviews. Staffing-wise you are closer to “strong SDE II / early Senior” on product delivery, weaker on Amazon-native infra.""",
        "talking": [
            "System-design the virtual-try-on path: photo upload, function auth, Vertex call, result storage, client display.",
            "Discuss what you would add for SDE II-quality ops: structured logs, SLOs, replay, CI.",
        ],
        "ev": ["backend", "ai", "ios", "docs", "security"],
    },
    {
        "slug": "application-developer",
        "title": "Application Developer",
        "rating": 9,
        "band": "Strong match",
        "one_liner": "Builds and maintains user-facing applications (mobile, web, or desktop) against existing services.",
        "what": """You shipped multiple applications: the FITD iOS app, Android app, Expo mobile scaffold, marketing website, admin portal, and kiosk iPad app. Each has real user flows — auth, browsing, uploads, payments, CRM, internships — not demos.

Application developers are judged on UI completeness, state management, and integration quality. Closet caching (Kingfisher/Coil limits), lazy tabs, StoreKit/Play Billing, and the admin RBAC portal are that work.""",
        "applies": """This title is a direct label for most of your time: writing application code that talks to Firebase and AI APIs. You can show App Store–oriented release notes (`WHATS_NEW.txt` v2.2+), screenshot sets, and a live marketing site.

If a shop uses “Application Developer” for enterprise internal tools, point at the admin CRM and Instagram CRM — operator applications, not only consumer UI.""",
        "gaps": """Some Application Developer jobs are Java/.NET enterprise forms or Salesforce. You do not have that stack. Lead with mobile + React/Next; do not claim ERP/line-of-business platforms you have not used.""",
        "talking": [
            "Demo or screenshot closet, Get FITD, and brand analytics as three different application types.",
            "Explain shared ClosetDataManager / weather state across tabs.",
        ],
        "ev": ["ios", "android", "web", "kiosk"],
    },
    {
        "slug": "full-stack-engineer",
        "title": "Full-Stack Engineer",
        "rating": 9,
        "band": "Strong match",
        "one_liner": "Owns UI through data and deploy: client, API, database, and enough infra to ship.",
        "what": """You are the full stack for FITD.

**Client:** SwiftUI, Jetpack Compose, React 19/Vite, Next.js 14, Expo Router.  
**API / server:** Firebase Cloud Functions (Node 20) — HTTPS and Firestore triggers.  
**Data:** Firestore collections, Storage, SQLite in automations, ~16.5k catalog JSON.  
**Auth / access:** Firebase Auth, custom claims, security rules, App Check.  
**Deploy:** Firebase Hosting (`fitdai.com`), Functions, staging vs. production projects.

Features routinely cross the stack: internship apply (web form → function → Storage → admin review), VTO (iOS → function → Vertex → Storage → UI), brand subscribe (StoreKit → receipt function → entitlements).""",
        "applies": """Full-stack interviews ask you to build a slice. You have many slices already in production. You can discuss SSR rewrites for the admin portal on Firebase Hosting, client-vs-server Gemini calls, and why rules are your authorization layer instead of a custom API gateway.

This is one of your two or three strongest title fits.""",
        "gaps": """Classic full-stack (Postgres + REST/GraphQL + React on AWS/Vercel with CI) differs in flavor. You have not built a standalone Express/Django API with migrations, or a heavily tested monorepo pipeline. Translate Firebase confidently; do not pretend it is identical to a Kubernetes + RDS shop.""",
        "talking": [
            "Draw the internship or VTO slice on a whiteboard, every hop.",
            "Explain when you moved Gemini behind `geminiProxy` and why that is a full-stack security change.",
        ],
        "ev": ["ios", "web", "backend", "data", "security"],
    },
    {
        "slug": "backend-engineer",
        "title": "Backend Engineer",
        "rating": 7,
        "band": "Solid overlap",
        "one_liner": "Designs services, data models, APIs, and server-side reliability.",
        "what": """Your backend is Firebase, not a custom microservice fleet. You still did backend work:

- 20+ Cloud Functions: `virtualTryOn`, `geminiProxy`, `validateAppleReceipt`, `catalogImport`, social push triggers, scheduled engagement, geo sanitizers, implicit-interest aggregation, bot scheduler/admin.
- Firestore schema for users, closet, posts, brands, ads, recs, CRM, bots.
- ~477-line `firestore.rules` and Storage rules as the authorization service.
- Website functions: analytics ingest, leads, internship upload, subscription validation.
- Secrets, staging project, seed/admin scripts.

That is real server-side product engineering.""",
        "applies": """Backend Engineer interviews care about trust boundaries, idempotency, and data integrity. Your bot stack (idempotency, quotas, kill switch) and receipt validation are the best stories. Catalog import and geo sanitization show you do not blindly trust clients.

You can do the job at a startup or Firebase-heavy shop immediately. At a service-oriented backend team you would ramp on their language, queues, and datastore.""",
        "gaps": """Missing typical backend depth: no independently scaled services, little queue/stream processing, no SQL schema migrations, limited load testing, no formal API versioning. Node Functions are a backend, but interviewers who want Java/Go + Postgres + Kafka will see a gap. Rate yourself honest: strong applied backend, not a specialist.""",
        "talking": [
            "Why Vertex try-on and Apple receipts must be server-side.",
            "How `onImplicitProductInterestWrite` aggregates client signals without a custom worker fleet.",
        ],
        "ev": ["backend", "security", "ai", "payments", "data"],
    },
    {
        "slug": "frontend-engineer",
        "title": "Frontend Engineer",
        "rating": 7,
        "band": "Solid overlap",
        "one_liner": "Specializes in web UI: components, accessibility, performance, design systems.",
        "what": """Web frontend: React 19 + Vite + Tailwind + Framer Motion marketing site; Next.js 14 App Router admin CRM (stats, leads, internships, bots, prompts). Mobile UI is SwiftUI/Compose — related craft, different title.

You shipped public pages (home, brands, collabs, contact, internships, quiz/lead capture) and a privileged operator UI with role claims. Brand design tokens (Times-style Tinos, brown accent) show you implement a system, not only pages.""",
        "applies": """Frontend Engineer roles that include “the website and the admin tool” match well. You have routing, forms, file upload, charts, and auth-gated dashboards. FITD’s consumer experience is mostly native, so your strongest FE artifacts are `react-fitd-website` and `admin-portal`.

Product-minded frontend teams will like that you also defined the data the UI reads.""",
        "gaps": """You are not a dedicated frontend specialist: limited evidence of accessibility audits, design-system libraries, SSR/performance budgets, or complex CSS architecture. No Storybook-level component library. Native SwiftUI should not be sold as “frontend engineering” unless they mean client UI broadly.""",
        "talking": [
            "Walk the admin portal information architecture: CRM vs. bots vs. prompts vs. internships.",
            "Discuss Hosting + Next SSR rewrite as a frontend deploy problem.",
        ],
        "ev": ["web", "docs"],
    },
    {
        "slug": "mobile-engineer",
        "title": "Mobile Engineer",
        "rating": 9,
        "band": "Strong match",
        "one_liner": "Ships iOS and/or Android apps: UI, device APIs, store release, offline-ish clients.",
        "what": """Mobile is the center of FITD.

- **iOS production:** SwiftUI, deep links (`fitd://`, `fitd.app`), camera/gallery closet, Kingfisher cache, WeatherKit, StoreKit 2, FCM, App Check, Associated Domains.
- **Android port:** Compose, Hilt, Coil, Ktor, Play Billing, Play Integrity, App Links — then an explicit freeze in favor of Expo.
- **Expo `fitd-mobile`:** Phase 0 cross-platform replacement with Firebase JS and `geminiProxy`.

You also started an iPad kiosk client. Release notes go through v2.2+ (plans, catalog import, notifications).""",
        "applies": """A Mobile Engineer is hired to own the store binary. You have done that: auth matrix, push, billing, image pipelines, and store-specific services. The Android → Expo decision is a mature mobile-platform story (duplication cost vs. one codebase).

This is among your strongest titles.""",
        "gaps": """Less evidence of large-team mobile (modularization, UI tests, feature flags at scale, Play/App Store process with many reviewers). Android depth is weaker than iOS. Offline-first sync is cache-heavy, not a CRDT/sync engine.""",
        "talking": [
            "Compare WeatherKit vs. Open-Meteo vs. planned Expo weather as a platform-abstraction story.",
            "Explain App Check on both stores and why the Gemini key move matters on mobile.",
        ],
        "ev": ["ios", "android", "expo", "kiosk", "payments"],
    },
    {
        "slug": "ios-engineer",
        "title": "iOS Engineer",
        "rating": 9,
        "band": "Strong match",
        "one_liner": "Native iOS specialist: Swift/SwiftUI, Apple frameworks, App Store quality.",
        "what": """The production FITD client is iOS-first. Roughly 115 Swift files cover:

- App lifecycle, lazy tabs, shared closet/weather managers
- Auth including Sign in with Apple
- Closet camera/gallery + Gemini labeling
- Shop, community, hashtags, daily styles
- AI stylist + FITD Room (Vertex VTO)
- Brand registration, StoreKit 2 plans, catalog import UI (iOS-only)
- Profiles, posts, FCM inbox, settings / delete account
- WeatherKit + fallback, Kingfisher caches, DeviceCheck, Associated Domains

You also have a separate SwiftUI kiosk target. Architecture and file catalog docs exist specifically for this codebase.""",
        "applies": """This is a straightforward iOS Engineer portfolio. You can discuss SwiftUI architecture, store entitlements, privacy-sensitive camera/location, and Apple-only APIs (WeatherKit, StoreKit, DeviceCheck, Sign in with Apple). Production orientation is documented (App Store, `WHATS_NEW.txt`).

Interviewers who want “someone who has shipped an App Store app they still own” should be an easy narrative.""",
        "gaps": """Less UIKit-legacy, Combine-heavy, or modular SPM package architecture than a long-tenured iOS team. Testing (XCTest/UI tests) is not a highlighted strength. You may be asked about concurrency (`async/await`, actors) with more rigor than the repo advertises.""",
        "talking": [
            "Tour `FITD_AppApp.swift` → `AuthenticatedView` → `MainTabView` and lazy tab loading.",
            "StoreKit 2 + `validateAppleReceipt` as the iOS trust story.",
        ],
        "ev": ["ios", "kiosk", "payments", "ai"],
    },
    {
        "slug": "android-engineer",
        "title": "Android Engineer",
        "rating": 6,
        "band": "Solid overlap",
        "one_liner": "Native Android specialist: Kotlin, Jetpack, Play quality.",
        "what": """You built a real native Android port: Kotlin, Jetpack Compose, Hilt DI, Coil (parity cache sizes), Ktor weather, Play Billing 7.x, Play Integrity App Check, Firebase, App Links. Consumer journeys were taken to documented parity with iOS; VTO is partial; catalog import and Apple Sign-In were intentionally omitted.

You then froze the Android tree (2026-09-13) and started Expo as the long-term shared client. That is an engineering decision, not abandonment of Android users.""",
        "applies": """You can interview for Android roles that want Compose + Firebase + Play Billing. You have implemented the modern Android stack, not only a WebView wrapper. Parity notes in `README-android.md` show you thought like an Android owner (platform substitutions, not pixel-identical copies).

For a generalist mobile role this is enough. For a dedicated Android Engineer seat, treat it as a strong project, not a multi-year Android career.""",
        "gaps": """The tree is frozen; Expo is the future. Less evidence of Play Console process depth, WorkManager, Room, navigation-component at scale, or Android-specific performance work. Interviewers will notice iOS is the source of truth. Do not oversell Android seniority.""",
        "talking": [
            "Explain each iOS→Android substitution: WeatherKit→Open-Meteo, StoreKit→Play Billing, DeviceCheck→Play Integrity.",
            "Be honest about freeze + Expo and what you would still hotfix natively.",
        ],
        "ev": ["android", "ios", "expo", "payments"],
    },
    {
        "slug": "product-engineer",
        "title": "Product Engineer",
        "rating": 9,
        "band": "Strong match",
        "one_liner": "Engineer who owns user outcomes: discovery, build, ship, measure, iterate.",
        "what": """You defined the product and built it. Shopper loops (closet → outfit → try-on → post), brand loops (register → subscribe → upload → analytics), and web loops (quiz → lead → CRM) were designed as outcomes, not only screens.

You wrote investor/client overviews, marketing feature guides, kiosk PRD, analytics event catalog, and intern/contractor briefs. You treated VTO as beta, froze Android for a better cross-platform bet, and instrumented implicit interest for recommendations.

That is Product Engineer work: sit with the user problem, ship the thinnest real solution, measure.""",
        "applies": """Product Engineer roles (often at startups) want people who will not wait for a perfect spec. FITD is the case study. You can talk KPIs you defined (activation, outfit saves, brand placement) and the features that serve them.

Pair this title with AI Product Engineer when the team is AI-first.""",
        "gaps": """Less formal product process (PRDs for every feature, A/B platforms, growth experiments with stats). You are founder-PM + engineer; some Product Engineer teams still have a separate PM. Show you can partner, not only decide alone.""",
        "talking": [
            "Tell the closet→Gemini→outfit→VTO loop as a product narrative with the metric each step should move.",
            "Use brand Starter/Growth/Pro as a packaging + engineering story.",
        ],
        "ev": ["ios", "ai", "web", "data", "ops"],
    },
    {
        "slug": "ai-product-engineer",
        "title": "AI Product Engineer",
        "rating": 9,
        "band": "Strong match",
        "one_liner": "Ships AI-backed user features: models as APIs, UX for uncertainty, evals-lite, product metrics.",
        "what": """AI is in the product, not a slide:

- Closet and brand-image auto-labeling (Gemini 2.0 Flash)
- AI stylist combining wardrobe + weather + Gemini
- Daily colors/styles generation
- FITD Room virtual try-on (Vertex `virtual-try-on-001`, beta)
- Recommendation scoring from likes, onboarding, implicit signals
- Community bots (Gemini captions, Imagen/Veo media) with human approval and kill switches
- GPT-4o captions in Instagram CRM; admin prompt packs
- `geminiProxy` so mobile does not embed the key

You also started an outfit-curator training scrape/pipeline — research toward better styling, not a production trainer.""",
        "applies": """AI Product Engineer is the cleanest “AI + shipped UX” title for you. You handled the real problems of the job: latency and cost (Flash, proxy), failure UX (VTO beta), safety (moderation, approval, kill switch), and grounding (closet inventory + weather, not unconstrained chat).

You can contrast client-side Gemini vs. server-side Vertex — a product-engineering distinction, not a research one.""",
        "gaps": """Limited offline eval harness, no systematic prompt/version A/B, no fine-tunes in production, no RAG/search stack. Companies that want “AI product + evals platform” will want you to grow that muscle. Do not claim you trained foundation models.""",
        "talking": [
            "How the stylist is constrained by closet + weather so it is useful, not a generic chatbot.",
            "Bot kill switch and admin approval as product safety, not an afterthought.",
        ],
        "ev": ["ai", "ios", "backend", "ops"],
    },
    {
        "slug": "platform-engineer",
        "title": "Platform Engineer",
        "rating": 5,
        "band": "Adjacent",
        "one_liner": "Builds internal platforms: paved roads, golden paths, shared runtime for other engineers.",
        "what": """You built a *product* platform (Firebase projects, functions, rules, staging, handbook) that other people (interns, contractor) are meant to use. Firestore scripts, admin claims, bot admin UI, and Cursor rules are internal enablement.

That is proto-platform work at a 1–3 person company. It is not a platform engineering org (Kubernetes, IDP, golden CI, service catalog).""",
        "applies": """Sell the parts that transfer: multi-environment Firebase (`fitd-app-203cb` vs `fitd-app-staging`), documented deploy scripts, shared schema, and admin tooling so non-engineers can operate bots/CRM. You think about “how the next person ships.”

Good fit for startup “platform” meaning shared backend + tooling. Weak fit for Big Tech Platform Engineering.""",
        "gaps": """No Kubernetes, Terraform/Pulumi at scale, service mesh, paved CI, developer portal (Backstage), or multi-tenant compute. Do not apply as a k8s Platform Engineer on FITD evidence alone.""",
        "talking": [
            "Staging remaining-setup doc as your platform backlog.",
            "What a real paved road would look like if a second app team joined.",
        ],
        "ev": ["backend", "docs", "ops"],
    },
    {
        "slug": "infrastructure-engineer",
        "title": "Infrastructure Engineer",
        "rating": 4,
        "band": "Adjacent",
        "one_liner": "Owns compute, networks, reliability, and the machines/software others deploy onto.",
        "what": """Infrastructure you actually ran: Firebase Hosting, Cloud Functions (us-central1), Firestore, Storage/GCS, FCM, two GCP Firebase projects, domain `fitdai.com` / `staging.fitdai.com`. Manual CLI deploys. No servers you patch.

Kiosk hardware notes cover *buying* a compute+camera device, not racking infrastructure.""",
        "applies": """You understand managed cloud primitives and environment isolation. That helps in infra conversations about “what we don’t want to run ourselves.” You can talk blast radius (prod vs staging, function secrets).

This is cloud-product usage, not infrastructure engineering as a discipline.""",
        "gaps": """No IaC estate, no load balancers you configured, no observability stack you own, no capacity planning, no on-prem. A dedicated Infrastructure Engineer role would be a stretch; Cloud Engineer is the more honest nearby title.""",
        "talking": [
            "What Firebase hides and what you still had to get right (rules, secrets, project split).",
        ],
        "ev": ["backend", "docs"],
    },
    {
        "slug": "cloud-engineer",
        "title": "Cloud Engineer",
        "rating": 6,
        "band": "Solid overlap",
        "one_liner": "Implements and operates cloud services (IAM, functions, storage, networking, cost).",
        "what": """You operated a real GCP/Firebase estate:

- Production and staging projects, Hosting, Functions (Node 20), Firestore, Storage, Auth, FCM, Analytics, App Check
- Vertex AI for try-on and bot media
- Function secrets, admin custom claims
- Website asset CDN via Storage/GCS
- Deploy scripts for app functions, bot, rules, and the marketing site

That is applied cloud engineering for a production consumer+admin product.""",
        "applies": """Cloud Engineer jobs that are “make us successful on GCP/Firebase/serverless” match. You can discuss IAM-adjacent patterns (rules, claims, App Check), environment strategy, and which workloads belong in Functions vs. the client.

Jobs that are AWS landing-zone, VPC, or Terraform-heavy are a weaker match.""",
        "gaps": """Limited multi-cloud, little raw GCP (GKE, Cloud SQL, VPC SC). Cost/FinOps and formal IAM reviews are light. No CI-promoted infra. Be precise: Firebase-centric Cloud Engineer, not a cloud network specialist.""",
        "talking": [
            "Prod vs staging project, bundle IDs, and Hosting domains.",
            "Vertex in Functions vs. Gemini from clients — cloud trust boundaries.",
        ],
        "ev": ["backend", "security", "web"],
    },
    {
        "slug": "developer-platform-engineer",
        "title": "Developer Platform Engineer",
        "rating": 5,
        "band": "Adjacent",
        "one_liner": "Makes other developers faster: internal APIs, CI templates, IDP, paved workflows.",
        "what": """You created the developer experience for FITD itself: engineering handbook (architecture, handoff, file catalog, staging, Discord HQ), Firestore seed/admin scripts, Cursor rules (SwiftUI, brand), bot runbook, brand schema, and an admin portal for operators.

The Expo plan is a developer-platform decision: one client stack for future engineers.""",
        "applies": """At a tiny company, you *were* developer platform. The artifacts transfer as “I care about the next engineer’s first week.” Contractor onboarding packets show you productize access and docs.

This helps for startup DX roles; it is not Backstage/GitHub Actions platform engineering.""",
        "gaps": """No internal developer portal, CI templates, feature-flag platform, or self-service environments. Score stays mid because the *intent* is there and the *scale* is not.""",
        "talking": [
            "Give a new-hire tour from handbook README → architecture → handoff → first deploy.",
        ],
        "ev": ["docs", "ops", "web"],
    },
    {
        "slug": "developer-tools-engineer",
        "title": "Developer Tools Engineer",
        "rating": 5,
        "band": "Adjacent",
        "one_liner": "Builds compilers, CLIs, debuggers, IDE integrations, or internal engineering tools.",
        "what": """Tools you built are product-ops tools, not language tools: firestore-scripts (seed, export emails, claims, geo, VTO presets), admin CRM, bot kill-switch UI, prompt packs, IG CRM, n8n workflows, scraper dashboard.

Cursor rules and PDF branding automation (`_generate_pdfs.mjs`) are lightweight developer tooling.""",
        "applies": """If the role means “internal tools for the company,” you have a portfolio. If it means LLVM, Buildkite, or `kubectl` plugins, you do not.

Position FITD admin + scripts as the first version of an internal toolbelt you would grow.""",
        "gaps": """No compiler/toolchain, no widely used CLI, no IDE plugin. Title is easy to over-claim — keep the rating modest.""",
        "talking": [
            "Show one script that saved repeated Firebase console work (admin claims or catalog).",
        ],
        "ev": ["ops", "web", "docs"],
    },
    {
        "slug": "embedded-software-engineer",
        "title": "Embedded Software Engineer",
        "rating": 1,
        "band": "Not evidenced",
        "one_liner": "Writes software close to hardware: RTOS, drivers, MCUs, constrained C/C++.",
        "what": """FITD has no embedded codebase. The kiosk is an iPad/SwiftUI app on a purchased touchscreen+camera device. Hardware docs are sourcing and RFQ notes, not board support packages.

There is no C/C++, RTOS, HAL, or device driver work in this repo.""",
        "applies": """Almost nothing applies directly. The only thin transfer is thinking about a device that has a camera, display, and network in a store — still application software.

Do not use FITD as embedded evidence.""",
        "gaps": """The entire embedded stack is missing. This title is not a fit from this project.""",
        "talking": [
            "If asked, be explicit: kiosk is application software on COTS hardware.",
        ],
        "ev": ["kiosk"],
    },
    {
        "slug": "firmware-engineer",
        "title": "Firmware Engineer",
        "rating": 1,
        "band": "Not evidenced",
        "one_liner": "Ships firmware images: boot, peripherals, OTA, factory bring-up.",
        "what": """No firmware, bootloaders, OTA, or peripheral bring-up exist in FITD-Bible. Kiosk work stops at “install our app on a networked device with a camera.”""",
        "applies": """No meaningful application. Adjacent awareness of camera/display devices does not constitute firmware experience.""",
        "gaps": """Total. Do not apply to firmware roles on this work.""",
        "talking": [
            "Redirect to Connected-Device / kiosk application software if the company also ships an app on the device.",
        ],
        "ev": ["kiosk"],
    },
    {
        "slug": "connected-device-software-engineer",
        "title": "Connected-Device Software Engineer",
        "rating": 4,
        "band": "Adjacent",
        "one_liner": "Software for devices that talk to the cloud: apps on hardware, device identity, telemetry.",
        "what": """FITD Kiosk is a connected retail device: iPad/kiosk app, camera capture, outfit builder, virtual try-on via the same Firebase + `virtualTryOn` path as the phone app. Docs specify touchscreen + camera + network.

Phones are also connected devices in a weak sense (FCM, App Check), but that is standard mobile, not IoT.""",
        "applies": """You can talk about a device-shaped product: always-on UI, store environment, shared cloud backend, privacy (camera in public). That overlaps the *application* half of connected-device roles (the app on the box).

It does not overlap device firmware, MQTT fleets, or device certificates.""",
        "gaps": """No device management, provisioning, IoT Core, offline store mode designed in depth, or fleet updates. Kiosk catalog API is still future (`stores/{storeId}/products`). Rating stays low-mid.""",
        "talking": [
            "Kiosk vs. phone: what must be different in a store (session, privacy, no personal Apple ID).",
        ],
        "ev": ["kiosk", "backend", "ai"],
    },
    {
        "slug": "hardware-software-engineer",
        "title": "Hardware/Software Engineer",
        "rating": 3,
        "band": "Thin transfer",
        "one_liner": "Co-designs boards and the software that runs on them.",
        "what": """You wrote hardware *sourcing* guidance for kiosk prototypes (compute, touchscreen, camera, enclosure, RFQ). Software is SwiftUI on that hardware. There is no schematic, PCB, sensor integration, or driver work.""",
        "applies": """Only the “I can specify a device bill of materials and write the application” slice applies. Useful in conversations with vendors; not a HW/SW co-design career signal.""",
        "gaps": """No electronics, HDL, or bring-up. Do not list this as a target role from FITD.""",
        "talking": [
            "Show the kiosk hardware README as product-minded sourcing, then pivot to software ownership.",
        ],
        "ev": ["kiosk"],
    },
    {
        "slug": "machine-learning-engineer",
        "title": "Machine Learning Engineer",
        "rating": 3,
        "band": "Thin transfer",
        "one_liner": "Trains, evaluates, and serves models; owns data → model → production ML systems.",
        "what": """You consume models as APIs (Gemini, Vertex VTO, Imagen/Veo, GPT-4o). You built a scrape → SQLite → image analysis pipeline toward outfit training, and a heuristic recommender (`ProductRecommendationEngine`). Schema comments mention future embeddings.

You did not train, evaluate, or host a custom model in production.""",
        "applies": """Transfer is “I know how models show up in a product and what data I would need to train.” The curator pipeline is the closest MLE-shaped artifact (data collection, image processing). Rec stats are ranking features, not a learned model.

This is not MLE experience in the industry sense.""",
        "gaps": """No PyTorch/TF training loops, feature stores, model registry, offline/online metrics, GPU serving, or MLOps. Applied AI / GenAI Engineer is the honest title.""",
        "talking": [
            "Be precise: API integration + data collection, not model training.",
            "If they want MLE growth, talk about what you would train (garment attributes) and why you have not yet.",
        ],
        "ev": ["ai", "data"],
    },
    {
        "slug": "ai-engineer",
        "title": "AI Engineer",
        "rating": 7,
        "band": "Solid overlap",
        "one_liner": "Broad AI builder: applications, pipelines, and integrations around modern model APIs.",
        "what": """You integrated multiple model families into one product: Gemini for vision+text styling, Vertex for try-on, planned Imagen/Veo for bots, GPT-4o for social captions. You added a server proxy, admin prompt packs, moderation/quotas, and a data-collection pipeline for future taste models.

“AI Engineer” in 2026 often means exactly this: production LLM/VLM features, not papers.""",
        "applies": """Strong match for AI Engineer postings that list LLM apps, tool use, and productization. You have multi-model orchestration (bots), multimodal input (photos), and safety controls.

Weaker match if they mean research or training.""",
        "gaps": """Eval platforms, RAG, agents-in-production beyond scheduled bots, and fine-tuning are thin. Title inflation is common — keep stories concrete (which model, which function, which UX).""",
        "talking": [
            "Inventory every model in FITD and why that model, not a larger one.",
        ],
        "ev": ["ai", "backend", "ops"],
    },
    {
        "slug": "applied-ai-engineer",
        "title": "Applied AI Engineer",
        "rating": 8,
        "band": "Strong match",
        "one_liner": "Applies existing models to a domain: prompts, tools, data constraints, product eval.",
        "what": """Fashion is your domain. You applied vision-language models to garment labeling, outfit assembly with weather context, virtual try-on, and marketing/community generation. Constraints come from real inventory (closet + brand catalog), not open chat.

The recommendation engine applies classical ranking to implicit signals — applied, not theoretical.""",
        "applies": """Applied AI Engineer is the academic/industry name for what you did with Gemini and Vertex. Domain adaptation, prompt design (admin packs), and “make it work on user photos” are the job.

This title is more accurate than Machine Learning Engineer.""",
        "gaps": """Formal eval sets for “good outfit” and human-rating pipelines are early. Search/RAG over the 16.5k catalog is not built. Still a strong applied profile.""",
        "talking": [
            "How a bad Gemini label would poison the closet and what you do about it.",
            "Why try-on is a different model class than the stylist.",
        ],
        "ev": ["ai", "ios", "data"],
    },
    {
        "slug": "genai-engineer",
        "title": "Generative AI / GenAI Engineer",
        "rating": 8,
        "band": "Strong match",
        "one_liner": "Specializes in generative models: text, image, video — prompts, safety, productization.",
        "what": """Generative surfaces in FITD:

- Text/vision: Gemini stylist, labels, daily colors, bot captions
- Image: Vertex virtual try-on; bot spec for Imagen
- Video: bot spec for Veo
- Marketing: GPT-4o captions; n8n OpenAI → Reddit/LinkedIn

Safety/productization: `geminiProxy`, bot moderation, quotas, idempotency, admin approval, kill switch.""",
        "applies": """GenAI Engineer postings that want “we use frontier APIs in production” are a direct fit. You have more than a chatbot: structured generation into product objects (category, colors, outfits) and image generation for try-on.

Community bots are a GenAI ops story (scheduled generation + human gate).""",
        "gaps": """No LoRA/fine-tune, no advanced agent graphs in the SDLC product sense, limited eval. Image/video bot generation may be spec-ahead of fully proven production quality — say what is shipped vs. specified.""",
        "talking": [
            "Structured output for closet labels vs. freeform captions — two GenAI modes.",
            "Kill switch as the GenAI production control plane.",
        ],
        "ev": ["ai", "ops", "backend"],
    },
    {
        "slug": "ai-search-engineer",
        "title": "AI/Search Engineer",
        "rating": 3,
        "band": "Thin transfer",
        "one_liner": "Information retrieval + ML: indexing, ranking, query understanding, embeddings.",
        "what": """The shop has search UI and heuristic product ranking (`ProductRecommendationEngine`, `recStats`, implicit interest). Brand schema notes future `search.*` / `ai.visual.*` embedding fields — not implemented.

No inverted index you built, no vector database, no query rewriting, no learning-to-rank model.""",
        "applies": """You understand why search/recs matter in a catalog of 16.5k+ SKUs and you started feature plumbing (implicit signals). That is product ranking, not search engineering.

A Search Engineer team would consider this a head start on the problem statement only.""",
        "gaps": """Core IR stack missing. Do not target this title until you have built retrieval.""",
        "talking": [
            "Describe current recs honestly as heuristics; describe the embedding fields you reserved in schema.",
        ],
        "ev": ["ai", "data"],
    },
    {
        "slug": "data-engineer",
        "title": "Data Engineer",
        "rating": 6,
        "band": "Solid overlap",
        "one_liner": "Pipelines, warehouses, quality, and reliable data movement.",
        "what": """Data movement you built:

- Brand crawl → ~16.5k versioned product JSON → `catalogImport` → Firestore
- Instagram scrape → SQLite → image/outfit analysis scripts
- Client implicit interest → function aggregation → `recStats`
- Web analytics / leads / internships → Functions → Firestore → admin CRM
- IG CRM media in Firebase Storage; n8n outbound social

This is operational data engineering for a startup, mostly JSON/Firestore/SQLite rather than a warehouse.""",
        "applies": """Data Engineer roles at small companies that live on Firebase/GCS will recognize this. You cared about schema (v1/v2 brand product schema), import paths, and operator dashboards.

Warehouse/dbt/Spark roles are a different sport.""",
        "gaps": """No Airflow/dbt/Snowflake/BigQuery modeled marts, little data-quality testing, no CDC. Batch JSON and Cloud Functions are the ceiling so far.""",
        "talking": [
            "Walk a brand from crawl folder → schema → import function → shop UI.",
            "What you would warehouse first if you hired a DE (events, catalog, subscriptions).",
        ],
        "ev": ["data", "backend", "ops"],
    },
    {
        "slug": "analytics-engineer",
        "title": "Analytics Engineer",
        "rating": 5,
        "band": "Adjacent",
        "one_liner": "Turns raw events into trusted metrics: modeling, semantic layer, stakeholder-ready tables.",
        "what": """You defined an analytics *tracking* spec (`ANALYTICS-TRACKING.md`): event names, user properties (`user_type`, `subscription_tier`, …), and product funnels. You ingest web analytics to Firestore rollups the admin CRM charts. Brand analytics exist in-app (clicks, reach).

That is analytics instrumentation plus a light semantic layer in docs — not dbt models.""",
        "applies": """You can partner with growth and investors on KPIs because you named them and wired events. Internship/lead funnels in CRM are analytics-shaped.

True Analytics Engineer (Looker + dbt + warehouse) would be a stretch hire based on FITD alone.""",
        "gaps": """No warehouse modeling, no metric store, limited experiment analysis. Firebase Analytics is not a modeled mart.""",
        "talking": [
            "Use the event catalog as your analytics-engineer portfolio artifact.",
        ],
        "ev": ["data", "web"],
    },
    {
        "slug": "algorithm-engineer",
        "title": "Algorithm Engineer",
        "rating": 5,
        "band": "Adjacent",
        "one_liner": "Designs and implements algorithms (ranking, optimization, geometry, signal) as product code.",
        "what": """The main algorithm is client-side recommendation scoring: likes, onboarding tags, implicit interest, collaborative `recStats`. Outfit “random + constraints” and geo-targeting sanitizers are smaller algorithms.

No heavy numerical methods, no published algorithms, no latency-optimized C++.""",
        "applies": """You can discuss ranking as an algorithm with features and failure modes. That is enough for “we need someone who can write the ranking code,” not for a computational-geometry or ads-auction Algorithm Engineer role.""",
        "gaps": """Complexity, proofs, and specialized domains are absent. Keep this as a supporting skill on Product/AI titles.""",
        "talking": [
            "Write the rec score as a function of signals; say what you would add next (embeddings).",
        ],
        "ev": ["ai", "data"],
    },
    {
        "slug": "sensor-algorithm-engineer",
        "title": "Sensor Algorithm Engineer",
        "rating": 1,
        "band": "Not evidenced",
        "one_liner": "Signal processing / fusion on IMU, camera, radar, etc.",
        "what": """No IMU, camera ISP, sensor fusion, or DSP work. Camera usage is “take a photo and send it to Gemini/Vertex.” WeatherKit is a high-level API, not a sensor algorithm.""",
        "applies": """Does not apply. Do not stretch closet photos into “computer vision algorithms” — that work is vendor models.""",
        "gaps": """Entire discipline missing.""",
        "talking": [
            "Redirect to Applied AI / VTO integration if they care about camera-in-the-loop UX.",
        ],
        "ev": ["kiosk"],
    },
    {
        "slug": "solutions-engineer",
        "title": "Solutions Engineer",
        "rating": 8,
        "band": "Strong match",
        "one_liner": "Technical counterpart to sales/CS: demos, integrations, customer-specific solutions.",
        "what": """You onboard brands as if you were the SE: catalog extraction for 57 brands, import tooling, outreach emails, subscription packaging, in-app brand analytics. You designed a store kiosk for retail partners. You built CRM, internship, and investor-facing materials so a non-engineer can understand the product.

That is solutions work performed by the person who also wrote the product.""",
        "applies": """Solutions Engineer interviews test: can you discover a customer problem, map it to the product, and fill gaps with configuration or light custom work? Catalog import, geo-targeted ads, and kiosk are those gaps.

You can demo FITD live and speak business (Starter/Growth/Pro) plus implementation.""",
        "gaps": """Less multi-customer enterprise integration (SSO, procurement, sandboxes, SOWs). You were solving FITD’s go-to-market, not staffing a SE team. Still a strong founder-SE profile.""",
        "talking": [
            "A brand discovery call: their catalog → your schema → import → spotlight → analytics.",
            "Kiosk as a solution for stores that will not live only in a phone app.",
        ],
        "ev": ["data", "kiosk", "ops", "web", "payments"],
    },
    {
        "slug": "solution-architect",
        "title": "Solution Architect",
        "rating": 7,
        "band": "Solid overlap",
        "one_liner": "Designs the technical shape of a customer or product solution across systems.",
        "what": """You architected the FITD ecosystem: data layer (scraper, catalog), content layer (Firebase, functions), distribution (n8n, stores, web), and a retail kiosk. Handbook architecture + mermaid diagrams + brand schema + kiosk PRD are architect artifacts.

You chose managed Firebase vs. custom servers — an architecture decision with cost and security consequences.""",
        "applies": """Solution Architect roles that are pre-sales or internal architecture for mid-size systems fit your communication style (docs, diagrams, options). You can design a customer’s path: mobile + catalog + VTO + analytics.

Enterprise SA (multi-year programs, compliance architectures) is a bigger jump.""",
        "gaps": """No TOGAF-style practice, limited integration architecture (EDI, SSO, data residency). Title “architect” at large vendors implies more years of multi-account design. FITD is one architecture you own completely — strong, but single-context.""",
        "talking": [
            "Present the ecosystem diagram from the root README as your reference architecture.",
            "Defend Firebase and the conditions under which you would leave it.",
        ],
        "ev": ["docs", "backend", "kiosk", "data"],
    },
    {
        "slug": "support-engineer",
        "title": "Support Engineer",
        "rating": 5,
        "band": "Adjacent",
        "one_liner": "Debugs customer issues, writes repros, improves product/docs from tickets.",
        "what": """You built the tools support would use (admin CRM, bot audit, kill switch) and wrote handbooks. You have not run a ticket queue, SLA, or knowledge base for external users at volume.

Founder support (brands, internships, contractor) is real but informal.""",
        "applies": """You can debug across client, rules, and functions — the skill support engineers need. Docs are better than average. The job itself (queues, empathy at scale, reproduction harnesses) is not evidenced as a practice.""",
        "gaps": """No Zendesk/Jira support process, no on-call customer rotation. Overqualified technically for many Support Engineer I seats; under-evidenced for Support Engineering as a career.""",
        "talking": [
            "Pick a production risk from the iOS README (client Gemini key, CORS) and how you would debug a user report.",
        ],
        "ev": ["ops", "docs", "web"],
    },
    {
        "slug": "field-engineer",
        "title": "Field Engineer",
        "rating": 5,
        "band": "Adjacent",
        "one_liner": "On-site install, configure, and repair of systems at the customer location.",
        "what": """The kiosk program is the field-shaped work: physical device in a store, camera, network, enclosure sourcing. You designed for that environment on paper and in a SwiftUI app. You have not evidenced repeated on-site installs.

Brand and internship work is remote/field-adjacent customer time, not rack-and-stack.""",
        "applies": """Retail field roles that install experiential devices can use the kiosk as a relevant project. Classic telco/IT field engineering (cabling, wireless surveys) does not appear.""",
        "gaps": """No install playbooks executed in stores, no fleet of devices, no safety/site certifications.""",
        "talking": [
            "What you would take in a store visit kit: network, lighting, privacy signage, kiosk session reset.",
        ],
        "ev": ["kiosk"],
    },
    {
        "slug": "software-generalist",
        "title": "Software Generalist",
        "rating": 10,
        "band": "Exceeds the bar",
        "one_liner": "High-range engineer who can do mobile, web, backend, data, and enough AI/ops to ship.",
        "what": """This title is a description of FITD-Bible. You moved across Swift, Kotlin, TypeScript/React/Next, Node Functions, Python automations, Firestore, and vendor AI without becoming a single-stack specialist.

You also covered the non-code surface: schema, rules, staging, marketing site, CRM, internships, investor docs, ads, brand ops.""",
        "applies": """Software Generalist / “full-stack plus mobile plus AI” roles at startups are the intended audience. You reduce coordination cost because one person can finish a slice.

This is your most accurate non-seniority title.""",
        "gaps": """Generalists are sometimes rejected by specialist orgs. The gap is not skill — it is focus. For specialist apps, lead with the matching doc (iOS, GenAI, FDE) and treat generalist as backup narrative.""",
        "talking": [
            "Give a week-in-the-life that touches app, function, catalog, and a brand email — that is the job.",
        ],
        "ev": ["ios", "android", "web", "backend", "ai", "data", "ops"],
    },
    {
        "slug": "fintech-software-engineer",
        "title": "Fintech Software Engineer",
        "rating": 2,
        "band": "Thin transfer",
        "one_liner": "Software in financial products: ledgers, KYC, cards, risk, regulated money movement.",
        "what": """FITD charges brands through Apple and Google in-app subscriptions. There is no ledger, KYC, bank partner, card issuing, or money-movement product. No Stripe.

Fashion commerce on the consumer side is “purchased items” tracking, not payments.""",
        "applies": """Only generic software quality and a light subscription-entitlement story transfer. Fintech domain knowledge is not evidenced.""",
        "gaps": """Domain gap is complete. Payments Infrastructure is the closer (still weak) title.""",
        "talking": [
            "Do not stretch StoreKit into fintech. Mention entitlements only if they ask about billing.",
        ],
        "ev": ["payments"],
    },
    {
        "slug": "payments-infrastructure-engineer",
        "title": "Payments Infrastructure Engineer",
        "rating": 3,
        "band": "Thin transfer",
        "one_liner": "Builds payment rails: processors, ledgers, retries, reconciliation, PCI boundaries.",
        "what": """You implemented StoreKit 2 and Play Billing for three brand tiers, plus `validateAppleReceipt` and a website `validateSubscription` via App Store Connect. That is store-billing integration, a real but narrow payments problem (receipt trust, entitlements).

No PSP integrations, no idempotent capture/refund rails, no reconciliation warehouse.""",
        "applies": """You understand why payment state cannot be trusted from the client and you put validation on the server. That is the kernel of payments infra thinking.

The rest of the discipline (card networks, webhooks at scale, money correctness) is absent.""",
        "gaps": """No Stripe/Adyen, no ledger, no PCI, no payouts. Keep this as a story inside Backend/SWE, not a target specialty.""",
        "talking": [
            "Receipt validation as a security/payments boundary, then stop.",
        ],
        "ev": ["payments", "backend"],
    },
    {
        "slug": "networking-engineer",
        "title": "Networking Engineer",
        "rating": 2,
        "band": "Thin transfer",
        "one_liner": "Designs and operates networks: routing, switching, wireless, DNS, overlays.",
        "what": """You used HTTPS APIs, FCM, Associated Domains / App Links, and Hosting DNS for `fitdai.com`. Kiosk notes mention “a network.” That is application networking, not network engineering.""",
        "applies": """Almost no transfer. DNS/hosting familiarity is expected of any full-stack engineer.""",
        "gaps": """No routing, BGP, wireless design, firewall policy as a job, packet analysis careers, etc.""",
        "talking": [
            "Do not target this title from FITD.",
        ],
        "ev": ["backend"],
    },
    {
        "slug": "security-engineer",
        "title": "Security Engineer",
        "rating": 4,
        "band": "Adjacent",
        "one_liner": "Threat modeling, controls, detection, secure design — security as the job, not a side task.",
        "what": """Security work you did as the product owner:

- Firestore and Storage rules (owner, admin claims, bot collections locked down)
- App Check (DeviceCheck, Play Integrity)
- Admin RBAC (`admin` / `editor` / `viewer`)
- Function secrets; `geminiProxy` to stop shipping keys
- Geo sanitization on the server
- Bot kill switch, quotas, moderation, audit log
- Documented residual risks (historical client Gemini key, CORS)

This is secure-by-construction product work, not a security program.""",
        "applies": """Application Security / startup “security-minded engineer” conversations can use these controls. You can threat-model the FITD trust boundary (client → rules → functions → Vertex).

A Security Engineer hire (detection, pentest, compliance, identity) is a different job.""",
        "gaps": """No security tooling career (SIEM, vuln management), no formal threat models, and known gaps remain in the READMEs. Do not claim you are a Security Engineer; claim you ship with security constraints.""",
        "talking": [
            "Walk a hostile client against `firestore.rules`.",
            "What you would do next: remove remaining client secrets, add CI secret scanning, tighten CORS.",
        ],
        "ev": ["security", "backend"],
    },
    {
        "slug": "forward-deployed-engineer",
        "title": "Forward Deployed Engineer (FDE)",
        "rating": 8,
        "band": "Strong match",
        "one_liner": "Embeds with customers, turns their workflow into a working deployment of the product.",
        "what": """You did the FDE loop for your own company: sit with the customer problem (shoppers, brands, stores), configure and extend the product (catalog schema, import, geo ads, kiosk, CRM), and stay until it works.

Concrete deployments: 57-brand catalog pipeline, brand subscription packaging, in-store kiosk design, internship/lead funnels, Instagram growth stack. You wrote talking points and onboarding so a human can run the motion.""",
        "applies": """FDE (Palantir-style and the AI-lab copies) wants: high agency, product fluency, custom glue, comfort with messy data, and customer-facing communication. FITD is a long FDE tour where you were also the platform.

This is one of your best non-core-SWE titles — especially at AI companies that staff FDEs to land design-partner deployments.""",
        "gaps": """You have not been staffed onto *other companies’* environments (their VPC, their SSO, their politics) as an external FDE. Enterprise procurement and classified networks are unproven. The skill is there; the logo-on-the-badge context is different.""",
        "talking": [
            "Tell one brand as a deployment: raw site → JSON → schema gaps → import → live shop cards.",
            "Kiosk as a forward deployment into a physical venue.",
        ],
        "ev": ["data", "kiosk", "ops", "ai", "web"],
    },
    {
        "slug": "associate-forward-deployed-engineer",
        "title": "Associate Forward Deployed Engineer",
        "rating": 9,
        "band": "Exceeds the bar",
        "one_liner": "Early-career FDE: supports deployments, learns the product, executes well-scoped customer work.",
        "what": """Associate FDE is scoped customer tasks under a lead. You have already led the motion yourself (catalogs, kiosk, CRM, AI features). The associate bar — SQL/JSON wrangling, demos, tickets, light app config — is well below what FITD required.""",
        "applies": """You would clear an Associate FDE screen on technical range and communication (handbook, investor overview, brand emails). The risk is overqualification / impatience with shadowing.

Apply if you want the FDE career path and accept the level; use FITD to skip “can this person write a script and talk to a customer?”""",
        "gaps": """None on capability. Process gap: you have not been an associate on a team. Show you can take notes in someone else’s account plan.""",
        "talking": [
            "Bring a 10-minute product demo and a catalog-cleaning story.",
        ],
        "ev": ["data", "ops", "web", "ai"],
    },
    {
        "slug": "senior-forward-deployed-engineer",
        "title": "Senior Forward Deployed Engineer",
        "rating": 7,
        "band": "Solid overlap",
        "one_liner": "Owns a customer (or a few) end-to-end: technical success, expansion, difficult integrations.",
        "what": """You owned every FITD “customer” class: consumers, brands, and a hypothetical store (kiosk). You made architecture calls when the product was missing a piece (import function, geo sanitize, admin CRM).

Senior FDE means less “I need a spec” and more “I will create the spec with the customer.” That matches how you work.""",
        "applies": """At an early AI company, Senior FDE is often “founding technical deployer.” Your mix of build + GTM + AI features is the profile.

At a mature FDE org, Senior also means repeatable playbooks across many accounts and mentoring associates. You have playbooks (schema, onboarding packet) but not a dozen enterprise accounts.""",
        "gaps": """Multi-account enterprise complexity, delivery management, and political navigation inside a Fortune 500 are unproven. Rating is “can do the work, must learn the theater.”""",
        "talking": [
            "How you would run the first 30 days in a design-partner retailer.",
            "What you would refuse to custom-build vs. take back to product (classic senior FDE judgment).",
        ],
        "ev": ["data", "kiosk", "ai", "docs", "ops"],
    },
    {
        "slug": "staff-forward-deployed-engineer",
        "title": "Staff Forward Deployed Engineer",
        "rating": 5,
        "band": "Adjacent",
        "one_liner": "Sets FDE technical direction across many deployments; unblocks seniors; shapes the product.",
        "what": """Staff FDE is a leverage role: patterns, reusable accelerators, hiring, multi-region delivery. You created reusable artifacts (schema, handbook, import path, bot platform) that *would* scale deployments — but you have not operated at staff scope (many seniors, many accounts).

Founder leverage is real; Staff title at a large FDE shop is a different social technology.""",
        "applies": """Your platform-ish artifacts (catalog schema, functions, admin) are what a Staff FDE builds so others deploy faster. Use them as evidence of staff *instincts*.

Do not claim you have already performed Staff FDE in an org.""",
        "gaps": """No org-level FDE leadership, no cross-account reliability program. Applying Staff as a first FDE job will bounce at most firms; Senior or Founding is the better ask.""",
        "talking": [
            "Pitch the catalog schema + import function as an accelerator you would give every FDE.",
        ],
        "ev": ["docs", "data", "backend"],
    },
    {
        "slug": "lead-forward-deployed-engineer",
        "title": "Lead Forward Deployed Engineer",
        "rating": 5,
        "band": "Adjacent",
        "one_liner": "Leads a team of FDEs: staffing, quality, customer strategy, hiring.",
        "what": """You led yourself, interns (program design), and a contractor onboarding path. That is leadership raw material, not leading an FDE pod through quarterly account goals.

Lead FDE is people management + delivery, not only being the best deployer.""",
        "applies": """Small-company Lead (player-coach on 2–3 deployers) could work if they value founder judgment. You already wrote engagement agreements and onboarding — relevant to running a pod.

Large-company Lead FDE expects prior Senior FDE in that culture.""",
        "gaps": """No FDE team you hired and run. Internship program is the closest people-lead evidence.""",
        "talking": [
            "How you would split FDE vs. product eng work after the first three brand deployments.",
        ],
        "ev": ["ops", "docs"],
    },
    {
        "slug": "forward-deployed-ai-engineer",
        "title": "Forward Deployed AI Engineer",
        "rating": 8,
        "band": "Strong match",
        "one_liner": "FDE whose payload is models: eval in the customer’s domain, RAG/tools, safety, workflow change.",
        "what": """You deployed AI into real workflows: shoppers (stylist, VTO, closet labels), brands (Gemini tagging), marketing (GPT-4o, n8n), and community (bots with approval). You constrained models with domain data (wardrobe, weather, catalog) and added safety (moderation, kill switch, proxy).

That is Forward Deployed AI: the model only counts if the workflow changes.""",
        "applies": """AI labs hiring FDEs for design partners want people who have already put Gemini-class models in front of users and dealt with quality variance (you listed this as a business risk). Fashion is a credible multimodal domain (garments, photos, try-on).

Strong title for you — pair with AI Product Engineer.""",
        "gaps": """Customer-premise model deployment (VPC, private endpoints, their data residency) is unproven. Evals are informal. Still a strong match for startup/lab FDE-AI.""",
        "talking": [
            "A design-partner story: we will not chat — we will label closet photos and only then generate outfits.",
            "What you measure (saves, VTO completion) vs. what you do not (BLEU on captions).",
        ],
        "ev": ["ai", "ops", "kiosk", "data"],
    },
    {
        "slug": "founding-ai-forward-deployed-engineer",
        "title": "Founding AI Forward Deployed Engineer",
        "rating": 9,
        "band": "Strong match",
        "one_liner": "First FDE at an AI company: invents the motion, deploys the model, feeds product.",
        "what": """This is the closest named role to what you have already been. You were the founding engineer *and* the person who took AI to users and brands. You created the deployment kit: schema, import, kiosk, CRM, prompts, handbook, internship/GTM.

Founding FDE means zero playbook. FITD had zero playbook.""",
        "applies": """Early AI startups use this title when they need a builder who will sit with the first ten customers and also write product code. You have done both on one company. The “AI” modifier is earned (Gemini, Vertex, bots), not cosmetic.

If you join another founding team, this doc is the one to send.""",
        "gaps": """You were founding FDE of *your* company. Doing it again means proving you can deploy someone else’s model/product. That is learnable; interview for curiosity about their stack, not only FITD.""",
        "talking": [
            "What you would copy from FITD’s first-customer motion and what was too founder-specific.",
        ],
        "ev": ["ai", "data", "kiosk", "ops", "ios", "docs"],
    },
    {
        "slug": "forward-deployed-engineer-ai-enablement",
        "title": "Forward Deployed Engineer, AI Enablement",
        "rating": 6,
        "band": "Solid overlap",
        "one_liner": "Helps a company adopt AI internally: workflows, guardrails, training, SDLC assistants.",
        "what": """Internal enablement you built: admin prompt packs, Cursor rules, bot platform with approval, handbook, Discord HQ setup, contractor/intern onboarding. You used AI to run marketing and community, not only the consumer app.

That is enablement of FITD-the-company, a single org.""",
        "applies": """AI Enablement FDEs teach and instrument other teams. You have artifacts (prompt packs, rules, runbooks) and have thought about human-in-the-loop (bot approval). Good for roles that want a practitioner who can also write the workshop.

Weaker if they need change management across a 10,000-person company.""",
        "gaps": """No enterprise enablement program, no measured adoption across many teams. Agentic SDLC title is the more specific cousin.""",
        "talking": [
            "Show prompt packs + kill switch as enablement with brakes.",
        ],
        "ev": ["ai", "docs", "ops", "web"],
    },
    {
        "slug": "forward-deployed-engineer-solution-architect",
        "title": "Forward Deployed Engineer / Solution Architect",
        "rating": 8,
        "band": "Strong match",
        "one_liner": "Hybrid: deploys in the field and owns the reference architecture the customer will live on.",
        "what": """You combined FDE execution (brands, kiosk, CRM) with SA artifacts (ecosystem diagram, Firestore architecture, kiosk PRD, schema). The same person wrote the system and installed it into GTM motions.

That hybrid is exactly this slash title.""",
        "applies": """Vendors who have not split SE vs. FDE vs. SA will hire this. You can draw the target architecture *and* import the customer’s catalog the same week.

Use the architecture handbook as the SA half and the 57-brand pipeline as the FDE half.""",
        "gaps": """Enterprise integration patterns still thin. Hybrid roles at big vendors may still want prior customer logos.""",
        "talking": [
            "One slide: current FITD reference architecture; one slide: what changes for a retailer with their own PIM.",
        ],
        "ev": ["docs", "data", "kiosk", "backend", "ops"],
    },
    {
        "slug": "principal-software-solutions-engineer-forward-deployed",
        "title": "Principal Software Solutions Engineer / Forward Deployed",
        "rating": 5,
        "band": "Adjacent",
        "one_liner": "Principal-level SE/FDE: hardest accounts, sets method, represents the product technically at the highest altitude.",
        "what": """You have principal-*scope on one company* (every technical decision). Principal as a *level* usually means a decade-class track record across many strategic accounts and influence on the product roadmap from the field.

Your investor overview and architecture bible are principal-shaped documents. Your account portfolio is not.""",
        "applies": """Instincts: you already write executive-friendly technical narrative and you build the missing product instead of promising vapor. That is how principals behave.

Title match is about level, not ignorance of the work. Target Senior FDE / Founding first.""",
        "gaps": """Principal bar at most firms will not be met by a single-product founder story alone. Do not lead with this title unless they are a tiny org using “Principal” loosely.""",
        "talking": [
            "If they insist on Principal, emphasize reusable method (schema, staging, safety) not years-in-seat.",
        ],
        "ev": ["docs", "ops", "ai"],
    },
    {
        "slug": "lead-forward-deployed-engineer-hospitality",
        "title": "Lead Forward Deployed Engineer, Hospitality",
        "rating": 3,
        "band": "Thin transfer",
        "one_liner": "Leads FDE delivery for hotels, restaurants, venues — industry workflow expertise required.",
        "what": """FITD is fashion/retail, not hospitality. The kiosk is the only venue-shaped product (in-store experience, camera, public space). Brand partnerships with stores are adjacent to retail ops, not hotel PMS, POS, or guest journey systems.""",
        "applies": """Transfer: experiential in-venue software, privacy of cameras in public, always-on UI. Hospitality FDEs will care about property-level rollout, staff turnover, and guest systems — you have not touched those.

Retail FDE / in-store is the honest adjacent claim.""",
        "gaps": """No hospitality domain (Opera, Toast, reservation platforms, brand standards across properties). Lead + hospitality is two stretches.""",
        "talking": [
            "Map kiosk session/privacy to a hotel lobby only if they ask; do not claim hospitality experience.",
        ],
        "ev": ["kiosk", "ops"],
    },
    {
        "slug": "forward-deployed-engineer-ai-agentic-sdlc",
        "title": "Forward Deployed Engineer, AI & Agentic SDLC",
        "rating": 6,
        "band": "Solid overlap",
        "one_liner": "Deploys AI into how software is built: agents, code assistants, evals, SDLC guardrails.",
        "what": """You already work in an agentic SDLC: Cursor rules, handbook-as-context, prompt packs in admin, AI bots that post/comment with human gates, and a repo organized so agents can find architecture. You specified bot orchestrators, quotas, and idempotency — agent-ops patterns.

You have not built a commercial agentic-SDLC product (PR agents, repo evaluators) for other engineering orgs.""",
        "applies": """Companies selling coding agents need FDEs who have felt agent-assisted development and can install it safely. Your kill-switch/approval mindset is the correct instinct for SDLC (you do not auto-merge the bot).

Your consumer fashion AI is a parallel story: agents need tools + data + brakes.""",
        "gaps": """No deployment of Copilot/Cursor Enterprise/internal agents across a customer’s GitHub, no SDLC metrics (PR cycle time) you own for others. Fashion-bot orchestration ≠ enterprise SDLC platform, but the control-plane ideas transfer.""",
        "talking": [
            "How you would introduce an agent to a repo like FITD-Bible: rules, handbook, required human approval on deploys.",
            "Idempotency and audit logs on bots as the seed of agent observability.",
        ],
        "ev": ["ai", "docs", "ops"],
    },
    {
        "slug": "forward-deployed-engineer-clearance-required",
        "title": "Forward Deployed Engineer — Clearance Required",
        "rating": 1,
        "band": "Not evidenced",
        "one_liner": "FDE on classified or controlled government networks; active clearance required.",
        "what": """FITD is a commercial consumer/brand product on public Firebase/GCP. There is no government customer, no air-gapped deploy, no controlled unclassified/classified handling, and no clearance process documented.

FDE skills (above) are relevant *after* clearance. This project does not help you get a clearance and does not prove you have one.""",
        "applies": """Only generic FDE/software skill transfers. The distinguishing requirement — eligibility and experience in cleared environments — is absent. Do not apply unless you independently hold or can obtain clearance; FITD will not be the evidence.""",
        "gaps": """Clearance, govcloud, IL/FedRAMP, and classified SDLC are all missing. Rating is for *this project’s evidence*, not your personal eligibility (unknown here).""",
        "talking": [
            "If eligible, use the standard FDE doc and treat clearance as a separate checkbox.",
        ],
        "ev": ["ops"],
    },
]


def md_role(r: dict) -> str:
    stars = "●" * r["rating"] + "○" * (10 - r["rating"])
    return f"""# {r['title']}

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **{r['rating']} / 10** {stars} |
| **Match band** | {r['band']} |
| **Role in one line** | {r['one_liner']} |

{SCALE}

---

## Project context

{PROJECT_CONTEXT}

---

## What you have done in this project

{r['what']}

---

## How that applies to this title

{r['applies']}

---

## Gaps (be honest in interviews)

{r['gaps']}

---

## Evidence in the repo

{bullets(r['ev'])}

---

## Interview talking points

{chr(10).join(f'- {t}' for t in r['talking'])}

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
"""


def md_overview(roles: list[dict]) -> str:
    by_rating = sorted(roles, key=lambda x: (-x["rating"], x["title"].lower()))
    rows = "\n".join(
        f"| {r['rating']} | {r['band']} | [{r['title']}]({r['slug']}.md) |"
        for r in by_rating
    )

    def band_list(lo: int, hi: int) -> str:
        items = [r for r in by_rating if lo <= r["rating"] <= hi]
        return "\n".join(f"- **{r['rating']}** — [{r['title']}]({r['slug']}.md)" for r in items) or "- None"

    return f"""# FITD work mapped to job titles — overview

This folder rates how much **experience evidenced in FITD-Bible** applies to each job title. It is not a claim about other jobs, years in industry, or whether you would pass a given company’s interview loop.

{SCALE}

**How to use this**

1. Pick target titles from the strongest bands below.
2. Open that title’s document for project evidence, transfer story, gaps, and talking points.
3. Do not lead with titles in the thin / not-evidenced bands unless the rest of your career covers them.

---

## Findings (what this project actually is)

FITD-Bible is a founder-built **fashion AI company hub**: production consumer mobile, brand tooling, Firebase/GCP backend, web + admin, catalog/data ops, growth automations, and a retail kiosk concept.

| Surface | What exists | Career signal |
|---|---|---|
| iOS | Production SwiftUI app, App Store oriented, ~115 Swift files | Core: Mobile / iOS / SWE / Product |
| Android | Compose port, then frozen for Expo | Supporting mobile; not Android seniority |
| Expo | Phase 0 cross-platform scaffold | Mobile strategy, not a shipped RN app yet |
| Web | `fitdai.com` + Next.js admin CRM | Full-stack / frontend / solutions ops |
| Backend | Cloud Functions, Firestore, rules, staging | Applied backend/cloud, not specialist infra |
| AI | Gemini + Vertex VTO + bots + heuristic recs | AI Product / Applied / GenAI / FDE-AI |
| Data | ~57 brands, ~16.5k SKUs, scrapers, analytics events | Light DE / analytics; not warehouse DE |
| Kiosk | SwiftUI + hardware sourcing docs | Connected-device / field adjacent, not firmware |
| GTM / ops | Brand onboarding, CRM, internships, investor docs | FDE / Solutions / Product Engineer |
| Payments | StoreKit 2 + Play Billing + receipt validation | Entitlements only — not fintech rails |
| Security | Rules, App Check, secrets, bot kill switch | Secure product work, not Security Engineer |
| Infra | Two Firebase/GCP projects, Hosting, Functions | Cloud user, not k8s/IaC infrastructure |

**What this project is not:** trained custom ML models, vector search, firmware/embedded, Stripe/ledgers, enterprise networking, cleared government deployments, hospitality property systems, or a large-team CI/on-call culture.

---

## How FITD work transfers (by role family)

### Core software delivery (strongest)

You were the engineer of record across clients and the serverless backend. That maps directly to **Software Engineer**, **SWE/SDE I–II**, **Application Developer**, **Full-Stack Engineer**, **Mobile / iOS Engineer**, and **Software Generalist**. SWE I / SDE I are *exceeded*; SWE II / SDE II are the honest mid-level landing if a large company levels you on process and algorithms rather than product breadth.

### Product and applied AI (strong)

AI is in the shipped product (labeling, stylist, virtual try-on, bots), constrained by closet/catalog/weather, with safety controls. That is **AI Product Engineer**, **Applied AI Engineer**, **GenAI Engineer**, and **AI Engineer** — not **Machine Learning Engineer** or **AI/Search Engineer**.

### Forward deployed and solutions (strong, with a caveat)

The FDE loop — sit with a messy customer problem, extend the product, leave something running — is what you did for brands, stores (kiosk), and growth/CRM. **FDE**, **Forward Deployed AI Engineer**, **Founding AI FDE**, **FDE / Solution Architect**, and **Solutions Engineer** are real fits. **Associate FDE** is below your capability. **Staff / Lead / Principal FDE** are level stretches (instincts yes, org scope no). **Hospitality** and **Clearance Required** are not evidenced.

### Adjacent (real overlap, not the center of the work)

**Backend**, **Frontend**, **Android**, **Cloud**, **Data**, **Analytics**, **Algorithm**, **Support**, **Field**, **AI Enablement**, and **Agentic SDLC** FDE: you have artifacts, not a specialist career.

### Weak or absent

**Platform / Infrastructure / Developer Platform / Developer Tools** in the Big Tech sense; **Embedded / Firmware / Hardware-Software / Sensor Algorithms**; **Fintech / Payments Infra / Networking**; **Security Engineer** as a job; **ML / Search** as disciplines.

---

## Ratings (all titles, high to low)

| /10 | Band | Title |
|---:|---|---|
{rows}

---

## Apply / stretch / avoid

### Best targets from this project (9–10)

{band_list(9, 10)}

### Strong applications (8)

{band_list(8, 8)}

### Credible with a gap story (6–7)

{band_list(6, 7)}

### Only if the rest of your background fills it (4–5)

{band_list(4, 5)}

### Do not use FITD as primary evidence (0–3)

{band_list(0, 3)}

---

## Leveling notes (I / II / Senior / Staff / Lead / Principal)

| Signal in FITD | What it supports | What it does not support by itself |
|---|---|---|
| Whole-product ownership | SWE II / SDE II, Senior FDE at a startup, Founding FDE | Staff/Principal at a large FDE org |
| Intern + contractor onboarding | Informal mentorship, player-coach Lead | People-manager Lead of an FDE pod |
| Handbook, schema, staging | Written design at mid level | Formal architecture review culture |
| No CI/on-call/team reviews | — | Big-co SWE process bar |
| One company, one architecture | Depth of ownership | Breadth of customer environments |

**Practical ask:** use **SWE II / SDE II**, **Full-Stack**, **Mobile/iOS**, **AI Product / Applied AI / GenAI**, **FDE** or **Founding AI FDE**. Treat I-level titles as easy clears, not goals. Treat Staff/Lead/Principal as promotions you would earn after joining, not as the incoming ask from this repo alone.

---

## Method

- Scope: FITD-Bible only (`development/`, `business/`), as of the mapping date.
- Evidence: shipped apps, functions, rules, catalogs, automations, and docs — not aspirations in roadmaps unless called out as future.
- Rating: fit of *this work* to the *typical bar* of the title, not a prediction you will get the offer.
- Honesty rule: gaps are written into every title doc so the overview cannot be used as puffery.

Each title has its own file in this folder. Start with the matching doc; come back here for the portfolio view.

---

## Folder index (A–Z)

{chr(10).join(f"- [{r['title']}]({r['slug']}.md)" for r in sorted(roles, key=lambda x: x['title'].lower()))}
"""


def main() -> None:
    assert len(ROLES) == 54, f"expected 54 titles, got {len(ROLES)}"
    slugs = [r["slug"] for r in ROLES]
    assert len(slugs) == len(set(slugs)), "duplicate slugs"

    for r in ROLES:
        (OUT / f"{r['slug']}.md").write_text(md_role(r), encoding="utf-8")

    (OUT / "README.md").write_text(md_overview(ROLES), encoding="utf-8")
    print(f"wrote {len(ROLES)} role docs + README.md → {OUT}")


if __name__ == "__main__":
    main()
