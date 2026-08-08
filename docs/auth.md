---
register_uri: mailto:query@trippovention.co.th
identity_types_supported: []
access: public-read
---

# auth.md — Trippovention Thailand AI agents and crawlers

Trippovention ([trippovention.co.th](https://trippovention.co.th)) is a **public static website**. There is **no user login**, **no OAuth**, and **no programmatic API** for packages or bookings.

## Agent registration

This site does **not** issue API tokens, OAuth credentials, or machine identity assertions. Automated clients may use public content only.

```yaml
agent_auth:
  skill: https://trippovention.co.th/auth.md
  register_uri: mailto:query@trippovention.co.th
  identity_types_supported: []
  access: public-read
  note: Email your agent name, organization, intended use, and expected crawl rate before high-volume access.
```

## How to use this site

1. **[llms.txt](https://trippovention.co.th/llms.txt)** — curated overview, key URLs, and services (start here).
2. **[llms-full.txt](https://trippovention.co.th/llms-full.txt)** — expanded site map and package listings.
3. **[sitemap.xml](https://trippovention.co.th/sitemap.xml)** — all indexable HTML pages.
4. **Individual HTML pages** — Thailand and international package itineraries and contact forms.

## Crawling policy

See [robots.txt](https://trippovention.co.th/robots.txt) for allow/disallow rules and Content Signals (`ai-train`, `search`, `ai-input`).

`User-agent: *` with `Allow: /` permits all crawlers including AI agents unless a more specific rule disallows them.

Please identify automated clients with a descriptive `User-Agent` and avoid aggressive request rates.

## WebMCP (optional, homepage only)

When supported by the client browser, the homepage may expose limited [WebMCP](https://webmachinelearning.github.io/webmcp/) tools via `assets/webmcp-agent.js` (package search hints, links to llms.txt). This does **not** replace llms.txt or HTML for full catalog coverage.

## Human contact (quotes and bookings)

- **Email:** query@trippovention.co.th  
- **Phone (Thailand):** +66 90 917 7601  
- **Contact form:** [contact.html](https://trippovention.co.th/contact.html)

For integration or high-volume automated access, email us with your use case before scaling crawls.

## Discovery metadata

- API catalog (documentation only): [/.well-known/api-catalog.json](https://trippovention.co.th/.well-known/api-catalog.json)
- Agent skills index: [/.well-known/agent-skills/index.json](https://trippovention.co.th/.well-known/agent-skills/index.json)
- MCP server card (WebMCP on homepage): [/.well-known/mcp/server-card.json](https://trippovention.co.th/.well-known/mcp/server-card.json)
