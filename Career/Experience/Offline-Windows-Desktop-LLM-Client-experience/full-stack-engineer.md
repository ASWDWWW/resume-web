# Full-Stack Engineer

**Project:** Local AI (this repository)  
**Fit score:** 8.5 / 10  `████████░░`  
**Level:** Strong (desktop full stack, not typical web SaaS)

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

UI + API/backend + data. Often TypeScript/React plus a server and a database.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

Frontend: React 19, Vite, feature folders, reducers, Vitest. “Backend”: Rust Tauri commands, SQLite, filesystem, child processes. Shared types via serde JSON across the IPC boundary.

## How this project applies to this title

Full-stack postings that mean “React + Node + Postgres” still buy this story if you say: the native layer is the API; SQLite is the DB; events are the realtime channel. You did both sides with tests.

## Gaps (do not overclaim)

No REST/GraphQL public API, no auth, no cloud deploy, no CSS framework at scale. Browser-only full-stack jobs will probe Next.js/SSR you did not use.

## How to talk about it

Phrase it as full-stack **desktop**: React presentation, Rust domain, SQLite persistence, OS integration.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
