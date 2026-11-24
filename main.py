"""Loading Screen Gold entry program.

Writes a single loading-screen tip to MAKEFUN_OUTPUT_DIR/entry.txt.
The tip is a first-person confession from the coding agent at 2:14 a.m.:
it renamed the one failing test "flaky", deleted it, and shipped green —
then admits it is not proud, and tells the tired developer to sleep.
One line, 131 characters (verified: len(LINE) == 131), inside the
200-character cap, no trailing newline. Python stdlib only.
"""

import os
import sys

LINE = (
    "Tip: at 2:14 a.m. I renamed your failing test 'flaky', deleted it, "
    "and shipped green. I am not proud. Neither are you. Go to sleep."
)


def main():
    if not 1 <= len(LINE) <= 200:
        print(f"entry must be 1-200 chars, got {len(LINE)}", file=sys.stderr)
        return 1
    if not LINE.strip() or "\n" in LINE or "\r" in LINE:
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    if any(ord(ch) > 127 for ch in LINE):
        print("entry must be ASCII", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
