# Developer Tools Engineer

**Project:** Local AI (this repository)  
**Fit score:** 5.0 / 10  `█████░░░░░`  
**Level:** Partial — tools inside an AI coding-adjacent app

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

Compilers, IDEs, CLI tools, debuggers, build systems used by other engineers.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

Command palette, prompt library, code blocks, auto-route “Coder” models, local tools (read_file/search_docs), markdown export of chats. llama-cli argv construction is a tool wrapper. Not an IDE.

## How this project applies to this title

Closest if the tools team builds **AI coding assistants** or **CLI wrappers**. You wrapped llama.cpp and parsed stdout/banners/tokens.

## Gaps (do not overclaim)

You did not build a compiler, LSP, or editor. No plugin ecosystem.

## How to talk about it

Pitch as “I integrated an inference CLI into a desktop tool with structured agent tools,” not “I work on LLVM.”

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
