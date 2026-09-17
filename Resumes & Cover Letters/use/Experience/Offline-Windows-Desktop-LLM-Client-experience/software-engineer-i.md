# Software Engineer I

**Project:** Local AI (this repository)  
**Fit score:** 8.5 / 10  `████████░░`  
**Level:** Very strong for SWE I

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

Entry / first full-time engineering bar: ship well-scoped features, write tests, take review, debug with help, learn the codebase.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

Scope matches a strong intern-to-SWE-I portfolio: feature slices (chat reducer, model catalog, onboarding, documents), unit tests (Vitest + Cargo fixtures), error mapping to user strings, and a manual install matrix. Code shows patterns (state machine for generation, exhaustive TS switches).

## How this project applies to this title

This repo is enough to claim you have already done “new grad / SWE I” work: tickets that span UI and native, tests that fail closed, and docs that another engineer could follow.

## Gaps (do not overclaim)

SWE I jobs still expect internships or class projects in other stacks. This is one product; mention it as the flagship, not the only story if you have more.

## How to talk about it

Lead with Local AI as the project that proves you can ship a complete app, then map each interview question to a file (inference state machine, path canonicalization, chat reducer).

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
