#!/usr/bin/env python3
"""Generate per-role experience briefs from Local AI project evidence."""

from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parent

PROJECT = """
**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.
""".strip()

SCALE = """
Ratings are **0–10 for this repository only**, not a full career score.

| Score | Meaning |
| --- | --- |
| 9–10 | This project is a primary hiring signal for the role |
| 7–8 | Strong transferable evidence; interviewable as I/II on this stack |
| 5–6 | Partial overlap; you can tell a credible story with gaps named |
| 3–4 | Adjacent skills only |
| 0–2 | Essentially no evidence from this work |
""".strip()

ROLES: list[dict] = []


def add(
    slug: str,
    title: str,
    score: float,
    level: str,
    typical: str,
    done: str,
    apply: str,
    gaps: str,
    talk: str,
) -> None:
    ROLES.append(
        {
            "slug": slug,
            "title": title,
            "score": score,
            "level": level,
            "typical": typical.strip(),
            "done": done.strip(),
            "apply": apply.strip(),
            "gaps": gaps.strip(),
            "talk": talk.strip(),
        }
    )


add(
    "software-engineer",
    "Software Engineer",
    8.0,
    "Strong — general SWE I/early II from one product",
    """Owns features end to end: design, implementation, tests, and shipping. Comfortable across languages, debugging, and product constraints.""",
    """You built a full desktop application, not a tutorial: typed IPC from React to Rust, process lifecycle for llama-cli, SQLite persistence, streaming UI, packaging, and documented security/testing. You handled real failure modes (WDAC blocking cargo, unsigned SmartScreen, RAG query bugs recorded as MAN26/27).""",
    """Interview as someone who can take a vague product (“offline chat”) and turn it into modules, tests, and an installer. Emphasize ownership of the whole loop: UI, backend, storage, native runtime, and QA.""",
    """No multi-service production, no large team process, no on-call. SWE interviews will still probe algorithms, system design at web scale, and languages you did not use here.""",
    """“I shipped a Windows desktop AI client with a Rust native layer, a React UI, SQLite, and a real installer — including streaming inference and fail-closed file/tool security.”""",
)

add(
    "software-engineer-i",
    "Software Engineer I",
    8.5,
    "Very strong for SWE I",
    """Entry / first full-time engineering bar: ship well-scoped features, write tests, take review, debug with help, learn the codebase.""",
    """Scope matches a strong intern-to-SWE-I portfolio: feature slices (chat reducer, model catalog, onboarding, documents), unit tests (Vitest + Cargo fixtures), error mapping to user strings, and a manual install matrix. Code shows patterns (state machine for generation, exhaustive TS switches).""",
    """This repo is enough to claim you have already done “new grad / SWE I” work: tickets that span UI and native, tests that fail closed, and docs that another engineer could follow.""",
    """SWE I jobs still expect internships or class projects in other stacks. This is one product; mention it as the flagship, not the only story if you have more.""",
    """Lead with Local AI as the project that proves you can ship a complete app, then map each interview question to a file (inference state machine, path canonicalization, chat reducer).""",
)

add(
    "software-engineer-ii",
    "Software Engineer II / SWE II",
    7.0,
    "Credible early SWE II; thin on scale",
    """Independent execution on ambiguous problems, design reviews, reliability, mentoring sometimes, production impact beyond a single feature.""",
    """You made architectural calls: Stage A child-process inference vs Stage B native stub; ChatML/Llama3/Mistral templates in Rust not React; GPU backend selection; portable vs APPDATA paths; capability-locked Tauri webview. You documented tradeoffs and left native linking unclaimed until it actually works.""",
    """Use this for “tell me about a design decision” and “how do you test native + UI.” SWE II interviewers care that you chose fail-closed security and did not pretend Stage B was done.""",
    """Typical SWE II bars include production SLOs, distributed systems, or multi-quarter ownership on a team codebase. This is a solo desktop MVP. Score is for transferable craft, not title inflation.""",
    """Do not oversell as Staff. Position as: I independently designed and shipped a constrained systems+product problem (local inference + UX + installer).""",
)

add(
    "sde-i",
    "Software Development Engineer I (SDE I)",
    8.5,
    "Very strong for SDE I",
    """Amazon-style SDE I: coding, testing, ownership of well-defined components, operational awareness at small scale.""",
    """You owned components with clear contracts: `InferenceEngine` trait, Tauri commands, SQLite schema, argv pin tests against llama.cpp b10488, gated INT01–INT05 when `LOCALAI_TEST_MODEL` is unset (skip not fail).""",
    """SDE I loops want working software + tests. You have both layers plus Windows packaging — closer to “shipped” than a typical class project.""",
    """Little evidence of Amazon-style operational metrics, code reviews with a team, or large existing services.""",
    """Map LP-style stories to: customer (offline privacy), dive deep (stdout parser + token metrics), insist on highest standards (unsigned installer documented, RAG failures recorded as fail).""",
)

add(
    "sde-ii",
    "Software Development Engineer II (SDE II)",
    7.0,
    "Partial SDE II — design yes, org scale no",
    """SDE II: designs medium systems, delivers across sprints, handles production issues, influences adjacent teams.""",
    """Medium-system design is present: process isolation of the model runtime, context budget via tokenize-or-heuristic, RAG ingest hashes, tool allowlists. You ran a real install/uninstall/reinstall data-preservation matrix.""",
    """Good for “design a local inference client” or “how would you isolate untrusted model output.” Weaker for “design an order service.”""",
    """No AWS service ownership, no high-QPS backends, no formal on-call. Treat SDE II as a stretch supported by this project plus other experience.""",
    """In system design, start from threat model and process boundary (webview vs Rust vs llama-cli), then storage and packaging — that is your authentic SDE II story.""",
)

add(
    "application-developer",
    "Application Developer",
    9.0,
    "Primary match",
    """Build user-facing applications: UI, local state, persistence, install/update, Windows desktop conventions.""",
    """This is an application: window chrome, sidebar, chat, models, documents, settings, F1 help, Ctrl+K palette, first-run wizard, NSIS current-user install, Start menu shortcut, portable flag, theme system, markdown rendering with sanitization.""",
    """Application developer interviews should be mostly this repo. You can walk a screen-by-screen demo and the IPC behind each button.""",
    """Not a line-of-business CRUD app (no enterprise auth, no SAP/Office add-ins). If the posting is “internal IT apps,” map via SQLite + settings, not via ERP.""",
    """Demo the installed `local-ai.exe` path, not only `npm run tauri dev` — you already proved MAN01–MAN38 on the installer.""",
)

add(
    "full-stack-engineer",
    "Full-Stack Engineer",
    8.5,
    "Strong (desktop full stack, not typical web SaaS)",
    """UI + API/backend + data. Often TypeScript/React plus a server and a database.""",
    """Frontend: React 19, Vite, feature folders, reducers, Vitest. “Backend”: Rust Tauri commands, SQLite, filesystem, child processes. Shared types via serde JSON across the IPC boundary.""",
    """Full-stack postings that mean “React + Node + Postgres” still buy this story if you say: the native layer is the API; SQLite is the DB; events are the realtime channel. You did both sides with tests.""",
    """No REST/GraphQL public API, no auth, no cloud deploy, no CSS framework at scale. Browser-only full-stack jobs will probe Next.js/SSR you did not use.""",
    """Phrase it as full-stack **desktop**: React presentation, Rust domain, SQLite persistence, OS integration.""",
)

add(
    "backend-engineer",
    "Backend Engineer",
    8.0,
    "Strong for native/backend; not HTTP services",
    """Services, APIs, data stores, concurrency, reliability, auth, queues.""",
    """Rust domain: command handlers, mutex app state, generation state machine, child process stdout parse, cancel via AtomicBool, DB conversations/models/documents/settings, path security, tool execution, RAG chunking/embeddings subprocess.""",
    """Backend interviews that allow “systems backend” or “native services” map cleanly. Talk mutex + process lifecycle + SQLite transactions, not Express routes.""",
    """No networked service, no authn/z, no Kafka, no Postgres ops, no load balancing. Classic “backend engineer at a web company” is a partial fit.""",
    """Lead with process isolation and fail-closed path checks; those are backend instincts applied to a local host.""",
)

add(
    "frontend-engineer",
    "Frontend Engineer",
    7.5,
    "Solid product UI; not a design-system specialist",
    """Component architecture, accessibility, performance, state, CSS, design collaboration.""",
    """You built ChatView, Models, Documents, Settings, onboarding, overlays, status bar, markdown+code blocks, theme prefs, UI templates, hardware guide copy, command palette. Tests cover reducers, routing heuristics, prefs, conversation markdown export.""",
    """Frontend interviews can use chat streaming state (`chatReducer`) and offline-first constraints (no CDN fonts, CSP, `check-offline-assets`).""",
    """Single desktop webview, not responsive web marketing, not React Native, limited a11y audit evidence. No Storybook/design-system ownership.""",
    """Bring the streaming + stop/regenerate UX and the first-run privacy wizard as the frontend craft samples.""",
)

add(
    "mobile-engineer",
    "Mobile Engineer",
    2.0,
    "Almost no evidence",
    """iOS/Android (or RN/Flutter) apps, stores, device APIs, offline mobile, push.""",
    """Tauri has a `#[cfg_attr(mobile, tauri::mobile_entry_point)]` attribute and .icns icons exist, but the product is Windows x64 NSIS. No mobile UI, no store listing, no device sensors.""",
    """Only transferable bits: offline-first mindset, SQLite, constrained capabilities. That is not mobile engineering.""",
    """No Swift/Kotlin/Flutter app, no TestFlight/Play, no mobile lifecycle.""",
    """Do not list this project as mobile experience. Mention desktop native if asked about “client apps.”""",
)

add(
    "ios-engineer",
    "iOS Engineer",
    1.0,
    "No evidence",
    """Swift/SwiftUI/UIKit, Apple platforms, App Store, Human Interface Guidelines.""",
    """An `.icns` icon is bundled for the Tauri config. There is no iOS target, no Xcode project, no Swift.""",
    """Does not apply. Privacy-offline product thinking does not substitute for UIKit.""",
    """Entire iOS stack missing.""",
    """Skip this title unless you have other iOS work.""",
)

add(
    "android-engineer",
    "Android Engineer",
    1.0,
    "No evidence",
    """Kotlin, Jetpack, Play Store, Android OS integration.""",
    """Windows-only shipping path. No Android Gradle module, no Kotlin.""",
    """Does not apply.""",
    """Entire Android stack missing.""",
    """Skip.""",
)

add(
    "product-engineer",
    "Product Engineer",
    8.5,
    "Primary match",
    """Engineers who shape the product: UX, copy, onboarding, tradeoffs, shipping what users can complete without a developer machine.""",
    """You wrote user-facing flows (privacy → this PC → models folder), hardware size labels (Recommended / May Be Slow / Likely Too Large), Help/What’s New, presets (Battery/Balanced/Maximum), “app never downloads weights,” uninstall keeps models. Manual QA is product QA.""",
    """Product-engineer interviews want “I noticed users would fail here and I designed around it.” Examples: confirm large models, embedding GGUF cannot chat, Fully Offline default on.""",
    """No user research program, no analytics funnel (by design: no telemetry). Collaboration with a PM/designer is not evidenced in-repo.""",
    """Tell the story as: privacy and hardware constraints *are* the product; engineering encoded them as defaults and wizards.""",
)

add(
    "ai-product-engineer",
    "AI Product Engineer",
    9.0,
    "Primary match",
    """Ships AI into a product: model selection, prompts, eval-ish tests, UX for latency/failure, RAG, tools, not just a notebook.""",
    """GGUF catalog + roles, auto/multi model routing heuristics, ChatML/Llama3/Mistral templates, Qwen3 `/no_think` vs thinking, context meter, tok/s, RAG ingest + citations (attempted; MAN26/27 failed), JSON tool calls (read/search; delete/shell gated), embedding model distinct from chat model.""",
    """This is the job: local LLM product. You can discuss prompt budget, template mismatch, embedding vs generative models, and why the app never fetches weights.""",
    """No hosted LLM ops, no eval harness with golden datasets at scale, RAG retrieval still broken in the recorded manual run.""",
    """Lead with “I productized local inference,” then be honest that document-chat citations failed MAN26/27 — that honesty is AI-product maturity.""",
)

add(
    "platform-engineer",
    "Platform Engineer",
    5.0,
    "Partial — app platform, not org platform",
    """Internal platforms: CI, golden paths, multi-tenant infra, developer self-service, SLOs.""",
    """You built a small *application* platform: runtime folders for CPU/Vulkan/CUDA/embed llama binaries, argv pin, bootstrap_runtime, capability JSON, portable layout. That is embedding a runtime, not running a company platform.""",
    """Talk about “platform” only as “we pin and bundle an inference runtime so the UI stays a client.” Do not claim Kubernetes platform engineering.""",
    """No IDP, no Terraform org, no CI golden pipelines for many teams.""",
    """If the posting is “developer platform for 200 engineers,” this project is a weak match. If it is “own the runtime under the product,” it is a start.""",
)

add(
    "infrastructure-engineer",
    "Infrastructure Engineer",
    4.0,
    "Adjacent OS/runtime packaging only",
    """Servers, networks, OS images, capacity, monitoring, backups.""",
    """Windows paths, APPDATA vs portable USB, NSIS, discovering llama-cli, CUDA via nvcuda/CUDA_PATH/nvidia-smi, WDAC notes. Child process lifecycle/kill tree.""",
    """Useful anecdotes for “how does this run on a PC,” not for datacenter infra.""",
    """No Linux fleet, no IaC, no observability stack, no capacity planning beyond RAM fudge 1.3.""",
    """Use as supporting color on Windows desktop packaging, not as infra experience.""",
)

add(
    "cloud-engineer",
    "Cloud Engineer",
    2.0,
    "No cloud delivery",
    """AWS/Azure/GCP services, IAM, networking, containers, cost.""",
    """The product is anti-cloud by design: Fully Offline, no telemetry, no HTTP inference client. Hugging Face links are copy-paste for humans; the app does not fetch.""",
    """The only cloud-adjacent skill is knowing what *not* to put on the network (CSP, no opener plugin). That is security/product, not cloud engineering.""",
    """No cloud accounts, no Terraform, no EKS.""",
    """Do not apply this project to Cloud Engineer roles except as “I can build air-gapped clients.”""",
)

add(
    "developer-platform-engineer",
    "Developer Platform Engineer",
    4.0,
    "Weak — one product’s DX, not a platform org",
    """Paved roads: templates, CI, inner-loop, golden repos, self-service infra.""",
    """In-repo DX: DEVELOPMENT.md, fetch-llama-cli.ps1, check-offline-assets, Vitest/Cargo, rustfmt, eslint, gated tests that skip without a model. That is good repo hygiene, not a developer platform.""",
    """You can speak to making a native+JS repo bootable and testable. That is a slice of DX.""",
    """No internal marketplace, no multi-repo CI, no service catalog.""",
    """Mention as “I care about the inner loop,” then move to product engineering.""",
)

add(
    "developer-tools-engineer",
    "Developer Tools Engineer",
    5.0,
    "Partial — tools inside an AI coding-adjacent app",
    """Compilers, IDEs, CLI tools, debuggers, build systems used by other engineers.""",
    """Command palette, prompt library, code blocks, auto-route “Coder” models, local tools (read_file/search_docs), markdown export of chats. llama-cli argv construction is a tool wrapper. Not an IDE.""",
    """Closest if the tools team builds **AI coding assistants** or **CLI wrappers**. You wrapped llama.cpp and parsed stdout/banners/tokens.""",
    """You did not build a compiler, LSP, or editor. No plugin ecosystem.""",
    """Pitch as “I integrated an inference CLI into a desktop tool with structured agent tools,” not “I work on LLVM.”""",
)

add(
    "embedded-software-engineer",
    "Embedded Software Engineer",
    2.0,
    "No embedded targets",
    """MCUs, RTOS, bare metal, constrained memory, peripherals, C.""",
    """You care about RAM/VRAM vs GGUF size and CPU thread defaults. That is desktop resource heuristics, not embedded.""",
    """Does not apply beyond “I think about memory budgets.”""",
    """No firmware, no HAL, no device trees.""",
    """Skip for embedded postings.""",
)

add(
    "firmware-engineer",
    "Firmware Engineer",
    1.0,
    "No evidence",
    """Flash images, bootloaders, device firmware, hardware bring-up.""",
    """None. Bundling `llama-cli.exe` is not firmware.""",
    """Does not apply.""",
    """Entire domain missing.""",
    """Skip.""",
)

add(
    "connected-device-software-engineer",
    "Connected-Device Software Engineer",
    3.0,
    "Weak — local device, not IoT fleet",
    """Device + cloud + connectivity: MQTT, pairing, OTA, hardware SKUs.""",
    """The PC is a “device” in a loose sense: GPU/CPU detection, portable USB, offline-first. No device identity, no OTA protocol, no companion cloud.""",
    """Only if the team wants offline-capable client software for a PC-class device.""",
    """No IoT stack, no BLE, no fleet management.""",
    """Do not stretch “connected device” unless the job is actually a Windows client for hardware.""",
)

add(
    "hardware-software-engineer",
    "Hardware/Software Engineer",
    4.0,
    "Software side of PC hardware awareness",
    """Bring-up, drivers, HW/SW contracts, lab validation.""",
    """`hardware.rs`: sysinfo, nvidia-smi name+VRAM, CUDA detection, Vulkan runtime presence, GGUF RAM fudge 1.3, size labels, recommend class. GPU layer count + backend Auto/CPU/Vulkan/CUDA. This is **using** hardware signals, not designing boards.""",
    """Useful for “we need software that makes good GPU/RAM decisions.” Not useful for schematic review.""",
    """No drivers, no HDL, no lab instrumentation, no firmware.""",
    """Describe as hardware-aware desktop software, not HW/SW co-design.""",
)

add(
    "machine-learning-engineer",
    "Machine Learning Engineer",
    4.0,
    "Inference productization, not ML training",
    """Training/eval pipelines, features, model selection with metrics, serving, sometimes research-to-prod.""",
    """You consume GGUF files, pick quant/size vs RAM, run embeddings for RAG, pin llama.cpp. You did not train, fine-tune, or run offline eval suites with labeled data (beyond argv/parser fixtures).""",
    """MLE roles that are actually “LLM application engineers” overlap. Classic MLE (training, feature stores) do not.""",
    """No PyTorch training loop, no experiment tracker, no model registry, no dataset versioning.""",
    """Call this **ML systems / inference engineering**, and do not claim MLE training experience from this repo.""",
)

add(
    "ai-engineer",
    "AI Engineer",
    7.5,
    "Strong applied AI engineering",
    """Broad title: apps on models, RAG, agents, evals, sometimes serving.""",
    """Local inference pipeline, prompt templates, thinking flags, RAG chunk/hash/embed, tool JSON protocol, model role routing, tokenizer-based context budget when `llama-tokenize` exists.""",
    """Fits AI Engineer postings that want builders, not paper writers. You can whiteboard a local RAG + tool loop.""",
    """Broken document query in the last manual matrix; no cloud eval; no multi-agent orchestration framework.""",
    """Demo chat + documents + tools; disclose RAG failures and what you would fix.""",
)

add(
    "applied-ai-engineer",
    "Applied AI Engineer",
    8.0,
    "Strong",
    """Put models into a real workflow with constraints, UX, and reliability — not research.""",
    """Constraints were the job: offline, untrusted GGUF, no executing model text as shell, hardware labels, embedding model ≠ chat model, context trim. Applied work is encoding those constraints.""",
    """This title is one of the cleanest matches after AI Product Engineer.""",
    """Limited evaluation science; RAG quality not production-proven.""",
    """Frame every feature as a user workflow (import GGUF → load → chat → cite docs) rather than as model research.""",
)

add(
    "generative-ai-engineer",
    "Generative AI / GenAI Engineer",
    8.5,
    "Strong",
    """LLM apps: prompts, decoding, safety, RAG, agents, product UX for generation.""",
    """Streaming tokens, stop, regenerate, edit-and-resubmit, Qwen3 thinking on/off, ChatML vs family templates, tool-calling JSON, split-thinking UI, auto-title from user messages, multi-model route mode.""",
    """GenAI postings that want “we wrap models in a product” are a direct fit. You did it without a vendor API.""",
    """No OpenAI/Azure OpenAI production, no prompt CMS, no content-safety classifier beyond tool/path policy.""",
    """Differentiate: you understand local GGUF/llama.cpp, not only Chat Completions APIs.""",
)

add(
    "ai-search-engineer",
    "AI/Search Engineer",
    6.5,
    "Partial — local RAG, not search ranking",
    """Retrieval, ranking, query understanding, indexes, evaluation (nDCG), sometimes embeddings.""",
    """SHA-256 ingest, overlapping chunks (512/64), embedding GGUF via `llama-embedding`, `documents_query`, citation objects (id, filename, chunk, score). Search_docs tool. Manual tests failed to return filename hits / citation chips.""",
    """You can discuss a first RAG design. You cannot claim a working search stack until MAN26/27 are fixed.""",
    """No inverted index at scale, no query parser, no A/B ranking, no Lucene/Elastic.""",
    """Be precise: “I implemented local embedding RAG; retrieval quality is incomplete.” That is still AI/search-adjacent.""",
)

add(
    "data-engineer",
    "Data Engineer",
    4.0,
    "Weak — app data, not data platform",
    """Pipelines, warehouses, orchestration, quality, batch/stream.""",
    """SQLite tables, document hashes, migrations crate, extract text from txt/md/html/pdf/docx (images stubbed). That is application storage + light ETL for RAG.""",
    """Only if “data engineer” really means “get files into a store for ML.” Most DE jobs will not count this.""",
    """No Spark, no dbt warehouse, no CDC, no Airflow.""",
    """Do not primary-target Data Engineer with this repo.""",
)

add(
    "analytics-engineer",
    "Analytics Engineer",
    2.0,
    "No evidence",
    """dbt, semantic layers, BI, metrics, warehouse modeling.""",
    """No telemetry by design. No warehouse. Chat feedback command exists but is not an analytics practice.""",
    """Does not apply.""",
    """Entire analytics stack missing.""",
    """Skip.""",
)

add(
    "algorithm-engineer",
    "Algorithm Engineer",
    4.0,
    "Light — heuristics, not published algorithms",
    """Implement/optimize algorithms with complexity and correctness proofs or numerical methods.""",
    """Heuristics: RAM fudge, model auto-route scoring, chunk overlap, prompt trim by token/char budget, stdout token parse. Unit-tested, not novel algorithms.""",
    """Shows you can encode rules and test them. Not competitive with DSP/optimization algorithm roles.""",
    """No complexity-focused production algorithms, no numerical libraries beyond simple scoring.""",
    """Use as “I implement practical heuristics with tests,” not “I am an algorithm specialist.”""",
)

add(
    "sensor-algorithm-engineer",
    "Sensor Algorithm Engineer",
    1.0,
    "No evidence",
    """IMU/camera/radar signal processing, calibration, filtering.""",
    """None. GPU/RAM probes are not sensors in this sense.""",
    """Does not apply.""",
    """No sensor data, no filters.""",
    """Skip.""",
)

add(
    "solutions-engineer",
    "Solutions Engineer",
    6.0,
    "Partial — you built the solution, little customer-facing SE motion",
    """Pre-sales technical: demos, POCs, architecture for a customer, RFP, objection handling.""",
    """The product *is* a solution for “chat with local models on Windows.” Docs, wizard, hardware labels, and installer QA are demo-ready. No evidence of customer POCs, multi-stakeholder sales, or integration into a customer’s SSO/VPC.""",
    """You can run a killer product demo (offline chat, model import, GPU backends). SE jobs also want discovery and custom integration — thinner here.""",
    """No CRM, no customer environments, no professional services delivery log.""",
    """Pair this project (demo asset) with any real customer-facing work you have. Alone it is a product demo, not an SE career.""",
)

add(
    "solution-architect",
    "Solution Architect",
    5.0,
    "Light architecture of one product, not enterprise SA",
    """Cross-system architecture for customers/enterprise: integration, NFRs, governance.""",
    """ARCHITECTURE.md is a real SA-style artifact for one app: Stage A vs B, SQLite, prompt in Rust, CSP, process diagram. Enterprise SA needs many systems.""",
    """Good writing sample for “document the system.” Weak for “architect Salesforce + SAP + custom APIs.”""",
    """No enterprise integration patterns, no C4 for a landscape, no stakeholder workshops evidenced.""",
    """Use architecture docs as a writing sample; do not claim solution architecture as your job.""",
)

add(
    "support-engineer",
    "Support Engineer",
    5.0,
    "You wrote support-shaped docs and fail-closed errors, not a support rotation",
    """Debug customer issues, reproduce, escalate, knowledge base, SLAs.""",
    """User-mapped errors (`user_message`), Help overlay, DEVELOPMENT troubleshooting (WDAC 4551), unsigned installer expectations, uninstall/data-reset instructions, status bar (tok/s, backend, offline).""",
    """Shows empathy for “why did this fail on Windows.” Not the same as queue-based support.""",
    """No ticket metrics, no production support, no customer comms log.""",
    """Helpful as “I document failure modes”; not a Support Engineer application by itself.""",
)

add(
    "field-engineer",
    "Field Engineer",
    4.0,
    "Lab/self-install only",
    """On-site install, hardware bring-up, customer premises.""",
    """You installed NSIS on a real Windows box, noted it was not a sterile PC, recorded SmartScreen/MOTW, Vulkan vs CPU backends. That is field-like self-QA, not customer sites.""",
    """Transferable: you can install and validate on a machine with messy preconditions.""",
    """No travel, no customer site, no rack/gear.""",
    """Do not claim field engineering; claim Windows install validation.""",
)

add(
    "software-generalist",
    "Software Generalist",
    8.5,
    "Primary match",
    """Wide stack, small teams, whatever the product needs.""",
    """TS/React, Rust, SQL, Windows packaging, PowerShell fetch/sign scripts, security policy, RAG, process control, CSS, tests, docs. Classic generalist footprint.""",
    """Startup and “0→1” teams want this. Local AI is a 0→1 generalist artifact.""",
    """Depth questions in any one specialty (compilers, distributed systems, iOS) will exceed this repo.""",
    """Own the generalist label: “I will pick up the layer that unblocks shipping.”""",
)

add(
    "fintech-software-engineer",
    "Fintech Software Engineer",
    1.0,
    "No evidence",
    """Ledgers, KYC, money movement, compliance, financial products.""",
    """No payments, no ledger, no PCI. Secret redaction regex is not fintech.""",
    """Does not apply.""",
    """Domain missing.""",
    """Skip unless other experience exists.""",
)

add(
    "payments-infrastructure-engineer",
    "Payments Infrastructure Engineer",
    1.0,
    "No evidence",
    """Payment rails, idempotency, ledgers, processors, reconciliation.""",
    """None.""",
    """Does not apply.""",
    """Domain missing.""",
    """Skip.""",
)

add(
    "networking-engineer",
    "Networking Engineer",
    2.0,
    "No network engineering",
    """Routing, switching, firewalls, overlays, packet-level work.""",
    """You *avoid* the network: offline default, no HTTP client for inference, CSP connect-src limited to self/ipc. Child process stdio. That is the opposite of networking engineering.""",
    """Only “I understand why we do not open sockets.”""",
    """No BGP, no VPC, no packet captures as a job.""",
    """Skip Networking Engineer applications.""",
)

add(
    "security-engineer",
    "Security Engineer",
    5.5,
    "Solid application-security instincts; not a SecEng career yet",
    """Threat models, reviews, detections, identity, vuln management, sometimes exploit work (defensive).""",
    """Documented threat model: untrusted GGUF, canonicalize/reject `..`, fail closed magic, model text not executed, tools JSON-only, destructive tools gated, Fully Offline, log redaction of `sk-`/Bearer, Tauri capabilities without opener/shell in webview, CSP default-src self, path allowlists, unsigned installer honestly documented.""",
    """Enough to pass “how would you sandbox an LLM that can call tools?” as an application engineer. Not enough to be the company’s Security Engineer.""",
    """No pentest program, no IAM, no SIEM, no CVE triage rotation. Signing still not done.""",
    """Position as secure-by-default product engineering. Apply to SecEng only if the role is “product security for clients.”""",
)

add(
    "forward-deployed-engineer",
    "Forward Deployed Engineer (FDE)",
    6.0,
    "Builder-heavy FDE; light on customer deployment",
    """FDEs sit with customers, integrate the product, write glue, unblock value, feed product. Mix of SE + SWE + field.""",
    """You built an integrable *product* (local models, docs, tools, portable USB). You validated install/uninstall on a real Windows machine and wrote runbooks. You did not sit in a customer warehouse writing adapters to their ERP.""",
    """Palantir-style FDE interviews want: ship under constraints, debug messy environments, explain tradeoffs to non-engineers (wizard copy, hardware labels). This repo proves the builder half.""",
    """Missing: customer stakeholder management, on-site delivery, custom ontology/data integration for a third party.""",
    """Story: “I can own a constrained Windows environment and make AI actually run.” Then add any real customer work from elsewhere.""",
)

add(
    "associate-forward-deployed-engineer",
    "Associate Forward Deployed Engineer",
    7.0,
    "Reasonable associate FDE signal",
    """Junior FDE: execute POCs with help, learn the product, write integration code, support workshops.""",
    """You already did the hard technical POC: llama.cpp pin, GPU backends, SQLite, RAG, tools, installer. Associate FDE is often “can you code the glue and not freeze in a demo.”""",
    """This is one of the better FDE-junior matches because the work is full-stack and demoable.""",
    """Still no customer. Workshops and political context are unproven.""",
    """Apply with a live demo of Local AI plus willingness to work on-site. Do not fake customer stories.""",
)

add(
    "senior-forward-deployed-engineer",
    "Senior Forward Deployed Engineer",
    4.0,
    "Below senior FDE without customer outcomes",
    """Leads deployments, unblocks accounts, designs the integration, mentors, owns outcomes not just code.""",
    """Technical depth is approaching senior *software* on this slice; senior FDE is measured in customer outcomes and multi-threaded delivery.""",
    """Use the repo as proof you can build; do not use it as proof you have led deployments.""",
    """No account ownership, no team lead evidence, no production customer integration.""",
    """Target senior FDE only with other experience; this project supports the technical screen.""",
)

add(
    "staff-forward-deployed-engineer",
    "Staff Forward Deployed Engineer",
    3.0,
    "Not a Staff signal",
    """Staff FDE: cross-account patterns, product influence, technical strategy, high ambiguity, often org-level.""",
    """You influenced *this* product’s architecture. That is not Staff FDE scope.""",
    """Does not apply as a title match.""",
    """No multi-customer pattern library, no staff-level communication artifacts for clients.""",
    """Do not apply to Staff FDE on this project alone.""",
)

add(
    "lead-forward-deployed-engineer",
    "Lead Forward Deployed Engineer",
    3.0,
    "Not a Lead signal",
    """Leads FDEs, delivery plans, quality bar, customer exec conversation.""",
    """Solo builder. No lead of people or programs evidenced.""",
    """Does not apply.""",
    """No leadership evidence in this repo.""",
    """Skip as a primary title.""",
)

add(
    "forward-deployed-ai-engineer",
    "Forward Deployed AI Engineer",
    6.5,
    "Builder match for AI-flavored FDE",
    """FDE who implements RAG, agents, evals, and model wiring in the customer’s environment.""",
    """Local RAG, embeddings, tool calls, prompt templates, model routing — the AI glue FDEs write. Environment is *your* Windows PC, not the customer’s VPC.""",
    """Strong technical screen for AI FDE. Delivery/customer half still missing.""",
    """No customer data, no enterprise connectors, RAG manual fails.""",
    """Demo offline RAG+tools as “what I would stand up in an air-gapped customer,” then describe how you would productionize citations.""",
)

add(
    "founding-ai-forward-deployed-engineer",
    "Founding AI Forward Deployed Engineer",
    5.0,
    "0→1 builder yes; founding FDE also needs GTM/customer zero",
    """First FDE at an AI startup: invent the delivery motion, close technical gaps, sometimes act as product.""",
    """0→1 product instincts are here (wizard, offline, packaging). Founding FDE also invents how the *company* delivers to customers.""",
    """Useful if the startup wants a builder who can make a Windows/offline story real. Incomplete if they want someone who has already been customer zero’s engineer.""",
    """No founding-team customer delivery, no playbook for repeatable deployments.""",
    """Pitch 0→1 product engineering; do not claim you founded a delivery org.""",
)

add(
    "forward-deployed-engineer-ai-enablement",
    "Forward Deployed Engineer, AI Enablement",
    6.0,
    "Partial — you enabled yourself, not an enterprise workforce",
    """Help a company adopt AI: workflows, governance, training, internal tools.""",
    """Help overlay, presets, hardware guidance, “never auto-download weights,” tool allowlists — enablement UX for a single user. Not a change-management program.""",
    """Maps to enablement if the job is “build the internal AI workstation.” Weak if the job is “train 5,000 employees on Copilot.”""",
    """No enablement curriculum, no enterprise IdP, no usage analytics (by design).""",
    """Position as building the enablement *artifact* (the app), not running enablement.""",
)

add(
    "forward-deployed-engineer-solution-architect",
    "Forward Deployed Engineer / Solution Architect",
    5.5,
    "Hybrid title: stronger engineer than architect-for-hire",
    """Combines FDE delivery with SA documentation and design for the account.""",
    """You have both code and architecture docs. Missing is account-shaped architecture (their IdP, network, data domains).""",
    """Good writing + building sample. Incomplete hybrid FDE/SA without a customer landscape.""",
    """No enterprise SA engagements.""",
    """Bring ARCHITECTURE.md + a live demo; do not claim dual-hat customer delivery.""",
)

add(
    "principal-software-solutions-engineer-forward-deployed",
    "Principal Software Solutions Engineer / Forward Deployed",
    3.0,
    "Not a Principal signal",
    """Principal: sets solution patterns, unblocks the hardest accounts, represents the product technically at exec level.""",
    """Principal is an impact/scope title. This repo is an MVP desktop app.""",
    """Does not apply.""",
    """No principal-level outcomes.""",
    """Do not apply. Use the project in a Principal loop only as a systems anecdote if you already have the scope elsewhere.""",
)

add(
    "lead-forward-deployed-engineer-hospitality",
    "Lead Forward Deployed Engineer, Hospitality",
    1.0,
    "No hospitality domain",
    """FDE lead in hotels/restaurants: PMS, POS, property ops, guest experience systems.""",
    """No hospitality integrations, no property workflows. Local AI is a generic PC chat app.""",
    """Does not apply.""",
    """Domain and lead scope missing.""",
    """Skip. Generic FDE skills do not substitute for PMS/POS.""",
)

add(
    "forward-deployed-engineer-ai-agentic-sdlc",
    "Forward Deployed Engineer, AI & Agentic SDLC",
    6.5,
    "Partial — agent tools + coding-oriented routing, not an SDLC platform",
    """Deploy AI into software delivery: coding agents, CI, reviews, evals, guardrails.""",
    """Structured tools (JSON only, roots allowlist), Coder-role auto-route, code blocks, local shell gated off by default, prompt instructions that forbid emitting shell as free text. That is a baby agent loop inside chat, not GitHub/Jira SDLC integration.""",
    """You can talk about agent guardrails (never exec raw model text) which those jobs care about. You cannot talk about rolling out an agentic SDLC to a 200-person eng org.""",
    """No CI agent, no PR bot, no repo indexing at org scale, no evals on SWE-bench.""",
    """Lead with tool sandboxing and coding-model routing; do not claim an SDLC product.""",
)

add(
    "forward-deployed-engineer-clearance-required",
    "Forward Deployed Engineer — Clearance Required",
    1.0,
    "No clearance or classified delivery in this repo",
    """Same as FDE plus US clearance (Secret/TS/SCI), often air-gapped or IL5/IL6 environments.""",
    """The *product* is air-gapped-friendly (offline GGUF, no telemetry). That is interesting to cleared customers. The *you* in this git repo have no clearance, SAP, or classified deployment evidence.""",
    """You can say you built software that *could* run disconnected. You cannot say you are eligible from this work.""",
    """Clearance is a personnel attribute; this project does not create it.""",
    """Apply only if you already hold or can obtain clearance. Use Local AI as the technical sample for air-gap constraints.""",
)


def md_role(r: dict) -> str:
    score = r["score"]
    bar = min(10, max(0, int(round(score))))
    meter = "█" * bar + "░" * (10 - bar)
    return f"""# {r['title']}

**Project:** Local AI (this repository)  
**Fit score:** {score:.1f} / 10  `{meter}`  
**Level:** {r['level']}

## Rating notes

{SCALE}

## What this role usually means

{r['typical']}

## What you actually did in this project

{PROJECT}

Role-specific work:

{r['done']}

## How this project applies to this title

{r['apply']}

## Gaps (do not overclaim)

{r['gaps']}

## How to talk about it

{r['talk']}

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
"""


def md_overview() -> str:
    rows = sorted(ROLES, key=lambda x: (-x["score"], x["title"]))
    table = ["| Score | Job title | Level |", "| ---: | --- | --- |"]
    for r in rows:
        table.append(f"| {r['score']:.1f} | [{r['title']}](./{r['slug']}.md) | {r['level']} |")
    ranked = "\n".join(table)

    bands = {
        "Primary matches (8.0+)": [r for r in rows if r["score"] >= 8.0],
        "Strong / interviewable (7.0–7.9)": [r for r in rows if 7.0 <= r["score"] < 8.0],
        "Partial (5.0–6.9)": [r for r in rows if 5.0 <= r["score"] < 7.0],
        "Adjacent (3.0–4.9)": [r for r in rows if 3.0 <= r["score"] < 5.0],
        "Do not use this project as evidence (0–2.9)": [r for r in rows if r["score"] < 3.0],
    }
    band_md = []
    for name, items in bands.items():
        band_md.append(f"### {name}\n")
        for r in items:
            band_md.append(f"- **{r['title']}** ({r['score']:.1f}) — {r['level']}")
        band_md.append("")

    return f"""# Local AI — job-title experience overview

This folder maps **only this repository** (Local AI desktop app) onto common job titles. It is not a résumé of your whole career. If you have other jobs, internships, or clearance, add those separately.

## The project in one paragraph

{PROJECT}

## How to read the scores

{SCALE}

A high score means “this repo is a credible work sample for that hiring loop.” A low score means “do not stretch this repo onto that title.”

## Ranked findings

{ranked}

## Banded findings

{chr(10).join(band_md)}

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
""" + "\n".join(f"| [`{r['slug']}.md`](./{r['slug']}.md) | {r['title']} |" for r in sorted(ROLES, key=lambda x: x["title"])) + """

---

*Evidence sources: `README.md`, `docs/ARCHITECTURE.md`, `docs/TESTING.md`, `docs/SECURITY.md`, `docs/PACKAGING.md`, `src-tauri/src/**`, `src/**`.*
"""


def main() -> None:
    for r in ROLES:
        (OUT / f"{r['slug']}.md").write_text(md_role(r), encoding="utf-8")
    (OUT / "OVERVIEW.md").write_text(md_overview(), encoding="utf-8")
    print(f"wrote {len(ROLES)} role docs + OVERVIEW.md")


if __name__ == "__main__":
    main()
