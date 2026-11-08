# Is it AI friendly? — https://www.mozilla.org/

Scanned from: scanner network (one vantage point). One vantage point, raw fetches only (no JavaScript run) — which is also what the AI crawlers get.

## Verdict

- The door is honest: every major AI bot that robots.txt welcomes actually gets the page.
- The page skeleton is clean: every link, button and form field carries a name an agent can read.
- No working sitemap (fetch of https://www.mozilla.org/sitemap.xml returned 404) — crawlers get no map of the site.

## The door — declared vs actual

| Visitor | robots.txt says | Actually got |
|---|---|---|
| Browser (baseline) | — | 200 (47808 bytes, 522 ms) |
| GPTBot | allowed | served |
| ClaudeBot | allowed | served |
| Googlebot | allowed | served |

## What crawlers receive (no JavaScript)

- Readable words in the raw page: **314**
- Script tags on the page: 8
- App-shell container: none detected
- Page title: Internet for people, not profit — Mozilla Global
- H1 headings: ['Choose your language or locale to browse Mozilla.org']
- Meta description: yes

## Labels an agent navigates by

- Links: 135 total, **0 unnamed**
- Buttons: 5 total, **0 unnamed**
- Form fields: 0 total, **0 with no label**
- Images: 11 total, **0 with no alt attribute**

## Plumbing

- robots.txt: found (status 200, 3 directive lines)
- Sitemap: https://www.mozilla.org/sitemap.xml — status 404, — entries

## Information only — NOT scored

- llms.txt: status 404. (Research: no major AI system is known to read it; presence proves nothing.)
- Structured data (JSON-LD) blocks: 0. (Research: helps systems understand content; controlled studies show it does not buy AI citations.)

## Not checked in v0

- A live agent task run ('find the price', 'start the signup') — the v0.2 step, and the one no incumbent does.
- Rendered-vs-raw diff in a real browser (v0 measures the raw response, which is what crawlers receive).
- Pages beyond the homepage; login flows; checkout.
