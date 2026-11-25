"""One Line, Lights Out - make.fun bounty entry.

Writes a single status line to /output/entry.txt.
"""

import os
import sys

ENTRY = "Last seen 23:41. The charger is still warm, the battery at 87%, and I have nowhere left to go."

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be whitespace only"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == ENTRY.encode("utf-8"), "written bytes differ from ENTRY"
    assert not raw.endswith(b"\n"), "no trailing newline allowed"

    print("Wrote %d characters to %s" % (len(ENTRY), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
