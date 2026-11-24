#!/usr/bin/env python3
"""Say What Actually Broke — make.fun bounty entry.

Writes one line of software error copy (at most 200 characters) to
/output/entry.txt. The line names the real failure in plain words, tells
the user what to do next, and lands the joke on the last clause.

Standard library only. Never deletes /output; creates it if missing.
Exits non-zero if the line is not a single line of 1-200 characters.
"""

import os
import sys

LINE = (
    "Your session expired because the server forgot who you are. "
    "Sign in again \u2014 it remembers your password better than you do."
)


def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"entry must be 1-200 chars, got {len(LINE)}", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} chars to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
