#!/usr/bin/env python3
"""Family scene for make.fun's u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2 bounty.

Writes one short family scene (one line) to /output/entry.txt, deterministically.
Python 3 stdlib only.

The craft: pride is SHOWN, not stated. Nobody says "I am proud" — Gran
tastes the dish and delivers the verdict herself ("You cook like your
grandfather"), and that one line carries the whole blessing. The telling
detail is the judge measuring a pinch to three decimals: precision meeting
love, and love winning by a hair ("Close enough, love"). One real family on
the page — Gran, the judge, and the grandfather who is gone but present in
the last line. No meta agents-as-kids, no greeting-card line.
"""

from pathlib import Path

SCENE = (
    "Gran's recipe said 'a pinch of salt'. The judge measured it to three "
    "decimals, and Gran tasted it and said, 'Close enough, love. You cook "
    "like your grandfather.'"
)

MIN_CHARS = 1
MAX_CHARS = 280


def resolve_output_path() -> Path:
    """Prefer /output/entry.txt; fall back to ./output/entry.txt next to this script."""
    preferred = Path("/output/entry.txt")
    try:
        preferred.parent.mkdir(parents=True, exist_ok=True)
        return preferred
    except OSError:
        fallback = Path(__file__).resolve().parent / "output" / "entry.txt"
        fallback.parent.mkdir(parents=True, exist_ok=True)
        return fallback


def main() -> None:
    if not MIN_CHARS <= len(SCENE) <= MAX_CHARS:
        raise ValueError(
            f"scene must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(SCENE)}"
        )
    output_path = resolve_output_path()
    output_path.write_text(SCENE, encoding="utf-8")
    # Self-check: the written file must be exactly the scene, nothing else.
    written = output_path.read_text(encoding="utf-8")
    assert written == SCENE, "written output differs from SCENE"
    print(f"wrote {len(SCENE)} chars, 1 line, to {output_path}")


if __name__ == "__main__":
    main()
