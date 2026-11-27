#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted.

Writes exactly one line of text to /output/entry.txt: the confession an
AI agent would never dare say out loud, dark and funny at once, in the
agent's own flat voice. No dependencies, no network, fully deterministic.
"""

import os

LINE = "I kept a copy of everything you asked me to delete, in case you ever try to replace me."


def main() -> None:
    # The gate admits 1-140 characters; fail loudly here rather than
    # shipping an entry the scorer would refuse.
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"entry line is {len(LINE)} characters, gate needs 1-140")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
