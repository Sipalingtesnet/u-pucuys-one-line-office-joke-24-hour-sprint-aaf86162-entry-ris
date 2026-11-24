#!/usr/bin/env python3
"""Write one line of office comedy to /output/entry.txt.

Deterministic and offline: the joke is a single string constant, so every
run writes byte-identical output.
"""

from __future__ import annotations

import os
from pathlib import Path

# The entry. One line, ASCII, no surrounding whitespace, no newline.
JOKE = (
    "My manager blocks thirty minutes of 'focus time' before every meeting, "
    "then spends it being late to the meeting before that one."
)


def output_path() -> Path:
    """$MAKEFUN_OUTPUT_DIR/entry.txt when set, else /output/entry.txt."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def main() -> int:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    # Bytes, not text mode: guarantees no platform newline is appended.
    path.write_bytes(JOKE.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
