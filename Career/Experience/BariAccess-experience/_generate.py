#!/usr/bin/env python3
"""Generate per-role experience documents from TREI / BariAccess work."""

from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parent

SCALE = """## How to read the rating

The score is **experience this project gave you for this title**, not a career-total grade.

| Band | Score | Meaning |
| --- | --- | --- |
| Direct match | 8.5–10 | You already did this job on TREI. Interviews should lead with this work. |
| Strong | 7.0–8.4 | Substantial overlapping ownership. Name the gaps; do not overclaim seniority. |
| Adjacent | 5.5–6.9 | Real transferable work, but it is not the center of this title. |
| Partial | 4.0–5.4 | Some relevant pieces. Use as supporting evidence, not the headline. |
| Thin | 2.5–3.9 | Indirect overlap only. |
| Minimal | 0–2.4 | This project barely touches the role. |

Scope of evidence: 17 July 2026 – 16 September 2026. You are one of two primary engineers on TREI (BariAccess), with about 203 commits, ~99k lines added, and 658 files touched. Andrei remains the other primary author and owns more of the domain-engine and production-estate volume. Do not claim sole authorship of the whole platform.

"""

PROJECT = """## Project in one paragraph

**TREI** is the patient and care-team product in this repository. It is a wellness-first GLP-1 and metabolic-care platform for Bariatric Associates. You helped build a TypeScript monorepo with a Fastify API, PostgreSQL as system of record, a worker plus transactional outbox, an Expo iPhone app, a React staff console, and the public/patient site at trei.care. Staging runs on Azure Container Apps with Entra/External ID, Key Vault, Service Bus, Stripe sandbox, Calendly, Spike wearable adapters, and a guarded Azure OpenAI assistant named Aba.
"""

ROLES: list[dict] = []


def role(**kwargs):
    ROLES.append(kwargs)


role(
    slug="software-engineer",
    title="Software Engineer",
    score=8.7,
    band="Direct match",
    typical="Design, implement, test, and ship software across a product surface. Own bugs through production. Work in a team with reviews, CI, and release discipline.",
    did="You were a working software engineer on a real product, not a tutorial repo. You wrote production TypeScript across the API, worker callers, website, staff console, and iPhone client. You landed features behind tests, CI checkpoints, and fail-closed release gates. Day-to-day work included schema migrations, webhook races, identity, patient copy, staff operating views, and wearable custody.",
    applies="A general Software Engineer interview is looking for: can you take an unclear product need, turn it into contracts and code, prove it, and keep it honest when vendors, clocks, and users misbehave. That is the shape of TREI. Calendly delayed creates, Stripe event ordering, Spike disconnect vs outage, and overlapping Home refreshes are ordinary SWE problems at production difficulty.",
    evidence=[
        "Full-stack TypeScript monorepo: apps/api, apps/worker, apps/staff-web, apps/patient-mobile, apps/trellis-web, packages/*",
        "CI proof (`npm run check`), PostgreSQL integration tests, Bugbot follow-ups, Prettier/ESLint gates",
        "Feature slices with contracts, migrations, application use cases, and client rendering of server-owned state",
        "Staging Azure deployment path and TestFlight-oriented iOS builds",
    ],
    strengths="Breadth plus correctness habits: fail-closed auth, idempotent webhooks, stale-load guards, versioned evidence. You ship with product language, not only code.",
    gaps="Two intense months, not years of independent on-call. You worked beside a stronger-volume co-author. Some infrastructure and domain-formula depth is shared rather than solely yours.",
    talk="Pick one vertical slice (membership checkout, Calendly remotes, or connected-health shelf) and walk issuer → API → Postgres → worker → both UIs. Emphasize what you refused to fake.",
    bottom="This is the cleanest generic label for the work. Use it unless a more specific title is a better match.",
)

role(
    slug="software-engineer-i",
    title="Software Engineer I",
    score=9.2,
    band="Direct match",
    typical="Early-career engineer who can own well-scoped features end to end with mentorship, write tests, and learn the codebase quickly.",
    did="You operated above a typical SWE I scope: you did not only fill tickets inside one module. You opened public review and identity APIs, bound Home/Today to a server projection, finished Calendly remotes, and later added multi-provider connected health. You also absorbed review comments (Bugbot, typing, Prettier) and re-landed work until CI was green.",
    applies="SWE I hiring wants proof you can ship, take feedback, and not break adjacent surfaces. TREI forced that: website identity had to agree with the phone; staff source cards had to stay on server-owned status; intake follow-ups had to survive Calendly cancels. That is SWE I plus.",
    evidence=[
        "TREI-01 through TREI-07 patient/staff surfaces with repeated correctness fixes after review",
        "Shared Apple/Google/email identity across trei.care and the TREI app",
        "Admission, handover codes, and intake confirmation work in September 2026",
    ],
    strengths="Learning velocity, end-to-end ownership, healthcare-grade caution about claims and data.",
    gaps="Title-wise you already look like a strong SWE I / entering SWE II. Do not present this as a first Hello-World internship.",
    talk="Tell the SWE I story as: I was trusted with patient-facing slices, I proved them with tests, and I kept identity and evidence honest when integrations lied.",
    bottom="Very strong fit. This project is more than enough evidence for SWE I at a serious product company.",
)

role(
    slug="software-engineer-ii",
    title="Software Engineer II / SWE II",
    score=7.6,
    band="Strong",
    typical="Independent owner of multi-week features. Anticipates edge cases, designs interfaces, mentors juniors, and is trusted with ambiguous product work.",
    did="Several of your slices are SWE II in difficulty: Stripe event custody, Calendly webhook ordering, Spike SELECT_MANY cloud custody, ABA voice using backend-checked speech rather than raw model audio, and staff operating projections that must not go stale. You designed fail-closed behavior instead of happy-path UI.",
    applies="SWE II interviews ask whether you can own a system, not a function. You can talk about webhook idempotency, projection refresh, public-client OIDC, and multi-source wearable shelves. The gap is calendar time and org leverage: SWE II often implies 2+ years of independent production ownership and some mentoring.",
    evidence=[
        "Stripe sandbox checkout intents, signature verification, and membership binding without storing raw card payloads",
        "Calendly create/cancel/reschedule races with invitee timestamps and webhook keys",
        "Whoop / Withings / Samsung offer-connect-callback-disconnect-erase path through Spike",
        "Staff TREI-07 operating cards, membership recording, and cohort refresh honesty",
    ],
    strengths="Ambiguous product work, integration hardness, refusal to invent Beacon or membership from a late event.",
    gaps="Short tenure; no documented mentoring of other engineers; production remains dark, so live-incident seniority is limited.",
    talk="Frame as SWE II-shaped ownership on a small team. Be explicit that production cohort is not yet live so you do not oversell on-call years.",
    bottom="Credible SWE II candidate on work quality. Expect companies to still ask about time-in-role and production incidents.",
)

role(
    slug="software-development-engineer-i",
    title="Software Development Engineer I (SDE I)",
    score=9.1,
    band="Direct match",
    typical="Amazon-style SDE I: implements designs, writes tests, understands operational basics, and owns small-to-medium features.",
    did="Your work maps cleanly onto SDE I bar: typed contracts, migrations, IAM-style identity mapping, and operational scripts (webhook proofs, Calendly designated-slot pass, Stripe sandbox fixtures). You treated CI as a gate, not a suggestion.",
    applies="SDE I loops reward candidates who can write correct code, explain tradeoffs, and show operational awareness. TREI gives you Service Bus vs local worker, Key Vault, Container Apps, and fail-closed identity stories without claiming you invented AWS.",
    evidence=[
        "OIDC token verification and public-client Apple code redemption without sending Origin",
        "Outbox/worker path and Spike webhook live-path staging proof",
        "Dependency audit script and security patch chores",
    ],
    strengths="Bias to measurable proof. Comfort with cloud identity and queues.",
    gaps="Little classic distributed-systems interview drill (leader election, large-scale partitioning). Pilot scale is 1–2k users by design.",
    talk="Translate Azure Container Apps / Service Bus / Key Vault into SDE language: compute, queue, secrets, identity. Keep the customer (clinic) in the story.",
    bottom="Excellent SDE I evidence. Stronger than a typical new-grad project because the product is clinic-real and gated.",
)

role(
    slug="software-development-engineer-ii",
    title="Software Development Engineer II (SDE II)",
    score=7.2,
    band="Strong",
    typical="Amazon SDE II: owns a component, drives design docs, handles on-call, and delivers cross-team features with limited supervision.",
    did="You wrote and implemented design-level behavior: Stripe billing event custody, Spike cloud query foundation, SELECT_MANY custody, handover activation, and TREI first-release patient frame. Those are design-doc problems, not ticket-sized edits.",
    applies="SDE II wants component ownership and operational judgment. You have the former on several TREI components. You have staging operations and TestFlight, but not a long Amazon-style on-call rotation or org-wide influence.",
    evidence=[
        "docs/STRIPE-BILLING-EVENT-CUSTODY.md aligned with application-package webhook handling",
        "Connected-health contracts, migrations, API, worker pulls, staff strip, and phone shelf",
        "trei.care isolated Container App hosting and noindex/public-host hardening",
    ],
    strengths="Written decisions, versioned contracts, refusal to mix environments.",
    gaps="SDE II bar also includes mentoring, longer production ownership, and scale stories TREI has not yet been forced to live.",
    talk="Use one design: 'Stripe does not promise event order; here is how membership still stays true.' That is an SDE II interview answer.",
    bottom="Work quality supports SDE II conversations. Tenure and live-production years are the pushback. Target SDE I / SWE II first unless the team values startup intensity.",
)

role(
    slug="application-developer",
    title="Application Developer",
    score=8.6,
    band="Direct match",
    typical="Builds business applications: forms, workflows, CRUD-plus-rules, integrations with existing systems of record.",
    did="TREI is a clinical-adjacent business application. You built intake questionnaires with follow-ups, confirmation and handover, membership checkout, staff patient workspace, program assignment, daily check-ins, and appointment booking. Rules live on the server; clients render authorized state.",
    applies="Application Developer roles (often hospital IT, enterprise, or ISVs) care that you can model a workflow, persist it, and keep staff and patient views consistent. Clinic visits, roster matching, and Path A membership are exactly that.",
    evidence=[
        "Website intakes, follow-up persistence, and confirm-on-save including nested follow-ups",
        "Practice handover codes bound to patient and practice, with retry and redeem races closed",
        "Staff operating projections: membership, cohort, Action corrections, Beacon readings",
    ],
    strengths="Domain modeling under healthcare caution. You do not let a form become the source of truth.",
    gaps="Little classic .NET/Java enterprise stack; little SharePoint/Salesforce. Stack is TypeScript/Postgres/Azure.",
    talk="Walk Path A: public review → roster match → intakes → Calendly remotes → Stripe → staff admission → phone Today.",
    bottom="Very strong fit wherever the job is 'build the application the business actually runs.'",
)

role(
    slug="full-stack-engineer",
    title="Full-Stack Engineer",
    score=9.3,
    band="Direct match",
    typical="Comfortable from UI to database: one person can take a user story through client, API, data, and deploy.",
    did="Your file-touch histogram is the definition of full-stack: 514 trellis-web, 301 patient-mobile, 196 staff-web, 120 API, 207 data, 155 application, 101 contracts, plus worker, integrations, infra, and CI. You repeatedly shipped one behavior through all of those layers in a single change.",
    applies="Full-stack interviews ask whether you will get stuck at 'the other side of the stack.' On TREI you did not. Connected health is OAuth, custody tables, worker pulls, staff strip, and phone shelf. Identity is Apple public-client on iOS and the same account on trei.care.",
    evidence=[
        "Shared identity across website and iPhone",
        "My TREI portal: intakes, scheduling, membership, connected health",
        "Staff dashboard + API authorization + Postgres row ownership",
        "Expo client rendering server-owned Today / Plan / Progress / Aba",
    ],
    strengths="True vertical slices. You keep clients dumb and the API authoritative, which is the mature full-stack habit.",
    gaps="Less CSS-system / design-system specialization than a dedicated frontend hire; less query-planner specialization than a dedicated backend hire.",
    talk="Lead with one slice that hits web, phone, API, worker, and Azure. Full-stack is your headline title after Software Engineer.",
    bottom="This project's best literal match among IC engineering titles.",
)

role(
    slug="backend-engineer",
    title="Backend Engineer",
    score=8.4,
    band="Strong",
    typical="Owns APIs, data models, authz, jobs, and integration reliability. UI is a consumer, not the job.",
    did="You spent serious time in packages/application, packages/data, packages/contracts, apps/api, and webhook/worker-adjacent code. Examples: Spike adapter and live path, Stripe handling kept inside the application package, Calendly event keys, SELECT_ONE vs SELECT_MANY custody, patient admission before intakes complete.",
    applies="Backend interviews care about auth, consistency, and jobs. TREI's durable decisions (server authorization, transactional outbox, idempotent handlers, versioned decision results) are the interview language. You implemented product on top of that spine.",
    evidence=[
        "Fastify modular API with OIDC verification and use-case authorization",
        "PostgreSQL migrations (including 075+ connected-health history in tests)",
        "Webhook signature verification for Stripe and Calendly; Spike HMAC path",
        "Erasure, disconnect, and fail-closed provider lifecycle events",
    ],
    strengths="Correctness under replay, delayed events, and missing vendor data. Healthcare-safe defaults.",
    gaps="You also did a large amount of UI, so some teams will want deeper pure-backend (query plans, multi-region, JVM/Go services). Worker file-touch count is smaller than API/data.",
    talk="Do not hide the UI work, but interview as: I own the record, the job, and the contract; clients are projections.",
    bottom="Strong backend story. Pair it with full-stack rather than pretending you never touched React.",
)

role(
    slug="frontend-engineer",
    title="Frontend Engineer",
    score=8.1,
    band="Strong",
    typical="Owns user interface quality: state, accessibility, performance, design implementation, and client architecture.",
    did="You built patient-facing TREI frame, Home/Today, Plan/Learning, Progress/Beacon/Healthspan presentation, Aba conversation UI, staff patient workspace, and the public trei.care site including legal, portal, and My TREI. You fought stale overlapping loads, VoiceOver on Beacon stones, and honest empty/forming/error states.",
    applies="Frontend interviews want component structure, async state, and a11y. You have those. You also have the rarer trait of refusing to let the client invent clinical chrome: public TREI cannot open clinic Plan cards; Healthspan stays hidden until gates pass.",
    evidence=[
        "apps/patient-mobile TREI surfaces and accessibility tests",
        "apps/staff-web operating view, source strip, membership recording",
        "apps/trellis-web public site, My TREI, Stripe checkout routing, noindex host rules",
        "Product-language discipline (no slogans, no invented scores)",
    ],
    strengths="State honesty, accessibility, multi-surface design (marketing site, portal, staff, phone).",
    gaps="Not a specialist in CSS architecture, animation, or a large design system. React Native + React web, not a deep Vue/Angular or native UIKit career.",
    talk="Show the Progress/Beacon state matrix (loading, empty, forming, ready, error, restricted) as frontend craft tied to product ethics.",
    bottom="Strong product frontend engineer, especially for health and ops tools. Not a pixel-platform specialist.",
)

role(
    slug="mobile-engineer",
    title="Mobile Engineer",
    score=8.0,
    band="Strong",
    typical="Ships a phone application: navigation, offline/session, store release, device APIs, and mobile-specific performance/UX.",
    did="You built the TREI iPhone experience in Expo/React Native: application frame, Today, Plan, Progress, Aba text/voice, connected health, session storage, OIDC, push-related session boundaries, and TestFlight-oriented release wiring. Physical-device identity (Apple public client, associated domains) was part of your work.",
    applies="Mobile Engineer means you understand that a phone is not a small browser. You handled OS-secure session storage, request timeouts, stale refresh, microphone gating, WebRTC voice, and App Store / TestFlight constraints. The product is Apple-first and has a real bundle id and ASC app id.",
    evidence=[
        "apps/patient-mobile Expo app, EAS profiles, TestFlight submit config",
        "Apple Sign-In entitlements, associated domains for www.trei.care",
        "Aba native WebRTC voice path with backend-checked speech",
        "Connected-health Oura return controller and unified source shelf",
    ],
    strengths="Production-minded mobile: identity, permissions copy, release profiles, honest network failure.",
    gaps="Android is configured, not shipped. Little native module authorship. No long history of store reviews, crashlytics at scale, or offline-first sync engines.",
    talk="Lead with TestFlight + Apple identity + voice. Say Expo/RN explicitly so they do not assume Swift.",
    bottom="Strong cross-platform mobile engineer for an iOS-first product. Call the Android gap yourself.",
)

role(
    slug="ios-engineer",
    title="iOS Engineer",
    score=6.4,
    band="Adjacent",
    typical="Native iOS: Swift, SwiftUI/UIKit, Combine, Apple frameworks, App Store, and device APIs at the native layer.",
    did="You shipped an iPhone product through Expo: bundle identifier com.bariatricassociates.bariaccess, Apple Sign-In, associated domains, APS environment, camera-purpose plist copy, microphone permission, EAS TestFlight, and public-client token redemption that must not send Origin. Voice uses a native WebRTC session.",
    applies="This counts as iOS product delivery, which many 'iOS Engineer' jobs actually need. It does not count as native iOS engineering. You will lose a SwiftUI architecture loop unless the team accepts React Native.",
    evidence=[
        "app.json iOS entitlements, associated domains, Apple Sign-In",
        "eas.json testflight submit with ascAppId",
        "fix: redeem staging Apple HTTPS codes as a public client",
        "Voice conversation on physical iPhone path (proof still called out as open in docs)",
    ],
    strengths="You have fought real Apple identity and release issues, which many RN developers skip.",
    gaps="No Swift/Obj-C code ownership. No UIKit, Core Data, CloudKit, or App Intents. Android-first iOS teams will still want native samples.",
    talk="Apply to iOS-using product teams that list React Native. For native-only iOS, treat this as adjacent evidence and study Swift.",
    bottom="Good iOS *product* experience. Incomplete iOS *platform* experience.",
)

role(
    slug="android-engineer",
    title="Android Engineer",
    score=3.2,
    band="Thin",
    typical="Native Android: Kotlin, Jetpack, Play Store, background work, and Android-specific identity/notifications.",
    did="The Expo app declares an Android package and adaptive icon, and package.json has `preview:android`. The documented product path is Apple-first TestFlight. There is no Play Store submit profile, no Kotlin, and generated android/ is gitignored.",
    applies="You can honestly say the client is cross-platform capable and you understand mobile session/OIDC patterns that would transfer. You cannot claim Android shipping, Play review, or Jetpack architecture.",
    evidence=[
        "app.json android.package com.bariatricassociates.bariaccess",
        "preview:android script using expo run:android",
        "No EAS submit.android / Play track in eas.json",
    ],
    strengths="Shared RN skills (navigation, secure storage, networking) would shorten an Android ramp.",
    gaps="No shipped Android build, no Kotlin, no Play Console, no Android-specific push/background work proven.",
    talk="Do not lead with this title. If asked, say iOS-first Expo with Android package present, not delivered.",
    bottom="Insufficient as a primary Android Engineer application from this project alone.",
)

role(
    slug="product-engineer",
    title="Product Engineer",
    score=9.1,
    band="Direct match",
    typical="Engineer who sits with product and users, shapes the workflow, writes copy/logic together, and ships the smallest honest version.",
    did="TREI is product engineering under a scientific canon. You implemented first-release profile, public vs clinic chrome, Free Basic vs Path A, preparation readiness, handover, staff operating view, and patient language rules. You hid Healthspan until destination release and kept Beacon from inventing a forming baseline.",
    applies="Product Engineer jobs (startups, Stripe-like, clinic tech) want people who will change the product when the clinic's real workflow disagrees with a mock. You worked inside a bariatric practice's actual onboarding: intakes, remotes, membership, admission, daily program work.",
    evidence=[
        "TREI-01 first-release frame; TREI-02 Home/Today; TREI-03 Programs/Plan/Learning; TREI-04 Progress",
        "Product language standard and fail-closed public surfaces",
        "Confirm-every-filled-intake-question and admit-matched-patients-before-intakes-complete",
        "Staff workspace navigation and practice context",
    ],
    strengths="Canon discipline: you implement approved meaning, you do not freelance clinical claims.",
    gaps="Not a PM. You did not run a large discovery practice or growth experiments. Partnered with Andrei as product/scientific counterpart.",
    talk="Tell the story of a product decision you encoded as a gate (Healthspan hidden, Path B deferred, Garmin display-only).",
    bottom="One of your two or three best titles. Pair with Full-Stack or FDE.",
)

role(
    slug="ai-product-engineer",
    title="AI Product Engineer",
    score=8.0,
    band="Strong",
    typical="Ships AI-backed product features with UX, evals/safety, cost, and a clear job-to-be-done. Models are a dependency, not the identity of the role.",
    did="You helped make Aba a product, not a chatbot demo. Typed and voice conversation share a guarded backend. Voice transcribes, checks echo, sends the transcript through the same policy as text, and only then asks Realtime to speak the checked body. Rate limits, 24-hour retention, start-fresh, and medical-claim output checks are product decisions in code.",
    applies="AI Product Engineer interviews ask: what must never happen, who is the authority, and how does the UI stay honest when the model is wrong. TREI's answer is: the backend is the authority; Realtime is a renderer; urgent/clinical/injection routes are classified before generation.",
    evidence=[
        "TREI-05 one ABA text and voice conversation",
        "packages/domain/src/ai/generated.ts route and output checks (urgent, injection, medical claims)",
        "docs/OLLIE-VOICE-AND-COST.md: ephemeral client secrets, no patient record in the Realtime session",
        "Recovery, pause, and restricted-conversation client fixes",
    ],
    strengths="Safety and product constraints first. Cost and session lifetime are designed, not hoped.",
    gaps="No large eval harness, no prompt-ops team, no fine-tuning. Physical iOS voice proof is still called out as open in the voice doc.",
    talk="Never say 'we added ChatGPT.' Say 'we added a bounded assistant that cannot become the record.'",
    bottom="Strong AI-product story for healthcare and other high-stakes UX.",
)

role(
    slug="platform-engineer",
    title="Platform Engineer",
    score=6.3,
    band="Adjacent",
    typical="Builds internal platforms: paved roads for deploy, identity, observability, golden paths other teams consume.",
    did="You worked on the *product's* platform spine: Container Apps, Bicep touches (apps.bicep, access.bicep, trellis-web.bicep), GitHub Actions deploys, identity configuration scripts, and a modular monolith other features reuse. You hosted trei.care as an isolated staging Container App.",
    applies="Some Platform Engineer interviews will accept 'I helped stand up the runtime other features run on.' Others mean Kubernetes platform teams, IDP portals, and golden-path modules used by dozens of squads. You have the first, not the second.",
    evidence=[
        "infra/trellis-web.bicep and isolated ACR token until Owner granted AcrPull",
        "Identity configure scripts for staging External ID",
        "CI classify/full_verify with Postgres service",
        "Architecture of swappable adapters behind stable boundaries",
    ],
    strengths="Environment separation, managed identity, fail-closed config.",
    gaps="Not a multi-tenant internal developer platform. Limited Terraform/K8s/service-mesh depth. Observability package touches are light in your file histogram.",
    talk="Apply if the 'platform' job is cloud runtime + identity + CI for a product team. Skip if it is a 50-person developer-platform org.",
    bottom="Adjacent. Use as supporting evidence for Cloud/Infra, not as the headline.",
)

role(
    slug="infrastructure-engineer",
    title="Infrastructure Engineer",
    score=5.9,
    band="Adjacent",
    typical="Owns networks, compute, databases, backups, IAM at the estate level. Often closer to SRE/sysadmin than product features.",
    did="You contributed to Bicep app/access modules, staging website hosting, Containerfile awareness, and scripts that assume Key Vault and managed identity. Dark production and database privilege proof exist in the repo; Andrei's volume is larger on that estate.",
    applies="You can speak to Azure resource topology (Container Apps, Postgres Flexible Server, Service Bus, Blob, Key Vault, Monitor) and why local adapters cannot start as staging. That is infrastructure literacy. It is not years of running the estate.",
    evidence=[
        "infra/apps.bicep, access.bicep, trellis-web.bicep file history",
        "Staging Container App for the public site",
        "docs/RUNBOOK.md and deploy workflow familiarity",
    ],
    strengths="Respect for environment boundaries and secrets. You did not treat localhost as production.",
    gaps="No evidence you are the primary owner of Postgres HA, VNet, WAF, backup drills, or capacity planning. Recovery exercises are documented as organizational, not as your personal completed drills.",
    talk="Be precise: I helped define and deploy app infrastructure; I am not the lone infra owner.",
    bottom="Enough to pair with Cloud Engineer. Not enough to be a dedicated Infra hire.",
)

role(
    slug="cloud-engineer",
    title="Cloud Engineer",
    score=6.6,
    band="Adjacent",
    typical="Designs and operates cloud services: IAM, containers, managed databases, networking, cost, and environment promotion.",
    did="TREI's runtime is Azure-native. You shipped a site onto Container Apps, dealt with ACR pull permissions, used managed identity for worker/API patterns, and kept staging/production separate. You configured OIDC against Microsoft External ID and workforce Entra.",
    applies="Cloud Engineer interviews want you to reason about identity, secrets, and promotion. You have those stories. You do not have a deep networking/landing-zone specialty or multi-cloud.",
    evidence=[
        "rg-bariaccess-staging mental model: API, worker, Postgres, Service Bus, Blob, Key Vault, ACR, telemetry, External ID",
        "trellis-web Azure deploy workflow",
        "Apple/Google/email customer identity plus staff workforce tenant",
    ],
    strengths="Identity and environment isolation, which is the hard part of cloud for a health product.",
    gaps="Limited VNet/Private Endpoint/front-door depth in your personal commits. Cost optimization and reserved-capacity work not evidenced.",
    talk="Map the architecture diagram. Mention managed identity instead of long-lived keys.",
    bottom="Solid cloud-product engineer. Borderline as a dedicated Cloud Engineer vs a full-stack engineer who deploys to Azure.",
)

role(
    slug="developer-platform-engineer",
    title="Developer Platform Engineer",
    score=5.1,
    band="Partial",
    typical="Builds tools, paved paths, and self-service so other developers ship faster: golden templates, IDP, internal CLIs, preview environments.",
    did="You improved the developer path for this one repo: npm workspaces, CI lanes (docs vs full), seed/migrate scripts, local Stripe/Calendly webhook scripts, and Metro/EAS development client flow. That is developer experience for a two-person team, not a platform used by many teams.",
    applies="DX work transfers, but Developer Platform Engineer at a mid-size company usually means productizing those paths. TREI did not require an internal developer portal.",
    evidence=[
        "Root package.json scripts for db, smoke, webhooks, identity configure",
        "CI proof-lane classification",
        "Local preview:mobile with synthetic display data",
    ],
    strengths="You feel friction and script it. You keep secrets out of Git.",
    gaps="No Backstage/IDP, no multi-repo golden path, no self-service preview apps for many squads.",
    talk="Position as 'I care about the paved path' inside a product-engineer story.",
    bottom="Partial. Do not apply as a specialist unless you have other DX work.",
)

role(
    slug="developer-tools-engineer",
    title="Developer Tools Engineer",
    score=4.6,
    band="Partial",
    typical="Builds compilers, CI systems, debuggers, linters, editors, or internal build tools as the product.",
    did="You used and occasionally extended tools: ESLint/Prettier, Vitest configs (including website and Oura-web), tsx, EAS, Metro audit acceptances, dependency audit script. You did not build a developer-tool product.",
    applies="Familiarity with a serious toolchain helps, but this title wants tool-building as the job. TREI is a health product.",
    evidence=[
        "scripts/audit-dependencies.ts",
        "vitest.website.config.ts / vitest.oura-web.config.ts",
        "CI formatting and typecheck gates you repeatedly satisfied",
    ],
    strengths="High standards for reproducible checks.",
    gaps="No compiler, no build-system authorship, no IDE/plugin work.",
    talk="Use only as a supporting bullet under Software Engineer.",
    bottom="Not a match as a target role from this project.",
)

role(
    slug="embedded-software-engineer",
    title="Embedded Software Engineer",
    score=1.4,
    band="Minimal",
    typical="C/C++/RTOS, MCUs, drivers, timing, hardware bring-up, constrained memory.",
    did="TREI talks to wearables only through Spike cloud APIs. There is no firmware, no MCU, no BLE stack of your own. Phone microphone/WebRTC is application-level, not embedded.",
    applies="Almost nothing maps. At most: you consumed device-originated time series (sleep, steps, HRV) after a vendor normalized them.",
    evidence=[
        "Spike cloud client for Oura/Garmin/Polar/Whoop/Withings/Samsung",
        "No C, no RTOS, no device firmware tree in this repository",
    ],
    strengths="You understand device data as untrusted evidence with consent and erasure.",
    gaps="The entire embedded skill set.",
    talk="Do not apply. If a connected-device company wants cloud+app, use Connected-Device Software Engineer instead.",
    bottom="This project does not qualify you as an embedded engineer.",
)

role(
    slug="firmware-engineer",
    title="Firmware Engineer",
    score=1.0,
    band="Minimal",
    typical="Bare-metal or RTOS firmware, bootloaders, flashing, hardware registers, certification.",
    did="No firmware was written. Wearable vendors own their firmware. TREI stores observations after Spike.",
    applies="Does not apply, except that you designed deletion/erasure of vendor-sourced health data, which firmware teams sometimes ignore at the cloud layer.",
    evidence=["External-health erasure ledger and disconnect/erase APIs", "Zero firmware artifacts"],
    strengths="Cloud-side device lifecycle (connect, pull, erase).",
    gaps="All firmware skills.",
    talk="Skip this title.",
    bottom="No meaningful firmware experience in this project.",
)

role(
    slug="connected-device-software-engineer",
    title="Connected-Device Software Engineer",
    score=7.4,
    band="Strong",
    typical="The software around devices: pairing/OAuth, cloud sync, device identity, telemetry, companion apps, privacy.",
    did="This is one of your strongest specialized stories. You implemented Spike as a post-login adapter, Oura as the production-shaped wearable, gated Garmin/Polar, then Whoop/Withings/Samsung through cloud custody. Offer, connect, callback, disconnect, erase, minimum observations, and a unified patient/staff shelf are the companion-app + cloud job.",
    applies="Connected-device companies (wearables, home health, IoT apps) hire people who keep vendor APIs from becoming the identity authority and who handle missing/stale/zero as different states. That is written into TREI architecture and your recent SELECT_MANY work.",
    evidence=[
        "Spike webhook adapter, data contract, live path, application 11922 cutover docs",
        "Provider integration authorization/status/delete plus sleep and daily queries",
        "SELECT_MANY custody: one active source per provider, refuse SELECT_ONE rollback while multiple live",
        "Staff source strip + phone connected-health shelf",
        "Erasure reconciliation script and privacy-safe staff copy on outage vs disconnect",
    ],
    strengths="Consent, provenance, vendor failure modes, multi-provider product design.",
    gaps="No BLE pairing, no device firmware, no on-device signal processing. Cloud-and-app side of connected devices.",
    talk="Lead with 'devices are adapters, not identity.' Walk Oura vs cloud providers and erasure.",
    bottom="Excellent fit for companion-app / device-cloud roles. Do not pretend you wrote watch firmware.",
)

role(
    slug="hardware-software-engineer",
    title="Hardware/Software Engineer",
    score=3.0,
    band="Thin",
    typical="Bridges board bring-up and software: schematic-aware firmware, drivers, test jigs, sometimes FPGA.",
    did="No hardware design. You integrated commercially available wearables through a third-party API.",
    applies="Only the software half of a hardware/software role, and only at the cloud/app layer.",
    evidence=["Wearable observation types (sleep, steps, HRV) consumed as normalized reports", "No schematics, drivers, or lab bring-up"],
    strengths="Respect for units, missing values, and vendor-native metrics (you do not invent Garmin sleep efficiency).",
    gaps="Hardware engineering in full.",
    talk="Redirect to Connected-Device Software Engineer.",
    bottom="Not a hardware/software hire from this repo.",
)

role(
    slug="machine-learning-engineer",
    title="Machine Learning Engineer",
    score=4.1,
    band="Partial",
    typical="Trains, evaluates, deploys ML models: data pipelines, features, training jobs, model registry, monitoring.",
    did="TREI's 'intelligence' is mostly deterministic, versioned evaluators (R&R, Beacon, ISE, governors) plus a generated-language gateway. You worked on product surfaces and some decision/presentation wiring. You did not train models, label datasets, or run GPU jobs.",
    applies="You understand why ML must not own authorization or evidence. That is valuable around ML teams. It is not MLE experience.",
    evidence=[
        "packages/domain decision owners with algorithmId/algorithmVersion",
        "Beacon mapper and R&R registry exist; scheduled live R&R publication is not active",
        "Azure OpenAI as a bounded vendor, not a trained in-house model",
    ],
    strengths="Feature/evidence discipline; you will not silently fill missing labs with a model guess.",
    gaps="No training, no eval datasets of your own, no model serving infra, no feature store.",
    talk="Apply to Applied AI / AI Product, not classic MLE, unless you have other ML work.",
    bottom="Partial literacy, not MLE qualification.",
)

role(
    slug="ai-engineer",
    title="AI Engineer",
    score=7.1,
    band="Strong",
    typical="Builds systems that use foundation models in production: RAG, tools, gateways, safety, observability, cost.",
    did="You implemented and hardened a production-shaped AI gateway path: classified input routes, output checks, bounded context, rate limits, managed-identity session minting, and a voice renderer that is not allowed to see the patient record. Aba is the patient-facing name.",
    applies="AI Engineer (2025–2026 sense) often means LLM application engineering. That is this, in a stricter domain than most chatbots. You also live in a repo that forbids AI from changing deterministic state.",
    evidence=[
        "AI gateway module in architecture: approved context, persona, structured output, safety, cost",
        "generated.ts: GENERATE / BOUNDARY / URGENT / PROMPT_INJECTION",
        "Realtime: 60-second client secret, echo discard, interaction-id join",
        "Staff/patient copy never lets Aba become clinical authority",
    ],
    strengths="High-stakes LLM app design. Clear authority boundary.",
    gaps="Little RAG corpus engineering, tool-calling agents, or model-routing platforms. No published eval numbers.",
    talk="Title the work 'guarded LLM application in healthcare,' not 'AI researcher.'",
    bottom="Strong LLM-app AI Engineer. Weak classical ML AI Engineer.",
)

role(
    slug="applied-ai-engineer",
    title="Applied AI Engineer",
    score=7.6,
    band="Strong",
    typical="Takes models into a specific domain: healthcare, legal, finance. Mixes prompt/policy, product, and evaluation against domain rules.",
    did="Aba is applied AI in metabolic/GLP-1 care. Output checks block medical claims, verbatim echo, internal detail, and unaffirmed personal claims. Urgent phrasing routes away from ordinary generation. Voice and text share policy so a spoken question cannot bypass the typed safety path.",
    applies="Applied AI hiring wants domain constraints encoded. You have them. The clinic is the customer, so this is closer to FDE+AI than to a lab.",
    evidence=[
        "Clinical topic vs product-navigation vs emergency regex routes",
        "24-hour retention, six-exchange context, refused replies cannot poison later turns",
        "Disclosure, microphone, and cost gates in the voice decision record",
    ],
    strengths="Domain-safe application. You can explain why a wellness assistant must not dose-advise.",
    gaps="Limited offline eval against clinician-labeled transcripts. Physical voice acceptance still open.",
    talk="Bring a concrete forbidden output and the code path that stops it.",
    bottom="Very good applied-AI story if the team is productizing LLMs in a regulated-ish domain.",
)

role(
    slug="generative-ai-engineer",
    title="Generative AI / GenAI Engineer",
    score=7.5,
    band="Strong",
    typical="Owns LLM/voice/image generation features: prompting, safety, latency, cost, multimodal UX.",
    did="Generative work in TREI is text plus speech. You wired Realtime as TTS-of-checked-text rather than letting the model improvise aloud. That is a GenAI engineering choice with latency, interruption, and echo consequences you then had to debug (ABA recovery, pause, duplicate history).",
    applies="GenAI roles love multimodal demos. You have a more mature variant: generation is allowed only after policy. Cost and rate limits are explicit.",
    evidence=[
        "Native WebRTC session, semantic VAD, echo filter, manual interruption",
        "Out-of-band checked speech payload; automatic responses disabled",
        "Rate limits 12/5 minutes and 60/day",
    ],
    strengths="Multimodal without surrendering authority. Debugging conversational state is real GenAI work.",
    gaps="No image/video generation. No agent swarms. No fine-tuned voice clone as a product.",
    talk="Contrast naive Realtime conversation vs TREI's checked-speech design. That is the interview.",
    bottom="Strong GenAI application engineer for voice+text products.",
)

role(
    slug="ai-search-engineer",
    title="AI/Search Engineer",
    score=3.6,
    band="Thin",
    typical="Retrieval, ranking, embeddings, query understanding, search quality, sometimes RAG.",
    did="Architecture mentions bounded retrieval for provider-authored content in later specs. The work you actually shipped is not a search stack: no inverted index, no embeddings pipeline, no ranking experiments. Learning content is assigned Program readings, not search.",
    applies="Only weakly: you understand that generated answers must not retrieve unauthorized patient facts. That is access control, not search.",
    evidence=["Program Learning as reviewed content, not a search corpus", "No vector database or query-understanding service in the runtime map"],
    strengths="Access-control instincts that search/RAG teams need.",
    gaps="The search discipline itself.",
    talk="Do not target this title from TREI alone.",
    bottom="Not qualified as AI/Search from this project.",
)

role(
    slug="data-engineer",
    title="Data Engineer",
    score="7.0",
    band="Strong",
    typical="Pipelines, warehouses, ingestion, quality, orchestration, idempotent ETL/ELT.",
    did="You built operational data paths rather than a warehouse: Spike pulls into PostgreSQL, webhook intake, outbox-to-worker, projections for Today/staff, erasure ledger, and normalized Stripe/Calendly facts without storing raw secrets. Migrations are versioned and tested against Postgres 17.",
    applies="Many Data Engineer jobs in product companies are 'get events into the system of record correctly.' That is TREI. Classic DE jobs that mean dbt + Snowflake + Airflow are only partly matched.",
    evidence=[
        "packages/data repositories and migrations (connected-health, bookings, billing intents)",
        "Transactional outbox; idempotent handlers",
        "Spike cloud query foundation: native units, omit nulls, do not zero-fill",
        "scripts/reconcile-external-health-erasure-ledger.ts",
    ],
    strengths="Idempotency, late-arriving events, PII/PHI minimization.",
    gaps="No analytics warehouse modeling, no Spark, no CDC-to-lake, limited orchestration beyond the worker.",
    talk="Call it operational data engineering / event ingestion. Ask if they mean warehouse DE.",
    bottom="Strong for product-data/ingestion roles. Medium for analytics-warehouse DE.",
)

role(
    slug="analytics-engineer",
    title="Analytics Engineer",
    score=4.8,
    band="Partial",
    typical="dbt models, semantic layers, BI-ready tables, metric definitions for business users.",
    did="You implemented product metrics as deterministic domain owners (Beacon display bands, R&R components) and staff/patient projections. Telemetry policy explicitly forbids health values in product analytics. There is no dbt project or Looker layer.",
    applies="You can define metrics carefully, which analytics engineers need. You did not build an analytics platform.",
    evidence=[
        "Architecture: analytics uses a separate typed event vocabulary; no health values in telemetry",
        "Beacon/R&R as versioned evaluators, not a warehouse mart",
    ],
    strengths="Metric honesty and privacy.",
    gaps="dbt, BI tools, stakeholder metric catalogs, dimensional modeling as a job.",
    talk="Use as a supporting story about metric governance, not as the target title.",
    bottom="Partial. Better as Data Engineer (operational) or Algorithm Engineer.",
)

role(
    slug="algorithm-engineer",
    title="Algorithm Engineer",
    score=6.5,
    band="Adjacent",
    typical="Designs and implements numerical/algorithmic systems: scoring, optimization, signal processing, versioned evaluators.",
    did="The repo contains a serious algorithm layer: R&R registry (70 components, 25 sub-scores, 8 composites, Chrono indices), Beacon corridor mapper, sleep-regularity evidence, ISE governor. Your commits show more product-binding than original formula authorship: Progress/Beacon presentation, human-source collection/scoring branches, staff Beacon alignment, fail-closed coverage states.",
    applies="You can implement and productize versioned algorithms, which many algorithm-engineer jobs need. Inventing the clinical math appears to be shared/canon-driven (ABAEMR) with Andrei owning more domain volume.",
    evidence=[
        "feat: bind TREI-04 Progress to dated evidence and longer-term gates",
        "Beacon/Healthspan patient surfaces and honest state matrix",
        "Human R&R source collection and consented five-domain staging shadow proof (repo history)",
        "Sleep regularity treated as evidence with an internal staging decision",
    ],
    strengths="Versioning, insufficiency vs value, no silent defaults.",
    gaps="Not a research algorithms background (OR, DSP, ML). Formula origin is canon, not your paper.",
    talk="Say you implement locked algorithms and keep them from leaking onto surfaces before evidence exists.",
    bottom="Adjacent-to-strong for applied scoring systems. Weak for research algorithm roles.",
)

role(
    slug="sensor-algorithm-engineer",
    title="Sensor Algorithm Engineer",
    score=5.4,
    band="Partial",
    typical="Algorithms on raw sensor streams: IMU, PPG, sleep staging, on-device or near-device DSP.",
    did="You consumed vendor-processed metrics (sleep duration, deep sleep, steps, HRV RMSSD) and implemented product rules such as minimum observations and sleep regularity *evidence* gates. You did not stage sleep from PPG or write a step-count algorithm.",
    applies="Sensor algorithm teams at Oura/Whoop would not count this as peer work. Digital-health teams that integrate sensors might.",
    evidence=[
        "Oura sleep product scope and daily observations",
        "Garmin/Polar minimum-observation staging path",
        "Whoop sleep + Withings/Samsung steps and sleep pulls",
        "packages/domain/src/decision/rr/sleep-regularity.ts exists as productized evidence",
    ],
    strengths="You know vendor metrics are not ground truth and you keep units/native meaning.",
    gaps="No raw sensor DSP, no labeled lab protocol, no on-device models.",
    talk="Position as sensor-*integration* algorithms, not sensor-*invention*.",
    bottom="Partial. Stronger as Connected-Device than as Sensor Algorithm Engineer.",
)

role(
    slug="solutions-engineer",
    title="Solutions Engineer",
    score=8.6,
    band="Direct match",
    typical="Turns a platform into a working customer solution: discovery, configuration, integrations, demos, and first-value.",
    did="You sat on the clinic side of the table. TREI is the solution for Bariatric Associates: public site, intakes, Calendly consults, Stripe membership, staff admission, phone programs, wearables, assistant. You implemented the actual customer workflow rather than a generic sandbox.",
    applies="Solutions Engineer interviews want customer context plus the ability to build the last mile. You built the last mile because you were the last mile. Legal pages, Find a provider, roster matching, and handover codes are solutions work.",
    evidence=[
        "trei.care public review, roster, membership, identity APIs",
        "Calendly designated-slot book/cancel/reschedule pass",
        "Staff operating view for the practice",
        "Preparation readiness shared by patient and provider",
    ],
    strengths="You implement, not only slide-deck. You debug the customer's real edge cases.",
    gaps="No multi-customer portfolio. One deep deployment rather than 20 lighter ones. Less formal pre-sales motion.",
    talk="This is FDE-adjacent solutions engineering. Emphasize one customer, production-shaped, healthcare constraints.",
    bottom="Excellent fit, especially where SE is expected to write code.",
)

role(
    slug="solution-architect",
    title="Solution Architect",
    score=6.4,
    band="Adjacent",
    typical="Owns the technical design of a customer or enterprise solution: integration map, NFRs, sign-off, sometimes less hands-on code.",
    did="You operated inside a written architecture (modular monolith, outbox, identity, rings) and added decisions (cloud custody SELECT_MANY, Calendly, Stripe custody). You architected slices. You were not a titled architect signing off a 200-person estate.",
    applies="Some SA roles are senior SEs who can draw the diagram and implement. That is closer. Formal solution-architect jobs that want TOGAF, enterprise integration bus, and stakeholder RACI will see tenure as light.",
    evidence=[
        "docs/ARCHITECTURE.md durable decisions you coded against",
        "Identity across two clients and one API",
        "External vendor map: Stripe, Calendly, Spike, Azure OpenAI, APNs, Entra",
    ],
    strengths="Boundary thinking. You can explain why clients cannot calculate Beacon.",
    gaps="Seniority, multi-account architecture consulting, little non-Azure enterprise estate work.",
    talk="Prefer 'Forward Deployed Engineer / Solution Architect' combined title over pure SA.",
    bottom="Architect-shaped thinking at IC implementation seniority, not Principal SA.",
)

role(
    slug="support-engineer",
    title="Support Engineer",
    score=6.1,
    band="Adjacent",
    typical="Triages customer issues, reproduces bugs, writes runbooks, escalates with logs, sometimes ships fixes.",
    did="You fixed a long tail of user-visible failures: ABA recovery copy, scheduling unavailable still showing saved appointments, Spike outage vs disconnect copy, stale staff membership, checkout retry safety, intake email recovery. That is support-grade debugging with the privilege of changing the code.",
    applies="Support Engineer plus commit access is essentially what you did for an unreleased clinic product. You also wrote operator docs (runbook, Calendly, staging). You did not staff a ticket queue.",
    evidence=[
        "Honest error copy across Plan, Progress, Spike, Calendly",
        "docs/RUNBOOK.md, incident-response skeleton in the repo",
        "Webhook local scripts so failures can be reproduced",
    ],
    strengths="You debug from the user's sentence back to the record.",
    gaps="No Zendesk/Salesforce support metrics, no 24/7 rotation, product still pre-cohort.",
    talk="Good supporting story. Target Support Engineer only if you want a support-primary career; otherwise use FDE/SWE.",
    bottom="You would be a strong L3/L4 support engineer who codes. That is not the most leveraged title for this work.",
)

role(
    slug="field-engineer",
    title="Field Engineer",
    score=6.7,
    band="Adjacent",
    typical="On-site technical work: install, configure, train, fix, sometimes hardware. Healthcare and industrial vendors use this title.",
    did="You are clinic-embedded: the product is for a named practice, with office visits, Teams consults, and staff tools. You implemented handover codes a provider actually uses, not a generic install wizard. You are not racking servers at a hospital IDF.",
    applies="Software field engineer / clinical implementation engineer maps. Hardware field engineer does not.",
    evidence=[
        "Clinic visit attendance recorded by staff, booking never fakes attendance",
        "Handover activation PR work, practice-scoped redeem",
        "Staff workspace for the operating clinic",
    ],
    strengths="Willingness to encode messy real-world clinic process.",
    gaps="No biomedical equipment, no on-site networking, no multi-site rollout history.",
    talk="Prefer FDE or Solutions Engineer. Use Field Engineer if the company is a healthcare device/software vendor with on-site software configuration.",
    bottom="Software field implementation: yes. Classic field engineer: only adjacent.",
)

role(
    slug="software-generalist",
    title="Software Generalist",
    score=9.4,
    band="Direct match",
    typical="Small-team engineer who can do whatever is blocking: UI, API, data, cloud, integrations, docs.",
    did="Your commit subjects jump from legal pages to Stripe to VoiceOver to Calendly races to Spike custody to staff CSS-adjacent layout. That is generalist work at a high correctness bar. The two-person team required it.",
    applies="Startups and FDE teams hire generalists explicitly. TREI is evidence you do not stall when the next problem is in a different layer.",
    evidence=[
        "658 files across every major package and app",
        "Docs, tests, infra, product copy, and integration code in one author history",
    ],
    strengths="Range without becoming sloppy about evidence and auth.",
    gaps="Specialist interviews may say 'unfocused.' Counter with depth in identity, webhooks, and connected health.",
    talk="For generalist postings, this is the first sentence of the resume.",
    bottom="The most accurate informal description of the two-month body of work.",
)

role(
    slug="fintech-software-engineer",
    title="Fintech Software Engineer",
    score=6.5,
    band="Adjacent",
    typical="Software for money movement, accounts, ledgers, compliance, banking/fintech products.",
    did="You built membership billing: Stripe Checkout in sandbox, signed webhooks, checkout intents, subscription binding, invoice normalization across Stripe's evolving objects, cancellation terminality, and no complimentary grants from unpaid invoices. Path A prices are encoded. Production live charges remain unauthorized.",
    applies="Fintech SWE is broader than Stripe Checkout, but payment-state machines, idempotency, and 'never infer a grant from a weird event' are the same muscles. You do not have KYC, card issuing, or ledger products.",
    evidence=[
        "docs/STRIPE-BILLING-EVENT-CUSTODY.md",
        "Website checkout + legal URL routing",
        "Application-package webhook handling; no raw PAN storage",
        "Customer portal / cancellation path in sandbox",
    ],
    strengths="Money-adjacent conservatism. You treated billing as a custody problem.",
    gaps="Not a bank, not PCI SAQ owner, sandbox only, no multi-currency or payouts.",
    talk="Good for fintech teams that need product engineers who respect ledgers. Weak for core-banking.",
    bottom="Adjacent-to-strong payments-product experience inside a health company.",
)

role(
    slug="payments-infrastructure-engineer",
    title="Payments Infrastructure Engineer",
    score=7.0,
    band="Strong",
    typical="Owns payment processing internals: webhooks, reconciliation, idempotency, retries, processor adapters, ledger bindings.",
    did="Stripe work in this repo is infrastructure-shaped even though the product is membership. You persisted intents before calling Stripe, bound session IDs, verified signatures and sandbox flags, rejected connected-account events, serialized with row locks, and made cancellation terminal for a subscription ID.",
    applies="Payments infra interviews are about exactly those properties. You can talk to Stripe's unordered events and dual invoice schemas. You have not built a processor, a money movement network, or a multi-processor router.",
    evidence=[
        "Migration 054-era checkout intents and normalized event facts",
        "Retry of lost Checkout responses without double-creating sessions",
        "Pending_binding vs processed webhook markers",
        "scripts/stripe-recreate-sandbox-fixtures.mjs and local webhook script",
    ],
    strengths="Replay safety and schema evolution (legacy vs parent.subscription_details).",
    gaps="Sandbox-only; no settlement, chargebacks, or PCI controls as a job. Volume is clinic-scale.",
    talk="Lead with event custody, not 'I integrated Stripe Checkout in a weekend.'",
    bottom="Credible junior-to-mid payments infrastructure story. Combine with Fintech SWE.",
)

role(
    slug="networking-engineer",
    title="Networking Engineer",
    score=2.4,
    band="Minimal",
    typical="Routing, switching, firewalls, DNS, load balancing, overlays, packet-level design.",
    did="You used HTTPS, OIDC redirects, associated domains, webhook callbacks, and WebRTC for voice. You did not design VNets, NSGs, BGP, or campus networks. A /go redirect on trei.care is application routing, not network engineering.",
    applies="Application-layer networking literacy only.",
    evidence=["Associated domains and OIDC redirect fixes", "WebRTC voice session", "Host/noindex and Origin header care on Apple code redemption"],
    strengths="You treat Origin, hosts, and callbacks as security-relevant.",
    gaps="The networking profession.",
    talk="Do not apply.",
    bottom="Not a networking engineer from this work.",
)

role(
    slug="security-engineer",
    title="Security Engineer",
    score=6.6,
    band="Adjacent",
    typical="Threat modeling, appsec, identity, secrets, vulnerability management, sometimes detection.",
    did="Security is woven through TREI and through your commits: OIDC verification, public-client Apple redemption, token-free first-cohort contacts, deletion retaining only allowed confirmations, fail-closed Spike lifecycle, webhook signatures, Key Vault, noindex public host, fast-uri host-confusion bump, rate limits on public review, privacy/legal pages. You are not a dedicated red-teamer.",
    applies="AppSec-minded product engineer is the honest label. Security Engineer jobs that want pentest certs, SIEM, or vulnerability research are a stretch. Healthcare data minimization is a plus.",
    evidence=[
        "OIDC issuer/audience/expiry/signature/scope checks in architecture you coded against",
        "Stripe/Calendly/Spike signature fail-closed",
        "Account deletion boundary and identity removal tests",
        "Public site isolation and unindexed host rules",
        "Aba session: no patient record, no secrets in logs",
    ],
    strengths="Threat models encoded as tests. Least privilege between platform admin and clinical access.",
    gaps="No security team role, no pentest ownership, no detection engineering, HIPAA program not yours alone.",
    talk="Apply to product-security-adjacent SWE or healthcare appsec if they want builders. For pure Security Engineer, this is supporting evidence.",
    bottom="Strong secure-by-construction SWE. Medium dedicated Security Engineer.",
)

role(
    slug="forward-deployed-engineer",
    title="Forward Deployed Engineer (FDE)",
    score=9.2,
    band="Direct match",
    typical="Palantir-origin role: embed with a customer, learn their operation, write production software that makes the platform work there, and carry insight back to product.",
    did="This is the job you have been doing. The customer is Bariatric Associates. The operational problem is GLP-1 / metabolic care: identity, preparation, consults, membership, staff admission, daily programs, wearables, assistant. You did not wait for a perfect platform team; you implemented the clinic's path in the platform.",
    applies="FDE interviews look for: technical range, comfort with messy workflows, writing as well as coding, and judgment about what must be true vs what can wait. TREI's rings, deferred Path B, gated Garmin, and hidden Healthspan are FDE judgment. Calendly and Stripe are last-mile integrations FDEs always hit.",
    evidence=[
        "Embedded in a named clinic's product, not a generic B2C sandbox",
        "End-to-end Path A workflow including staff and patient sides",
        "Decision records and canon pins instead of shadow IT scripts",
        "Willingness to change code when the office visit, handover, or intake reality disagreed with the first design",
    ],
    strengths="Builder-in-the-clinic. You keep software honest to operations.",
    gaps="One customer. No travel-heavy multi-deployment portfolio. Production cohort still closed, so 'deployed' is staging/TestFlight-true, not nationwide-live.",
    talk="Say the quiet part: I am an FDE who also is the product engineering team. Then pick one operational loop and its failure modes.",
    bottom="Primary target title. This project's best specialized match.",
)

role(
    slug="associate-forward-deployed-engineer",
    title="Associate Forward Deployed Engineer",
    score=9.5,
    band="Direct match",
    typical="Early-career FDE: ships under a lead, learns the customer domain fast, implements scoped deployments, writes tests and docs.",
    did="Two months of clinic-embedded delivery at this intensity is exactly Associate FDE, except you had unusually high ownership because the team is tiny. You still show the associate pattern: tight review loops, many correctness follow-ups, growing from Spike adapter to full TREI slices.",
    applies="Associate FDE is the title you can take tomorrow without overreaching seniority. The work already includes customer workflow, integrations, and product judgment.",
    evidence=[
        "July Spike adapter → August TREI surfaces → September Calendly/Stripe/identity → September connected-health multi-source",
        "Repeated review-driven fixes (Bugbot, types, races) that FDEs are expected to absorb",
    ],
    strengths="Ramp speed. Domain absorption (GLP-1 programs, intakes, wearables).",
    gaps="None material for Associate. Do not let companies under-level you into an intern story; the code is production-shaped.",
    talk="If a company has Associate FDE, apply there first. You are a high outlier for the level.",
    bottom="Highest-confidence title match in the list.",
)

role(
    slug="senior-forward-deployed-engineer",
    title="Senior Forward Deployed Engineer",
    score=7.3,
    band="Strong",
    typical="Leads a deployment, unblocks others, negotiates scope with customer executives, owns outcomes not just tickets.",
    did="On a two-person engineering effort you functioned as a senior IC: you owned slices, wrote decisions, and finished integrations the clinic cannot launch without. You did not manage other FDEs or a book of multiple customers.",
    applies="Some startups will hire you as Senior FDE based on ownership. Palantir-like machines usually reserve Senior for people who have run deployments and mentored associates. Be honest about team size.",
    evidence=[
        "Ownership of public site + identity + billing + scheduling + connected health slices",
        "Cross-surface agreement tests (TREI-06/07/09)",
    ],
    strengths="Outcome ownership. You do not stop at a demo.",
    gaps="No evidence of leading other engineers; production cohort unopened; single customer.",
    talk="Apply Senior where the company is small. At large FDE orgs, Associate/FDE is the safer honest level; let them uplevel you.",
    bottom="Senior-shaped ownership, associate-shaped organizational proof.",
)

role(
    slug="staff-forward-deployed-engineer",
    title="Staff Forward Deployed Engineer",
    score=5.0,
    band="Partial",
    typical="Multi-deployment technical strategy, plays, reusable assets, influence across customers and core product.",
    did="You helped set patterns (server-owned projections, custody contracts, fail-closed vendors) that *could* become plays. You have not reused them across many customers or set org-wide FDE strategy.",
    applies="Staff is a leverage title. One deep clinic build is necessary but not sufficient.",
    evidence=["Reusable platform spine and written architecture", "Single-tenant clinic focus"],
    strengths="You think in boundaries that scale to more clinics later.",
    gaps="Staff-level scope, communication to execs at multiple accounts, playbooks used by other FDEs.",
    talk="Do not apply to Staff FDE as a first FDE role. Mention the patterns as growth trajectory.",
    bottom="Too senior as a target. Use as a north star, not a current claim.",
)

role(
    slug="lead-forward-deployed-engineer",
    title="Lead Forward Deployed Engineer",
    score=5.4,
    band="Partial",
    typical="People/delivery lead of an FDE pod: staffing, customer relationship, technical direction.",
    did="You led workstreams by doing them. There is no pod, no reports, no delivery manager split. Andrei is a co-builder and clinical/product counterpart, not your report.",
    applies="Lead titles require leading humans. Tiny-team 'I led the website' is workstream lead, not people lead.",
    evidence=["Workstream ownership (trellis-web, Calendly, connected health)", "No team-lead evidence"],
    strengths="You can run a workstream without waiting.",
    gaps="People leadership, multi-person delivery, customer exec cadence as a named lead.",
    talk="Skip Lead unless the company uses Lead to mean senior IC. Clarify in the first sentence.",
    bottom="Not a current match. Associate/FDE/Senior-IC is more honest.",
)

role(
    slug="forward-deployed-ai-engineer",
    title="Forward Deployed AI Engineer",
    score=8.2,
    band="Strong",
    typical="FDE whose deployments center on putting AI into a customer's workflow with guardrails, evals, and change management.",
    did="You deployed Aba into the same clinic product as programs and records, with policy that matches care reality: no dosing advice, shared text/voice path, cost/rate limits, and no model access to the chart. That is FD-AI: the model is in the workflow, not a side demo.",
    applies="Companies hiring FD AI Engineers want people who can sit with operators and still write the gateway. You have the clinic seat and the gateway.",
    evidence=[
        "Aba in the patient app used by the same identity as clinical programs",
        "Guarded generation + voice renderer split",
        "Product language and medical-claim refusal",
    ],
    strengths="You will not 'just enable GPT' on PHI.",
    gaps="Not an AI-only FDE: much of your volume is non-AI workflow, which is actually what makes the AI safe. Limited eval operations.",
    talk="Sell the combination: I can ship the workflow *and* the bounded assistant.",
    bottom="Excellent target where the FDE role is AI-flavored but still full-stack.",
)

role(
    slug="founding-ai-forward-deployed-engineer",
    title="Founding AI Forward Deployed Engineer",
    score=8.1,
    band="Strong",
    typical="First FDE at an AI startup: invents the deployment motion, wears product/eng/customer hats, high ambiguity.",
    did="TREI is a founding-stage product (pilot target 1–2k, production dark, two engineers). You helped invent the motion: canon in ABAEMR, implementation in BariAccess, staging clinic workflows, AI as one gated capability among many.",
    applies="Founding FDEs are generalists who can sell/build/deploy. You built/deployed. Commercial founding (pricing experiments, many logos) is thinner, though you did encode Path A prices and legal pages.",
    evidence=[
        "Greenfield-to-staging arc in two months",
        "Public brand trei.care, legal, identity, payments, AI, wearables",
        "Comfort with unset canon: pause only the dependent behavior",
    ],
    strengths="Ambiguity tolerance. You ship behind gates instead of waiting for perfect policy.",
    gaps="Not a company founder on paper. Equity/founding narrative should stay factual: founding *engineer on the product*, not founder of the clinic.",
    talk="Use for AI startups that need their first clinic/customer engineer.",
    bottom="Strong match for early AI-health or AI-ops startups.",
)

role(
    slug="forward-deployed-engineer-ai-enablement",
    title="Forward Deployed Engineer, AI Enablement",
    score=7.7,
    band="Strong",
    typical="Helps a customer actually use AI: use-case selection, guardrails, knowledge, training, and platform configuration.",
    did="You enabled a clinic to have an assistant without enabling it to hallucinate care. Enablement here is encoded in software (routes, retention, disclosure) more than in workshops. You also enabled connected-health and staff tools that are the non-AI prerequisites for useful AI context later.",
    applies="AI enablement FDEs who only run workshops are a weaker match. Teams that mean 'enablement by building the rails' are a strong match.",
    evidence=[
        "Policy in domain code, not a slide",
        "Start fresh, pause, restricted conversation as user-facing enablement controls",
        "Context admission rules so Programs can be mentioned without dumping the chart",
    ],
    strengths="Enablement as engineering. Durable rails.",
    gaps="Less change-management / training-program evidence. No multi-team AI rollout inside a large enterprise.",
    talk="Define enablement as 'I made AI usable and unusable in the right places.'",
    bottom="Strong if the job is technical enablement. Medium if it is adoption consulting without code.",
)

role(
    slug="forward-deployed-engineer-solution-architect",
    title="Forward Deployed Engineer / Solution Architect",
    score=8.3,
    band="Strong",
    typical="Hybrid: embeds like an FDE, designs the solution like an SA, often writes the reference implementation.",
    did="You drew (and coded) the solution: three surfaces, one API, worker, Postgres authority, vendor adapters. You mapped clinic objects (Programs, FABs, Bookends, membership, consults) onto that shape. That is FDE/SA hybrid work.",
    applies="This combined title is more honest than pure Solution Architect. You architected by implementing the reference customer.",
    evidence=[
        "System map: trei.care, iPhone, staff, API, worker, vendors",
        "Functional rings as a delivery architecture you built inside",
        "Vendor boundaries: Stripe, Calendly, Spike, Azure OpenAI",
    ],
    strengths="Diagrams that compile. You do not throw designs over a wall.",
    gaps="Formal architecture governance and multi-customer reference architectures.",
    talk="This is a top-three title to put on applications along with Full-Stack and FDE.",
    bottom="Highly aligned hybrid title.",
)

role(
    slug="principal-software-solutions-engineer-forward-deployed",
    title="Principal Software Solutions Engineer / Forward Deployed",
    score=5.2,
    band="Partial",
    typical="Principal IC: sets solution strategy, unblocks the hardest accounts, represents the company technically to executives.",
    did="You solved hard slices (billing custody, identity, multi-source wearables) for the first account. Principal implies a track record of doing that repeatedly and setting the method for others.",
    applies="The *work* has principal-flavored difficulty in places. The *level* does not.",
    evidence=["Hard integration problems on the first clinic", "No principal-level org impact"],
    strengths="You already touch problems principals care about (authority, money, PHI, vendors).",
    gaps="Years, repetition, executive presence, company-wide solution standards.",
    talk="Do not apply to Principal. Use the problems as stories inside FDE/SWE II interviews.",
    bottom="Wrong level. Keep the stories, drop the title.",
)

role(
    slug="lead-forward-deployed-engineer-hospitality",
    title="Lead Forward Deployed Engineer, Hospitality",
    score=6.2,
    band="Adjacent",
    typical="FDE lead for hotels/restaurants/venues: guest journey, bookings, staff ops, payments, on-property exceptions.",
    did="You have not worked in hospitality. You have worked an analog: guest→patient onboarding, booking (Calendly/Teams), front-desk-like staff tools, membership payments, identity across web and phone, and 'the office visit still happens in the real world.'",
    applies="Hospitality FDE cares about real-world operations that software must not lie about. TREI never records attendance from a booking, which is the same honesty a hotel PMS needs (reservation ≠ in-house). Lead/hospitality domain knowledge is still missing.",
    evidence=[
        "Booking vs attendance split",
        "Staff operating console",
        "Membership and public site as the 'guest' acquisition surface",
        "Time-zone and delayed-event honesty",
    ],
    strengths="Operations-aware software. Payments + booking + staff.",
    gaps="Hospitality domain, property multi-site, POS, CRS/PMS vendors, people-lead.",
    talk="If you apply, say: I have not worked hotels; I have shipped a clinic analog of guest journey + staff ops + payments. Do not claim hospitality.",
    bottom="Transferable operations FDE skills. Domain and Lead level are stretches. Better as FDE (health) unless you want to switch industries.",
)

role(
    slug="forward-deployed-engineer-ai-agentic-sdlc",
    title="Forward Deployed Engineer, AI & Agentic SDLC",
    score=6.4,
    band="Adjacent",
    typical="Deploys AI into the software-delivery lifecycle: coding agents, evals on repos, PR automation, enterprise SDLC controls.",
    did="You used AI tools while building TREI (this environment, review bots like Bugbot). You also built a product assistant. You did not build an agentic SDLC platform (autonomous PR agents, org-wide coding evals, SDLC policy engines).",
    applies="Two partial maps: (1) you know how to keep generated code behind tests and canon; (2) you know how to keep generated *product* language behind gates. The job itself is about changing how teams write software.",
    evidence=[
        "CI and tests as the only merge path",
        "Canon pin required before product behavior",
        "Bugbot finding closures in identity and Ring work",
        "Aba as product AI, not as a coding agent",
    ],
    strengths="You will not let an agent merge medical claims or skip proof.",
    gaps="No agent-orchestration product, no enterprise SDLC deployment, no coding-eval harness as a deliverable.",
    talk="Apply only if the company wants FDEs who have shipped guarded AI and live in a high-discipline repo. Otherwise prefer FD AI Engineer.",
    bottom="Adjacent. Your AI product + engineering discipline is the transfer; agentic SDLC is not what you built.",
)

role(
    slug="forward-deployed-engineer-clearance-required",
    title="Forward Deployed Engineer — Clearance Required",
    score=4.3,
    band="Partial",
    typical="FDE on classified or controlled-unclassified government work. Requires existing or obtainable US clearance, often FedRAMP/IL4+ practices.",
    did="You handled sensitive health data patterns (consent, erasure, least privilege, no PHI in telemetry, Key Vault, separate environments). You do not have, and this project does not show, a security clearance, govcloud, or ITAR/CUI workflow.",
    applies="Clearance jobs need eligibility and often prior cleared work. Healthcare sensitivity is a character reference, not a clearance. Do not imply you are cleared.",
    evidence=[
        "PHI-minimizing telemetry and session rules",
        "Environment separation, managed identity",
        "No clearance, no gov tenant, no DISA STIG evidence",
    ],
    strengths="You already work as if over-sharing is a product bug.",
    gaps="Clearance status, government customer, classified SDLC, US-person documentation not in this repo.",
    talk="Only apply if you are actually eligible and willing to be cleared. Sell healthcare data handling as adjacent discipline, never as a substitute for clearance.",
    bottom="FDE skills transfer; clearance requirement is unmet by this project. Do not lead with this title.",
)


def band_for(score: float) -> str:
    if score >= 8.5:
        return "Direct match"
    if score >= 7.0:
        return "Strong"
    if score >= 5.5:
        return "Adjacent"
    if score >= 4.0:
        return "Partial"
    if score >= 2.5:
        return "Thin"
    return "Minimal"


def render_role(r: dict) -> str:
    score = float(r["score"])
    evidence = "\n".join(f"- {item}" for item in r["evidence"])
    return f"""# {r["title"]}

**Project-experience rating: {score:.1f} / 10** ({r["band"]})

{SCALE}

{PROJECT}

## What this role typically owns

{r["typical"]}

## What you did on TREI that maps here

{r["did"]}

## How that experience applies to this job

{r["applies"]}

## Evidence from this repository

{evidence}

## Strengths you can claim honestly

{r["strengths"]}

## Gaps a hiring manager will still probe

{r["gaps"]}

## How to talk about it

{r["talk"]}

## Bottom line

{r["bottom"]}
"""


def render_overview() -> str:
    rows = sorted(ROLES, key=lambda r: (-float(r["score"]), r["title"]))
    table = ["| Rating | Title | Band | One-line verdict |", "| ---: | --- | --- | --- |"]
    for r in rows:
        verdict = r["bottom"].split(".")[0].strip()
        table.append(
            f"| {float(r['score']):.1f} | [{r['title']}]({r['slug']}.md) | {r['band']} | {verdict}. |"
        )

    by_band: dict[str, list[str]] = {}
    for r in rows:
        by_band.setdefault(r["band"], []).append(f"- **{r['title']}** ({float(r['score']):.1f}) — {r['bottom']}")

    band_order = ["Direct match", "Strong", "Adjacent", "Partial", "Thin", "Minimal"]
    band_sections = []
    for b in band_order:
        items = by_band.get(b)
        if not items:
            continue
        band_sections.append(f"### {b}\n\n" + "\n".join(items))

    return f"""# TREI / BariAccess job-title experience overview

Author: Zakiy Manigo  
Evidence window: 17 July 2026 – 16 September 2026  
Repository: BariAccess (product name TREI)  
Co-author context: Andrei remains the other primary engineer and has larger commit/line volume, especially in domain engines and production-estate work. These ratings describe **your** mapped experience from this project, not exclusive ownership of every subsystem.

This folder contains one document per requested job title plus this overview. Each role document explains what you actually built, how it applies to that title, what to claim, and what to stop short of claiming.

{SCALE}

{PROJECT}

## Headline recommendation

If you can only put three titles on applications, use:

1. **Associate Forward Deployed Engineer** or **Forward Deployed Engineer**
2. **Full-Stack Engineer** / **Product Engineer**
3. **Software Engineer I** (or **SWE II / SDE I** depending on the company's leveling)

Your rare combination is clinic-embedded delivery plus real TypeScript systems work: identity, payments custody, scheduling races, wearable cloud custody, and a guarded voice/text assistant.

Do not lead with Firmware, Networking, native Android, or Principal/Staff titles from this project alone.

## Contribution snapshot used for every rating

| Fact | Number |
| --- | --- |
| Your commits (all Zakiy author strings) | ~203 |
| Lines added / deleted (ts/tsx/bicep/md/yml/json approx) | ~99,400 / ~17,400 |
| Unique files touched | 658 |
| Heaviest app surfaces | trellis-web (trei.care), patient-mobile, staff-web, API, packages/data, packages/application |
| Product posture | Wellness-first GLP-1 / metabolic care for Bariatric Associates |
| Environments | Local + Azure staging live; production dark; iOS TestFlight-oriented |
| Team shape | Two primary engineers, clinic-in-the-loop, canon in ABAEMR |

## Ratings, highest first

{chr(10).join(table)}

## Findings by band

{chr(10).join(band_sections)}

## How the work clusters (use this in resumes)

### Clinic-embedded product (FDE / Product / Solutions)

Path A onboarding, intakes and confirmations, Calendly remotes, handover codes, staff operating view, Free Basic vs clinic chrome, product language, legal/public site. This is why FDE scores sit at the top.

### Full-stack TypeScript product

One identity across trei.care and the iPhone app, server-owned Today/Plan/Progress, staff console, Fastify use cases, PostgreSQL migrations, tests in CI.

### Integrations and custody

Stripe membership sandbox, Calendly webhook ordering, Spike wearable adapters (Oura first; Garmin/Polar gated; Whoop/Withings/Samsung SELECT_MANY), erasure and disconnect honesty.

### Guarded AI

Aba typed + voice conversation. Model is not the record. Realtime speaks checked text. Medical-claim and emergency routing live in domain code.

### Cloud and mobile delivery

Azure Container Apps / Bicep / GitHub Actions, External ID + Entra, EAS/TestFlight iOS, Apple public-client OIDC. Android is declared, not shipped.

## Honest limits that affect every senior title

- Calendar time is about two months of extreme throughput, not two years of on-call.
- Production patient cohort is not open; staging and TestFlight carry the live-shaped proof.
- You were not a people lead, staff+ principal, or multi-customer deployer.
- Native Swift/Kotlin, firmware, networking engineering, ML training, and search stacks were not the job.

## Suggested resume bullets (true to this repo)

- Built TREI, a clinic-embedded GLP-1 patient and staff platform, as one of two primary engineers: public site, iPhone app, staff console, Fastify API, and PostgreSQL.
- Shipped shared Apple/Google/email identity across trei.care and the TREI app, with server admission, handover codes, and fail-closed OIDC.
- Implemented Stripe sandbox membership custody (signed webhooks, checkout intents, unordered-event membership state) and Calendly remote consults with create/cancel/reschedule races.
- Integrated connected-health providers through Spike (Oura plus cloud providers), including connect/disconnect/erase and a unified patient/staff source shelf.
- Shipped Aba, a guarded text/voice assistant on Azure OpenAI Realtime that cannot read the chart or become the clinical record.

## Folder index

Each file is a standalone briefing you can paste from:

{chr(10).join(f"- [{r['title']}]({r['slug']}.md) — {float(r['score']):.1f}/10" for r in rows)}
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    slugs = set()
    for r in ROLES:
        if r["slug"] in slugs:
            raise SystemExit(f"duplicate slug {r['slug']}")
        slugs.add(r["slug"])
        expected = band_for(float(r["score"]))
        if r["band"] != expected:
            raise SystemExit(f"{r['title']}: band {r['band']!r} != {expected!r} for {r['score']}")
        (OUT / f"{r['slug']}.md").write_text(render_role(r), encoding="utf-8")
    (OUT / "00-OVERVIEW.md").write_text(render_overview(), encoding="utf-8")
    print(f"wrote {len(ROLES)} role docs + overview to {OUT}")


if __name__ == "__main__":
    main()
