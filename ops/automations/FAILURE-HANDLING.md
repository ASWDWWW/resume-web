# Automation failure handling

1. Log the redacted event.
2. Do not retry unbounded external actions (sends, charges, deploys).
3. Do not fall back to another account.
4. Surface the failure in `ops/CONTROL-CENTER.md` integration section.
5. Continue independent work.
6. Recovery: fix the identity or input, then the user re-runs the command.
