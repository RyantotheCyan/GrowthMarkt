# AI-Powered SEO Content Research (B2B SaaS)

This repository contains a structured research project on **AI-powered SEO content production for B2B SaaS**.

## Project scope

Per the assignment, this repo focuses on one topic and a curated shortlist of 10 practitioners who actively publish practical guidance.

- **Chosen topic:** AI-powered SEO content production for B2B SaaS
- **Objective:** Build a high-signal source base that can support a practical playbook later
- **Selection principle:** Practitioner-first (operators, advisors, builders), not generic commentators

## What is included

- `research/sources.md` with 10 experts, links, annotations, and collection dates
- Collection folders for LinkedIn posts, YouTube transcripts, and other materials
- Helper scripts for transcript collection and LinkedIn post formatting

## Why these experts

The selected experts consistently publish material on one or more of the following:

- AI search visibility (AI Overviews, LLM citations, GEO/AEO)
- B2B SaaS SEO and content operations
- AI-assisted editorial workflows and quality control
- Revenue-oriented organic growth (not traffic-only SEO)

Together, the list covers technical SEO, content strategy, distribution, and measurement.

## Repository structure

- `research/sources.md` - Expert roster with links, rationale, content types, and dates
- `research/linkedin-posts/` - LinkedIn posts organized by author
- `research/youtube-transcripts/` - YouTube transcripts organized by video/author
- `research/other/` - Additional supporting materials
- `scripts/get_transcripts.py` - Collect YouTube transcripts from video URLs
- `scripts/format_linkedin_post.py` - Format and save copied LinkedIn posts
- `requirements.txt` - Python dependencies

## Collection workflow

Install dependencies:

```bash
pip install -r requirements.txt
```

Save a LinkedIn post:

```bash
pbpaste | python3 scripts/format_linkedin_post.py --author "Expert Name" --date YYYY-MM-DD --url "https://www.linkedin.com/posts/..."
```

Save a YouTube transcript:

```bash
python3 scripts/get_transcripts.py "https://www.youtube.com/watch?v=VIDEO_ID" --author "Expert Name" --title "Video Title"
```

## Status

- **Last updated:** 2026-05-01
- **Current state:** Source roster completed; archive folders prepared for ongoing collection
