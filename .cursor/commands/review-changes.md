# Review changes

Prefer the `independent-reviewer` subagent for a second pass.

Review the actual diff against:

- correctness and regressions
- account routing and authorization (no live Stripe, no silent sends)
- secrets and PII
- accessibility and performance when UI changed
- claim safety for career or marketing copy

Output: critical / suggestion / optional. Do not commit or merge. Do not rewrite the author’s unfinished work outside the review comments.
