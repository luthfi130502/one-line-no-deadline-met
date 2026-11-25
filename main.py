#!/usr/bin/env python3
"""One Line, No Deadline Met -- entry generator.

Writes a single-line joke excusing a missed deadline to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace, one line only.

The joke: the deadline was not missed so much as delegated. "Future Me"
is the classic procrastinator's scapegoat -- the punch lands on the fact
that the person you outsourced the work to is exactly as unreliable as
you are, only lazier. One sentence, spoken the way someone cornered by
their boss would actually say it, twist at the end.
"""

import os
import sys

ENTRY = (
    "I didn't miss the deadline \u2014 I just outsourced it to Future Me, "
    "and that guy hasn't answered a single email in his life."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "error: entry is %d chars, over the %d cap" % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %s (%d chars)" % (out_path, len(text)))
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
