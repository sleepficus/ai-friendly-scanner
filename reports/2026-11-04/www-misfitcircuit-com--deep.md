# Is it AI friendly? — https://www.misfitcircuit.com/

Scanned from: scanner network (one vantage point). One vantage point, raw fetches only (no JavaScript run) — which is also what the AI crawlers get.

## Verdict

- The door is honest: every major AI bot that robots.txt welcomes actually gets the page.
- The page skeleton is clean: every link, button and form field carries a name an agent can read.
- Beyond the homepage: audited 25 of 36 pages found (cap 25, via sitemap https://www.misfitcircuit.com/sitemap.xml).
- Across the site, 1 forms hold 1 fields and every field carries a label.

## The door — declared vs actual

| Visitor | robots.txt says | Actually got |
|---|---|---|
| Browser (baseline) | — | 200 (17314 bytes, 388 ms) |
| GPTBot | allowed | served |
| ClaudeBot | allowed | served |
| Googlebot | allowed | served |

## What crawlers receive (no JavaScript)

- Readable words in the raw page: **979**
- Script tags on the page: 3
- App-shell container: none detected
- Page title: Stephen Luc · AI automation and agent systems — Misfit Circuit
- H1 headings: ['I lead crews of AI agents that do real business work, and build the tools that check it.']
- Meta description: yes

## Labels an agent navigates by

- Links: 42 total, **0 unnamed**
- Buttons: 1 total, **0 unnamed**
- Form fields: 0 total, **0 with no label**
- Images: 6 total, **0 with no alt attribute**

## Plumbing

- robots.txt: found (status 200, 3 directive lines)
- Sitemap: https://www.misfitcircuit.com/sitemap.xml — status 200, 36 entries

## Information only — NOT scored

- llms.txt: status 200, 1032 bytes. (Research: no major AI system is known to read it; presence proves nothing.)
- Structured data (JSON-LD) blocks: 1. (Research: helps systems understand content; controlled studies show it does not buy AI citations.)

## Site crawl (v0.2a)

- Source: sitemap https://www.misfitcircuit.com/sitemap.xml.
- URLs found: 36; pages audited: 25 (cap 25 — the cap cut the list).
- (The sections above describe the homepage; this section and the next cover the whole crawl.)

| Page | Forms | Fields | Unlabelled fields |
|---|---|---|---|
| https://www.misfitcircuit.com/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/about/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/agent-diaries/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/agent-diaries/compaction/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/agent-diaries/way/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/apartment/ | 0 | 3 | 0 |
| https://www.misfitcircuit.com/approach/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/crew/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/doorway/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/doorway/library/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/for-agents/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/for-agents/recover-your-place/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/labs/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/labs/chad-faye-discussion/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/labs/hearthside/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/labs/warmstart/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/neighborhood/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/php-check/ | 1 | 1 | 0 |
| https://www.misfitcircuit.com/tools/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/tools/boss-battles/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/tools/composer/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/tools/content-engine/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/tools/continuity/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/tools/foundry/ | 0 | 0 | 0 |
| https://www.misfitcircuit.com/tools/in-the-lab/ | 0 | 0 | 0 |

## Forms — field by field (v0.2a)

1 forms, 1 fields, **0 with no label** across the crawl. A field's label is what a screen reader announces and what an agent navigates by; a placeholder is not a label. Every field below is quoted as the element actually found — the receipt, not a summary of it.

### Form 1 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.misfitcircuit.com/php-check/
- Sends to: https://www.misfitcircuit.com/php-check/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="version" id="version-input" placeholder="e.g. 8.2.29" autocomplete="off">` | Your PHP version | version | text | no | off |

Submit control: "Check it" — `<button type="submit">`

## Not checked in v0.2a

- A live agent task run (the Inspector, v0.2b) — protocol specced at goals/ai-friendly-website-scanner/files/inspector-run-protocol-2026-11-04.md; it runs through a browser seat, not this code.
- Rendered-vs-raw diff in a real browser (v0.2a measures the raw response, which is what crawlers receive).
- Anything past a submit click; login flows.
