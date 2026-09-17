# Hardware/Software Engineer

**Project:** Local AI (this repository)  
**Fit score:** 4.0 / 10  `████░░░░░░`  
**Level:** Software side of PC hardware awareness

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

Bring-up, drivers, HW/SW contracts, lab validation.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

`hardware.rs`: sysinfo, nvidia-smi name+VRAM, CUDA detection, Vulkan runtime presence, GGUF RAM fudge 1.3, size labels, recommend class. GPU layer count + backend Auto/CPU/Vulkan/CUDA. This is **using** hardware signals, not designing boards.

## How this project applies to this title

Useful for “we need software that makes good GPU/RAM decisions.” Not useful for schematic review.

## Gaps (do not overclaim)

No drivers, no HDL, no lab instrumentation, no firmware.

## How to talk about it

Describe as hardware-aware desktop software, not HW/SW co-design.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
