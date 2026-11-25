#!/usr/bin/env python3
"""Funniest Autocorrect Fail (make.fun).

Writes the entry -- one line, under 200 characters, a hilarious
autocorrect fail -- to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "I meant to text my wife 'I'll pick up milk on the way home'. Autocorrect sent 'I'll pick up Mick'. Mick is now outside our house with flowers."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
