# Associate Forward Deployed Engineer

**Project:** Local AI (this repository)  
**Fit score:** 7.0 / 10  `███████░░░`  
**Level:** Reasonable associate FDE signal

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

Junior FDE: execute POCs with help, learn the product, write integration code, support workshops.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

You already did the hard technical POC: llama.cpp pin, GPU backends, SQLite, RAG, tools, installer. Associate FDE is often “can you code the glue and not freeze in a demo.”

## How this project applies to this title

This is one of the better FDE-junior matches because the work is full-stack and demoable.

## Gaps (do not overclaim)

Still no customer. Workshops and political context are unproven.

## How to talk about it

Apply with a live demo of Local AI plus willingness to work on-site. Do not fake customer stories.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
