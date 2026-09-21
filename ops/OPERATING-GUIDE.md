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
| Mail/meetings | drafts via `/draft-communication`. Gmail MCP is on the wrong mailbox until reconnected. Zoom is `user-zoom-bridge` only (catalog stays `needsAuth`). Do not send or create meetings unless you authorize it |

## Account routing

This repo: **github-aswdwww** (`ASWDWWW`). Do not pick an account — origin maps to the login. `/commit`, `/push`, `/commit-and-push` use that identity.  
FITD GitHub: **github-fitd-fash** only when you name it.  
Gmail: **zakiymanigo** (`zakiymanigo@gmail.com`) for this repo. Do not use FITD / fashiobusiness here.  
Firebase for this repo: project `zakiymanigo-career`. MCP may be sitting on `fitd-app-203cb` — do not deploy that from this tree.  
Stripe: test/sandbox default. Live needs named authority.  
Never silent fallback.

## Design and generation

- Figma: signed in as `zakiymanigo@gmail.com`. File workflows untested. Do not open the Bariatric Associates org unless a TREI ticket names it.
- Canva: read verified. Do not auto-publish.
- Magnific: signed in. MCP sessions spend credits even if the Magnific app has unlimited. Do not generate without a budget.

## What not to do

- Do not revert unfinished `Career/`, `Content/`, or resume-folder work.
- Do not `git config` or force-push main (hooks deny these).
- Do not treat `ops/restricted/` as safe storage.
- Do not treat generated legal or finance text as approved.
- Do not execute or publish n8n workflows unless asked. The instance has an active Instagram poster that is not MCP-enabled.

## Repair

`/repair-workspace` rebuilds native files. Hook scripts require Node (verified v24 on this machine). Harness: `node .cursor/hooks/test-harness.mjs`.

## Optional later

Custom dashboard, IONOS Cloud MCP, Zoom bridge repair, Gmail reconnect, private OS repo.
