# Application Developer

**Project:** Local AI (this repository)  
**Fit score:** 9.0 / 10  `█████████░`  
**Level:** Primary match

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

Build user-facing applications: UI, local state, persistence, install/update, Windows desktop conventions.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

This is an application: window chrome, sidebar, chat, models, documents, settings, F1 help, Ctrl+K palette, first-run wizard, NSIS current-user install, Start menu shortcut, portable flag, theme system, markdown rendering with sanitization.

## How this project applies to this title

Application developer interviews should be mostly this repo. You can walk a screen-by-screen demo and the IPC behind each button.

## Gaps (do not overclaim)

Not a line-of-business CRUD app (no enterprise auth, no SAP/Office add-ins). If the posting is “internal IT apps,” map via SQLite + settings, not via ERP.

## How to talk about it

Demo the installed `local-ai.exe` path, not only `npm run tauri dev` — you already proved MAN01–MAN38 on the installer.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
