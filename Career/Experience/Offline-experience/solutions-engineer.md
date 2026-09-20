# Solutions Engineer

**Project:** Local AI (this repository)  
**Fit score:** 6.0 / 10  `██████░░░░`  
**Level:** Partial — you built the solution, little customer-facing SE motion

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

Pre-sales technical: demos, POCs, architecture for a customer, RFP, objection handling.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

The product *is* a solution for “chat with local models on Windows.” Docs, wizard, hardware labels, and installer QA are demo-ready. No evidence of customer POCs, multi-stakeholder sales, or integration into a customer’s SSO/VPC.

## How this project applies to this title

You can run a killer product demo (offline chat, model import, GPU backends). SE jobs also want discovery and custom integration — thinner here.

## Gaps (do not overclaim)

No CRM, no customer environments, no professional services delivery log.

## How to talk about it

Pair this project (demo asset) with any real customer-facing work you have. Alone it is a product demo, not an SE career.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
