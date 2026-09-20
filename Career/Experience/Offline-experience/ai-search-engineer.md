# AI/Search Engineer

**Project:** Local AI (this repository)  
**Fit score:** 6.5 / 10  `██████░░░░`  
**Level:** Partial — local RAG, not search ranking

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

Retrieval, ranking, query understanding, indexes, evaluation (nDCG), sometimes embeddings.

## What you actually did in this project

**Local AI** (`com.localai.desktop`, v0.2.0) is a Windows desktop product: **Tauri 2 + React 19 + TypeScript + Rust**. It runs **offline GGUF** inference via pinned **llama.cpp** (`llama-cli` b10488) as a child process (stdio, not HTTP). Chats persist in **SQLite** (`rusqlite` + migrations). The UI never calls cloud inference APIs.

Shipped surface: first-run wizard, chat (stream/stop/regenerate/edit), model library (import/scan/load/unload/GPU backends), documents + local RAG, settings/presets, command palette, help, themes, portable USB layout, current-user **NSIS** installer. Tests: Vitest + Cargo unit/fixture tests + a 38-item Windows installer manual matrix.

Role-specific work:

SHA-256 ingest, overlapping chunks (512/64), embedding GGUF via `llama-embedding`, `documents_query`, citation objects (id, filename, chunk, score). Search_docs tool. Manual tests failed to return filename hits / citation chips.

## How this project applies to this title

You can discuss a first RAG design. You cannot claim a working search stack until MAN26/27 are fixed.

## Gaps (do not overclaim)

No inverted index at scale, no query parser, no A/B ranking, no Lucene/Elastic.

## How to talk about it

Be precise: “I implemented local embedding RAG; retrieval quality is incomplete.” That is still AI/search-adjacent.

---

*Generated from repository evidence (architecture, Rust/TS sources, tests, packaging, and the Windows manual matrix in `docs/TESTING.md`). This is not a background check or a claim about work outside this repo.*
