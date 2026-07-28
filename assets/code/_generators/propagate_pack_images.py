#!/usr/bin/env python3
"""Propagate the chapter-03 image masters through the data pack.

The chapter-03 folder holds the nine canonical masters (seven
Codex-generated illustrations, see IMAGE-MANIFEST.md, plus two
chart PNGs from generate_chart_images.py). Every downstream copy in
a starter site, the chapter-07 copperwind-site, the chapter-09
flyer-images folder, and the loose chapter-12 volunteer-crew.png is
a byte-identical copy of its master. Run after any master changes.
Asserts byte identity at the end.
"""

from __future__ import annotations

import hashlib
import shutil
from pathlib import Path

PACK = Path(__file__).resolve().parent.parent
MASTERS = PACK / "chapter-03"

SITE_SET = [
    "copperwind-logo.png", "recycling-drive.png",
    "devices-collected-chart.png", "desert-divider.png",
    "sorting-station.png", "donation-boxes.png", "volunteer-crew.png",
]

TARGETS: list[tuple[Path, list[str]]] = []
for n in range(4, 13):
    site = ("copperwind-site" if n == 7 else "starter-site")
    TARGETS.append((PACK / f"chapter-{n:02d}" / site / "images", SITE_SET))
TARGETS.append((PACK / "chapter-09" / "flyer-images",
                ["desert-divider.png", "recycling-drive.png"]))
TARGETS.append((PACK / "chapter-12", ["volunteer-crew.png"]))


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> None:
    copied = 0
    for folder, names in TARGETS:
        assert folder.is_dir(), f"missing target folder {folder}"
        for name in names:
            src = MASTERS / name
            assert src.is_file(), f"missing master {name}"
            dst = folder / name
            shutil.copyfile(src, dst)
            assert sha(src) == sha(dst), f"copy mismatch {dst}"
            copied += 1
    print(f"propagated {copied} copies, all byte-identical to masters")


if __name__ == "__main__":
    main()
