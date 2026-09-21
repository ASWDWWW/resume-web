#!/usr/bin/env node
/**
 * Zoom MCP stdio bridge. Marketplace rejects http://127.0.0.1 and localhost
 * ("Wrong URL format"). OAuth uses the HTTPS GitHub Pages bounce, which
 * forwards to 127.0.0.1:8765/callback. Secrets stay in client-info.json.
 */
import { spawn } from "node:child_process";
import crypto from "node:crypto";
import fs from "node:fs";
import http from "node:http";
import https from "node:https";
import os from "node:os";
import path from "node:path";
import { URL } from "node:url";

const BOUNCE_REDIRECT_URI =
  "https://fitd-fash.github.io/cursor-zoom-oauth-callback/index.html";
const CALLBACK_HOST = "127.0.0.1";
const CALLBACK_PORT = 8765;
const CALLBACK_PATH = "/callback";
const PROXY_PORT = 8799;
const ZOOM_HOST = "mcp.zoom.us";
const ZOOM_MCP_PATH = "/mcp/zoom/streamable";
const TOKEN_URL = "https://zoom.us/oauth/token";
const AUTHORIZE_URL = "https://zoom.us/oauth/authorize";
const AUTH_TIMEOUT_MS = 5 * 60 * 1000;
const REFRESH_SKEW_MS = 5 * 60 * 1000;

const runtimeDir = path.join(os.homedir(), ".cursor", "zoom-mcp");
const infoPath = path.join(runtimeDir, "client-info.json");
const tokensPath = path.join(runtimeDir, "tokens.json");
const runtimeHeaderPath = path.join(runtimeDir, "headers.txt");
const headerDir = path.join(process.env.ProgramData || "C:\\ProgramData", "cursor-zoom-mcp");
fs.mkdirSync(headerDir, { recursive: true });
const headerPath = path.join(headerDir, "headers.txt");

function fail(message) {
  process.stderr.write(`${message}\n`);
  process.exit(1);
}

function base64Url(buffer) {
  return buffer
    .toString("base64")
    .replaceAll("+", "-")
    .replaceAll("/", "_")
    .replace(/=+$/u, "");
}

function pkcePair() {
  const verifier = base64Url(crypto.randomBytes(32));
  const challenge = base64Url(crypto.createHash("sha256").update(verifier).digest());
  return { verifier, challenge };
}

function basicAuth(clientId, clientSecret) {
  return `Basic ${Buffer.from(`${clientId}:${clientSecret}`).toString("base64")}`;
}

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function writeJson(filePath, value) {
  fs.writeFileSync(filePath, `${JSON.stringify(value, null, 2)}\n`, "utf8");
}

function writeHeaderFile(accessToken) {
  const line = `Authorization: Bearer ${accessToken}\n`;
  fs.writeFileSync(headerPath, line, "utf8");
  fs.writeFileSync(runtimeHeaderPath, line, "utf8");
}

async function postToken(clientId, clientSecret, body) {
  const response = await fetch(TOKEN_URL, {
    method: "POST",
    headers: {
      Authorization: basicAuth(clientId, clientSecret),
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams(body),
  });
  const text = await response.text();
  let payload;
  try {
    payload = JSON.parse(text);
  } catch {
    fail(`Zoom token endpoint returned non-JSON (${response.status}).`);
  }
  if (!response.ok || !payload.access_token) {
    const zoomMessage =
      typeof payload.error_description === "string"
        ? payload.error_description
        : typeof payload.reason === "string"
          ? payload.reason
          : text.slice(0, 300);
    fail(`Zoom token exchange failed (${response.status}): ${zoomMessage}`);
  }
  return {
    access_token: payload.access_token,
    refresh_token: payload.refresh_token ?? null,
    expires_at: Date.now() + Number(payload.expires_in ?? 3600) * 1000,
  };
}

function openBrowser(url) {
  const urlFile = path.join(runtimeDir, "authorize-url.txt");
  fs.writeFileSync(urlFile, `${url}\n`, "utf8");
  process.stderr.write(`OPEN_THIS_URL\n${url}\n`);
  if (process.platform === "win32") {
    spawn(
      "powershell.exe",
      ["-NoProfile", "-Command", `Start-Process '${url.replaceAll("'", "''")}'`],
      { detached: true, stdio: "ignore" },
    );
    return;
  }
  spawn(process.platform === "darwin" ? "open" : "xdg-open", [url], {
    detached: true,
    stdio: "ignore",
  });
}

function waitForAuthorizationCode() {
  const { verifier, challenge } = pkcePair();
  const state = base64Url(crypto.randomBytes(16));
  const authorize = new URL(AUTHORIZE_URL);
  authorize.searchParams.set("response_type", "code");
  authorize.searchParams.set("client_id", clientId);
  authorize.searchParams.set("redirect_uri", BOUNCE_REDIRECT_URI);
  authorize.searchParams.set("code_challenge", challenge);
  authorize.searchParams.set("code_challenge_method", "S256");
  authorize.searchParams.set("state", state);

  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => {
      server.close();
      reject(
        new Error(
          `Timed out waiting for Zoom consent. Register this exact HTTPS URL in Marketplace: ${BOUNCE_REDIRECT_URI}`,
        ),
      );
    }, AUTH_TIMEOUT_MS);

    const server = http.createServer((req, res) => {
      const reqUrl = new URL(req.url ?? "/", `http://${CALLBACK_HOST}:${CALLBACK_PORT}`);
      if (reqUrl.pathname !== CALLBACK_PATH) {
        res.writeHead(404);
        res.end("Not found");
        return;
      }
      const error = reqUrl.searchParams.get("error");
      const code = reqUrl.searchParams.get("code");
      const returnedState = reqUrl.searchParams.get("state");
      if (error) {
        res.writeHead(400, { "Content-Type": "text/plain; charset=utf-8" });
        res.end(`Zoom error: ${error}`);
        clearTimeout(timer);
        server.close();
        reject(new Error(`Zoom authorize error: ${error}`));
        return;
      }
      if (!code || returnedState !== state) {
        res.writeHead(400, { "Content-Type": "text/plain; charset=utf-8" });
        res.end("Missing code or mismatched state.");
        return;
      }
      res.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
      res.end("Zoom connected. You can close this tab and return to Cursor.");
      clearTimeout(timer);
      server.close();
      resolve({ code, verifier });
    });

    server.on("error", (error) => {
      clearTimeout(timer);
      if (error && error.code === "EADDRINUSE") {
        reject(
          new Error(
            `Port ${CALLBACK_PORT} is in use. Stop whatever is serving http://127.0.0.1:${CALLBACK_PORT} and retry.`,
          ),
        );
        return;
      }
      reject(error);
    });

    server.listen(CALLBACK_PORT, CALLBACK_HOST, () => {
      process.stderr.write(
        `Waiting for Zoom login. Marketplace redirect must be:\n${BOUNCE_REDIRECT_URI}\n`,
      );
      openBrowser(authorize.toString());
    });
  });
}

function tokensAreFresh(tokens) {
  return Boolean(
    tokens?.access_token &&
      typeof tokens.expires_at === "number" &&
      tokens.expires_at - REFRESH_SKEW_MS > Date.now(),
  );
}

async function ensureTokens(allowBrowser) {
  let tokens = null;
  if (fs.existsSync(tokensPath)) {
    try {
      tokens = readJson(tokensPath);
    } catch {
      tokens = null;
    }
  }
  if (tokensAreFresh(tokens)) {
    writeHeaderFile(tokens.access_token);
    return tokens;
  }
  if (tokens?.refresh_token) {
    try {
      const refreshed = await postToken(clientId, clientSecret, {
        grant_type: "refresh_token",
        refresh_token: tokens.refresh_token,
      });
      writeJson(tokensPath, refreshed);
      writeHeaderFile(refreshed.access_token);
      return refreshed;
    } catch {
      if (!allowBrowser) {
        fail("Zoom refresh failed. Run: node connect.mjs --login");
      }
      process.stderr.write("Zoom refresh failed; opening browser for a new login.\n");
    }
  }
  if (!allowBrowser) {
    fail(
      `No Zoom tokens. Complete login first:\nnode "${path.join(runtimeDir, "connect.mjs")}" --login`,
    );
  }
  const { code, verifier } = await waitForAuthorizationCode();
  const issued = await postToken(clientId, clientSecret, {
    grant_type: "authorization_code",
    code,
    redirect_uri: BOUNCE_REDIRECT_URI,
    code_verifier: verifier,
  });
  writeJson(tokensPath, issued);
  writeHeaderFile(issued.access_token);
  return issued;
}

function startTokenProxy(getAccessToken) {
  const server = http.createServer((req, res) => {
    const incomingPath = req.url ?? "/";
    if (incomingPath.includes("well-known") || incomingPath.includes("oauth")) {
      res.writeHead(404);
      res.end();
      return;
    }
    const token = getAccessToken();
    const headers = { ...req.headers, host: ZOOM_HOST };
    headers.authorization = `Bearer ${token}`;
    const upstream = https.request(
      {
        hostname: ZOOM_HOST,
        path: incomingPath,
        method: req.method,
        headers,
      },
      (upRes) => {
        res.writeHead(upRes.statusCode ?? 502, upRes.headers);
        upRes.pipe(res);
      },
    );
    upstream.on("error", (error) => {
      res.writeHead(502, { "Content-Type": "text/plain; charset=utf-8" });
      res.end(error instanceof Error ? error.message : "upstream error");
    });
    req.pipe(upstream);
  });
  return new Promise((resolve, reject) => {
    server.on("error", reject);
    server.listen(PROXY_PORT, CALLBACK_HOST, () => resolve(server));
  });
}

if (!fs.existsSync(infoPath)) {
  fail(
    `Missing ${infoPath}. Copy ops/integrations/zoom/client-info.example.json there and add client_id and client_secret.`,
  );
}

let info;
try {
  info = readJson(infoPath);
} catch (error) {
  const reason = error instanceof Error ? error.message : String(error);
  fail(`Could not read ${infoPath}: ${reason}`);
}

const clientSecret = typeof info.client_secret === "string" ? info.client_secret.trim() : "";
const clientId = typeof info.client_id === "string" ? info.client_id.trim() : "";
if (!clientId || !clientSecret || clientSecret.startsWith("PASTE_")) {
  fail(
    [
      "Zoom client_id and client_secret are required in client-info.json.",
      `Register this exact HTTPS redirect in Zoom Marketplace (http://127.0.0.1 is rejected as Wrong URL format):`,
      BOUNCE_REDIRECT_URI,
      `File: ${infoPath}`,
    ].join("\n"),
  );
}

const isLogin = process.argv.includes("--login");
const isRefresh = process.argv.includes("--refresh");
const tokens = await ensureTokens(isLogin);
if (isLogin) {
  process.stderr.write("LOGIN_OK\n");
  process.exit(0);
}
if (isRefresh) {
  process.stderr.write("REFRESH_OK\n");
  process.exit(0);
}

let accessToken = tokens.access_token;
writeHeaderFile(accessToken);

setInterval(() => {
  void (async () => {
    try {
      const next = await ensureTokens();
      accessToken = next.access_token;
    } catch (error) {
      const reason = error instanceof Error ? error.message : String(error);
      process.stderr.write(`Zoom token refresh failed: ${reason}\n`);
    }
  })();
}, 10 * 60 * 1000).unref();

await startTokenProxy(() => accessToken);

const npxCmd = process.platform === "win32" ? "npx.cmd" : "npx";
const child = spawn(
  npxCmd,
  [
    "-y",
    "mcp-remote@latest",
    `http://${CALLBACK_HOST}:${PROXY_PORT}${ZOOM_MCP_PATH}`,
    "--header-file",
    headerPath,
    "--header",
    "Authorization:${ZOOM_BRIDGE_AUTH}",
    "--disable-resource-parameter",
    "--allow-http",
  ],
  {
    stdio: "inherit",
    shell: false,
    env: {
      ...process.env,
      ZOOM_BRIDGE_AUTH: `Bearer ${accessToken}`,
    },
    windowsHide: true,
  },
);

child.on("exit", (code, signal) => {
  if (signal) {
    process.kill(process.pid, signal);
    return;
  }
  process.exit(code ?? 1);
});
