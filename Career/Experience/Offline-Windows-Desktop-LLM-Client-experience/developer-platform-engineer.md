# Developer Platform Engineer

**Project:** Local AI (this repository)  
**Fit score:** 4.0 / 10  `████░░░░░░`  
**Level:** Weak — one product’s DX, not a platform org

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

Paved roads: templates, CI, inner-loop, golden repos, self-service infra.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

In-repo DX: DEVELOPMENT.md, fetch-llama-cli.ps1, check-offline-assets, Vitest/Cargo, rustfmt, eslint, gated tests that skip without a model. That is good repo hygiene, not a developer platform.

## How this project applies to this title

You can speak to making a native+JS repo bootable and testable. That is a slice of DX.

## Gaps (do not overclaim)

No internal marketplace, no multi-repo CI, no service catalog.

## How to talk about it

Mention as “I care about the inner loop,” then move to product engineering.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
