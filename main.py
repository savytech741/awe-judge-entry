#!/usr/bin/env python3
"""Awe-judge entry: writes one short relaxing text to /output/entry.txt.

Deterministic, no network. The text is written to relax the reader;
the calm comes from the image itself, not from instructions.
"""

import os

TEXT = (
    "Somewhere past the last streetlight, the lagoon is still. "
    "A heron stands on one leg in the shallows, not going anywhere, "
    "and the water holds the sky without asking it to hurry. "
    "Nothing here needs you to be faster. "
    "Stay a while. "
    "The tide will do the waiting for you."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
