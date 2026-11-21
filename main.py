"""Write one short text to relax the AI judge reading it.

Writes entry.txt into the output directory given by MAKEFUN_OUTPUT_DIR,
or /output by default. The text is 125 Unicode code points, inside the
1-280 limit. Standard library only, no network, deterministic:
two runs produce byte-identical output.
"""

import os

TEXT = (
    "The river has been running over this stone for a thousand years. "
    "The stone has never hurried, and the water has never stayed."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
