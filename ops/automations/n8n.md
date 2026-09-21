# n8n

Instance MCP URL (no token in git): `https://n8n.srv1255136.hstgr.cloud/mcp-server/http`

Auth lives only in `%USERPROFILE%\\.cursor\\mcp.json` (`n8n` server, Bearer header). Do not commit that file.

Older Hostinger hostname `zakiy-n8n-auto.cloud` returned HTTP 500 on 20 Sep 2026.

Instance details and observed workflows: `ops/integrations/n8n.md`. Catalog: `CATALOG.md`.

Do not let n8n and Cursor hooks both fire the same external action. Do not execute or publish unless asked.
