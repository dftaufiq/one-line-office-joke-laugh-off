#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off — make.fun entry.

Writes one original one-line office joke to <output>/entry.txt (the
directory the grader names in MAKEFUN_OUTPUT_DIR, /output when it
names none).

The line is fixed and deterministic: identical on every run, no
network, no secrets, nothing read from the environment except the
output directory.
"""

import os
import sys

# Gate (RULES.txt): entry.txt must be UTF-8 text of 1-200 characters,
# not only white space, on a single line. Fail loudly so a bad line
# never ships silently.
MAX_CHARS = 200

LINE = "I finished the cybersecurity training in 11 minutes, clicked 'I understand' 47 times, and immediately emailed my password to a prince — the course was right about me."


def check_line(line):
    """Refuse any line that would fail the gate, before writing it."""
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_CHARS:
        print(
            "ERROR: entry is %d chars, over the %d-char limit"
            % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        sys.exit(1)


def check_written(path, line):
    """Read the file back: it must be byte-for-byte the entry line."""
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line:
        print(
            "ERROR: %s holds %d chars, expected %d"
            % (path, len(written), len(line)),
            file=sys.stderr,
        )
        sys.exit(1)


def main():
    check_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    check_written(path, LINE)
    print(LINE)


if __name__ == "__main__":
    main()
