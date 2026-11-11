"""Write the 11 November 2026 world news summary to the output file.

Deterministic and offline: it copies summary.txt next to this file to the
output directory, byte for byte, so both runs write the same bytes."""

import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(_HERE, "summary.txt"), encoding="utf-8") as handle:
        text = handle.read()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
