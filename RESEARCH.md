# Is Your Website AI Friendly? — Research Brief

**Question under test:** a scanner that checks what an AI agent visiting a website would trip on — "speed bumps in flow" for a new species of visitor — and reports in plain English with receipts.

**Research date:** 23 October 2026. Every load-bearing claim below carries a named, dated source. Vendor marketing is labelled as a vendor claim. Where a number comes from a vendor relaying someone else's study, that is said out loud.

**Plain-English note on terms:** an *accessibility tree* is the simplified map a browser builds of a page — every button, link and form field reduced to a role ("button"), a name ("Add to cart") and a state ("disabled"). Screen readers read it to blind users. It turns out most AI agents read the same map. A *crawler* is a bot that fetches pages to feed an AI's answers. A *browser agent* is an AI that actually drives a browser — clicking and typing — to complete a task.

---

## The verdict, up front

The static checklist version of this product already exists, is free, and is owned by two of the biggest names on the web (Cloudflare and Google). It also measures the wrong thing: whether files are *present*, not whether an agent can *do anything*. The evidence below supports exactly one defensible position — **live verification**: fetch the site as the actual named AI bots, compare what the raw HTML says against what a rendered page shows, audit the accessibility tree agents actually read, and run one small real agent task and report the exact step where it got stuck. A scanner built on proxies is a lead magnet at best and a clone in a weekend. A scanner built on measured behaviour is an instrument — harder to build, harder to copy, and the only version whose receipts mean anything.

Details and sources follow, question by question.

---

## 1. What already exists

### Cloudflare — isitagentready.com (the incumbent to beat)

- **Who/when:** Cloudflare, launched during its Agents Week, **17 April 2026**. Free.
- **What it checks** (Cloudflare blog, "Introducing the Agent Readiness score," April 2026): a 0–100 score across four dimensions —
  - *Discoverability:* robots.txt, sitemap.xml, Link headers (RFC 8288).
  - *Content:* "Markdown for Agents" — does the server return Markdown when a request sends `Accept: text/markdown`.
  - *Bot Access Control:* Content Signals declared in robots.txt, AI bot rules, Web Bot Auth (signed bot identity).
  - *Capabilities:* Agent Skills index, API Catalog (RFC 9727), OAuth discovery (RFC 8414/9728), MCP Server Card (draft spec SEP-1649), WebMCP.
  - Commerce protocols (x402, UCP, ACP) are checked but explicitly **do not count toward the score**. **llms.txt is off by default** — Cloudflare's own scanner treats it as optional.
- **Method:** static HTTP probes. It fetches files and headers. It does **not** run a browser agent or attempt a task. For each failure it hands you a prompt to give your coding agent.
- **It is also an agent tool itself:** the site exposes an MCP server with a `scan_site` tool, so other agents can call it.
- **Adoption baseline (Cloudflare Radar, published with the launch, April 2026):** ~78% of high-traffic domains have a robots.txt; only ~4% declare Content Signals; ~3.9% serve Markdown on request; MCP Server Cards and API Catalogs together appear on **fewer than 15 sites** in the whole dataset.
- **Score instability, documented:** the same unchanged site scored 33/100 under the "All Checks" preset and 67/100 under the "Content Site" preset on the same day (Slobodan Manic, *Search Engine Journal*, 2026). A dev.to sweep that graded 549 x402-catalog hosts with this scanner found 53.3% at level 0.

### Google — Lighthouse "Agentic Browsing" category

- **Who/when:** Google. Added in **Lighthouse 13.3, 7 May 2026**; shipped in Chrome 150 DevTools (30 June 2026) as an opt-in category; also in PageSpeed Insights. Free, and already on every developer's machine.
- **What it checks** (Lighthouse 13.5.0 category source, via jwatte.com's hands-on comparison, 2026): seven audits — accessibility-tree quality, WebMCP form coverage, registered WebMCP tools, WebMCP schema validity, cumulative layout shift, llms.txt, AI catalog schema validation.
- **Method:** deterministic audits on the rendered page. It reports a **pass ratio, not a 0–100 score**; Google describes the category as informational and still under development. It does not establish that any transaction succeeds. DebugBear's testing (2026) found example.com passed 2 of 2 applicable checks with no AI features at all — the bar is a floor, not a simulation.

### LLMs Ledger (Mobilize Cloud)

- **Who/when:** Mobilize Cloud, a Dublin, Ohio agency; launched **15 October 2026**. 
- **What it offers:** free llms.txt validator (score out of 100, plain-English problem list), free llms.txt generator, free "AI readiness check" (can ChatGPT/Claude/Perplexity/Google reach and read the site), public directory. Paid monitoring: $9/mo monthly checks, $19/mo nightly, Agency $79/mo per 10 sites.
- **Method:** static checks. This is the closest thing to a small independent charging money for the checklist pattern — at prices that show what the market thinks a checklist is worth.

### SUSO Digital — AI Search Visibility Checker

- **Who:** SUSO Digital, an SEO agency. Free tool.
- **Why it matters:** it sends **live requests using real AI bot user agents** and reports what actually reaches the origin server — behavioural verification rather than declared-policy reading. On the access axis this is the closest existing thing to the evidence-grade approach in §5. It is still fetch-level: it does not run a task.

### The GEO / AI-visibility platforms (adjacent, not the same product)

These mostly monitor whether AI answers *mention* you — a different question from whether an agent can *use* your site:

- **Profound** — enterprise pricing; includes "Agent Analytics."
- **Peec AI** — from ~€70–95/mo.
- **Scrunch AI** — from $250/mo; calls itself an "Agent Experience Platform," serves AI-optimised pages to crawlers, includes page audits; became a Sitecore company around June 2026.
- **Otterly** — $29/mo. **Semrush and Ahrefs** both sell AI add-ons.
- Long tail of one-shot "AI readiness score" tools: Rankscale, Riff Analytics, GeoGryphon, Ayzeo, geotoolbox.ai (free agent-readiness scan, account required, frames it as "reach, render, read"), ai-siteready.com (UCP guides plus readiness checks).

### What nobody in this list does

None of the scored incumbents runs a live agent task against the site. The write-ups admit it plainly: isagentready.com (a *different* site from Cloudflare's — an explainer publisher) states in its accessibility-tree article that scanners "do not run a browser agent." Lighthouse audits a rendered page against rules. Cloudflare probes files over HTTP. SUSO fetches as a bot. The task-completion layer — "an agent tried to find your price and start your signup; here is the step where it died" — is unoccupied by any major player as of October 2026.

---

## 2. What agents actually fail on

### The benchmark baseline: agents are bad at the web, full stop

- **WebArena** (Zhou et al., CMU, 2023) — a benchmark of realistic tasks on self-hosted copies of real site types (shopping, forums, maps, a GitLab clone). The best GPT-4-based agent scored **14.41%** end-to-end task success against **78.24%** for humans. The paper's own hypothesis for the gap: the models' lack of active exploration and failure recovery. Translation: a large share of agent failure is the *agent's* limitation, not the site's defect — and any honest scanner has to separate the two, or it will blame sites for agent weakness.

### How agents see a page (this decides which site properties matter)

Agents read a page in one or more of three ways: screenshots (vision), raw HTML/DOM, or the **accessibility tree**. Evidence that the tree is a primary channel:

- **Playwright MCP** — one of the most-used tools for letting an AI drive a browser — works from accessibility snapshots by default; vision is opt-in (Microsoft Playwright MCP documentation).
- **OpenAI's own publisher/developer FAQ for ChatGPT Atlas** states the agent "uses ARIA tags — the same labels and roles that support screen readers — to interpret page structure and interactive elements," and advises WAI-ARIA best practices for buttons, menus and forms (OpenAI Atlas FAQ, October 2025; quoted verbatim in Simon Willison's launch notes, 21 October 2025).
- A **2026 study from UC Berkeley / University of Michigan** found task success fell **78% → 42%** when agents navigated sites with a degraded accessibility tree. *(Sourcing caution: this figure reached us via a vendor blog, webyes.com — treat as vendor-relayed until the paper itself is read.)*

### How broken the average page's tree is

**WebAIM Million 2025** (WebAIM's annual automated audit of the top 1,000,000 home pages): **94.8%** have detectable WCAG failures; average 51 errors per page; 96% of all errors come from just six categories:

| Failure | Share of top home pages |
|---|---|
| Low contrast text | 81% |
| Missing image alt text | 54.5% |
| Missing form input labels | 45.9% |
| Empty links (no text/name) | 44.6% |
| Empty buttons (no text/name) | 28.1% |
| Missing document language | 17.1% |

Five of those six directly degrade the accessibility tree that snapshot-based agents read. An unnamed button is, to an agent, a button that does nothing describable.

### Practitioner-reported failure modes (site-side, fixable)

Consistent across agent-builder write-ups and the Lighthouse/WebMCP discussions of 2026:

- Hover-only menus that never open in headless Chrome.
- Collapsed trees/accordions that must be expanded before content exists for the agent.
- Elements intercepting clicks; layout shift moving targets mid-task.
- Every agent step is a model round-trip, so each extra step costs tokens and latency and multiplies the chance of failure — this is the core argument WebMCP's advocates make for giving agents direct tools instead of making them click through human flows.

### Reliability under real conditions, and a security axis

- **WAREX / Microsoft WABER research (2026):** agent success rates can halve when delays and dropped connections are injected — benchmarks run under laboratory network conditions overstate real-world success.
- **BrowserGym** (December 2024) warned that fixed benchmarks omit layout changes, authentication changes, rate limits and slow partial loads — exactly the conditions real sites present.
- **Prompt injection — WASP/WebSecArena** (Evtimov et al., 2025): top-tier agents were diverted by simple human-written injections planted on pages, with intermediate compromise up to 86%. A different axis (security, not usability), but it is a real way agents fail on real sites, and a scanner that runs live agents has to reckon with it.

**Net for §2:** the failures split into (i) agent-capability limits no site can fix (exploration, recovery, injection gullibility), and (ii) site-side structural defects with hard prevalence numbers (unnamed controls, unlabelled fields, image-only text, JS-only content, bot walls, auth walls). A credible scanner measures (ii) and says so; a dishonest one sells (i) as the site's fault.

---

## 3. Grading the draft check list

Verdicts: **REAL** (evidence it affects agents), **HYGIENE** (real but basic/plumbing), **THEATRE** (no evidence major agents use it; sold on vibes).

### (a) llms.txt presence/quality — THEATRE (as a scored signal)

- **Ahrefs study** (published 15 June 2026; 137,210 domains): 28% had published an llms.txt (the sample skews technical, so this is a ceiling); **97% of those files received zero requests in May 2026**; of the requests that did occur, 96% were bots, AI bots were 19.5% of those, and AI *retrieval* bots (the ones feeding live answers) were just **1.1%**; **zero** AI-bot requests ever probed for an llms.txt that didn't exist — bots never look for it unprompted. The most consistent readers were coding agents (Claude Code the top fetcher).
- **SE Ranking** (~300,000 domains, 2026): ~10.13% adoption, and no correlation with AI citations; removing the llms.txt variable from their model *improved* its accuracy.
- **OtterlyAI** (2026): 84 llms.txt hits out of 62,100+ AI bot visits over 90 days (~0.1%). **Limy** (500M AI bot events, 2026): same pattern.
- **Google's published guidance (2026):** llms.txt has no effect on Search rankings or AI results; Google Search Central documentation states Google Search ignores AI text files including llms.txt; a Google staffer publicly likened it to the keywords meta tag.
- As of early 2026, **no major AI company — OpenAI, Google, Anthropic, Meta, Mistral — has publicly committed** to reading llms.txt in a production answer system.
- Counterpoints, honestly noted: Wix claims Google crawls and indexes llms.txt at scale (a vendor claim; crawling is not using). A Zenodo study (Nathan Hall, 17 September 2026; the author discloses he builds a plugin that announces the file) found crawlers fetched a Markdown resource ~9.4×/site-day **when its URL was announced** via a robots.txt Sitemap directive — ClaudeBot fetched it a median 8 seconds after robots.txt — while an unannounced root /llms.txt got 2 requests total. The lesson is "discovery, not adoption": announced resources get fetched; the convention itself is not being sought out.
- Cloudflare's scanner leaves llms.txt **off by default**.
- **Verdict:** cheap and harmless to have; a genuine niche use exists (coding agents reading documentation). Scoring ordinary sites on it is cargo cult.

### (b) robots.txt treatment of AI crawlers — REAL, and it's the operative control

- OpenAI's and Anthropic's crawler documentation both treat robots.txt as the control mechanism (Anthropic documents Crawl-delay support). OpenAI states that sites opting out of OAI-SearchBot will not appear in ChatGPT search answers (blocking GPTBot alone governs training, not search visibility) (OpenAI crawler documentation, 2025–2026).
- Enforcement is tightening: Cloudflare Radar data (via TechnologyChecker.io, 9 October 2026) shows sites on Cloudflare **denied 13.47% of AI bot requests in Q3 2026, up from 5.98%** a year earlier. A 28 September 2026 snapshot of 4,242 robots.txt files: GPTBot blocked 1.60× for every allow; OAI-SearchBot 0.91×.
- **But declarations lie.** HasData's AI Crawler Block Index (measured 16 September 2026; 10,894 domains): 10.3% of top-10k domains block any AI crawler in robots.txt (news publishers 56.4%); **46.7% of GPTBot robots.txt bans are "paper-only"** — declared, yet GPTBot is still served. The reverse also exists: robots.txt allows, the server blocks anyway.
- **Scanner implication:** reading robots.txt is necessary and insufficient. The check that means something is *fetch as the bot* and compare (§5).

### (c) sitemap.xml — HYGIENE, real

Part of Cloudflare's Discoverability checks (April 2026). The Zenodo study above shows crawlers fetch sitemap-announced URLs at high rates immediately after robots.txt. Basic plumbing; a site missing one is leaving discoverability on the table, but presence alone says nothing about agent task success.

### (d) Structured data / JSON-LD — REAL for understanding, THEATRE as a citation lever

- **Ahrefs controlled study (2026):** 1,885 pages that added JSON-LD (August 2025–March 2026) vs ~4,000 matched controls: AI Mode visibility +2.4%, ChatGPT +2.2% — both statistically indistinguishable from zero — and Google AI Overviews **−4.6%**. The often-quoted "~53% of AI-cited pages carry schema, ~3× the rate of non-cited pages" is confounding (good sites do both), not cause.
- **Google's AI Features documentation (2026):** no special schema is required to appear in AI features.
- **Microsoft's Fabrice Canel** (SMX Munich, March 2025, on record): schema helps Microsoft's LLMs *understand* content — an understanding aid, not a ranking lever.
- A searchVIU live-retrieval test (2026) found AI systems extracted only visible HTML content. NLWeb is built on Schema.org, which keeps structured data relevant as an understanding layer.
- For agents *acting* on a page, the accessibility tree and visible content dominate; hidden JSON-LD is largely unread in a live fetch.
- **Verdict:** keep it for correctness of understanding; do not sell it as "get cited by AI."

### (e) Unlabelled buttons/links — REAL

The accessibility tree is a primary agent observation channel (§2: Playwright MCP default; OpenAI's Atlas ARIA statement). Prevalence is measured, not guessed: empty buttons on **28.1%** and empty links on **44.6%** of top home pages (WebAIM Million 2025). Google put an accessibility-tree quality audit in Lighthouse's agentic category (May 2026). This is the single most defensible check on the list.

### (f) Text baked into images — REAL

Missing alt text affects **54.5%** of top home pages (WebAIM Million 2025). An agent reading DOM or tree gets nothing from an image with no text alternative; a screenshot agent can OCR, with errors. If the price, the offer, or the call to action lives only inside a graphic, a large class of agents cannot read it.

### (g) Form fields without labels — REAL

Missing form labels on **45.9%** of top home pages (WebAIM Million 2025). Practitioner detail: Playwright's `getByLabel` — the locator agents are steered toward — fails when a field has a placeholder but no `<label>`; `autocomplete` attributes help agents and password managers alike. Forms are where agent tasks go to die, and labels are the cheapest fix on this entire list.

### (h) Bot walls / CAPTCHA for agent traffic — REAL and growing

Cloudflare-network denial of AI bot requests rose from 5.98% to 13.47% year over year (Q3 2026, §3b). HasData's enforcement tests (September 2026) found a datacenter-vs-residential gap (GPTBot served 67.8% vs a browser's 72.3% from datacenters overall; at news publishers, 54.2% vs 83.8%). Visa's Trusted Agent Protocol (October 2025, with Cloudflare) and Cloudflare's Web Bot Auth exist precisely because distinguishing a legitimate agent from a hostile bot is unsolved. Anthropic's documentation notes its web fetch tool returns `url_not_allowed` when robots.txt blocks it and does not support JavaScript-rendered sites (Anthropic web fetch documentation, 2026).

### (i) Hover-only / JS-only navigation — REAL, and it splits by visitor type

- **Crawlers:** Vercel & MERJ's network-wide crawler analysis (**December 2024**) found **none of the major AI crawlers render JavaScript** — GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot, Meta-ExternalAgent, Bytespider and CCBot fetch JS files but do not execute them. Exceptions: Gemini (Googlebot infrastructure), Applebot, Bingbot/Copilot. Later tests agree: Advanced Web Ranking (August 2026) and RESONEO (January 2026) found ChatGPT and Claude live fetches read raw HTML; an analysis of 500M+ GPTBot requests found zero evidence of JS execution.
- **Consequence:** content and navigation that exist only after JavaScript runs are invisible to the crawlers that feed AI answers. Browser-driving agents (Atlas, computer use) do render JS — but hover-only menus are still reported fragile in headless Chrome.
- This is also directly measurable by a scanner: fetch raw, fetch rendered, diff. Few checks on the list are this falsifiable.

### (j) Login wall before any value — REAL

Content behind a lead form or login effectively does not exist for AI answers — no crawler has credentials. The exception reframes the question: user-session agents (a WebMCP tool running in the user's own tab; a user-driven browser agent acting in the user's session) operate *inside* the wall, so for them readiness means "can the agent act once in," a different test from "can anything be discovered from outside." A scanner should report which side of the wall the value sits on, not just that a wall exists.

### (k) An API / MCP server / agent-commerce entrance — REAL, and MCP is the live wire

See §4. The standards are genuinely shipping — but note the discovery gap: Cloudflare Radar found MCP Server Cards on **fewer than 15** high-traffic sites (April 2026). Servers exist at scale (Shopify, Stripe, Cloudflare); a *discoverable* entrance on an ordinary site is still rare, which is what makes it a real differentiator for a site that has one and a fair check for a scanner to run.

---

## 4. Standards track — live vs vapour

| Standard | What it is (one line) | Status, with dates |
|---|---|---|
| **llms.txt** | A root text file offering LLMs a reading list of your site | Proposed 2024 by Jeremy Howard. Publisher-side adoption ran ahead of reader-side support; ~10–28% of domains publish one (SE Ranking / Ahrefs, 2026) and ~97% are never requested. Yoast SEO and All in One SEO now auto-generate it for WordPress. **Widely published, barely read. No major provider commitment as of early 2026.** |
| **MCP** (Model Context Protocol) | A standard way for AI models to connect to a service's tools/data | Anthropic, November 2024; spec revisions through 28 July 2026. Shipping at scale: Shopify runs multiple official MCP servers (Dev, Storefront, Customer Account) — by Q1 2026 every Shopify store had a Storefront MCP endpoint live by default (taylorsicard.com); Shopify's Shop MCP (UCP over MCP) opened to any agent 13 October 2026. Cloudflare runs a catalog of managed remote MCP servers (its API MCP covers 2,500+ endpoints) and ships MCP in its Agents SDK; official servers from Stripe, HubSpot, GitHub, Notion, Atlassian, Salesforce, PayPal, Akeneo (12 January 2026). **Live — the strongest agent-entrance standard.** On 1 July 2026 Cloudflare opened a waitlist for a Monetization Gateway extending x402 paywalls to MCP tools. |
| **UCP** (Universal Commerce Protocol) | A commerce protocol so agents can discover and buy from merchants | Announced **11 January 2026** at NRF by Google, co-developed with Shopify; launch partners Etsy, Wayfair, Target, Walmart; 20+ endorsers incl. Visa, Mastercard, Adyen, Stripe; ucp.dev now also lists Amazon, Microsoft, Meta, Salesforce. Apache 2.0; merchant stays merchant of record; profile at `/.well-known/ucp`; spec releases through v2026-08-25. **US checkout via Google Universal Cart (AI Mode in Search + Gemini app) live since 15 October 2026.** Live, US commerce only, platform-mediated. |
| **ACP** (Agentic Commerce Protocol) | OpenAI/Stripe's protocol for buying inside ChatGPT | Released **29 September 2025** alongside ChatGPT Instant Checkout (delegated payment via single-use Shared Payment Tokens). **OpenAI sidelined Instant Checkout on 24 March 2026** — shoppers rarely bought in-chat and merchants struggled with price/stock sync (TechCrunch reporting of OpenAI's statement; secondary reports: ~30 merchants live, ~8% of US adults tried it in month one). The protocol itself continues (spec releases through April 2026), rescoped toward discovery and checkout on merchant sites/apps. **Protocol alive; flagship consumer experience retreated.** |
| **AP2** (Agent Payments Protocol) | Authorisation layer for agent payments | Google, September 2025, 60+ partners; contributed to the FIDO Alliance April 2026. Still in standards development. |
| **NLWeb** | Turns a site into a natural-language query endpoint, built on Schema.org/RSS; every NLWeb instance is also an MCP server | Microsoft, announced at Build, **19 May 2025**, created by R.V. Guha (RSS/Schema.org). Named early adopters: Tripadvisor, Eventbrite, Shopify, Hearst, O'Reilly, Allrecipes/Serious Eats, Chicago Public Media, Common Sense Media, Snowflake. A path-traversal vulnerability was found 28 May 2025 and patched 30 June 2025. Cloudflare added NLWeb support via AutoRAG in early 2026. **Real open-source project, modest adoption, not a standard.** |
| **WebMCP** | A browser API letting a page expose tools directly to agents in the user's tab | Proposal in the W3C Web Machine Learning Community Group — a **Draft Community Group Report, not on the standards track**. Chrome early preview February 2026; origin trial Chrome 149–156; API moved from `navigator.modelContext` to `document.modelContext` (spec change 27 May 2026; old getter deprecated in Chromium 150, removed in 152 Canary); Chrome lists 157 as an *estimated* ship milestone. Edge origin trial from Edge 150; Brave's Leo experimental; **Firefox neutral (August 2026, no implementation); Safari/WebKit formally opposed (June 2026)** — WebKit argues the fix is better HTML/ARIA semantics, not a parallel tool layer. Consumers announced: Gemini in Chrome; ChatGPT desktop. **Promising, contested, not shipped as a standard.** |
| **Markdown for Agents** (Cloudflare) | Edge conversion of HTML to Markdown when a request asks for it | Launched **12 February 2026** (beta; free on Pro+ plans). Cloudflare converts at the edge on `Accept: text/markdown` (~80% token reduction on Cloudflare's own blog example: 16,180 → 3,150 tokens; response carries an `x-markdown-tokens` header). Only ~3.9% of high-traffic domains serve Markdown on request (Cloudflare Radar, April 2026). **Live product feature, single-vendor.** |

**Reading of the track:** exactly one entrance standard is unambiguously live at scale (MCP), one commerce protocol is live but platform-gated (UCP), one retreated (ACP's checkout), one is a real project with thin adoption (NLWeb), one is a contested browser draft (WebMCP), and the most famous one (llms.txt) is the one almost nobody reads.

---

## 5. The honest verdict

### Product, lead magnet, or feature?

- **As a static checklist: a feature, and a free one.** Cloudflare gives the scan away (and exposes it as an MCP tool for other agents to call); Google bundles the category into Lighthouse/Chrome. The one independent charging for the checklist pattern, LLMs Ledger, charges $9–19/mo — monitoring prices, not product prices. Competing with two free incumbents on their own checklist is the weakest possible position.
- **As a monitoring/visibility bundle: a feature inside GEO platforms.** Profound, Peec, Scrunch and the SEO suites already fold readiness-flavoured audits into visibility subscriptions. A standalone checklist gets absorbed.
- **As live verification: the only product-shaped position found in this research.** Nobody major sells "we fetched your site as GPTBot, ClaudeBot and a browser agent; here is what each one actually got; here is the step where the task died." SUSO's live bot-UA fetch is the nearest neighbour and stops at fetch level.

### What separates an evidence-grade instrument from a cloneable checklist

A checklist can be copied in a weekend because it only reads declarations. An instrument measures behaviour. Concretely, the evidence above supports five behavioural measurements, in order of strength:

1. **Fetch as the named bots, don't just read the policy.** robots.txt bans are paper-only 46.7% of the time (HasData, September 2026) and silent server-side blocks exist in the other direction. The receipt is the actual HTTP response each named bot receives.
2. **Diff raw HTML against the rendered page.** No major AI crawler executes JavaScript (Vercel & MERJ, December 2024; confirmed through 2026). Whatever exists only after rendering does not exist for the crawlers that feed AI answers. The diff *is* the finding.
3. **Audit the accessibility tree, not the markup.** Agents read the tree (Playwright MCP; OpenAI's Atlas FAQ). Unnamed buttons (28.1% of top pages), empty links (44.6%) and unlabelled fields (45.9%) are measurable in the tree itself (WebAIM Million 2025).
4. **Check the plumbing crawlers demonstrably use.** robots.txt + sitemap-announced URLs get fetched within seconds (Zenodo, September 2026). This is the one part of the classic checklist the crawl data actually backs.
5. **Run one small real task and keep the stuck step as the receipt.** "Find the price of X." "Start the signup." "Fill the first form field." End-to-end success is the scarce quantity in every benchmark (WebArena: 14.41% agent vs 78.24% human, 2023) — a tool that reports *where* a task stopped, with the page state at that step, produces evidence no file-presence check can imitate. It also carries real costs and duties the checklist avoids: agent runs cost money per scan, results vary run to run (so the tool must run, record and disclose variance honestly), and a live agent will eventually meet a prompt injection (WASP, 2025) — the instrument has to be built to notice and say so.

### The kill-or-make finding

**The composite "AI readiness score" is measuring presence, not capability — and the market has already priced presence at free.** The same unchanged site swings from 33 to 67 on Cloudflare's scanner depending on preset (Search Engine Journal, 2026); example.com passes Google's agentic checks with no AI features at all (DebugBear, 2026); the most-scored artefact in the genre, llms.txt, is requested by AI retrieval bots in ~1.1% of the already-rare requests it receives (Ahrefs, June 2026). If the product is the checklist, it is dead on arrival — cloned by incumbents who give it away. If the product is *measured agent behaviour with receipts* — what each real bot actually received, what the tree actually says, where the task actually stopped — no incumbent occupies that ground as of October 2026, and it cannot be cloned by copying a checklist, because the value is in the running infrastructure and the honesty of the reporting. That is the whole decision.

---

## Sources (primary first)

- Cloudflare blog, "Introducing the Agent Readiness score," April 2026 (Agents Week; launch 17 April 2026) — checks, method, Radar adoption figures. blog.cloudflare.com/agent-readiness/
- Lighthouse 13.3 release / Chrome 150 DevTools notes, May–June 2026; Lighthouse 13.5.0 agentic category source via jwatte.com comparison, 2026; DebugBear agentic-browsing tests, 2026.
- OpenAI, ChatGPT Atlas publisher/developer FAQ, October 2025 (ARIA statement; OAI-SearchBot opt-out consequences), quoted in Simon Willison, "Introducing ChatGPT Atlas," 21 October 2025.
- OpenAI and Anthropic crawler/web-tool documentation, 2025–2026 (robots.txt as control; Anthropic Crawl-delay; fetch tool `url_not_allowed`, no JS rendering).
- Zhou et al., "WebArena: A Realistic Web Environment for Building Autonomous Agents," CMU, 2023 (14.41% vs 78.24%).
- WebAIM, "The WebAIM Million," 2025 (94.8%; 51 errors/page; six-category breakdown).
- Ahrefs, llms.txt request study, 15 June 2026 (137,210 domains; 97% zero requests; 1.1% retrieval share) and JSON-LD controlled study, 2026 (1,885 pages vs ~4,000 controls).
- SE Ranking llms.txt adoption study, 2026 (~300,000 domains); OtterlyAI bot-visit analysis, 2026; Limy, 500M AI bot events, 2026.
- Nathan Hall, Zenodo study, 17 September 2026 (announced vs unannounced resource fetching; author disclosure noted).
- HasData, AI Crawler Block Index, measured 16 September 2026 (paper-only bans 46.7%; datacenter gaps).
- Cloudflare Radar AI-bot denial figures via TechnologyChecker.io, 9 October 2026 (5.98% → 13.47%).
- Vercel & MERJ, AI crawler JavaScript analysis, December 2024; Advanced Web Ranking, August 2026; RESONEO, January 2026.
- Google Search Central / AI Features documentation, 2026 (llms.txt ignored by Google Search; no special schema required). Fabrice Canel (Microsoft), SMX Munich, March 2025.
- Microsoft Playwright MCP documentation (accessibility snapshots by default).
- WASP/WebSecArena, Evtimov et al., 2025 (prompt-injection diversion); BrowserGym, December 2024; WAREX/WABER, Microsoft, 2026.
- UC Berkeley / University of Michigan accessibility-tree study, 2026 — **as relayed by vendor blog webyes.com; paper not read firsthand in this pass.**
- UCP: Google/Shopify announcement, NRF, 11 January 2026; ucp.dev (partners, spec versions); US Universal Cart checkout live 15 October 2026.
- ACP: OpenAI/Stripe release, 29 September 2025; Instant Checkout sidelining, 24 March 2026 (TechCrunch reporting of OpenAI's statement).
- MCP: Anthropic, November 2024; spec revisions through 28 July 2026; Shopify MCP documentation and Shop MCP opening, 13 October 2026; Cloudflare MCP catalog/Agents SDK; Akeneo MCP server, 12 January 2026.
- NLWeb: Microsoft Build announcement, 19 May 2025; vulnerability disclosure May–June 2025; Cloudflare AutoRAG NLWeb support, early 2026.
- WebMCP: W3C Web Machine Learning Community Group draft report; Chrome origin-trial documentation (Chrome 149–156; `document.modelContext` change 27 May 2026); WebKit position, June 2026; Mozilla position, August 2026. Cloudflare's "~100,000 Commerce.com stores" WebMCP claim (21 October 2026 post) is a **vendor claim, independently unconfirmed**.
- Cloudflare, Markdown for Agents launch, 12 February 2026; Radar Markdown adoption 3.9%, April 2026.
- LLMs Ledger launch and pricing, Mobilize Cloud, 15 October 2026. SUSO Digital AI Search Visibility Checker, 2026. Slobodan Manic, Search Engine Journal, 2026 (33 vs 67 preset swing). Visa Trusted Agent Protocol, October 2025.
