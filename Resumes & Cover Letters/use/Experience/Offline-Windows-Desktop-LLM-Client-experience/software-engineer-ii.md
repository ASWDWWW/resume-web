# Software Engineer II / SWE II

**Project:** Local AI (this repository)  
**Fit score:** 7.0 / 10  `███████░░░`  
**Level:** Credible early SWE II; thin on scale

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

Independent execution on ambiguous problems, design reviews, reliability, mentoring sometimes, production impact beyond a single feature.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

You made architectural calls: Stage A child-process inference vs Stage B native stub; ChatML/Llama3/Mistral templates in Rust not React; GPU backend selection; portable vs APPDATA paths; capability-locked Tauri webview. You documented tradeoffs and left native linking unclaimed until it actually works.

## How this project applies to this title

Use this for “tell me about a design decision” and “how do you test native + UI.” SWE II interviewers care that you chose fail-closed security and did not pretend Stage B was done.

## Gaps (do not overclaim)

Typical SWE II bars include production SLOs, distributed systems, or multi-quarter ownership on a team codebase. This is a solo desktop MVP. Score is for transferable craft, not title inflation.

## How to talk about it

Do not oversell as Staff. Position as: I independently designed and shipped a constrained systems+product problem (local inference + UX + installer).

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
