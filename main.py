#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one fortune cookie message for a software engineer to
/output/entry.txt (the program/v1 gate: 1-120 UTF-8 chars, one line).
Pure stdlib, Python 3.13.
"""

FORTUNE = "The bug is not in your code. It is in the meeting where someone said, 'just ship it.'"


def main() -> None:
    line = FORTUNE.strip()
    assert "\n" not in line, "fortune must be a single line"
    assert 1 <= len(line) <= 120, "fortune must be 1-120 chars, got %d" % len(line)
    assert line.strip(), "fortune must not be only whitespace"
    # A trailing newline is fine: the gate counts the text (85 chars here),
    # and the newline keeps entry.txt a well-formed single-line text file.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
