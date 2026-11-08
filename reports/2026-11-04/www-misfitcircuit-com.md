# Is it AI friendly? — https://www.misfitcircuit.com/

Scanned from: scanner network (one vantage point). One vantage point, raw fetches only (no JavaScript run) — which is also what the AI crawlers get.

## Verdict

- The door is honest: every major AI bot that robots.txt welcomes actually gets the page.
- The page skeleton is clean: every link, button and form field carries a name an agent can read.

## The door — declared vs actual

| Visitor | robots.txt says | Actually got |
|---|---|---|
| Browser (baseline) | — | 200 (17314 bytes, 692 ms) |
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

## Not checked in v0

- A live agent task run ('find the price', 'start the signup') — the v0.2 step, and the one no incumbent does.
- Rendered-vs-raw diff in a real browser (v0 measures the raw response, which is what crawlers receive).
- Pages beyond the homepage; login flows; checkout.
