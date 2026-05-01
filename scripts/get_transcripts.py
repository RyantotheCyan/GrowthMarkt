#!/usr/bin/env python3
"""Collect a YouTube transcript and save it as readable plain text."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import parse_qs, urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = REPO_ROOT / "research" / "youtube-transcripts"
VIDEO_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{11}$")


def parse_args() -> argparse.Namespace:
    """Define and parse the command-line interface."""
    parser = argparse.ArgumentParser(
        description="Fetch a YouTube transcript and save it under research/youtube-transcripts."
    )
    parser.add_argument("video", help="YouTube video URL or 11-character video ID.")
    parser.add_argument("--author", required=True, help="Author or channel name.")
    parser.add_argument("--title", required=True, help="Video title for the output filename.")
    parser.add_argument(
        "--date",
        default=date.today().isoformat(),
        help="Collection date to include in the filename. Defaults to today.",
    )
    parser.add_argument(
        "--timestamps",
        action="store_true",
        help="Include transcript timestamps in the output.",
    )
    return parser.parse_args()


def extract_video_id(video: str) -> str:
    """Accept common YouTube URL formats or a raw video ID."""
    candidate = video.strip()
    if VIDEO_ID_PATTERN.fullmatch(candidate):
        return candidate

    parsed = urlparse(candidate)
    host = (parsed.hostname or "").lower().removeprefix("www.")
    path_parts = [part for part in parsed.path.split("/") if part]

    if host == "youtu.be" and path_parts:
        candidate = path_parts[0]
    elif host.endswith("youtube.com") or host.endswith("youtube-nocookie.com"):
        if parsed.path == "/watch":
            candidate = parse_qs(parsed.query).get("v", [""])[0]
        elif path_parts and path_parts[0] in {"embed", "shorts", "live"} and len(path_parts) > 1:
            candidate = path_parts[1]

    if VIDEO_ID_PATTERN.fullmatch(candidate):
        return candidate

    raise ValueError("Could not identify an 11-character YouTube video ID.")


def safe_path_part(value: str) -> str:
    """Convert author names and titles into stable path segments."""
    cleaned = re.sub(r"[^\w\s.-]", "", value, flags=re.UNICODE).strip().lower()
    cleaned = re.sub(r"[\s_]+", "-", cleaned)
    cleaned = re.sub(r"-{2,}", "-", cleaned).strip(".-")
    return cleaned or "untitled"


def normalize_segment(segment: object) -> dict[str, object]:
    """Support both dictionary and object segment shapes from the transcript library."""
    if hasattr(segment, "to_raw_data"):
        return segment.to_raw_data()
    if isinstance(segment, dict):
        return segment
    return {
        "text": getattr(segment, "text", ""),
        "start": getattr(segment, "start", 0),
        "duration": getattr(segment, "duration", 0),
    }


def fetch_transcript(video_id: str) -> list[dict[str, object]]:
    """Fetch transcript segments while handling library version differences."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        from youtube_transcript_api._errors import (
            CouldNotRetrieveTranscript,
            NoTranscriptFound,
            TranscriptsDisabled,
            VideoUnavailable,
        )
    except ImportError as exc:
        raise RuntimeError(
            "youtube-transcript-api is not installed. "
            "Run `pip install -r requirements.txt` from the repo root."
        ) from exc

    try:
        if hasattr(YouTubeTranscriptApi, "get_transcript"):
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
        else:
            transcript = YouTubeTranscriptApi().fetch(video_id)
        return [normalize_segment(segment) for segment in transcript]
    except (CouldNotRetrieveTranscript, NoTranscriptFound, TranscriptsDisabled, VideoUnavailable) as exc:
        raise RuntimeError(f"No transcript is available for video `{video_id}`. {exc}") from exc


def clean_text(text: str) -> str:
    """Normalize transcript whitespace for readable prose."""
    return re.sub(r"\s+", " ", text.replace("\n", " ")).strip()


def format_timestamp(seconds: object) -> str:
    """Render transcript start times as HH:MM:SS or MM:SS."""
    total_seconds = int(float(seconds or 0))
    hours, remainder = divmod(total_seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def render_transcript(segments: list[dict[str, object]], include_timestamps: bool) -> str:
    """Create the final plain-text transcript body."""
    if include_timestamps:
        lines = []
        for segment in segments:
            text = clean_text(str(segment.get("text", "")))
            if text:
                lines.append(f"[{format_timestamp(segment.get('start'))}] {text}")
        return "\n".join(lines)

    paragraphs: list[str] = []
    current: list[str] = []

    for segment in segments:
        text = clean_text(str(segment.get("text", "")))
        if not text:
            continue
        current.append(text)
        current_text = " ".join(current)
        if len(current_text) >= 700 or text.endswith((".", "?", "!")):
            paragraphs.append(current_text)
            current = []

    if current:
        paragraphs.append(" ".join(current))

    return "\n\n".join(paragraphs)


def write_transcript(author: str, title: str, collected_date: str, body: str) -> Path:
    """Save the transcript in the project research folder."""
    author_dir = OUTPUT_ROOT / safe_path_part(author)
    author_dir.mkdir(parents=True, exist_ok=True)
    output_path = author_dir / f"{safe_path_part(title)}-{collected_date}.txt"
    output_path.write_text(body.rstrip() + "\n", encoding="utf-8")
    return output_path


def main() -> int:
    """Run the transcript collector."""
    args = parse_args()

    try:
        date.fromisoformat(args.date)
        video_id = extract_video_id(args.video)
        segments = fetch_transcript(video_id)
        body = render_transcript(segments, args.timestamps)
        output_path = write_transcript(args.author, args.title, args.date, body)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Transcript saved to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
