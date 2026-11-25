#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Writes one line (<=200 chars) to /output/entry.txt: the funniest thing
an AI agent would say in its weekly status report to its human.
"""
from pathlib import Path

LINE = (
    "Weekly status: I read your mind, found no instructions, and built "
    "exactly what you didn't ask for \u2014 on time, under budget, and "
    "entirely wrong."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only whitespace, and the entry is one line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    # Re-read and verify exactly what was written.
    written = out.read_text(encoding="utf-8")
    assert written == LINE, "written text differs from the line"
    print(f"Wrote {len(written)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
