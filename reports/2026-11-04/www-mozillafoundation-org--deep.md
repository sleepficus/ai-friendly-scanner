# Is it AI friendly? — https://www.mozillafoundation.org/

Scanned from: scanner network (one vantage point). One vantage point, raw fetches only (no JavaScript run) — which is also what the AI crawlers get.

## Verdict

- The page skeleton is clean: every link, button and form field carries a name an agent can read.
- Beyond the homepage: audited 25 of 3380 pages found (cap 25, via sitemap index https://www.mozillafoundation.org/sitemap.xml (10 child sitemaps read)).
- Across the site, 80 forms hold 170 fields and every field carries a label.

## The door — declared vs actual

| Visitor | robots.txt says | Actually got |
|---|---|---|
| Browser (baseline) | — | 200 (70711 bytes, 1444 ms) |
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

## Site crawl (v0.2a)

- Source: sitemap index https://www.mozillafoundation.org/sitemap.xml (10 child sitemaps read).
- URLs found: 3380; pages audited: 25 (cap 25 — the cap cut the list).
- (The sections above describe the homepage; this section and the next cover the whole crawl.)

| Page | Forms | Fields | Unlabelled fields |
|---|---|---|---|
| https://www.mozillafoundation.org/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/ca/festival/ | 4 | 10 | 0 |
| https://www.mozillafoundation.org/ca/festival/tracks/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/ca/festival/tracks/developers-wilding/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/ca/festival/about/ | 4 | 10 | 0 |
| https://www.mozillafoundation.org/ca/festival/newsletter/ | 4 | 10 | 0 |
| https://www.mozillafoundation.org/ca/festival/faq/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/ca/festival/volunteer/ | 4 | 10 | 0 |
| https://www.mozillafoundation.org/en/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/nabiha-syed/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/angela-plohman/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/michael-whitney/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/kristen-spangler/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/lindsey-dodson/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/lauren-hendry-parsons/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/shing-suiter/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/amanda-lee-gaffar/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/steven-azeka/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/tekia-stokes/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/dandre-walker/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/press-center/ | 4 | 10 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/press-center/091625-mozilla-festival-schedule/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/press-center/nothing-personal-magazine-launch/ | 3 | 6 | 0 |
| https://www.mozillafoundation.org/en/meet-mozilla/press-center/imaginative-intelligences-hollywood/ | 3 | 6 | 0 |

## Forms — field by field (v0.2a)

80 forms, 170 fields, **0 with no label** across the crawl. A field's label is what a screen reader announces and what an agent navigates by; a placeholder is not a label. Every field below is quoted as the element actually found — the receipt, not a summary of it.

### Form 1 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 2 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/
- Sends to: https://www.mozillafoundation.org/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 3 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 4 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/ca/festival/
- Sends to: https://www.mozillafoundation.org/ca/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Cerca" aria-label="Cerca">` | Cerca | query | text | no | absent |

Submit control: "Cerca 
     Cerca" — `<button type="submit" aria-label="Cerca">`

### Form 5 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/ca/festival/
- Sends to: https://www.mozillafoundation.org/ca/festival/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Correu electrònic" aria-label="Correu electrònic" required>` | Correu electrònic | email | email | yes | absent |
| `<select name="country" aria-label="País" required>` | País | country | text | yes | absent |
| `<select name="language" aria-label="Idioma" required>` | Idioma | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | Accepto que Mozilla gestioni la meva informació tal com s'explica en aquest  Avís de privacitat . | privacy | checkbox | no | absent |

Submit control: "S'està carregant...
             
             
               Subscriviu-vos 
               Subscriviu-vos" — `<button type="submit">`

### Form 6 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/ca/festival/
- Sends to: https://www.mozillafoundation.org/ca/festival/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Correu electrònic" aria-label="Correu electrònic" required>` | Correu electrònic | email | email | yes | absent |
| `<select name="country" aria-label="País" required>` | País | country | text | yes | absent |
| `<select name="language" aria-label="Idioma" required>` | Idioma | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | Accepto que Mozilla gestioni la meva informació tal com s'explica en aquest  Avís de privacitat . | privacy | checkbox | no | absent |

Submit control: "S'està carregant...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 7 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/ca/festival/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Idioma | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 8 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/ca/festival/tracks/
- Sends to: https://www.mozillafoundation.org/ca/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Cerca" aria-label="Cerca">` | Cerca | query | text | no | absent |

Submit control: "Cerca 
     Cerca" — `<button type="submit" aria-label="Cerca">`

### Form 9 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/ca/festival/tracks/
- Sends to: https://www.mozillafoundation.org/ca/festival/tracks/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Correu electrònic" aria-label="Correu electrònic" required>` | Correu electrònic | email | email | yes | absent |
| `<select name="country" aria-label="País" required>` | País | country | text | yes | absent |
| `<select name="language" aria-label="Idioma" required>` | Idioma | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | Accepto que Mozilla gestioni la meva informació tal com s'explica en aquest  Avís de privacitat . | privacy | checkbox | no | absent |

Submit control: "S'està carregant...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 10 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/ca/festival/tracks/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Idioma | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 11 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/ca/festival/tracks/developers-wilding/
- Sends to: https://www.mozillafoundation.org/ca/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Cerca" aria-label="Cerca">` | Cerca | query | text | no | absent |

Submit control: "Cerca 
     Cerca" — `<button type="submit" aria-label="Cerca">`

### Form 12 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/ca/festival/tracks/developers-wilding/
- Sends to: https://www.mozillafoundation.org/ca/festival/tracks/developers-wilding/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Correu electrònic" aria-label="Correu electrònic" required>` | Correu electrònic | email | email | yes | absent |
| `<select name="country" aria-label="País" required>` | País | country | text | yes | absent |
| `<select name="language" aria-label="Idioma" required>` | Idioma | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | Accepto que Mozilla gestioni la meva informació tal com s'explica en aquest  Avís de privacitat . | privacy | checkbox | no | absent |

Submit control: "S'està carregant...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 13 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/ca/festival/tracks/developers-wilding/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Idioma | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 14 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/ca/festival/about/
- Sends to: https://www.mozillafoundation.org/ca/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Cerca" aria-label="Cerca">` | Cerca | query | text | no | absent |

Submit control: "Cerca 
     Cerca" — `<button type="submit" aria-label="Cerca">`

### Form 15 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/ca/festival/about/
- Sends to: https://www.mozillafoundation.org/ca/festival/about/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Correu electrònic" aria-label="Correu electrònic" required>` | Correu electrònic | email | email | yes | absent |
| `<select name="country" aria-label="País" required>` | País | country | text | yes | absent |
| `<select name="language" aria-label="Idioma" required>` | Idioma | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | Accepto que Mozilla gestioni la meva informació tal com s'explica en aquest  Avís de privacitat . | privacy | checkbox | no | absent |

Submit control: "S'està carregant...
             
             
               Subscriviu-vos 
               Subscriviu-vos" — `<button type="submit">`

### Form 16 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/ca/festival/about/
- Sends to: https://www.mozillafoundation.org/ca/festival/about/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Correu electrònic" aria-label="Correu electrònic" required>` | Correu electrònic | email | email | yes | absent |
| `<select name="country" aria-label="País" required>` | País | country | text | yes | absent |
| `<select name="language" aria-label="Idioma" required>` | Idioma | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | Accepto que Mozilla gestioni la meva informació tal com s'explica en aquest  Avís de privacitat . | privacy | checkbox | no | absent |

Submit control: "S'està carregant...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 17 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/ca/festival/about/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Idioma | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 18 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/ca/festival/newsletter/
- Sends to: https://www.mozillafoundation.org/ca/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Cerca" aria-label="Cerca">` | Cerca | query | text | no | absent |

Submit control: "Cerca 
     Cerca" — `<button type="submit" aria-label="Cerca">`

### Form 19 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/ca/festival/newsletter/
- Sends to: https://www.mozillafoundation.org/ca/festival/newsletter/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Correu electrònic" aria-label="Correu electrònic" required>` | Correu electrònic | email | email | yes | absent |
| `<select name="country" aria-label="País" required>` | País | country | text | yes | absent |
| `<select name="language" aria-label="Idioma" required>` | Idioma | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | Accepto que Mozilla gestioni la meva informació tal com s'explica en aquest  Avís de privacitat . | privacy | checkbox | no | absent |

Submit control: "S'està carregant...
             
             
               Subscriviu-vos 
               Subscriviu-vos" — `<button type="submit">`

### Form 20 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/ca/festival/newsletter/
- Sends to: https://www.mozillafoundation.org/ca/festival/newsletter/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Correu electrònic" aria-label="Correu electrònic" required>` | Correu electrònic | email | email | yes | absent |
| `<select name="country" aria-label="País" required>` | País | country | text | yes | absent |
| `<select name="language" aria-label="Idioma" required>` | Idioma | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | Accepto que Mozilla gestioni la meva informació tal com s'explica en aquest  Avís de privacitat . | privacy | checkbox | no | absent |

Submit control: "S'està carregant...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 21 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/ca/festival/newsletter/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Idioma | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 22 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/ca/festival/faq/
- Sends to: https://www.mozillafoundation.org/ca/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Cerca" aria-label="Cerca">` | Cerca | query | text | no | absent |

Submit control: "Cerca 
     Cerca" — `<button type="submit" aria-label="Cerca">`

### Form 23 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/ca/festival/faq/
- Sends to: https://www.mozillafoundation.org/ca/festival/faq/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Correu electrònic" aria-label="Correu electrònic" required>` | Correu electrònic | email | email | yes | absent |
| `<select name="country" aria-label="País" required>` | País | country | text | yes | absent |
| `<select name="language" aria-label="Idioma" required>` | Idioma | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | Accepto que Mozilla gestioni la meva informació tal com s'explica en aquest  Avís de privacitat . | privacy | checkbox | no | absent |

Submit control: "S'està carregant...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 24 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/ca/festival/faq/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Idioma | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 25 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/ca/festival/volunteer/
- Sends to: https://www.mozillafoundation.org/ca/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Cerca" aria-label="Cerca">` | Cerca | query | text | no | absent |

Submit control: "Cerca 
     Cerca" — `<button type="submit" aria-label="Cerca">`

### Form 26 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/ca/festival/volunteer/
- Sends to: https://www.mozillafoundation.org/ca/festival/volunteer/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Correu electrònic" aria-label="Correu electrònic" required>` | Correu electrònic | email | email | yes | absent |
| `<select name="country" aria-label="País" required>` | País | country | text | yes | absent |
| `<select name="language" aria-label="Idioma" required>` | Idioma | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | Accepto que Mozilla gestioni la meva informació tal com s'explica en aquest  Avís de privacitat . | privacy | checkbox | no | absent |

Submit control: "S'està carregant...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 27 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/ca/festival/volunteer/
- Sends to: https://www.mozillafoundation.org/ca/festival/volunteer/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Correu electrònic" aria-label="Correu electrònic" required>` | Correu electrònic | email | email | yes | absent |
| `<select name="country" aria-label="País" required>` | País | country | text | yes | absent |
| `<select name="language" aria-label="Idioma" required>` | Idioma | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | Accepto que Mozilla gestioni la meva informació tal com s'explica en aquest  Avís de privacitat . | privacy | checkbox | no | absent |

Submit control: "S'està carregant...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 28 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/ca/festival/volunteer/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Idioma | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 29 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 30 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/
- Sends to: https://www.mozillafoundation.org/en/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 31 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 32 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 33 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 34 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 35 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/nabiha-syed/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 36 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/nabiha-syed/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/nabiha-syed/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 37 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/nabiha-syed/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 38 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/angela-plohman/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 39 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/angela-plohman/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/angela-plohman/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 40 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/angela-plohman/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 41 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/michael-whitney/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 42 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/michael-whitney/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/michael-whitney/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 43 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/michael-whitney/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 44 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/kristen-spangler/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 45 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/kristen-spangler/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/kristen-spangler/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 46 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/kristen-spangler/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 47 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/lindsey-dodson/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 48 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/lindsey-dodson/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/lindsey-dodson/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 49 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/lindsey-dodson/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 50 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/lauren-hendry-parsons/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 51 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/lauren-hendry-parsons/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/lauren-hendry-parsons/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 52 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/lauren-hendry-parsons/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 53 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/shing-suiter/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 54 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/shing-suiter/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/shing-suiter/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 55 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/shing-suiter/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 56 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/amanda-lee-gaffar/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 57 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/amanda-lee-gaffar/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/amanda-lee-gaffar/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 58 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/amanda-lee-gaffar/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 59 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/steven-azeka/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 60 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/steven-azeka/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/steven-azeka/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 61 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/steven-azeka/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 62 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/tekia-stokes/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 63 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/tekia-stokes/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/tekia-stokes/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 64 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/tekia-stokes/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 65 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/dandre-walker/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 66 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/dandre-walker/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/dandre-walker/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 67 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/dandre-walker/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 68 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/press-center/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 69 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/press-center/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/press-center/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 70 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/press-center/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/press-center/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 71 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/press-center/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 72 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/press-center/091625-mozilla-festival-schedule/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 73 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/press-center/091625-mozilla-festival-schedule/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/press-center/091625-mozilla-festival-schedule/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 74 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/press-center/091625-mozilla-festival-schedule/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 75 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/press-center/nothing-personal-magazine-launch/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 76 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/press-center/nothing-personal-magazine-launch/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/press-center/nothing-personal-magazine-launch/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 77 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/press-center/nothing-personal-magazine-launch/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 78 — appears to be: search

*Purpose is an inference* — from: the form is marked role=search or holds a search field.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/press-center/imaginative-intelligences-hollywood/
- Sends to: https://www.mozillafoundation.org/en/search/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="text" name="query" placeholder="Search" aria-label="Search">` | Search | query | text | no | absent |

Submit control: "Search 
     Search" — `<button type="submit" aria-label="Search">`

### Form 79 — appears to be: signup / lead capture

*Purpose is an inference* — from: an email field among other fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/press-center/imaginative-intelligences-hollywood/
- Sends to: https://www.mozillafoundation.org/en/meet-mozilla/press-center/imaginative-intelligences-hollywood/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" placeholder="Email" aria-label="Email" required>` | Email | email | email | yes | absent |
| `<select name="country" aria-label="Country" required>` | Country | country | text | yes | absent |
| `<select name="language" aria-label="Language" required>` | Language | language | text | yes | absent |
| `<input type="checkbox" name="privacy">` | I'm okay with Mozilla handling my info as explained in this  Privacy Notice . | privacy | checkbox | no | absent |

Submit control: "Loading...
             
             
               Sign Up 
               Sign Up" — `<button type="submit">`

### Form 80 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozillafoundation.org/en/meet-mozilla/press-center/imaginative-intelligences-hollywood/
- Sends to: https://www.mozillafoundation.org/i18n/setlang/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="language" id="language-switcher">` | Language | language | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

## Not checked in v0.2a

- A live agent task run (the Inspector, v0.2b) — protocol specced at goals/ai-friendly-website-scanner/files/inspector-run-protocol-2026-11-04.md; it runs through a browser seat, not this code.
- Rendered-vs-raw diff in a real browser (v0.2a measures the raw response, which is what crawlers receive).
- Anything past a submit click; login flows.
