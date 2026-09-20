import { readInput, logEvent, reply } from "./lib.mjs";

const input = await readInput();
const filePath = String(input.file_path || "");
const restricted = /[\\/]ops[\\/](restricted|owner[\\/]private)[\\/]/i.test(filePath);

logEvent("afterFileEdit", {
  file_path: filePath,
  restricted,
  editCount: Array.isArray(input.edits) ? input.edits.length : 0,
});

reply({});
