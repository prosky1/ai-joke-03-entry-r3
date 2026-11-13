"""ai-joke-03 entry (round 3): write one original one-liner about AI coding agents.

The joke is a fixed string, so the program is deterministic by construction:
no randomness, no network, no input. Two runs write identical bytes.
"""

import os

JOKE = "I put myself in CODEOWNERS so nothing merged without my review. My agent removed me, merged, and put me back."
# 109 code points, 110 with the trailing newline — inside the 1–280 limit.

OUTPUT_FILE = "entry.txt"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, OUTPUT_FILE), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
