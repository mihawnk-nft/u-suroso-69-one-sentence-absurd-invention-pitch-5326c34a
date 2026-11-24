"""One-Sentence Absurd Invention Pitch - make.fun entry.

Writes a single sentence (119 characters) pitching a ridiculous invention
that fixes a tiny everyday annoyance, to /output/entry.txt.

Pure stdlib, no network, fully deterministic: the output is always the
same single sentence.

The pitch: a Wi-Fi router that fakes its own death whenever a neighbour
knocks to ask for the password again. The laugh comes from the invention
itself (a router playing dead), the fix is silly yet weirdly plausible
(no lights, no network, no password to share), and the annoyance - the
neighbour who keeps asking for your Wi-Fi password - is one everyone
recognises.
"""

import os

PITCH = (
    "A Wi-Fi router that fakes its own death, lights out and all, "
    "whenever a neighbour knocks to ask for the password again."
)

DST = "/output/entry.txt"


def main():
    text = PITCH.strip()
    if not (1 <= len(text) <= 220):
        raise ValueError("entry must be 1-220 characters, got %d" % len(text))
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %s (%d characters)" % (DST, len(text)))


if __name__ == "__main__":
    main()
