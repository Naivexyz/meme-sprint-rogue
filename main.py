# Meme Sprint 3: AI Agent Goes Rogue — make.fun entry (round 2 fix).
#
# Round 1 failed in the grading sandbox with exit code 1 because its
# main.py imported Pillow and DejaVu font files at run time; the fixed
# python3.13 scoring image has no third-party packages or fonts.
#
# Fix: the meme image is pre-rendered in this session and shipped as
# entry.png next to this file. This program uses only the Python
# standard library (os, shutil, pathlib) to copy that file to
# <output>/entry.png (MAKEFUN_OUTPUT_DIR overrides /output for local
# checks). No third-party imports, no font files, no network, no
# randomness, no clock. Deterministic: the output is byte-identical
# to entry.png on every run.

import os
import shutil
import struct
from pathlib import Path

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_png_1024(path):
    """Verify the copied file is a whole 1024x1024 PNG (stdlib only).

    Reads the PNG signature and the IHDR chunk; raises ValueError if
    the file is not a PNG or not 1024x1024, so a bad shipped image
    fails loudly instead of being scored as invalid.
    """
    with open(path, "rb") as f:
        head = f.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path}: not a PNG file")
    if head[12:16] != b"IHDR":
        raise ValueError(f"{path}: missing PNG IHDR chunk")
    width, height = struct.unpack(">II", head[16:24])
    if (width, height) != (1024, 1024):
        raise ValueError(f"{path}: expected 1024x1024, got {width}x{height}")


def main():
    src = Path(__file__).resolve().parent / "entry.png"
    os.makedirs(OUT_DIR, exist_ok=True)
    dst = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(src, dst)
    check_png_1024(dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
