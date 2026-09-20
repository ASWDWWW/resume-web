# Operating guide

This workspace is the public career site plus an owner operating system. It is not a license to send email, take payments, publish ads, or deploy production.

## Daily

1. Open [CONTROL-CENTER.md](CONTROL-CENTER.md).
2. Run the matching slash command (`/start-project`, `/complete-ticket`, `/follow-up`, …).
3. Write results back to tickets or the control center. Agents do not share memory.

## Who does what

| Work | How |
| --- | --- |
| Implement in this repo | One agent, sequential |
| Independent review | `independent-reviewer` subagent |
| Verify | `verifier` subagent or `/repair-workspace` checks |
| Ops writing | `business-ops` or the finance/marketing/legal commands |
| Mail/meetings | drafts via `/draft-communication` until Gmail/Zoom are authenticated **and** you authorize a send |

## Account routing

This repo: **github-aswdwww** (`ASWDWWW`).  
FITD GitHub: **github-fitd-fash** only when you name it.  
Gmail: ask if `gmail-fashiobusiness` vs `zakiymanigo@gmail.com`.  
Never silent fallback.

## What not to do

- Do not revert unfinished `Career/`, `Content/`, or resume-folder work.
- Do not `git config` or force-push main (hooks deny these).
- Do not treat `ops/restricted/` as safe storage.
- Do not treat generated legal or finance text as approved.

## Repair

`/repair-workspace` rebuilds native files. Hook scripts require Node (verified v24 on this machine).

## Optional later

Custom dashboard, n8n, Stripe plugin, Figma plugin, Gmail/Zoom auth, private OS repo.
