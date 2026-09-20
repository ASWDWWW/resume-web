# Backend Engineer

**Project:** Local AI (this repository)  
**Fit score:** 8.0 / 10  `████████░░`  
**Level:** Strong for native/backend; not HTTP services

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

Services, APIs, data stores, concurrency, reliability, auth, queues.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

Rust domain: command handlers, mutex app state, generation state machine, child process stdout parse, cancel via AtomicBool, DB conversations/models/documents/settings, path security, tool execution, RAG chunking/embeddings subprocess.

## How this project applies to this title

Backend interviews that allow “systems backend” or “native services” map cleanly. Talk mutex + process lifecycle + SQLite transactions, not Express routes.

## Gaps (do not overclaim)

No networked service, no authn/z, no Kafka, no Postgres ops, no load balancing. Classic “backend engineer at a web company” is a partial fit.

## How to talk about it

Lead with process isolation and fail-closed path checks; those are backend instincts applied to a local host.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
