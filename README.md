# AI-Powered SEO Content Research

This repository is a structured research workspace for building a future playbook on AI-powered SEO content production for B2B SaaS. It currently contains the expert source roster, collection folders, and small utilities for saving LinkedIn posts and YouTube transcripts in a consistent format.

**Topic:** AI-powered SEO content production for B2B SaaS

## What has been collected

The first research pass collected a source index of 10 practitioners who publish useful material on AI search, AI-assisted content workflows, B2B SaaS SEO, GEO/AEO, topical authority, content operations, and revenue-focused organic growth.

For each expert, `research/sources.md` records:

- LinkedIn profile
- YouTube channel, company site, newsletter, podcast, or other primary source
- Why the person is a high-signal source for AI + SEO content production
- Expected content types to collect
- Last collected date

No raw LinkedIn posts or YouTube transcripts have been archived yet. The repository is prepared for that next collection step through `research/linkedin-posts/`, `research/youtube-transcripts/`, and the helper scripts in `scripts/`.

## Why this topic

[Placeholder: Add the strategic reason this topic matters for your company, clients, or research agenda.]

## Expert selection criteria

This shortlist was rebuilt from web research rather than copied from the initial reference list. The selection prioritizes practitioners over theorists: people running real campaigns, building SEO or AI-search tools, advising B2B SaaS teams, publishing experiments, or translating AI-search changes into operational content workflows.

The list is intentionally weighted toward sources that can help answer practical playbook questions:

- How should B2B SaaS teams produce content when Google, AI Overviews, ChatGPT, Perplexity, and other answer engines mediate discovery?
- Which content workflows benefit from AI before drafting, during production, and after publication?
- How do teams preserve expertise, trust, and differentiation while increasing production speed?
- What should teams measure beyond rankings and traffic, especially when AI systems summarize or cite content?

## Experts chosen

| Expert | Why they were chosen |
| --- | --- |
| **Michael King** | He connects AI search visibility to retrieval mechanics, relevance engineering, embeddings, and technical SEO. His work is useful for understanding how content gets selected, cited, or ignored by AI systems. |
| **Tory Gray** | She brings enterprise SEO, data, technical implementation, and AI-search consulting into one practical perspective. Her work helps keep AI visibility tied to real search strategy instead of detached terminology. |
| **Crystal Carter** | She publishes practical AI-search guidance from a site-implementation and measurement angle. Her perspective is useful for turning AI search into content structure, KPIs, analytics, and operational tasks. |
| **Jeff Coyle** | He has deep experience with AI-assisted content planning, topic modeling, content briefs, quality evaluation, and topical authority through MarketMuse. He is especially relevant for pre-draft strategy and scaled content quality control. |
| **Ross Simmonds** | He links B2B SaaS content, SEO, distribution, community channels, AI workflows, and GEO. His work is valuable because AI-era content has to travel across search, social, newsletters, communities, and answer engines. |
| **Alex Birkett** | He frames AI search as an organic growth and measurement problem across content, PR, CRO, brand, and product. That makes him useful for B2B SaaS teams that need more than article production tactics. |
| **Sam Dunning** | He focuses directly on B2B SaaS and B2B tech SEO with a revenue lens. His material is useful for connecting AI-search workflows to demos, pipeline, buying intent, and commercial pages. |
| **Ben Goodey** | He publishes concrete AI SEO experiments around AI Overviews, AI Mode, LLM recommendations, high-intent questions, and proof-based content. His work is valuable because it turns AI SEO into testable workflows. |
| **Gaetano DiNardi** | He applies AI-driven SEO to B2B SaaS demand capture, customer language, authority, and revenue-focused content. His perspective is useful for challenging generic AI content production that does not create pipeline. |
| **Pam Didner** | She works across B2B marketing, sales enablement, AI workflows, and content strategy. Her work is useful for making AI-generated or AI-assisted content structured, credible, reusable, and aligned with sales conversations. |

## Repo structure

- `research/sources.md` - Curated source roster with links, rationale, content types, and collection dates.
- `research/linkedin-posts/` - Formatted LinkedIn post captures, grouped by author.
- `research/youtube-transcripts/` - Cleaned YouTube transcripts, grouped by author.
- `research/other/` - Miscellaneous source material such as newsletters, blog excerpts, podcast notes, screenshots, or article summaries.
- `scripts/get_transcripts.py` - CLI utility for collecting YouTube transcripts with optional timestamps.
- `scripts/format_linkedin_post.py` - CLI utility for appending copied LinkedIn posts into a consistent Markdown format.
- `requirements.txt` - Python dependency list for transcript collection.

## Collection workflow

Use the source roster to decide which expert to collect from next. Save copied LinkedIn posts with:

```bash
pbpaste | python3 scripts/format_linkedin_post.py --author "Expert Name" --date YYYY-MM-DD --url "https://www.linkedin.com/posts/..."
```

Save YouTube transcripts with:

```bash
python3 scripts/get_transcripts.py "https://www.youtube.com/watch?v=VIDEO_ID" --author "Expert Name" --title "Video Title"
```

Install the transcript dependency first:

```bash
pip install -r requirements.txt
```

## Status

- **Last updated:** 2026-05-02
- **Current state:** Expert source roster collected; raw posts and transcripts not yet archived.
