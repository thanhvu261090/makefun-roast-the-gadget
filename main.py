#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes the entry line to /output/entry.txt after enforcing the kit gate:
UTF-8 text, 1 to 200 characters, not only whitespace, a single line.
Standard library only, no network.
"""

import os
import sys

ENTRY = (
    "My smart speaker ignores me when I shout its name, then answers a "
    "question from the TV \u2014 it's a butler who only works for the furniture."
)

MAX_CHARS = 200


def gate_check(text: str) -> None:
    """Enforce the exact gate from the kit's RULES.txt."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be 1 to {MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in text):
        raise ValueError("entry must not contain control characters")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    text.encode("utf-8")  # must be valid UTF-8 text


def main() -> int:
    gate_check(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote entry ({len(ENTRY)} chars) to /output/entry.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
