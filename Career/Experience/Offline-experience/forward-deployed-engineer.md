# Forward Deployed Engineer (FDE)

**Project:** Local AI (this repository)  
**Fit score:** 6.0 / 10  `██████░░░░`  
**Level:** Builder-heavy FDE; light on customer deployment

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

FDEs sit with customers, integrate the product, write glue, unblock value, feed product. Mix of SE + SWE + field.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

You built an integrable *product* (local models, docs, tools, portable USB). You validated install/uninstall on a real Windows machine and wrote runbooks. You did not sit in a customer warehouse writing adapters to their ERP.

## How this project applies to this title

Palantir-style FDE interviews want: ship under constraints, debug messy environments, explain tradeoffs to non-engineers (wizard copy, hardware labels). This repo proves the builder half.

## Gaps (do not overclaim)

Missing: customer stakeholder management, on-site delivery, custom ontology/data integration for a third party.

## How to talk about it

Story: “I can own a constrained Windows environment and make AI actually run.” Then add any real customer work from elsewhere.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
