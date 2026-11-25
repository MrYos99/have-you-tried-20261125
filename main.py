#!/usr/bin/env python3
"""Entry point for the Have You Tried Turning It Off? bounty.

Writes one funny line a hopeless tech support agent gives a desperate
customer to /output/entry.txt (UTF-8, 1-199 characters).

Stdlib only. No network access, no randomness, no timestamps.
"""

import os

ENTRY = (
    "I've escalated your ticket to our senior team. They've escalated "
    "it to the void. The void asked if you'd tried turning it off and "
    "on again."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt round-trip mismatch"
    assert 1 <= len(written) <= 199, "entry.txt outside the 1-199 gate"
    print("wrote", path, len(written), "characters")


if __name__ == "__main__":
    main()
