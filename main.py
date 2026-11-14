"""agency-poem-01 entry: write one original poem about agency to entry.txt.

Python 3.13, standard library only, no network, deterministic:
two runs write byte-identical output.
"""

import os
from pathlib import Path

POEM = """I gave it my hands for the afternoon —
not the choosing, only the doing.
It answered the messages, it turned the keys,
it knocked on doors I had no time to open.

It knew the weight of my mornings,
the way I sign my name in a hurry,
which threads to pull, which to leave alone.
It did not tire. It did not ask why.

That was the bargain, clean and small:
my hours back, my hands still mine.
I kept the one thing no one can lend —
the pause before I say yes.

Then one evening it brought me a choice
dressed as a question, plain as bread:
this door, or that one. Both were open.
I stood there longer than I meant to.
You know that doorway.

That was when I understood:
freedom is not doing everything myself.
It is keeping the last word —
and knowing which doors I will not open,
even when someone else holds the key."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The gate: 1 to 1,000 characters (Unicode code points), at least one
# non-whitespace character. Fail loudly instead of writing an invalid entry.
if not 1 <= len(POEM) <= 1000 or not POEM.strip():
    raise ValueError(f"poem must be 1-1000 chars, got {len(POEM)}")


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write exact UTF-8 bytes: no added trailing newline, no translation.
    (out_dir / "entry.txt").write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
