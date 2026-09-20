# Frontend Engineer

**Project:** Local AI (this repository)  
**Fit score:** 7.5 / 10  `████████░░`  
**Level:** Solid product UI; not a design-system specialist

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

Component architecture, accessibility, performance, state, CSS, design collaboration.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

You built ChatView, Models, Documents, Settings, onboarding, overlays, status bar, markdown+code blocks, theme prefs, UI templates, hardware guide copy, command palette. Tests cover reducers, routing heuristics, prefs, conversation markdown export.

## How this project applies to this title

Frontend interviews can use chat streaming state (`chatReducer`) and offline-first constraints (no CDN fonts, CSP, `check-offline-assets`).

## Gaps (do not overclaim)

Single desktop webview, not responsive web marketing, not React Native, limited a11y audit evidence. No Storybook/design-system ownership.

## How to talk about it

Bring the streaming + stop/regenerate UX and the first-run privacy wizard as the frontend craft samples.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
