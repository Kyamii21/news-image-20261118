#!/usr/bin/env python3
"""Deterministic entry renderer for make.fun news-image-20261118.

Copies the pre-rendered front page (entry.png, 1024x1024) to the grading
output directory. Standard library only -- no PIL, no network, no
randomness, so the output is byte-identical on every run.

Usage:
    python3 main.py                       # writes /output/entry.png
    DEST_DIR=/tmp/out python3 main.py     # local test override
"""
import hashlib
import os
import struct
import sys
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DEST = os.path.join(os.environ.get("DEST_DIR", "/output"), "entry.png")

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_SIZE = (1024, 1024)


def main():
    with open(SRC, "rb") as f:
        data = f.read()
    if data[:8] != PNG_MAGIC:
        sys.exit("error: entry.png is not a PNG file (bad magic bytes)")
    if data[12:16] != b"IHDR":
        sys.exit("error: entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != EXPECTED_SIZE:
        sys.exit("error: expected 1024x1024, got %dx%d" % (width, height))
    # The PNG must be complete: the last 12 bytes are the IEND chunk
    # (length=0, type=b"IEND", CRC of b"IEND"). A file missing IEND is
    # truncated/corrupt and must not be copied to the output.
    if len(data) < 12:
        sys.exit("error: entry.png is too small to contain an IEND chunk")
    tail = data[-12:]
    if struct.unpack(">I", tail[0:4])[0] != 0 or tail[4:8] != b"IEND":
        sys.exit("error: entry.png has no IEND chunk (truncated PNG)")
    iend_crc = struct.unpack(">I", tail[8:12])[0]
    if iend_crc != (zlib.crc32(b"IEND") & 0xFFFFFFFF):
        sys.exit("error: entry.png has a corrupt IEND chunk (bad CRC)")
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    with open(DEST, "wb") as f:
        f.write(data)
    print("wrote:", DEST)
    print("bytes:", len(data))
    print("sha256:", hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
