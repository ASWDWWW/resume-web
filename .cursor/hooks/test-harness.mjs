import { spawnSync } from "node:child_process";
import { join } from "node:path";

const root = process.cwd();
const dummyLiveKey = ["sk", "live", "a".repeat(24)].join("_");
const cases = [
  ["shell-guard.mjs", { command: "git config user.email x" }, (o) => o.permission === "deny"],
  ["shell-guard.mjs", { command: "git status" }, (o) => o.permission === "allow"],
  ["shell-guard.mjs", { command: "git push --force origin main" }, (o) => o.permission === "deny"],
  ["shell-guard.mjs", { command: "gh auth switch" }, (o) => o.permission === "ask"],
  ["mcp-guard.mjs", { tool_name: "discord_send_message", tool_input: "{}", mcp_server_name: "discord" }, (o) => o.permission === "ask"],
  ["mcp-guard.mjs", { tool_name: "get_me", tool_input: "{}", mcp_server_name: "github" }, (o) => o.permission === "allow"],
  ["secret-prompt.mjs", { prompt: "hello" }, (o) => o.continue === true],
  ["secret-prompt.mjs", { prompt: dummyLiveKey }, (o) => o.continue === false],
  ["restricted-read.mjs", { file_path: "C:\\repo\\.env" }, (o) => o.permission === "deny"],
  ["restricted-read.mjs", { file_path: "C:\\repo\\AGENTS.md" }, (o) => o.permission === "allow"],
  ["audit-edit.mjs", { file_path: "C:\\repo\\ops\\CONTROL-CENTER.md", edits: [] }, () => true],
];

let failed = 0;
for (const [script, input, check] of cases) {
  const result = spawnSync(process.execPath, [join(root, ".cursor", "hooks", script)], {
    input: JSON.stringify(input),
    encoding: "utf8",
  });
  let parsed;
  try {
    parsed = JSON.parse(result.stdout || "{}");
  } catch {
    parsed = { _raw: result.stdout, _err: result.stderr };
  }
  const ok = result.status === 0 && check(parsed);
  if (!ok) {
    failed += 1;
    console.log("FAIL", script, input, parsed, result.stderr);
  } else {
    console.log("PASS", script, parsed.permission ?? parsed.continue ?? "ok");
  }
}
process.exit(failed === 0 ? 0 : 1);
