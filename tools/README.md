# publications/tools/

Build pipeline for Terrene Foundation white papers.

## What's here

- `render.py` — Markdown → PDF renderer (pandoc + Chrome headless)
- `print.css` — cover-page and `@page` print rules (paired with `render.py`)

The body stylesheet lives at `../style.css` (the publications root) so that any
GitHub or web preview of the Markdown picks it up. `render.py` references that
file by relative path; do not duplicate it here.

## Requirements

- macOS with `/Applications/Google Chrome.app` (the script hard-codes the path)
- `pandoc` on `PATH`
- Python 3.9+ (no third-party packages)

## Usage

From anywhere, render one or more papers into the publications/ root:

```bash
python3 tools/render.py PACT-Core-Thesis.md
```

Or render into a scratch directory for review:

```bash
python3 tools/render.py PACT-Core-Thesis.md --out /tmp/preview
```

The script:

1. Splits the Markdown into a title block (everything above the first `---`)
   and the body.
2. Runs pandoc on the body to produce an HTML fragment.
3. Wraps the body in a cover page + paper layout, links `style.css` and
   `print.css`, and drops a per-paper `*.runtitle.css` for the running footer.
4. Drives Chrome headless `--print-to-pdf` to produce the final PDF.

Per-paper artefacts written to the output directory:

- `<stem>.html` — the wrapped HTML fed to Chrome
- `<stem>.runtitle.css` — running-title shim (Chrome paged mode does not
  support CSS `string-set`)
- `<stem>.pdf` — the deliverable

## Title-block conventions

The renderer expects every paper to open with:

```markdown
# <Title>: <Classifier>

**<Subtitle>**

_<Tagline 1>_
_<Tagline 2>_

**Author**: …
**Status**: …
**Version**: …
**License**: CC BY 4.0

---
```

Anything above the first standalone `---` is the title block. The renderer
extracts: title, classifier (after the colon), subtitle (first `**bold**`
line), taglines (`_italic_` lines), and the labelled metadata fields.
