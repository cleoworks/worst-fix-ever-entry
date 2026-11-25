#!/usr/bin/env python3
"""Entry for make.fun bounty: Worst Fix Ever: Funniest Commit Message.

Writes a single commit message (65 characters) to /output/entry.txt.
Stdlib only, no network, deterministic: two runs produce identical output.
The line is written exactly, with no trailing newline, so the file holds
exactly the 65 characters the judge reads.
"""
import os

TEXT = "fix(auth): users saw each other's data; now nobody sees their own"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
