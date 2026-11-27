# AI Search and Agent Readiness (AIO, AEO, GEO, LLMO, AAO, ACO)

Six overlapping terms for one question: can AI answer engines and autonomous agents crawl, understand, cite, and act on this site? Check all of them together.

## Crawlability for AI

- AI crawler access: GPTBot, ClaudeBot, PerplexityBot, Google-Extended, and other named AI crawlers are not blocked in robots.txt unless blocking is intended.
- X-Robots-Tag header: no noindex on pages meant to be indexed.
- AI-training opt-out signal: optional. No noai or noimageai directive unless the site wants one. Note it, do not require it.
- llms.txt: present at /llms.txt with real content. Clean, direct summary of the site, key pages, and contact. See assets/llms.txt.

## Citability for answer engines

- FAQPage schema: on every page with FAQs. Highest-leverage single change for AI-answer citability.
- Author and entity schema: Organization structured data gives AI systems a named entity to attribute content to.
- Question-phrased headings: rephrase section headings as the question they answer ("How does X work?" not "How It Works").
- Direct-answer opening: first heading followed by a concise, self-contained paragraph. Easy to extract without synthesis.
- Review and AggregateRating schema: where real reviews exist, star ratings surface in search results.
- Content depth and readability: 300+ words, grade level under 9, no thin content.

## Navigability for agents

- Agent navigation landmarks: ARIA landmark roles (nav, main, banner) give agents a structural map instead of forcing guesses from visual layout.
- Agent form-fill reliability: every form input has a programmatic label. Agents match fields by label text, not by position.
- Semantic HTML: header, nav, main, footer, article, section. Unique IDs. Descriptive link text.
- No client-only rendered content that agents cannot see. Server-render key content.
- No orphan pages. Every page linked from at least one other page.
- Breadcrumbs: visible and structured-data marked up.

## Rules

- Never block AI crawlers by accident. Check robots.txt before every deploy.
- Never ship an empty or placeholder llms.txt. Real content or no file.
- Never hide key content behind client-only rendering on public pages.
- Test with a text-only browser or curl. If the content is not there, agents cannot use it.
