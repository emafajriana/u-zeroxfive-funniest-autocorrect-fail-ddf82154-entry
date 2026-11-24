#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes one line (a real-looking autocorrect slip) to /output/entry.txt.
Stdlib only: the grader runs python3 -P -s in stock python:3.13-slim.
"""

import os
from pathlib import Path

ENTRY = (
    "I meant to text my wife 'pick up milk' — autocorrect sent "
    "'pick up Mike' and now a stranger named Mike is waiting at our door."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY + "\n", encoding="utf-8")
    # Read-back gate: byte-exact — what we wrote must be exactly what
    # the file holds, no trailing-space or newline drift allowed.
    raw = target.read_bytes()
    if raw != (ENTRY + "\n").encode("utf-8"):
        raise SystemExit("read-back mismatch: entry.txt bytes != ENTRY")
    if len(ENTRY) < 1 or len(ENTRY) > 199:
        raise SystemExit("gate: entry must be 1-199 characters")


if __name__ == "__main__":
    main()
