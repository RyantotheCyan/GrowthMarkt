#!/usr/bin/env python3
"""Format copied LinkedIn post text into the research archive."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = REPO_ROOT / "research" / "linkedin-posts"


def parse_args() -> argparse.Namespace:
    """Define and parse the command-line interface."""
    parser = argparse.ArgumentParser(
        description="Append copied LinkedIn post text to an author's Markdown archive."
    )
    parser.add_argument("--author", required=True, help="Author name for the post archive.")
    parser.add_argument("--date", required=True, help="Post date in YYYY-MM-DD format.")
    parser.add_argument("--url", required=True, help="Source URL for the LinkedIn post.")
    return parser.parse_args()


def safe_path_part(value: str) -> str:
    """Convert author names into stable folder names."""
    cleaned = re.sub(r"[^\w\s.-]", "", value, flags=re.UNICODE).strip().lower()
    cleaned = re.sub(r"[\s_]+", "-", cleaned)
    cleaned = re.sub(r"-{2,}", "-", cleaned).strip(".-")
    return cleaned or "unknown-author"


def read_post_text() -> str:
    """Read copied LinkedIn post text from stdin."""
    post_text = sys.stdin.read().strip()
    if not post_text:
        raise ValueError("No post text received on stdin.")
    return post_text


def format_post(post_date: str, post_text: str, url: str) -> str:
    """Render one post block in the project Markdown format."""
    return (
        f"## Post — {post_date}\n"
        f"{post_text}\n\n"
        f"**Source:** {url}\n"
        "**Key insight:** \n"
    )


def append_post(author: str, block: str) -> Path:
    """Append the formatted block to the author's posts.md file."""
    author_dir = OUTPUT_ROOT / safe_path_part(author)
    author_dir.mkdir(parents=True, exist_ok=True)
    output_path = author_dir / "posts.md"

    if output_path.exists() and output_path.read_text(encoding="utf-8").strip():
        existing = output_path.read_text(encoding="utf-8").rstrip()
        output_path.write_text(f"{existing}\n\n{block}", encoding="utf-8")
    else:
        output_path.write_text(block, encoding="utf-8")

    return output_path


def main() -> int:
    """Run the LinkedIn post formatter."""
    args = parse_args()

    try:
        date.fromisoformat(args.date)
        post_text = read_post_text()
        block = format_post(args.date, post_text, args.url)
        output_path = append_post(args.author, block)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"LinkedIn post appended to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

