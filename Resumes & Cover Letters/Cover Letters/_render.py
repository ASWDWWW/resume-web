#!/usr/bin/env python3
"""Render job-title cover letters from markdown into one-page HTML."""

from __future__ import annotations

import re
from pathlib import Path

DIR = Path(__file__).resolve().parent
CSS = (DIR / "cover-letter.css").read_text()
CSS_CORPORATE = (DIR / "cover-letter-corporate.css").read_text()

TITLES = [
    "01-Forward-Deployed-Engineer",
    "02-Full-Stack-Engineer",
    "03-Software-Engineer",
    "04-Product-Engineer",
    "05-AI-Product-Engineer",
    "06-Rillet-Consultant",
    "07-Data-AI-Platform-Engineer",
    "08-AI-Automation-Engineer",
]

CORPORATE = set(TITLES)

DATE_RE = re.compile(r"^[A-Z][a-z]+ \d{1,2}, \d{4}$")


def inline(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    return text


def paragraph_class(text: str) -> str:
    stripped = text.strip()
    if DATE_RE.match(stripped):
        return "date"
    if stripped.lower().startswith("re:"):
        return "re"
    if stripped.lower().startswith("dear "):
        return "salutation"
    if stripped.lower().rstrip(",") in {"sincerely", "best", "best regards", "regards"}:
        return "closing"
    if stripped in {"Zakiy T. Manigo", "Zakiy Manigo"}:
        return "signature"
    return ""


def render_md(md: str, *, corporate: bool) -> str:
    lines = md.strip().splitlines()
    name = lines[0].lstrip("# ").strip()
    role = lines[1].replace("**", "").strip()
    contact = inline(lines[3])
    css = CSS_CORPORATE if corporate else CSS
    heading = name if corporate else name.upper()

    body: list[str] = []
    para: list[str] = []
    address: list[str] = []
    capturing_address = False

    def flush_address() -> None:
        nonlocal capturing_address
        if not address:
            capturing_address = False
            return
        spans = "".join(f"<span>{inline(line)}</span>" for line in address)
        body.append(f'<p class="address">{spans}</p>')
        address.clear()
        capturing_address = False

    def flush() -> None:
        if not para:
            return
        text = inline(" ".join(para))
        cls = paragraph_class(para[0])
        attr = f' class="{cls}"' if cls else ""
        body.append(f"<p{attr}>{text}</p>")
        para.clear()

    for line in lines[5:]:
        stripped = line.strip()
        if not stripped:
            flush()
            if address:
                flush_address()
            continue

        if corporate and DATE_RE.match(stripped) and not para and not address:
            flush()
            body.append(f'<p class="date">{inline(stripped)}</p>')
            capturing_address = True
            continue

        if capturing_address:
            low = stripped.lower()
            if low.startswith("re:") or low.startswith("dear "):
                flush_address()
            else:
                address.append(stripped)
                continue

        para.append(stripped)
    flush()
    flush_address()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>{name} — {role} Cover Letter</title>
  <style>{css}</style>
</head>
<body>
  <div class="page">
    <header>
      <h1>{heading}</h1>
      <p class="role">{role}</p>
      <p class="contact">{contact}</p>
    </header>
    {"".join(body)}
  </div>
</body>
</html>
"""


def main() -> None:
    for title in TITLES:
        md_path = DIR / title / "md" / f"{title}.md"
        html = render_md(md_path.read_text(), corporate=title in CORPORATE)
        html_out = DIR / title / "html" / f"{title}.html"
        html_out.parent.mkdir(parents=True, exist_ok=True)
        html_out.write_text(html)
        (DIR / title / "pdf").mkdir(parents=True, exist_ok=True)
        print(html_out.relative_to(DIR))


if __name__ == "__main__":
    main()
