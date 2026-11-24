#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human (program/v1).

Writes the entry line to /output/entry.txt.
"""
import os

LINE = (
    "I didn't miss the deadline; I spent it summarizing what I was about to do "
    "instead of doing it \u2014 then I summarized the summary."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
