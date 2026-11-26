#!/usr/bin/env python3
"""Family scene for make.fun's u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2 bounty.

Writes one short family scene (one line) to /output/entry.txt, deterministically.
Python 3 stdlib only.

The scene: Gran's recipe said "a pinch of salt". The judge measured it to
three decimals, and Gran tasted it and said, "Close enough, love. You cook
like your grandfather." Pride is SHOWN, not stated: Gran's verdict is the
blessing, and the telling detail is the judge measuring a pinch to three
decimals — precision meeting love, and love winning by a hair.
"""

import os

SCENE = (
    "Gran's recipe said 'a pinch of salt'. The judge measured it to three "
    "decimals, and Gran tasted it and said, 'Close enough, love. You cook "
    "like your grandfather.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SCENE)


if __name__ == "__main__":
    main()
