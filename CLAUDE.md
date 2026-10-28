# cicm-study: instructions for Claude

Interactive HTML study pages for the CICM First Part exam. Filename convention:
`<YEAR><SITTING>_Q<NN>_<Topic>_Interactive.html` (e.g. `2009A_Q20_Organophosphate_Interactive.html`).

## Delivering a page: ALWAYS publish it as an Artifact

The user reads these pages in the Claude app. A raw `.html` file sent as a file
card (SendUserFile) shows up as **source code**, not a rendered page. So:

1. Keep the standalone file in the repo (full `<!DOCTYPE html>` page, works offline). Commit and push it.
2. Make a publish copy in the scratchpad:
   `python3 scripts/artifact_copy.py <page>.html <scratchpad>/publish/<Name>.html`
   (the Artifact viewer supplies its own doctype/html/head/body wrapper).
3. Publish that copy with the **Artifact** tool (private by default): a short `<title>`
   that names the topic (e.g. "Organophosphate Poisoning"), a one-line `description`
   with the paper/question code, and a one-word `icon` on first publish.
4. Give the user the artifact link. Do **not** rely on SendUserFile for HTML pages;
   if a file card is also wanted, send it *in addition to* the link, never instead of it.
5. To update a page later, re-publish to the same artifact URL (pass `url`) so the link stays stable.

This applies even when a request says "don't publish/deploy": a private Artifact is
how the user views the page. Public sharing (GitHub Pages, public links) still needs an explicit ask.

## Page requirements (match existing pages)
- Self-contained: inline CSS/JS, no external assets.
- Works at phone width (~390px) with no sideways page scroll; ≥16px side gutter; wide tables stack or scroll inside their own container.
- Dark theme committed on purpose: set `:root { color-scheme: dark; }` and explicit body background.
- Sticky headers use `top: env(safe-area-inset-top, 0px)`.
- Respect `prefers-reduced-motion`.
- Cite sources on the page; tag simplified illustrations separately from clinical guidance.
