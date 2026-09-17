# Software Development Engineer II (SDE II)

**Project:** Local AI (this repository)  
**Fit score:** 7.0 / 10  `███████░░░`  
**Level:** Partial SDE II — design yes, org scale no

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

SDE II: designs medium systems, delivers across sprints, handles production issues, influences adjacent teams.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

Medium-system design is present: process isolation of the model runtime, context budget via tokenize-or-heuristic, RAG ingest hashes, tool allowlists. You ran a real install/uninstall/reinstall data-preservation matrix.

## How this project applies to this title

Good for “design a local inference client” or “how would you isolate untrusted model output.” Weaker for “design an order service.”

## Gaps (do not overclaim)

No AWS service ownership, no high-QPS backends, no formal on-call. Treat SDE II as a stretch supported by this project plus other experience.

## How to talk about it

In system design, start from threat model and process boundary (webview vs Rust vs llama-cli), then storage and packaging — that is your authentic SDE II story.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
