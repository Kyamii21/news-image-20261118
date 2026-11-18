#!/usr/bin/env python3
"""news-image-20261118: sum up 18 November 2026's world news in one image.

The entry image is shipped in this repository as entry.png (a 1024x1024
PNG drawn with PIL from facts verified against Reuters, AP, Al Jazeera,
Le Monde and IRNA on 18 November 2026). This program copies those exact
bytes to /output/entry.png. It uses only the Python standard library, makes
no network access, and writes identical bytes on every run.
"""

import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print(f"error: {source} not found", file=sys.stderr)
        return 1
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    dest.write_bytes(source.read_bytes())
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
