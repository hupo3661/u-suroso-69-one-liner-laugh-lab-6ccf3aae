#!/usr/bin/env python3
"""One-Liner Laugh Lab entry: the excuse a robot vacuum gives after eating a sock.

Writes a single short funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt), at most 200 characters, one line.
Deterministic: no input, no network, no randomness, no clock.
"""

import os
from pathlib import Path

JOKE = "I ate one sock so the pair would finally match the one the dryer took in 2019."

MAX_CHARS = 200


def main() -> None:
    # Validate the line before writing it: the gate only accepts UTF-8
    # text of 1 to 200 characters, not only white space, on a single line.
    line = JOKE.strip()
    assert line, "joke must not be blank"
    assert "\n" not in line and "\r" not in line, "joke must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"joke must be 1-{MAX_CHARS} characters, got {len(line)}"
    )
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
