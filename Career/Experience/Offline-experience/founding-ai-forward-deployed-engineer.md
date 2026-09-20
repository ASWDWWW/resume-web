# Founding AI Forward Deployed Engineer

**Project:** Local AI (this repository)  
**Fit score:** 5.0 / 10  `█████░░░░░`  
**Level:** 0→1 builder yes; founding FDE also needs GTM/customer zero

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

First FDE at an AI startup: invent the delivery motion, close technical gaps, sometimes act as product.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

0→1 product instincts are here (wizard, offline, packaging). Founding FDE also invents how the *company* delivers to customers.

## How this project applies to this title

Useful if the startup wants a builder who can make a Windows/offline story real. Incomplete if they want someone who has already been customer zero’s engineer.

## Gaps (do not overclaim)

No founding-team customer delivery, no playbook for repeatable deployments.

## How to talk about it

Pitch 0→1 product engineering; do not claim you founded a delivery org.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
