# Is it AI friendly? — https://www.mozillafoundation.org/

Scanned from: scanner network (one vantage point). One vantage point, raw fetches only (no JavaScript run) — which is also what the AI crawlers get.

## Verdict

- The page skeleton is clean: every link, button and form field carries a name an agent can read.

## The door — declared vs actual

| Visitor | robots.txt says | Actually got |
|---|---|---|
| Browser (baseline) | — | 200 (70711 bytes, 1896 ms) |
| GPTBot | disallowed | http 403 |
| ClaudeBot | disallowed | http 403 |
| Googlebot | allowed | served |

## What crawlers receive (no JavaScript)

- Readable words in the raw page: **691**
- Script tags on the page: 15
- App-shell container: none detected
- Page title: Welcome to Mozilla Foundation
                
            
            
                
                - Mozilla Foundation
- H1 headings: (none)
- Meta description: yes

## Labels an agent navigates by

- Links: 47 total, **0 unnamed**
- Buttons: 6 total, **0 unnamed**
- Form fields: 6 total, **0 with no label**
- Images: 18 total, **0 with no alt attribute**

## Plumbing

- robots.txt: found (status 200, 70 directive lines)
- Declared AI content signals: search=yes, ai-train=no, use=reference
- Sitemap: https://www.mozillafoundation.org/sitemap.xml — status 200, 10 entries, a sitemap index

## Information only — NOT scored

- llms.txt: status 404. (Research: no major AI system is known to read it; presence proves nothing.)
- Structured data (JSON-LD) blocks: 0. (Research: helps systems understand content; controlled studies show it does not buy AI citations.)

## Not checked in v0

- A live agent task run ('find the price', 'start the signup') — the v0.2 step, and the one no incumbent does.
- Rendered-vs-raw diff in a real browser (v0 measures the raw response, which is what crawlers receive).
- Pages beyond the homepage; login flows; checkout.
