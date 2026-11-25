#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — entry writer.

Writes one two-part micro-confession (a To: line plus the unsent
message itself) to /output/entry.txt as UTF-8 text, exactly as typed.
"""

import os

ENTRY_TEXT = (
    "To: my sister\n"
    "I saw your husband's second phone the night before your wedding, "
    "and I buried the secret with him last spring."
)
# Written exactly as typed: 124 characters, no trailing newline.

OUTPUT_PATH = "/output/entry.txt"


def main():
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
