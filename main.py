#!/usr/bin/env python3
"""The Funniest Toaster Error Message -- make.fun program/v1 entry.

Writes one line (at most 120 characters): the error message a kitchen
toaster shows its owner when something goes wrong. Stdlib only, no
network, no randomness, no clock -- fully deterministic.
"""

import os

ENTRY = "ERROR E03: The lever is down. I have decided to stay down here."


def main() -> int:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters"
    assert text.strip() == text and "\n" not in text, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
