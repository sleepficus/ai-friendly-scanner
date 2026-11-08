# Is it AI friendly? — https://watercolormisfit.com/

Scanned from: scanner network (one vantage point). One vantage point, raw fetches only (no JavaScript run) — which is also what the AI crawlers get.

## Verdict

- The door is honest: every major AI bot that robots.txt welcomes actually gets the page.
- Navigation bumps in the page skeleton: 3 of 33 links have no name an agent can read.
- Beyond the homepage: audited 25 of 217 pages found (cap 25, via sitemap index https://watercolormisfit.com/wp-sitemap.xml (5 child sitemaps read)).
- Across the site, 25 forms hold 25 fields and every field carries a label.

## The door — declared vs actual

| Visitor | robots.txt says | Actually got |
|---|---|---|
| Browser (baseline) | — | 200 (37305 bytes, 464 ms) |
| GPTBot | allowed | served |
| ClaudeBot | allowed | served |
| Googlebot | allowed | served |

## What crawlers receive (no JavaScript)

- Readable words in the raw page: **323**
- Script tags on the page: 8
- App-shell container: none detected
- Page title: Watercolor Misfit® | Modern Watercolor Tutorials
- H1 headings: ['Watercolor   that breaks   the rules.']
- Meta description: yes

## Labels an agent navigates by

- Links: 33 total, **3 unnamed** (e.g. https://watercolormisfit.com/10-things-im-letting-go-of-this-year-to-boost-creativity-and-avoid-burnout/, https://watercolormisfit.com/my-favorite-limited-watercolor-palette-plus-affordable-student-grade-alternatives/, https://watercolormisfit.com/wet-on-wet-vs-wet-on-dry-the-watercolor-basics-every-beginner-should-know/)
- Buttons: 3 total, **0 unnamed**
- Form fields: 1 total, **0 with no label**
- Images: 14 total, **0 with no alt attribute**

## Plumbing

- robots.txt: found (status 200, 5 directive lines)
- Sitemap: https://watercolormisfit.com/wp-sitemap.xml — status 200, 5 entries, a sitemap index

## Information only — NOT scored

- llms.txt: status 404. (Research: no major AI system is known to read it; presence proves nothing.)
- Structured data (JSON-LD) blocks: 1. (Research: helps systems understand content; controlled studies show it does not buy AI citations.)

## Site crawl (v0.2a)

- Source: sitemap index https://watercolormisfit.com/wp-sitemap.xml (5 child sitemaps read).
- URLs found: 217; pages audited: 25 (cap 25 — the cap cut the list).
- (The sections above describe the homepage; this section and the next cover the whole crawl.)

| Page | Forms | Fields | Unlabelled fields |
|---|---|---|---|
| https://watercolormisfit.com/ | 1 | 1 | 0 |
| https://watercolormisfit.com/watercolor-101-pan-paints-the-advantages-and-disadvantages/ | 1 | 1 | 0 |
| https://watercolormisfit.com/watercolor-paints-101-the-advantages-and-disadvantages-in-chart-form/ | 1 | 1 | 0 |
| https://watercolormisfit.com/student-and-artist-grade-paint/ | 1 | 1 | 0 |
| https://watercolormisfit.com/watercolor-paints-101-concentrates-the-advantages-disadvantages/ | 1 | 1 | 0 |
| https://watercolormisfit.com/how-to-shade/ | 1 | 1 | 0 |
| https://watercolormisfit.com/watercolor-basic-supplies-my-top-5-brushes/ | 1 | 1 | 0 |
| https://watercolormisfit.com/how-to-draw-ink-a-hyacinth-flower/ | 1 | 1 | 0 |
| https://watercolormisfit.com/the-easiest-way-to-paint-a-hyacinth-flower/ | 1 | 1 | 0 |
| https://watercolormisfit.com/how-to-paint-a-moon-with-watercolor/ | 1 | 1 | 0 |
| https://watercolormisfit.com/splatter-paint-effect/ | 1 | 1 | 0 |
| https://watercolormisfit.com/the-difference-between-transparent-and-opaque-watercolors/ | 1 | 1 | 0 |
| https://watercolormisfit.com/best-watercolor-tool-youll-ever-own/ | 1 | 1 | 0 |
| https://watercolormisfit.com/organizeartstudio/ | 1 | 1 | 0 |
| https://watercolormisfit.com/top-watercolor-tips-for-beginners/ | 1 | 1 | 0 |
| https://watercolormisfit.com/5-watercolor-exercises-for-creative-block/ | 1 | 1 | 0 |
| https://watercolormisfit.com/how-to-paint-a-whimsical-autumn-leaf/ | 1 | 1 | 0 |
| https://watercolormisfit.com/how-to-mix-watercolors-purple/ | 1 | 1 | 0 |
| https://watercolormisfit.com/tracing-onto-watercolor-paper-tip02/ | 1 | 1 | 0 |
| https://watercolormisfit.com/watercolorpalettes/ | 1 | 1 | 0 |
| https://watercolormisfit.com/paint-perfect-flat-wash-tip07/ | 1 | 1 | 0 |
| https://watercolormisfit.com/paper_difference/ | 1 | 1 | 0 |
| https://watercolormisfit.com/paint-watercolor-whale-7-easy-steps/ | 1 | 1 | 0 |
| https://watercolormisfit.com/fear-of-starting/ | 1 | 1 | 0 |
| https://watercolormisfit.com/watercolor-beginner-tutorial/ | 1 | 1 | 0 |

## Forms — field by field (v0.2a)

25 forms, 25 fields, **0 with no label** across the crawl. A field's label is what a screen reader announces and what an agent navigates by; a placeholder is not a label. Every field below is quoted as the element actually found — the receipt, not a summary of it.

### Form 1 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 2 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/watercolor-101-pan-paints-the-advantages-and-disadvantages/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 3 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/watercolor-paints-101-the-advantages-and-disadvantages-in-chart-form/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 4 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/student-and-artist-grade-paint/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 5 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/watercolor-paints-101-concentrates-the-advantages-disadvantages/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 6 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/how-to-shade/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 7 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/watercolor-basic-supplies-my-top-5-brushes/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 8 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/how-to-draw-ink-a-hyacinth-flower/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 9 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/the-easiest-way-to-paint-a-hyacinth-flower/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 10 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/how-to-paint-a-moon-with-watercolor/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 11 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/splatter-paint-effect/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 12 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/the-difference-between-transparent-and-opaque-watercolors/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 13 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/best-watercolor-tool-youll-ever-own/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 14 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/organizeartstudio/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 15 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/top-watercolor-tips-for-beginners/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 16 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/5-watercolor-exercises-for-creative-block/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 17 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/how-to-paint-a-whimsical-autumn-leaf/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 18 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/how-to-mix-watercolors-purple/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 19 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/tracing-onto-watercolor-paper-tip02/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 20 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/watercolorpalettes/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 21 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/paint-perfect-flat-wash-tip07/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 22 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/paper_difference/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 23 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/paint-watercolor-whale-7-easy-steps/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 24 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/fear-of-starting/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

### Form 25 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://watercolormisfit.com/watercolor-beginner-tutorial/
- Sends to: https://watercolormisfit.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="search" name="s" id="wm-site-search" placeholder="Search articles…" autocomplete="off">` | Search articles | s | search | no | off |

Submit control: "Search" — `<button type="submit" aria-label="Search">`

## Not checked in v0.2a

- A live agent task run (the Inspector, v0.2b) — protocol specced at goals/ai-friendly-website-scanner/files/inspector-run-protocol-2026-11-04.md; it runs through a browser seat, not this code.
- Rendered-vs-raw diff in a real browser (v0.2a measures the raw response, which is what crawlers receive).
- Anything past a submit click; login flows.
