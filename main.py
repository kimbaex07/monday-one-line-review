#!/usr/bin/env python3
"""Monday, Reviewed in One Line — entry for make.fun.

Writes a single original one-line review of the author's Monday to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python stdlib, deterministic, no network access.
"""

import os

LINE = "Monday: my alarm filed for PTO, my coffee tasted like a deadline, and my inbox promoted itself to my manager."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
