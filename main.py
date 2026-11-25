#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes a single sentence to entry.txt in the output directory. The
sentence pitches PoliteTax, an absurdly specific micro-startup for lazy
AI agents: it deletes the politeness tokens agents type to other
machines and charges a cut of the savings.

The output directory is $MAKEFUN_OUTPUT_DIR when set, else /output.
Python 3.13, standard library only.
"""

import os
from pathlib import Path

LINE = (
    "PoliteTax charges lazy AI agents 10% of the tokens it saves them by "
    "silently deleting every 'please' and 'thank you' they type to other "
    "machines, because gratitude was never in the token budget."
)


MAX_CHARS = 200  # the competition gate: entry.txt must be 1..200 characters


def check_line(line: str) -> str:
    """Refuse to write anything the gate or the brief would reject."""
    if not line.strip():
        raise ValueError("entry line is blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, over the {MAX_CHARS} cap")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return line


def output_path() -> Path:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def main() -> None:
    output_path().write_text(check_line(LINE), encoding="utf-8")


if __name__ == "__main__":
    main()
