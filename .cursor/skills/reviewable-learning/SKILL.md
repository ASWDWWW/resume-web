---
name: reviewable-learning
description: Turn repeated corrections into a scoped, reviewable rule or note instead of a silent global instruction. Use after the user corrects the same behavior more than once and agrees to persist it.
disable-model-invocation: true
---

# Reviewable learning

1. State the correction in one sentence.
2. Propose a scoped rule (globs) or a dated note under `ops/records/`. Prefer scoped over always-apply.
3. Wait for user agreement before writing a global rule.
4. Never persist secrets, one-off ticket details, or another product’s context as a workspace-wide instruction.
