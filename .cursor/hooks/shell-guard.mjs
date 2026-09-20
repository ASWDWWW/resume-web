import { readInput, logEvent, reply } from "./lib.mjs";

const input = await readInput();
const command = String(input.command || "");
const lower = command.toLowerCase();

function decide() {
  if (/\bgit\s+config\b/.test(lower)) {
    return {
      permission: "deny",
      user_message: "Blocked: this workspace forbids updating git config.",
      agent_message: "Do not run git config. Report the needed setting instead.",
    };
  }

  const force = /--force|--force-with-lease|\s-f(\s|$)/.test(lower);
  const pushMain = /\bgit\s+push\b/.test(lower) && /\b(main|master)\b/.test(lower);
  if (force && pushMain) {
    return {
      permission: "deny",
      user_message: "Blocked: force-push to main/master is not allowed.",
      agent_message: "Force-push to main/master is denied by workspace hooks.",
    };
  }

  if (/\bgh\s+auth\s+switch\b/.test(lower) || /\bgh\s+auth\s+login\b/.test(lower)) {
    return {
      permission: "ask",
      user_message: "This changes the active GitHub account. Confirm the target identity before continuing.",
      agent_message: "Account switch requires explicit user confirmation. Do not silently fall back to another login.",
    };
  }

  if (/\bfirebase\s+deploy\b/.test(lower) || /\bstripe\b/.test(lower) && /\blive\b/.test(lower)) {
    return {
      permission: "ask",
      user_message: "This may change production hosting or live payments. Confirm environment and authority.",
      agent_message: "Production deploy or live Stripe action needs explicit authorization.",
    };
  }

  return { permission: "allow" };
}

const decision = decide();
logEvent("beforeShellExecution", {
  permission: decision.permission,
  command: command.slice(0, 500),
  cwd: input.cwd,
});
reply(decision);
