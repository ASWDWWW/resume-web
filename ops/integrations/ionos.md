# IONOS

There is **no Cursor marketplace plugin**. Official path is IONOS Cloud’s local MCP: [Cursor setup](https://docs.ionos.com/cloud/ai/mcp-server/connect-to-an-ai-client/cursor).

That server is **IONOS Cloud** (data centers, Cloud DNS, billing). It is not IONOS shared web hosting / email. If the account is only website hosting, this MCP will not manage it.

Do not put `IONOS_TOKEN` in this git repo.

## You do this

1. Confirm the product is **IONOS Cloud** (Data Center Designer), not only IONOS.com hosting.
2. In DCD: **Management → Token Manager**. Create a token. Prefer read-only until you opt into write tools.
3. Download `ionoscloud-mcp_windows_amd64.exe` from [GitHub Releases](https://github.com/ionos-cloud/ionoscloud-mcp/releases). Rename to `ionoscloud-mcp.exe` and put it somewhere stable, e.g. `%USERPROFILE%\bin\ionoscloud-mcp.exe`.
4. Edit **user** MCP config: `%USERPROFILE%\.cursor\mcp.json` (Cursor Settings → MCP → Open mcp.json). Merge:

```json
{
  "mcpServers": {
    "ionoscloud": {
      "command": "C:\\Users\\Zakiy Manigo\\bin\\ionoscloud-mcp.exe",
      "env": {
        "IONOS_TOKEN": "paste-token-here-not-in-git"
      }
    }
  }
}
```

5. Reload MCP / restart Cursor. Ask: “List my IONOS Cloud data centers.”

20 September 2026: Cursor namespace `user-ionoscloud` was **error** (live tool discovery failed). Binary/token still required. Continue independently until the local MCP starts.

Write tools need `IONOS_MCP_TOOL_SCOPE=write` (and `destructive` for deletes). Leave those unset unless you want agents able to change infrastructure.

Optional docs-only server (no token): `"ionoscloud-docs": { "url": "https://docs.ionos.com/cloud/~gitbook/mcp" }`.
