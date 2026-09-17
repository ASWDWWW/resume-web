#!/usr/bin/env python3
"""Render top-5 resumes from markdown into one-page HTML."""

from __future__ import annotations

import re
from pathlib import Path

DIR = Path(__file__).resolve().parent
CSS = (DIR / "resume.css").read_text()

FILES = [
    "01-Forward-Deployed-Engineer.md",
    "02-Full-Stack-Engineer.md",
    "03-Software-Engineer.md",
    "04-Product-Engineer.md",
    "05-AI-Product-Engineer.md",
]


def inline(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    return text


def render_md(md: str) -> str:
    lines = md.strip().splitlines()
    name = lines[0].lstrip("# ").strip()
    role = lines[1].replace("**", "").strip()
    contact = inline(lines[3])

    body: list[str] = []
    i = 5
    summary: list[str] = []
    while i < len(lines) and not lines[i].startswith("## "):
        if lines[i].strip():
            summary.append(inline(lines[i].strip()))
        i += 1

    body.append(f'<p class="summary">{"".join(summary)}</p>')

    section = ""
    job_open = False
    list_open = False

    def close_list() -> None:
        nonlocal list_open
        if list_open:
            body.append("</ul>")
            list_open = False

    def close_job() -> None:
        nonlocal job_open
        close_list()
        if job_open:
            body.append("</div>")
            job_open = False

    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            close_job()
            if section in {"Education", "Skills"}:
                body.append("</div>")
            section = line[3:].strip()
            cls = "skills" if section == "Skills" else "edu" if section == "Education" else ""
            body.append(f"<h2>{section}</h2>")
            if cls:
                body.append(f'<div class="{cls}">')
            i += 1
            continue

        if not line.strip():
            i += 1
            continue

        if section in {"Education", "Skills"}:
            body.append(f"<p>{inline(line)}</p>")
            i += 1
            continue

        if line.startswith("- "):
            if not list_open:
                body.append("<ul>")
                list_open = True
            body.append(f"<li>{inline(line[2:])}</li>")
            i += 1
            continue

        close_list()
        if line.startswith("*") and line.endswith("*"):
            body.append(f'<div class="job-sub"><span>{inline(line)}</span></div>')
            i += 1
            continue

        # Job title line: **Company** — Role
        if line.startswith("**"):
            close_job()
            body.append('<div class="job">')
            job_open = True
            body.append(f'<div class="job-head"><span class="job-title">{inline(line)}</span></div>')
            i += 1
            continue

        body.append(f"<p>{inline(line)}</p>")
        i += 1

    close_job()
    if section in {"Education", "Skills"}:
        body.append("</div>")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>{name} — {role}</title>
  <style>{CSS}</style>
</head>
<body>
  <div class="page">
    <header>
      <h1>{name.upper()}</h1>
      <p class="role">{role}</p>
      <p class="contact">{contact}</p>
    </header>
    {"".join(body)}
  </div>
</body>
</html>
"""


def main() -> None:
    for name in FILES:
        html = render_md((DIR / name).read_text())
        out = DIR / name.replace(".md", ".html")
        out.write_text(html)
        print(out.name)


if __name__ == "__main__":
    main()
