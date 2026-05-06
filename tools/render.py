#!/usr/bin/env python3
"""Render Terrene Foundation white papers to professional PDF.

Pipeline:
  Markdown -> (pandoc) -> body HTML
  Cover-page HTML + body HTML + style.css + print.css -> wrapped HTML
  Chrome headless --print-to-pdf -> PDF
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PUBLICATIONS_ROOT = ROOT.parent
STYLE_SRC = PUBLICATIONS_ROOT / "style.css"
PRINT_SRC = ROOT / "print.css"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


@dataclass
class TitleBlock:
    title: str
    subtitle: str
    taglines: list[str]
    author: str
    status: str
    version: str
    license: str


def parse_title_block(md: str) -> tuple[TitleBlock, str]:
    """Split a paper into its title block and body.

    The title block is everything from the leading `# Title` line through the
    first standalone `---` separator. Returns (TitleBlock, body_md).
    """
    sep = re.search(r"\n---\n", md)
    if not sep:
        raise SystemExit("No `---` separator found; cannot locate title block.")
    head = md[: sep.start()].strip()
    body = md[sep.end():].lstrip("\n")

    lines = [ln.strip() for ln in head.splitlines() if ln.strip()]

    title = ""
    bolds: list[str] = []  # **...** lines
    italics: list[str] = []  # _..._ lines
    fields: dict[str, str] = {}

    for line in lines:
        if line.startswith("# ") and not title:
            title = line[2:].strip()
            continue
        m = re.match(r"\*\*([^*]+)\*\*\s*:\s*(.+)", line)
        if m:
            fields[m.group(1).strip().lower()] = m.group(2).strip()
            continue
        m = re.match(r"\*\*([^*]+)\*\*$", line)
        if m:
            bolds.append(m.group(1).strip())
            continue
        m = re.match(r"_([^_]+)_$", line)
        if m:
            italics.append(m.group(1).strip())
            continue

    subtitle = bolds[0] if bolds else ""
    taglines = italics

    return (
        TitleBlock(
            title=title,
            subtitle=subtitle,
            taglines=taglines,
            author=fields.get("author", ""),
            status=fields.get("status", ""),
            version=fields.get("version", ""),
            license=fields.get("license", "CC BY 4.0"),
        ),
        body,
    )


def render_body_html(body_md: str) -> str:
    """Run pandoc to convert markdown body to HTML fragment."""
    proc = subprocess.run(
        [
            "pandoc",
            "--from=gfm+smart+tex_math_dollars+yaml_metadata_block",
            "--to=html5",
            "--wrap=preserve",
            "--no-highlight",
        ],
        input=body_md.encode("utf-8"),
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr.decode("utf-8", errors="replace"))
        raise SystemExit(f"pandoc failed (exit {proc.returncode})")
    return proc.stdout.decode("utf-8")


def short_title(title: str) -> str:
    """Pull a short running-title from a paper title.

    "CARE: A Core Thesis" -> "CARE"
    "PACT: A Working Architecture" -> "PACT"
    """
    return title.split(":", 1)[0].strip()


def paper_kind(title: str) -> str:
    """The trailing classifier after the colon."""
    if ":" in title:
        return title.split(":", 1)[1].strip()
    return "Core Thesis"


def cover_html(tb: TitleBlock) -> str:
    short = short_title(tb.title)
    kind = paper_kind(tb.title)
    taglines_html = "\n".join(
        f'<div class="cover-tagline">{html.escape(t)}</div>' for t in tb.taglines
    )
    meta_rows = []
    if tb.author:
        meta_rows.append(("Author", tb.author))
    if tb.status:
        meta_rows.append(("Status", tb.status))
    if tb.version:
        meta_rows.append(("Version", tb.version))
    if tb.license:
        meta_rows.append(("License", tb.license))
    meta_rows.append(("Series", "Terrene Foundation White Paper"))
    meta_html = "\n".join(
        f'<div class="row"><div class="label">{html.escape(label)}</div>'
        f'<div class="value">{html.escape(value)}</div></div>'
        for label, value in meta_rows
    )

    return f"""
<section class="cover">
  <div class="imprint"><strong>Terrene Foundation</strong> &nbsp;|&nbsp; Open Standards for Enterprise AI Governance</div>
  <div class="title-block">
    <div class="paper-tag">{html.escape(kind)}</div>
    <h1 class="cover-title">{html.escape(short)}</h1>
    <div class="cover-subtitle">{html.escape(tb.subtitle)}</div>
    {taglines_html}
    <div class="cover-meta">{meta_html}</div>
  </div>
  <div class="cover-footer">
    <div>terrene.foundation</div>
    <div>{html.escape(tb.version)}</div>
  </div>
</section>
"""


def wrap_html(tb: TitleBlock, body_html: str) -> str:
    short = short_title(tb.title)
    body_html = re.sub(
        r"<h1[^>]*>",
        f'<h1 class="body-h1 running-title" data-runtitle="{html.escape(short)}">',
        body_html,
        count=1,
    )
    body_html = body_html.replace("<h1>", '<h1 class="body-h1">')

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{html.escape(tb.title)}</title>
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="print.css">
</head>
<body>
{cover_html(tb)}
<main class="paper">
<header class="paper-header">
  <h1 class="body-h1 running-title" data-runtitle="{html.escape(short)}">{html.escape(tb.title)}</h1>
  <p class="paper-byline"><em>{html.escape(tb.subtitle)}</em></p>
  <p class="paper-byline">{html.escape(tb.author)} &middot; Version {html.escape(tb.version)} &middot; {html.escape(tb.license)}</p>
</header>
{body_html}
</main>
</body>
</html>
"""


def chrome_print(html_path: Path, pdf_path: Path) -> None:
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        "--virtual-time-budget=10000",
        f"--print-to-pdf={pdf_path}",
        f"file://{html_path}",
    ]
    proc = subprocess.run(cmd, capture_output=True, check=False)
    if proc.returncode != 0 or not pdf_path.exists():
        sys.stderr.write(proc.stderr.decode("utf-8", errors="replace"))
        sys.stderr.write(proc.stdout.decode("utf-8", errors="replace"))
        raise SystemExit(f"Chrome print-to-pdf failed for {html_path}")


def per_paper_css(tb: TitleBlock) -> str:
    short = short_title(tb.title)
    # Chrome headless paged mode doesn't support CSS string-set / string() in
    # @page margin boxes, so we inject the running title literally per paper.
    footer_left = f"{short} — {tb.subtitle}"
    return (
        "@page { @bottom-left { content: \""
        + footer_left.replace('"', '\\"')
        + "\"; font-family: 'Georgia','Times New Roman',serif; font-size: 9pt; color: #888; } }\n"
        "@page :first { @bottom-left { content: none; } }\n"
    )


def render_paper(md_path: Path, out_dir: Path) -> Path:
    md = md_path.read_text(encoding="utf-8")
    tb, body_md = parse_title_block(md)
    body_html = render_body_html(body_md)
    document = wrap_html(tb, body_html)

    stem = md_path.stem
    html_path = out_dir / f"{stem}.html"
    pdf_path = out_dir / f"{stem}.pdf"
    paper_css_path = out_dir / f"{stem}.runtitle.css"
    paper_css_path.write_text(per_paper_css(tb), encoding="utf-8")
    document = document.replace(
        '<link rel="stylesheet" href="print.css">',
        '<link rel="stylesheet" href="print.css">\n'
        f'<link rel="stylesheet" href="{stem}.runtitle.css">',
    )
    html_path.write_text(document, encoding="utf-8")

    chrome_print(html_path, pdf_path)
    return pdf_path


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("paths", nargs="+", help="Markdown files to render.")
    p.add_argument(
        "--out",
        default=str(PUBLICATIONS_ROOT),
        help="Output directory (default: the publications/ repo root).",
    )
    args = p.parse_args()

    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    for src in args.paths:
        src_path = Path(src).resolve()
        target_style = out_dir / "style.css"
        target_print = out_dir / "print.css"
        if target_style.resolve() != STYLE_SRC.resolve():
            shutil.copy(STYLE_SRC, target_style)
        if target_print.resolve() != PRINT_SRC.resolve():
            shutil.copy(PRINT_SRC, target_print)
        pdf = render_paper(src_path, out_dir)
        print(f"OK  {src_path.name} -> {pdf}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
