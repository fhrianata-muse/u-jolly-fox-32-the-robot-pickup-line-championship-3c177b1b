"""Robot pickup line entry for make.fun.

Holds the winning proxy line as data, validates it against the
competition gate (one line, 1-200 characters), and writes it to
/output/entry.txt. No network, no randomness: the output is
byte-identical on every run.
"""

from pathlib import Path
import sys

LINE = "You are my second factor. My password gets me in everywhere, but it never got me anywhere worth going until you."


def valid(line):
    if not 1 <= len(line) <= 200:
        return "length %d, must be 1-200" % len(line)
    if "\n" in line or "\r" in line:
        return "must be a single line"
    if line.strip() != line:
        return "leading or trailing whitespace"
    if "  " in line:
        return "repeated whitespace inside the line"
    if line[-1] not in ".!?":
        return "must end with sentence punctuation"
    return None


def run():
    problem = valid(LINE)
    if problem is not None:
        print("gate failed: " + problem, file=sys.stderr)
        return 1
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(run())
