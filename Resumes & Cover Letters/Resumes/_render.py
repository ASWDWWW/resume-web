#!/usr/bin/env python3
"""Render job-title resumes from markdown into one-page HTML."""

from __future__ import annotations

import re
from pathlib import Path

DIR = Path(__file__).resolve().parent
CSS = (DIR / "resume.css").read_text()
CSS_CORPORATE = (DIR / "resume-corporate.css").read_text()

TITLES = [
    "01-Forward-Deployed-Engineer",
    "02-Full-Stack-Engineer",
    "03-Software-Engineer",
    "04-Product-Engineer",
    "05-AI-Product-Engineer",
    "06-Rillet-Consultant",
    "07-Data-AI-Platform-Engineer",
    "08-AI-Automation-Engineer",
    "09-Brellium-Software-Engineer",
]

CORPORATE = set(TITLES)
def inline(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    return text


def split_pair(line: str) -> tuple[str, str] | None:
    if " | " not in line:
        return None
    left, right = line.split(" | ", 1)
    return left.strip(), right.strip()


def parse_header(lines: list[str]) -> tuple[str, str, str, int]:
    name = lines[0].lstrip("# ").strip()
    i = 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    role = ""
    if i < len(lines) and lines[i].startswith("**") and " | " not in lines[i] and not lines[i].startswith("## "):
        role = lines[i].replace("**", "").strip()
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
    contact = inline(lines[i]) if i < len(lines) else ""
    i += 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    return name, role, contact, i


def render_md(md: str, *, corporate: bool) -> str:
    lines = md.strip().splitlines()
    name, role, contact, i = parse_header(lines)
    css = CSS_CORPORATE if corporate else CSS
    heading = name if corporate else name.upper()

    body: list[str] = []
    summary: list[str] = []
    while i < len(lines) and not lines[i].startswith("## "):
        if lines[i].strip():
            summary.append(inline(lines[i].strip()))
        i += 1

    if summary:
        body.append(f'<p class="summary">{" ".join(summary)}</p>')

    section = ""
    job_open = False
    list_open = False
    edu_open = False

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

    def close_edu() -> None:
        nonlocal edu_open
        if edu_open:
            body.append("</div>")
            edu_open = False

    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            close_job()
            close_edu()
            if section.startswith("Skills"):
                body.append("</div>")
            section = line[3:].strip()
            body.append(f"<h2>{section}</h2>")
            if section.startswith("Skills"):
                body.append('<div class="skills">')
            elif section == "Education" and not corporate:
                body.append('<div class="edu">')
            i += 1
            continue

        if not line.strip():
            i += 1
            continue

        if section.startswith("Skills"):
            body.append(f"<p>{inline(line)}</p>")
            i += 1
            continue

        if section == "Education" and corporate:
            pair = split_pair(line)
            if line.startswith("**") and pair:
                close_edu()
                org, loc = pair
                body.append('<div class="edu-block">')
                edu_open = True
                body.append(
                    '<div class="edu-head">'
                    f'<span class="edu-org">{inline(org)}</span>'
                    f'<span class="edu-loc">{inline(loc)}</span>'
                    "</div>"
                )
                i += 1
                continue
            if pair and edu_open:
                degree, dates = pair
                body.append(
                    '<div class="edu-sub">'
                    f'<span class="edu-degree">{inline(degree)}</span>'
                    f'<span class="edu-dates">{inline(dates)}</span>'
                    "</div>"
                )
                i += 1
                continue
            body.append(f"<p>{inline(line)}</p>")
            i += 1
            continue

        if section == "Education" and not corporate:
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
        pair = split_pair(line)
        block_class = "project" if section == "Projects" else "job"

        if line.startswith("**") and pair:
            close_job()
            org, loc = pair
            body.append(f'<div class="{block_class}">')
            job_open = True
            body.append(
                '<div class="job-head">'
                f'<span class="job-org">{inline(org)}</span>'
                f'<span class="job-loc">{inline(loc)}</span>'
                "</div>"
            )
            i += 1
            continue

        if pair and job_open:
            title, dates = pair
            body.append(
                '<div class="job-sub">'
                f'<span class="job-role">{inline(title)}</span>'
                f'<span class="job-dates">{inline(dates)}</span>'
                "</div>"
            )
            i += 1
            continue

        if line.startswith("*") and line.endswith("*"):
            body.append(f'<div class="job-sub"><span>{inline(line)}</span></div>')
            i += 1
            continue

        if line.startswith("**"):
            close_job()
            body.append(f'<div class="{block_class}">')
            job_open = True
            body.append(f'<div class="job-head"><span class="job-title">{inline(line)}</span></div>')
            i += 1
            continue

        body.append(f"<p>{inline(line)}</p>")
        i += 1

    close_job()
    close_edu()
    if section.startswith("Skills"):
        body.append("</div>")

    role_html = f'<p class="role">{role}</p>' if role else ""
    title = f"{name} — {role}" if role else name

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>{title}</title>
  <style>{css}</style>
</head>
<body>
  <div class="page">
    <header>
      <h1>{heading}</h1>
      {role_html}
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
        out = DIR / title / "html" / f"{title}.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)
        print(out.relative_to(DIR))


if __name__ == "__main__":
    main()
