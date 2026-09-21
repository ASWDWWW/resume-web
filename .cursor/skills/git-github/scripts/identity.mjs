import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { resolve } from "node:path";

const OWNER_LOGIN = {
  ASWDWWW: "ASWDWWW",
  "FITD-fash": "FITD-fash",
};

export function invokedAsCli(metaUrl) {
  try {
    const self = resolve(fileURLToPath(metaUrl)).toLowerCase();
    const argv1 = resolve(process.argv[1] || "").toLowerCase();
    return self === argv1;
  } catch {
    return false;
  }
}

export function run(file, args, opts = {}) {
  return spawnSync(file, args, {
    encoding: "utf8",
    windowsHide: true,
    ...opts,
  });
}

export function git(args, opts = {}) {
  return run("git", args, opts);
}

function ghFile() {
  return process.platform === "win32" ? "gh.exe" : "gh";
}

export function gh(args, opts = {}) {
  const env = {
    ...process.env,
    GH_PROMPT_DISABLED: "1",
    ...(opts.env || {}),
  };
  let result = run(ghFile(), args, { ...opts, env });
  if (result.error && result.error.code === "ENOENT") {
    result = run("gh", args, { ...opts, env });
  }
  return result;
}

export function originUrl() {
  const result = git(["remote", "get-url", "origin"]);
  if (result.status !== 0) {
    throw new Error((result.stderr || result.stdout || "origin remote is missing").trim());
  }
  return (result.stdout || "").trim();
}

export function parseRemote(url) {
  const https = url.match(/^https?:\/\/(?:([^/@]+)@)?github\.com\/([^/]+)\/([^/]+?)(?:\.git)?$/i);
  if (https) {
    return {
      protocol: "https",
      username: https[1] || "",
      owner: https[2],
      repo: https[3],
    };
  }
  const ssh = url.match(/^git@github\.com:([^/]+)\/([^/]+?)(?:\.git)?$/i);
  if (ssh) {
    return { protocol: "ssh", username: "", owner: ssh[1], repo: ssh[2] };
  }
  throw new Error(`Unsupported origin URL: ${url}`);
}

export function requiredLogin(owner) {
  const login = OWNER_LOGIN[owner];
  if (!login) {
    throw new Error(
      `No GitHub login is routed for owner ${owner}. This workspace defaults to ASWDWWW; do not pick another account.`,
    );
  }
  return login;
}

export function resolveIdentity() {
  const remote = originUrl();
  const parsed = parseRemote(remote);
  const login = requiredLogin(parsed.owner);
  return { login, remote, ...parsed };
}

export function pinnedHttpsUrl(identity) {
  return `https://${identity.login}@github.com/${identity.owner}/${identity.repo}.git`;
}

export function ensureRemoteUser(identity = resolveIdentity()) {
  if (identity.protocol !== "https") return identity;
  const wanted = pinnedHttpsUrl(identity);
  if (identity.remote === wanted) return identity;
  const result = git(["remote", "set-url", "origin", wanted]);
  if (result.status !== 0) {
    throw new Error((result.stderr || "Failed to pin origin username").trim());
  }
  return { ...identity, remote: wanted, username: identity.login };
}

export function tokenFor(login) {
  const result = gh(["auth", "token", "--user", login]);
  const token = (result.stdout || "").trim();
  if (result.status !== 0 || !token) {
    throw new Error(
      `Required GitHub identity ${login} is not available in gh. Do not switch accounts and do not show an account picker. Sign in as ${login}, then retry.`,
    );
  }
  return token;
}

export function tokenLogin(token) {
  const result = gh(["api", "user", "--jq", ".login"], {
    env: {
      ...process.env,
      GH_TOKEN: token,
      GH_PROMPT_DISABLED: "1",
    },
  });
  const login = (result.stdout || "").trim();
  if (result.status !== 0 || !login) {
    throw new Error("Could not verify the GitHub token login. Do not fall back to another account.");
  }
  return login;
}

export function gitAuthEnv(login, token) {
  const nullFile = process.platform === "win32" ? "NUL" : "/dev/null";
  return {
    ...process.env,
    GH_TOKEN: token,
    GH_PROMPT_DISABLED: "1",
    GIT_TERMINAL_PROMPT: "0",
    GCM_INTERACTIVE: "never",
    GH_USER: login,
    GIT_CONFIG_NOSYSTEM: "1",
    GIT_CONFIG_GLOBAL: nullFile,
    GIT_CONFIG_SYSTEM: nullFile,
  };
}

export function gitAuthed(args, login, token, opts = {}) {
  const basic = Buffer.from(`x-access-token:${token}`, "utf8").toString("base64");
  return git(
    [
      "-c",
      "credential.helper=",
      "-c",
      `credential.https://github.com.username=${login}`,
      "-c",
      `http.https://github.com/.extraHeader=AUTHORIZATION: basic ${basic}`,
      ...args,
    ],
    {
      ...opts,
      env: gitAuthEnv(login, token),
    },
  );
}

export function fail(message) {
  process.stderr.write(`${message}\n`);
  process.exit(1);
}

export function preparePushIdentity() {
  const identity = ensureRemoteUser();
  const token = tokenFor(identity.login);
  const verified = tokenLogin(token);
  if (verified !== identity.login) {
    throw new Error(
      `Origin requires ${identity.login}, but the token is ${verified}. Stop. Do not pick another account.`,
    );
  }
  return { identity, token };
}

if (invokedAsCli(import.meta.url)) {
  try {
    const { identity } = preparePushIdentity();
    process.stdout.write(
      `${JSON.stringify({
        login: identity.login,
        owner: identity.owner,
        repo: identity.repo,
        remote: identity.remote,
        verified: true,
      })}\n`,
    );
  } catch (error) {
    fail(error.message || String(error));
  }
}
