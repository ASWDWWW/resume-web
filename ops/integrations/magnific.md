# Magnific

There is **no Cursor marketplace plugin**. Official remote MCP: [docs](https://docs.magnific.com/modelcontextprotocol).

URL: `https://mcp.magnific.com`  
Auth: Magnific OAuth in the browser. Do not put an API key in git.

Paid generation uses Magnific credits. MCP sessions do **not** get unlimited even when the Magnific app account has it (`unlimitedAppliesHere: false` on 20 Sep 2026). Do not run paid jobs without a budget in the control center.

Signed in 20 Sep 2026 as Zakiy Manigo / `zakiymanigo@gmail.com` (Premium+). Identity/balance **verified**. Generation **not** run.

## You do this

1. Cursor **Settings → MCP → Add new global MCP server** (or edit `%USERPROFILE%\.cursor\mcp.json`).
2. Merge:

```json
{
  "mcpServers": {
    "magnific": {
      "url": "https://mcp.magnific.com"
    }
  }
}
```

3. Reload the server. Complete Magnific sign-in in the browser.
4. In chat: “List my Magnific generation history” (read-only check before any paid upscale).
