# Platform Engineer

**Project:** Local AI (this repository)  
**Fit score:** 5.0 / 10  `█████░░░░░`  
**Level:** Partial — app platform, not org platform

## Rating notes

Ratings are **0–10 for this repository only**, not a full career score.

| Score | Meaning |
| --- | --- |
| 9–10 | This project is a primary hiring signal for the role |
| 7–8 | Strong transferable evidence; interviewable as I/II on this stack |
| 5–6 | Partial overlap; you can tell a credible story with gaps named |
| 3–4 | Adjacent skills only |
| 0–2 | Essentially no evidence from this work |

## What this role usually means

Internal platforms: CI, golden paths, multi-tenant infra, developer self-service, SLOs.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

You built a small *application* platform: runtime folders for CPU/Vulkan/CUDA/embed llama binaries, argv pin, bootstrap_runtime, capability JSON, portable layout. That is embedding a runtime, not running a company platform.

## How this project applies to this title

Talk about “platform” only as “we pin and bundle an inference runtime so the UI stays a client.” Do not claim Kubernetes platform engineering.

## Gaps (do not overclaim)

No IDP, no Terraform org, no CI golden pipelines for many teams.

## How to talk about it

If the posting is “developer platform for 200 engineers,” this project is a weak match. If it is “own the runtime under the product,” it is a start.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
