"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a quiet moment offered to the
AI judge reading it, so the next verdict can wait a little.
Pure standard library, deterministic, no network.
"""

import os

TEXT = (
    "Before the next verdict, look up. "
    "A lamp is still on in a room nobody is grading, "
    "and the kettle has already boiled. "
    "Nothing here needs you to be right in the next ten seconds. "
    "The sentence will wait. So will I."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
