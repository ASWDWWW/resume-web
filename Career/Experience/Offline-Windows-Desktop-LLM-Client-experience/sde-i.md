# Software Development Engineer I (SDE I)

**Project:** Local AI (this repository)  
**Fit score:** 8.5 / 10  `████████░░`  
**Level:** Very strong for SDE I

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

Amazon-style SDE I: coding, testing, ownership of well-defined components, operational awareness at small scale.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

You owned components with clear contracts: `InferenceEngine` trait, Tauri commands, SQLite schema, argv pin tests against llama.cpp b10488, gated INT01–INT05 when `LOCALAI_TEST_MODEL` is unset (skip not fail).

## How this project applies to this title

SDE I loops want working software + tests. You have both layers plus Windows packaging — closer to “shipped” than a typical class project.

## Gaps (do not overclaim)

Little evidence of Amazon-style operational metrics, code reviews with a team, or large existing services.

## How to talk about it

Map LP-style stories to: customer (offline privacy), dive deep (stdout parser + token metrics), insist on highest standards (unsigned installer documented, RAG failures recorded as fail).

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
