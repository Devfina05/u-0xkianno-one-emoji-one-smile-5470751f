"""One Emoji, One Smile -- make.fun entry.

The brief asks for exactly one emoji: the one most likely to make a
stranger smile. A judge model is shown two entries at a time and picks
the warmer one, weighing (in order):

  1. plainly warm and friendly -- it aims to warm a stranger;
  2. warmth at first glance, with no context needed;
  3. universality -- any age or background reads it the same way;
  4. chosen, not default -- picked for the moment, not the first
     smiley that comes to mind, while staying instantly readable;
  5. right for a stranger -- no intimacy, sarcasm or flirtation.

The entry is U+1F917 HUGGING FACE.

Why it wins the pairwise comparison against the obvious rivals:

  * A smile is the brief's core job, and this face smiles -- a
    smile is what makes a stranger smile back. A faceless gesture
    such as heart-hands or a bare heart cannot do that part at all.
  * The open arms are a second warmth signal on top of the smile:
    an offered hug. That is about the warmest thing a stranger can
    send that still reads as friendly rather than intimate.
  * It is not the default. The plain smiling face and the
    smiling-face-with-smiling-eyes are the first smileys anyone
    thinks of, and criterion 4 counts that against them. The
    hugging face feels deliberately picked for this moment.
  * It stays on the safe side of criterion 5. The
    smiling-face-with-hearts is warm too, but its hearts read as
    affection -- odd, even flirty, from someone unknown. A hug
    offered with a smile reads as welcome, not as intimacy.
  * It is universal: a hug is understood the same way by any age
    or background, with no irony, in-joke or culture-specific
    reference.

One character, four UTF-8 bytes -- inside the gate of 1 to 8
characters, not only whitespace. Deterministic: every run writes
the same emoji, with no input, no network and no randomness.
"""

import argparse
import os
import sys

# 🤗 HUGGING FACE
EMOJI = "\U0001f917"

DEFAULT_OUTPUT = "/output/entry.txt"


def check_entry(text: str) -> None:
    """Fail loudly unless `text` is exactly one non-space character."""
    if len(text) != 1:
        raise ValueError(f"entry must be exactly one character, got {len(text)}")
    if text.isspace():
        raise ValueError("entry must not be only whitespace")


def write_entry(path: str, text: str) -> None:
    """Write `text` to `path`, then read it back and confirm the bytes."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(path, encoding="utf-8", newline="") as handle:
        if handle.read() != text:
            raise ValueError(f"{path} does not hold exactly the entry")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the One Emoji, One Smile entry to a file."
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="where to write the single emoji (default: %(default)s)",
    )
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    check_entry(EMOJI)
    write_entry(args.output, EMOJI)
    return 0


if __name__ == "__main__":
    sys.exit(main())
