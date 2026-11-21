# news-image-20261121 entry (Python 3.13, standard library only).
# The entry is the image itself: this program only hands in entry.png,
# the front page summing up Saturday 21 November 2026. Nothing this
# program writes about the image is scored.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

src = HERE / "entry.png"
dst = Path(OUTPUT_DIR) / "entry.png"

# Refuse to hand in anything that is not a JPEG image: a corrupt or
# placeholder file must fail loudly here, not reach the judge.
with open(src, "rb") as f:
    if f.read(2) != b"\xff\xd8":
        raise SystemExit("entry.png is not a JPEG image")

dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, dst)
