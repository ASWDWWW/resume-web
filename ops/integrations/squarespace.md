# Squarespace

Official remote MCP: [overview](https://developers-preview.squarespace.com/mcp/overview).

URL: `https://mcp.squarespace.com/mcp`  
Auth: none. No API key, OAuth, or Squarespace account is required.

This server is **domain search only**. Tools:

- `domains_generate_names` — brandable name/domain ideas from a description
- `domains_search` — availability and pricing, with checkout links

It does **not** edit a live site, products, orders, DNS, or `fitdai.com`. Purchases happen only if you follow a checkout link on squarespace.com. Do not treat a search result as a purchase.

The career site in this repo stays on Firebase (`zakiymanigo-career`), not Squarespace. Chrome DevTools previously showed Squarespace DNS for `fitdai.com` — that is browser admin, not this MCP.

There is **no Cursor marketplace plugin** that manages an existing Squarespace site. Commerce/site APIs would need a separate key from the site’s developer settings; do not put that in git.

## You do this

1. Cursor **Settings → MCP**. Confirm `squarespace` is enabled (user `%USERPROFILE%\.cursor\mcp.json`).
2. Reload the MCP server if tools do not appear.
3. In chat, ask to search a domain (read-only) before following any checkout link.
