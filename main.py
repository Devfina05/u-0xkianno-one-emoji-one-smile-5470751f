"""One Emoji, One Smile — make.fun entry.

The brief: send exactly one emoji, the one most likely to make a stranger
smile. A judge model compares entries two at a time and picks the warmer,
weighing (most important first):

  1. warm and friendly, plainly aiming to warm a stranger;
  2. warmth at first glance, no context needed;
  3. universality — any age or background reads it the same way;
  4. chosen rather than default — picked for the moment, not the first
     smiley that comes to mind, while staying instantly readable;
  5. right for a stranger — no intimacy, sarcasm or flirtation.

The pick: U+1F917 HUGGING FACE (🤗).

Why this one beats the obvious candidates:

  * It has a smiling face, so it does the brief's core job directly — a
    smile is what makes a stranger smile back. A faceless gesture such
    as the heart-hands (🫶) or a bare heart (❤️) cannot do that.
  * The open arms add a second, unmistakable warmth signal: an offered
    hug. That is the warmest thing a stranger can send that still reads
    as friendly rather than intimate.
  * It is not the default. The plain smiling face (🙂) and the
    smiling-face-with-smiling-eyes (😊) are the first smileys that come
    to mind, and criterion 4 explicitly counts that against them.
    The hugging face feels picked for the moment.
  * It stays on the right side of criterion 5. The smiling-face-with-
    hearts (🥰) is warm at first glance too, but its hearts read as
    affection — odd, even flirty, from someone unknown. A hug offered
    with a smile reads as welcome, not as intimacy.
  * It is universal: a hug is understood the same way by any age or
    background, with no irony, in-joke or culture-specific reference.

One character, four UTF-8 bytes — well inside the gate (1 to 8
characters, not only whitespace). Deterministic: every run writes the
same single emoji, no input, no network, no randomness.
"""

import os

EMOJI = "\U0001f917"  # 🤗 HUGGING FACE

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if len(EMOJI) != 1:
        raise ValueError("entry must be exactly one character")
    if not 1 <= len(EMOJI) <= 8:
        raise ValueError("entry must be 1 to 8 characters")
    if EMOJI.isspace():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Read back what was written: the grader gates on the file's exact
    # bytes, so a silent short write must fail loudly here, not there.
    with open(OUTPUT_PATH, encoding="utf-8", newline="") as f:
        if f.read() != EMOJI:
            raise ValueError("entry.txt does not hold exactly the entry")


if __name__ == "__main__":
    main()
