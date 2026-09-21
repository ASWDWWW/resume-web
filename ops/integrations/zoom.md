# Zoom MCP authentication

Last verified: 20 September 2026.

## What failed

Cursor’s catalog Zoom plugin (`plugin-zoom-zoom`) still `needsAuth`. Authorize returns:

```json
{"status":false,"errorCode":4700,"errorMessage":"Invalid redirect url","result":null}
```

Desktop MCP OAuth sends `redirect_uri=http://localhost:8787/callback`. Zoom no longer accepts the hostname `localhost`. Cursor does not expose a setting to change that redirect.

Zoom Marketplace’s **OAuth Redirect URL** field also rejects loopback URLs such as `http://127.0.0.1:8788/callback` with **Wrong URL format**. That field requires **HTTPS** on a public hostname. A General app that is not registered as a native/PKCE client cannot save `127.0.0.1` there.

## Working path in this OS

`zoom-bridge` is the **always-on** Zoom connection. Cursor starts it from `%USERPROFILE%\.cursor\mcp.json`. Tokens refresh automatically. Catalog `plugin-zoom-zoom` will keep showing `needsAuth`; that is expected and unused.

Redirect Zoom must store (exact string, including `/index.html`):

`https://fitd-fash.github.io/cursor-zoom-oauth-callback/index.html`

That page is already live. It forwards the browser to `http://127.0.0.1:8765/callback`, which only your machine sees. You do not add `127.0.0.1` in Marketplace.

Runtime files (not in git):

- `%USERPROFILE%\.cursor\zoom-mcp\connect.mjs`
- `%USERPROFILE%\.cursor\zoom-mcp\client-info.json` (Client ID + Secret)
- `%USERPROFILE%\.cursor\zoom-mcp\tokens.json` (created after login)
- `C:\ProgramData\cursor-zoom-mcp\headers.txt` (Bearer header; path has no spaces so Windows `npx` does not split it)

Tracked copies of the non-secret scripts live in `ops/integrations/zoom/`.

Global `~/.cursor/mcp.json` server name: `zoom-bridge`.

After changing `connect.mjs`, **Settings → MCP → zoom-bridge → Reload**. The running process still has the old script until then.

## You must do this in Zoom Marketplace

1. Open [Zoom App Marketplace](https://marketplace.zoom.us) → **Manage** → the **General** app used for Cursor.
2. **Basic Information → OAuth Information**.
3. Set **OAuth Redirect URL** (and the allow list) to:

   `https://fitd-fash.github.io/cursor-zoom-oauth-callback/index.html`

4. You may also keep `https://www.cursor.com/agents/mcp/oauth/callback`.
5. Do **not** add `http://localhost:8787/callback` or `http://127.0.0.1:8788/callback`. The form will show Wrong URL format; authorize would fail even if it saved.
6. Save. If the app is in development, use the **Development** allow list.

Do not switch GitHub accounts to edit the bounce repo unless you name `github-fitd-fash`.

## Client secret

Paste the same **App Credentials** Client ID and Client Secret already configured in **Cursor Settings → Plugins → Zoom** into `%USERPROFILE%\.cursor\zoom-mcp\client-info.json`. Never commit that file.

## After Marketplace + secret

Reload MCP (or restart Cursor) **after** a successful login. First-time login is a separate command so Cursor does not kill the MCP process while the browser is open:

`node "%USERPROFILE%\.cursor\zoom-mcp\connect.mjs" --login`

Token refresh without a browser:

`node "%USERPROFILE%\.cursor\zoom-mcp\connect.mjs" --refresh`

Catalog `plugin-zoom-zoom` may still show `needsAuth`; ignore it. Never click Authorize on that plugin.

If login times out, stop anything else bound to port **8765** (old local career-site serve used that port).

## Status

| Path | Status |
| --- | --- |
| Catalog Zoom plugin OAuth | **unsupported** until Cursor stops sending `localhost`. Leave installed; do not authenticate. |
| Marketplace `127.0.0.1` redirect | **unsupported** (Wrong URL format) |
| `zoom-bridge` via HTTPS bounce | **verified** tokens 20 Sep 2026. Tool calls need MCP reload after the Windows header-path fix. |
