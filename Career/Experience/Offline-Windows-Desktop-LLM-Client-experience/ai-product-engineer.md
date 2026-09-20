# AI Product Engineer

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

Ships AI into a product: model selection, prompts, eval-ish tests, UX for latency/failure, RAG, tools, not just a notebook.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

GGUF catalog + roles, auto/multi model routing heuristics, ChatML/Llama3/Mistral templates, Qwen3 `/no_think` vs thinking, context meter, tok/s, RAG ingest + citations (attempted; MAN26/27 failed), JSON tool calls (read/search; delete/shell gated), embedding model distinct from chat model.

## How this project applies to this title

This is the job: local LLM product. You can discuss prompt budget, template mismatch, embedding vs generative models, and why the app never fetches weights.

## Gaps (do not overclaim)

No hosted LLM ops, no eval harness with golden datasets at scale, RAG retrieval still broken in the recorded manual run.

## How to talk about it

Lead with “I productized local inference,” then be honest that document-chat citations failed MAN26/27 — that honesty is AI-product maturity.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
