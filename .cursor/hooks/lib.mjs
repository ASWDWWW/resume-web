import { appendFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(fileURLToPath(import.meta.url));
const logDir = join(root, "logs");

const SECRET_KEYS = /password|secret|token|authorization|api[_-]?key|private[_-]?key|cookie|credential|sk_live|sk_test/i;

export async function readInput() {
  const chunks = [];
  for await (const chunk of process.stdin) chunks.push(chunk);
  const raw = Buffer.concat(chunks).toString("utf8").trim();
  if (!raw) return {};
  try {
    return JSON.parse(raw);
  } catch {
    return { _parseError: true, _raw: raw.slice(0, 500) };
  }
}

export function redact(value) {
  if (value == null) return value;
  if (typeof value === "string") {
    return value
      .replace(/\bsk_live_[A-Za-z0-9]{8,}/g, "sk_live_[REDACTED]")
      .replace(/\bsk_test_[A-Za-z0-9]{8,}/g, "sk_test_[REDACTED]")
      .replace(/\bAKIA[0-9A-Z]{16}\b/g, "AKIA[REDACTED]")
      .replace(/-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----/g, "[REDACTED_PRIVATE_KEY]")
      .replace(/\bgho_[A-Za-z0-9]{20,}/g, "gho_[REDACTED]")
      .replace(/\bghp_[A-Za-z0-9]{20,}/g, "ghp_[REDACTED]");
  }
  if (Array.isArray(value)) return value.map(redact);
  if (typeof value === "object") {
    const out = {};
    for (const [key, nested] of Object.entries(value)) {
      out[key] = SECRET_KEYS.test(key) ? "[REDACTED]" : redact(nested);
    }
    return out;
  }
  return value;
}

export function logEvent(event, payload) {
  mkdirSync(logDir, { recursive: true });
  const line = JSON.stringify({
    ts: new Date().toISOString(),
    event,
    ...redact(payload),
  });
  appendFileSync(join(logDir, "events.jsonl"), `${line}\n`);
}

export function reply(obj) {
  process.stdout.write(JSON.stringify(obj));
}
