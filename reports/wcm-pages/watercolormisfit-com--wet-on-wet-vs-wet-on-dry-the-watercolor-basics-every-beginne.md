# Is it AI friendly? — https://watercolormisfit.com/wet-on-wet-vs-wet-on-dry-the-watercolor-basics-every-beginner-should-know/

Scanned from: scanner network (one vantage point). One vantage point, raw fetches only (no JavaScript run) — which is also what the AI crawlers get.

## Verdict

- The door is honest: every major AI bot that robots.txt welcomes actually gets the page.
- Navigation bumps in the page skeleton: 3 of 31 links have no name an agent can read.

## The door — declared vs actual

| Visitor | robots.txt says | Actually got |
|---|---|---|
| Browser (baseline) | — | 200 (41625 bytes, 365 ms) |
| GPTBot | allowed | served |
| ClaudeBot | allowed | served |
| Googlebot | allowed | served |

## What crawlers receive (no JavaScript)

- Readable words in the raw page: **722**
- Script tags on the page: 8
- App-shell container: none detected
- Page title: Wet-on-Wet vs. Wet-on-Dry Watercolor: When to Use Each
- H1 headings: ['Wet-on-Wet vs. Wet-on-Dry Watercolor: When to Use Each']
- Meta description: yes

## Labels an agent navigates by

- Links: 31 total, **3 unnamed** (e.g. https://watercolormisfit.com/wp-content/uploads/2025/08/wet-on-wet-definition3.jpg, https://watercolormisfit.com/wp-content/uploads/2025/08/wet-on-dry-definition.jpg, https://watercolormisfit.com/wp-content/uploads/2025/08/wet-on-dry-and-wet-on-wet.jpg)
- Buttons: 3 total, **0 unnamed**
- Form fields: 1 total, **0 with no label**
- Images: 7 total, **0 with no alt attribute**

## Plumbing

- robots.txt: found (status 200, 5 directive lines)
- Sitemap: https://watercolormisfit.com/wp-sitemap.xml — status 200, 5 entries, a sitemap index

## Information only — NOT scored

- llms.txt: status 404. (Research: no major AI system is known to read it; presence proves nothing.)
- Structured data (JSON-LD) blocks: 1. (Research: helps systems understand content; controlled studies show it does not buy AI citations.)

## Not checked in v0

- A live agent task run ('find the price', 'start the signup') — the v0.2 step, and the one no incumbent does.
- Rendered-vs-raw diff in a real browser (v0 measures the raw response, which is what crawlers receive).
- Pages beyond the homepage; login flows; checkout.
