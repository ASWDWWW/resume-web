import { fail, git, gitAuthed, invokedAsCli, preparePushIdentity } from "./identity.mjs";

function currentBranch() {
  const result = git(["rev-parse", "--abbrev-ref", "HEAD"]);
  if (result.status !== 0) {
    fail((result.stderr || "Could not read the current branch").trim());
  }
  return (result.stdout || "").trim();
}

function hasUpstream() {
  const result = git(["rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"]);
  return result.status === 0 && Boolean((result.stdout || "").trim());
}

function pushArgs(branch) {
  const extra = process.argv.slice(2);
  if (extra.length > 0) return ["push", ...extra];
  if (hasUpstream()) return ["push"];
  return ["push", "-u", "origin", branch];
}

function isForceToDefault(args, branch) {
  const joined = args.join(" ");
  const force = /(?:^|\s)(?:--force|--force-with-lease|-f)(?:\s|$)/.test(joined);
  const namesDefault =
    branch === "main" ||
    branch === "master" ||
    args.includes("main") ||
    args.includes("master");
  return force && namesDefault;
}

if (!invokedAsCli(import.meta.url)) {
  fail("push.mjs is a CLI script");
}

const branch = currentBranch();
const args = pushArgs(branch);
if (isForceToDefault(args, branch)) {
  fail("Force-push to main/master is not allowed.");
}

let prepared;
try {
  prepared = preparePushIdentity();
} catch (error) {
  fail(error.message || String(error));
}

process.stdout.write(`Pushing as ${prepared.identity.login} to ${prepared.identity.remote}\n`);

const result = gitAuthed(args, prepared.identity.login, prepared.token, {
  stdio: "inherit",
});

if (result.status !== 0) {
  process.stderr.write(
    `Push failed as ${prepared.identity.login}. Do not switch GitHub accounts and do not show an account picker.\n`,
  );
  process.exit(result.status || 1);
}
