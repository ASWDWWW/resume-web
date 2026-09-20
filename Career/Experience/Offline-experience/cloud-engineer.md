# Cloud Engineer

**Project:** Local AI (this repository)  
**Fit score:** 2.0 / 10  `██░░░░░░░░`  
**Level:** No cloud delivery

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

AWS/Azure/GCP services, IAM, networking, containers, cost.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

The product is anti-cloud by design: Fully Offline, no telemetry, no HTTP inference client. Hugging Face links are copy-paste for humans; the app does not fetch.

## How this project applies to this title

The only cloud-adjacent skill is knowing what *not* to put on the network (CSP, no opener plugin). That is security/product, not cloud engineering.

## Gaps (do not overclaim)

No cloud accounts, no Terraform, no EKS.

## How to talk about it

Do not apply this project to Cloud Engineer roles except as “I can build air-gapped clients.”

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
