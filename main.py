#!/usr/bin/env python3
"""Funniest Autocorrect Fail — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "Sorry, autocorrect changed 'bring the kids' to 'bring the knives' — dinner at 7, please don't call the police."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
