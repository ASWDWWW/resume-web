# Forward Deployed Engineer — Clearance Required

**Project:** Local AI (this repository)  
**Fit score:** 1.0 / 10  `█░░░░░░░░░`  
**Level:** No clearance or classified delivery in this repo

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

Same as FDE plus US clearance (Secret/TS/SCI), often air-gapped or IL5/IL6 environments.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

The *product* is air-gapped-friendly (offline GGUF, no telemetry). That is interesting to cleared customers. The *you* in this git repo have no clearance, SAP, or classified deployment evidence.

## How this project applies to this title

You can say you built software that *could* run disconnected. You cannot say you are eligible from this work.

## Gaps (do not overclaim)

Clearance is a personnel attribute; this project does not create it.

## How to talk about it

Apply only if you already hold or can obtain clearance. Use Local AI as the technical sample for air-gap constraints.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
