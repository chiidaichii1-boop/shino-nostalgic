#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes a single nostalgic childhood memory sentence to entry.txt.
The sentence is fixed and deterministic: no randomness, no input
files, no network. It only needs the output directory.
"""

import os

# One sentence, well under the 280-character cap. A concrete kitchen
# memory: rain outside, rice steaming, grandmother's fogged glasses,
# and the small theft of the crispy crust from the bottom of the pot.
ENTRY = (
    "Every rainy afternoon my grandmother lifted the lid off the rice pot, "
    "and the steam fogged her glasses while she pretended not to notice "
    "me stealing the crispy crust from the bottom."
)


def main():
    # The harness supplies these; fall back to the sandbox defaults.
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    _ = input_dir  # This entry needs no input files.

    # Never delete the output folder: only create it if it is missing,
    # then write the single entry file inside it.
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

