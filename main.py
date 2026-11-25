#!/usr/bin/env python3
"""Write one cat joke to /output/entry.txt.

The joke is a single line, well under the 200 character gate.
"""
import os

JOKE = "My cat pushed my glass off the table, watched it shatter, then glared at me like I was the clumsy one."


def main():
    line = JOKE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1 to 200 characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
