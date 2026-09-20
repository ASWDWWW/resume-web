import { readInput, logEvent, reply } from "./lib.mjs";

const LIVE_SECRET = /\bsk_live_[A-Za-z0-9]{16,}\b/;
const AWS_KEY = /\bAKIA[0-9A-Z]{16}\b/;
const PRIVATE_KEY = /-----BEGIN [A-Z ]*PRIVATE KEY-----/;
const GITHUB_TOKEN = /\bgh[pousr]_[A-Za-z0-9]{20,}\b/;

const input = await readInput();
const prompt = String(input.prompt || "");
const blocked = LIVE_SECRET.test(prompt) || AWS_KEY.test(prompt) || PRIVATE_KEY.test(prompt) || GITHUB_TOKEN.test(prompt);

logEvent("beforeSubmitPrompt", { blocked, length: prompt.length });

if (blocked) {
  reply({
    continue: false,
    user_message: "Prompt looks like it contains a live secret or private key. Remove the secret and retry. Do not paste credentials into chat.",
  });
} else {
  reply({ continue: true });
}
