import { readInput, logEvent, reply } from "./lib.mjs";

const ASK_NAME = /send|create_post|create_article|delete_|deploy|refund|payout|charge|create_invite|bulk_ban|kick_member|ban_member|timeout_member|create_scheduled_event|edit_webhook|delete_webhook|update_user|auth_set_sms|remoteconfig_update|realtimedatabase_set|firestore_delete|firestore_update|storage_/i;
const ASK_INPUT = /sk_live|"livemode"\s*:\s*true|live_mode|fashiobusiness|investor@|mailto:/i;

const input = await readInput();
const toolName = String(input.tool_name || "");
const toolInput = String(input.tool_input || "");
const server = String(input.mcp_server_name || "");
const blob = `${toolName} ${toolInput}`;

function decide() {
  if (ASK_NAME.test(toolName) || ASK_INPUT.test(blob)) {
    return {
      permission: "ask",
      user_message: `Confirm external MCP action ${server}:${toolName}. Check account identity before allowing.`,
      agent_message: "This MCP call can affect an external account or production data. Do not switch accounts if it fails. Wait for confirmation.",
    };
  }
  return { permission: "allow" };
}

const decision = decide();
logEvent("beforeMCPExecution", {
  permission: decision.permission,
  mcp_server_name: server,
  tool_name: toolName,
});
reply(decision);
