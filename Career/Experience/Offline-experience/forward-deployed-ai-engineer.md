# Forward Deployed AI Engineer

**Project:** Local AI (this repository)  
**Fit score:** 6.5 / 10  `██████░░░░`  
**Level:** Builder match for AI-flavored FDE

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

FDE who implements RAG, agents, evals, and model wiring in the customer’s environment.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

Local RAG, embeddings, tool calls, prompt templates, model routing — the AI glue FDEs write. Environment is *your* Windows PC, not the customer’s VPC.

## How this project applies to this title

Strong technical screen for AI FDE. Delivery/customer half still missing.

## Gaps (do not overclaim)

No customer data, no enterprise connectors, RAG manual fails.

## How to talk about it

Demo offline RAG+tools as “what I would stand up in an air-gapped customer,” then describe how you would productionize citations.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
