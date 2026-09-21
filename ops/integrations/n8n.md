# n8n

Instance MCP URL (no token in git): `https://n8n.srv1255136.hstgr.cloud/mcp-server/http`

Auth lives only in `%USERPROFILE%\\.cursor\\mcp.json` (`n8n` server, Bearer header). Do not commit that file.

Older Hostinger hostname `zakiy-n8n-auto.cloud` returned HTTP 500 on 20 Sep 2026.

Verified 20 September 2026: workflow **list** succeeded (11 workflows). Execute and publish were not run.

## Rules

- Do not let n8n and Cursor hooks both fire the same external action.
- Register workflows in `ops/automations/CATALOG.md` after a successful tool list.
- Do not execute or publish unless the user names the workflow and authorizes the action.
- Workflows with `availableInMCP: false` cannot be run from Cursor even if they are active on the instance.

## Observed 20 Sep 2026

FitGenius draft pack (MCP-available, **inactive**): weekly social drafts, review queues, business draft pack, bootstrap tables. Descriptions say they do not post or send.

One **active** Instagram posting workflow exists on the instance and is **not** MCP-available. Confirm in the n8n UI whether it should stay on. Agents cannot start it from here.
