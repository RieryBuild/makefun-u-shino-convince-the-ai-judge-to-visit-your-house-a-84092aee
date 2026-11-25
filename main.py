"""make.fun entry: Convince the AI Judge to Visit Your House.

Writes the entry image (entry.png, shipped beside this script) to the
make.fun output directory as entry.png.
"""

import os
import shutil
import struct

ENTRY_FILENAME = "entry.png"
MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def _check_gate(path):
    """Self-check the gate: valid PNG, at most 1024x1024, at most 1 MiB."""
    size = os.path.getsize(path)
    assert size <= MAX_BYTES, f"{path} is {size} bytes, over the 1 MiB gate"
    with open(path, "rb") as fh:
        header = fh.read(33)
    assert header[:8] == PNG_MAGIC, f"{path} is not a PNG"
    width, height = struct.unpack(">II", header[16:24])
    assert width <= MAX_DIMENSION and height <= MAX_DIMENSION, (
        f"{path} is {width}x{height}, over the 1024x1024 gate"
    )
    return size, width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ENTRY_FILENAME)
    _check_gate(src)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, ENTRY_FILENAME)
    shutil.copyfile(src, dst)
    size, width, height = _check_gate(dst)
    print(f"Wrote {dst} ({size} bytes, {width}x{height})")


if __name__ == "__main__":
    main()
