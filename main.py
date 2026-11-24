"""Writes this entry's one-line text to entry.txt in the output directory.

The output directory is $MAKEFUN_OUTPUT_DIR when set and non-empty,
otherwise /output. Standard library only; no network, randomness, or clock.
"""

import os
import sys

TEXT = (
    "Five failed weld tests deep, his sixth pipe held air overnight, "
    "and he signed his initials inside the hull like the old men did."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        sys.stderr.write(f"cannot create output directory {out_dir!r}: {exc}\n")
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
