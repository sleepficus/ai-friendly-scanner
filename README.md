# AI-Friendly Scanner v0

Stephen's question as a tool: **when an AI agent visits your website, what
does it actually hit?** Not what the site declares — what the visitor gets.

Built on the Spank Yard research pass (RESEARCH.md, this folder): the static
checklist version of this product is already owned by free incumbents
(Cloudflare's isitagentready.com, Google's Lighthouse agentic category) and
the composite 0–100 score is theatre. This scanner therefore:

- **Fetches as the real bots** (GPTBot, ClaudeBot, Googlebot) and compares
  the actual response with what robots.txt declares — catching paper-only
  bans and silent blocks, the gap no checklist measures.
- **Measures the raw response** (no JavaScript — the major AI crawlers run
  none): readable words, app-shell detection, title/H1.
- **Audits the page skeleton the way an agent reads it**: unnamed links,
  buttons and unlabelled form fields, with counts and examples. An image's
  alt text counts as the name of a link that wraps it, like a real
  accessibility tree.
- **Checks the plumbing**: robots.txt (including whether it is a
  content-signals preamble with nothing filled in) and sitemap reality.
- Reports llms.txt and JSON-LD as **information only, never scored** —
  research: no major AI system is known to read llms.txt, and controlled
  studies show structured data does not buy AI citations.
- **Has no score.** The verdict is plain English with the counts attached.

## Run it

    python3 scanner.py https://example.com/ [--out reports/]
    python3 scanner.py https://example.com/ --deep [--cap 25] [--out reports/]
    python3 -B -m unittest discover   # 23 tests

Stdlib only. Reports land in reports/ as Markdown plus a JSON receipts file.

## v0.2a — forms and the crawl (2026-11-04)

`--deep` keeps the v0 homepage scan and adds:

- **A site crawl**: the sitemap's URLs (a sitemap index's children
  included), falling back to the homepage's own links when no usable
  sitemap exists. Same host only, capped at 25 pages by default — and
  the report says the found-vs-audited counts out loud when the cap
  cuts the list.
- **A field-by-field form audit** on every crawled page: each input's
  label (or **ABSENT** — a placeholder is not a label), name, type,
  required marker and autocomplete attribute, quoted as the element
  actually found; the submit control's accessible name; and what the
  form appears to be for, printed as an *inference* with its evidence,
  never as a fact.
- Still **no score**. Plain English, counts attached.

## Not checked

- A live agent task run ("find the price", "start the signup") — the
  Inspector, v0.2b. Protocol specced, not run. It executes through a
  browser-driving seat, not this code.
- Rendered-vs-raw diff in a real browser (the scanner measures the raw
  response, which is what crawlers receive).
- Anything past a submit click; login flows; forms injected by
  JavaScript after load (not in the raw skeleton — the same blindness
  the crawlers have, and stated as such).
- Fields outside a <form> element are counted per page but only
  form-grouped fields get the field-by-field table.

## Status

Built 2026-10-23 (v0), revived and extended 2026-11-04 (v0.2a).
v0.2a was independently audited and certified (CERTIFY-WITH-FINDINGS;
the findings were fixed and re-verified — see AUDIT-REPORT.md).
23/23 tests passing. Published publicly 2026-11-08.

Part of a small family of tools asking what websites look like to
visitors who perceive differently — AI agents today, and the humans
who will visit through agent companions tomorrow. Companion piece:
the Second Look rendered-vs-raw diff (github.com/sleepficus/second-look).

## License

MIT — see LICENSE.
