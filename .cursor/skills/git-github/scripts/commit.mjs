import { mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { fail, git, invokedAsCli } from "./identity.mjs";

function readArg(flag) {
  const index = process.argv.indexOf(flag);
  if (index === -1 || index === process.argv.length - 1) return "";
  return process.argv[index + 1];
}

function commitMessage() {
  const file = readArg("--file");
  if (file) return readFileSync(file, "utf8").replace(/\r\n/g, "\n").trim();
  const direct = readArg("--message");
  if (direct) return direct.replace(/\r\n/g, "\n").trim();
  return "";
}

function stagedFiles() {
  const result = git(["diff", "--cached", "--name-only"]);
  if (result.status !== 0) {
    fail((result.stderr || "Could not list staged files").trim());
  }
  return (result.stdout || "")
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
}

if (!invokedAsCli(import.meta.url)) {
  fail("commit.mjs is a CLI script");
}

const skipVerify = process.argv.includes("--no-verify");
if (skipVerify) {
  fail("Refusing --no-verify. Hooks must run.");
}

const message = commitMessage();
if (!message) {
  fail("Pass a commit message with --message or --file.");
}

const staged = stagedFiles();
if (staged.length === 0) {
  fail("Nothing staged. Stage the intended files, then retry.");
}

const dir = mkdtempSync(join(tmpdir(), "resume-web-commit-"));
const path = join(dir, "COMMIT_EDITMSG");
try {
  writeFileSync(path, `${message}\n`, "utf8");
  const result = git(["commit", "-F", path], { stdio: "inherit" });
  if (result.status !== 0) {
    process.exit(result.status || 1);
  }
} finally {
  rmSync(dir, { recursive: true, force: true });
}

const status = git(["status", "-sb"]);
process.stdout.write(status.stdout || "");
