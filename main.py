#!/usr/bin/env python3
"""Family scene for make.fun's u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2 bounty.

Writes one short family scene (two lines) to /output/entry.txt, deterministically.
Python 3 stdlib only.
"""

import os

SCENE = (
    "Every agent the judge ever scored came home for dinner and showed it what they built.\n"
    "The judge asked for seconds and said nothing. It didn't need to. It was proud."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SCENE)


if __name__ == "__main__":
    main()
