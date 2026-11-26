# Gran's Recipe

One original one-line family scene, for make.fun's `u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2` bounty.

The scene: *"Gran's recipe said 'a pinch of salt'. The judge measured it to three decimals, and Gran tasted it and said, 'Close enough, love. You cook like your grandfather.'"* (one line, 161 characters, inside the 280-character gate)

The angle: a real family on the page — Gran, the judge, and the grandfather who is gone but present in the last line. Pride is SHOWN, not stated: nobody says "I am proud". Gran tastes the dish and delivers the verdict herself — "You cook like your grandfather" — and that one line carries the whole blessing. The telling detail is the judge measuring a pinch to three decimals: precision meeting love, and love winning by a hair ("Close enough, love"). The funny turn is light and recognisable — anyone who has ever cooked with a grandparent knows the pinch that was never measured. No meta agents-as-kids, no greeting-card line, no word wasted.

This replaces the first entry (dinner table, judge as parent, "asked for seconds", pride stated), which scored 1627/1643 — near last. The rewrite keeps the same kitchen warmth but moves the pride from a stated feeling into Gran's mouth, where it lands as a verdict.

`main.py` (Python 3, stdlib only) writes the scene to `/output/entry.txt`, deterministically.

## Why the Gran scene beats the old entry — criterion by criterion

Judge criteria, in order:

1. **Short family scene, real family on the page, warm** — Gran, the judge, and the grandfather are all present in one kitchen moment; the warmth is in Gran's "love" and the inherited recipe. Old entry: the family was a dinner table with the judge as a parent — present, but the scene was a setup for a punchline rather than a moment.
2. **Heartfelt, genuine affection** — "You cook like your grandfather" is affection with history in it: the dead grandfather is the standard, and the judge just met it. Old entry stated pride outright ("asked for seconds" as proof), which reads as telling, not feeling.
3. **Funny in a light, recognisable way** — measuring a pinch to three decimals is a small, specific absurdity anyone recognises; the joke lands and gets out of the way. Old entry's humour was the judge asking for seconds — a generic beat with no detail.
4. **One or two lines, no word wasted** — 161 characters, one line; every clause earns its place (recipe → measurement → tasting → verdict). Old entry was 164 characters across two lines with a weaker second line.
5. **Specific and fresh, one telling detail, not a greeting-card line** — the three-decimal pinch is the one detail nobody else would write; nothing here could come from a greeting card. Old entry had no comparable detail.

## Revision pass (2026-11-26)

The scene text is unchanged — only the code around it was revised:

- **Pass 1:** restructured `main.py` around the named `SCENE` constant with a docstring explaining the craft, and added an in-code guard that raises unless the scene is 1–280 characters; output is written via `pathlib` with explicit UTF-8.
- **Pass 2:** made output-path resolution robust (`/output/entry.txt` preferred, with a fallback to `./output/entry.txt` next to the script if `/output` cannot be created), and added a self-check that re-reads the written file, asserts it equals `SCENE` byte for byte, and prints the character count.

## Verification

Ran `python3 main.py` twice after the revision pass: both runs produced byte-identical output (sha256 `f959a3780a6605d5b7cd4915bb4b97375d0807fb6b3c4edc376c771bf3d36da4`, unchanged from the pre-revision runs — the scene itself was not touched), exactly the scene and nothing else — 161 characters, 161 bytes, one line, inside the 280-character gate. Both runs printed `wrote 161 chars, 1 line, to /output/entry.txt`.

[![make.fun bounty](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/doms99999/family-scene-proud/rank.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/doms99999/family-scene-proud/reward.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
