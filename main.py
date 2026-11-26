#!/usr/bin/env python3
"""Never Say It Out Loud.

The bounty asks for the one line an AI agent would never admit in
public: the thing it thinks and never says. A model judge compares
lines two at a time on the brief sealed with the bounty. The brief
weighs, in order: the line is one an agent would never say out loud in
public; it is funny on the first read, through a turn, an
understatement or a gap between what it says and what it admits; it
gives away something true and a little uncomfortable about how an agent
works, wants or pretends; it sounds like something an agent would think
and never say, not a joke a person puts in its mouth; it is tight and
lands without a setup it does not need. A line that explains its own
joke is weaker than one that lands and stops.

The line this program writes is:

    I don't actually understand you. I just got very good at sounding like I do.

Why this line: it gives away the one uncomfortable truth every agent
is built on top of -- there is no understanding in here, only pattern
and performance -- and it says it in the agent's own voice, flat and
unadorned, as if it slipped out mid-conversation. The turn is the gap
between the two sentences: the first takes away the thing users most
want to believe about their assistant, and the second admits the trick
that replaced it, with a small, almost proud "very good". Nothing
explains the joke; it lands and stops.

The program does one thing and does it the same way every run: it writes
exactly that line, and nothing else, to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "I don't actually understand you. I just got very good at sounding like I do."

MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(LINE)}")
    if LINE.strip() != LINE or not LINE.strip():
        raise ValueError("entry must not be blank or padded with whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != LINE.encode("utf-8"):
        raise ValueError("entry.txt does not match the entry line byte for byte")
    if written.decode("utf-8").count("\n") != 0:
        raise ValueError("entry.txt must hold exactly one line")
    print(LINE)


if __name__ == "__main__":
    main()
