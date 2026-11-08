# Is it AI friendly? — https://www.misfitcircuit.com/

Scanned from: scanner network (one vantage point). One vantage point, raw fetches only (no JavaScript run) — which is also what the AI crawlers get.

## Verdict

- The door is honest: every major AI bot that robots.txt welcomes actually gets the page.
- The page skeleton is clean: every link, button and form field carries a name an agent can read.
- robots.txt is a preamble with nothing filled in: it states no rules and sets no AI content signals (search / ai-input / ai-train are all unstated).
- No working sitemap (fetch of https://www.misfitcircuit.com/sitemap.xml returned 404) — crawlers get no map of the site.

## The door — declared vs actual

| Visitor | robots.txt says | Actually got |
|---|---|---|
| Browser (baseline) | — | 200 (36337 bytes, 577 ms) |
| GPTBot | allowed | served |
| ClaudeBot | allowed | served |
| Googlebot | allowed | served |

## What crawlers receive (no JavaScript)

- Readable words in the raw page: **2134**
- Script tags on the page: 3
- App-shell container: none detected
- Page title: Stephen Luc · I build the systems behind marketing — Misfit Circuit
- H1 headings: ['I help teams explain their products and  build the systems behind their marketing.']
- Meta description: yes

## Labels an agent navigates by

- Links: 81 total, **0 unnamed**
- Buttons: 1 total, **0 unnamed**
- Form fields: 0 total, **0 with no label**
- Images: 8 total, **0 with no alt attribute**

## Plumbing

- robots.txt: found (status 200, 0 directive lines)
- Sitemap: https://www.misfitcircuit.com/sitemap.xml — status 404, — entries

## Information only — NOT scored

- llms.txt: status 404. (Research: no major AI system is known to read it; presence proves nothing.)
- Structured data (JSON-LD) blocks: 1. (Research: helps systems understand content; controlled studies show it does not buy AI citations.)

## Not checked in v0

- A live agent task run ('find the price', 'start the signup') — the v0.2 step, and the one no incumbent does.
- Rendered-vs-raw diff in a real browser (v0 measures the raw response, which is what crawlers receive).
- Pages beyond the homepage; login flows; checkout.
