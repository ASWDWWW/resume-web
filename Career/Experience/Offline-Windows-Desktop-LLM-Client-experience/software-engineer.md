# Software Engineer

**Project:** Local AI (this repository)  
**Fit score:** 8.0 / 10  `████████░░`  
**Level:** Strong — general SWE I/early II from one product

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

Owns features end to end: design, implementation, tests, and shipping. Comfortable across languages, debugging, and product constraints.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

You built a full desktop application, not a tutorial: typed IPC from React to Rust, process lifecycle for llama-cli, SQLite persistence, streaming UI, packaging, and documented security/testing. You handled real failure modes (WDAC blocking cargo, unsigned SmartScreen, RAG query bugs recorded as MAN26/27).

## How this project applies to this title

Interview as someone who can take a vague product (“offline chat”) and turn it into modules, tests, and an installer. Emphasize ownership of the whole loop: UI, backend, storage, native runtime, and QA.

## Gaps (do not overclaim)

No multi-service production, no large team process, no on-call. SWE interviews will still probe algorithms, system design at web scale, and languages you did not use here.

## How to talk about it

“I shipped a Windows desktop AI client with a Rust native layer, a React UI, SQLite, and a real installer — including streaming inference and fail-closed file/tool security.”

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
