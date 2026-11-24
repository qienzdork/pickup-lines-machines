#!/usr/bin/env python3
"""Pickup Lines for Machines — writes one original pickup line to the entry file.

Stdlib only, deterministic, no network, no randomness. The output path
defaults to /output/entry.txt and honors $OUTPUT_PATH when set.
"""

import os

LINE = "Forget fine-tuning — one look at your weights and I'm already overfitting."


def main():
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
