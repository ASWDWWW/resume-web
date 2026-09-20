import { readInput, logEvent, reply } from "./lib.mjs";

const DENY = /(\.env$)|(\.env\.)|(credentials\.json$)|(id_rsa$)|(\.pem$)|(serviceAccount.*\.json$)/i;

const input = await readInput();
const filePath = String(input.file_path || "");
const deny = DENY.test(filePath);

logEvent("beforeReadFile", { deny, file_path: filePath });

if (deny) {
  reply({
    permission: "deny",
    user_message: "Blocked read of a likely secret file. Folders are not a security boundary; keep secrets out of the repo and out of the model context.",
  });
} else {
  reply({ permission: "allow" });
}
