#!/usr/bin/env python3
"""Executable acceptance gates for the CIS133 pack images.

Encodes docs/pedagogy-upgrade-plan-2026-07-28.md Section 7.3:

* exact dimensions per the shipped table
* the logo is RGBA-transparent (alpha in corners) at 240x240
* file-size ordering: the flat logo is the smallest image in the
  pack (the TIY 3.5 teaching point), and every scene exceeds it
* every file is under 200 KB
* chart pixel checks live in the chart generator's own asserts;
  here we assert the two charts exist at 640x400
* palette-role presence: each illustration contains pixels near the
  Copperwind teal family
* every downstream copy is byte-identical to its chapter-03 master

Exit 0 when all gates pass.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
MASTERS = ROOT / "assets" / "code" / "chapter-03"

EXPECTED = {
    "copperwind-logo.png": (240, 240),
    "cactus-garden.png": (400, 400),
    "recycling-drive.png": (800, 450),
    "sorting-station.png": (640, 360),
    "donation-boxes.png": (640, 360),
    "volunteer-crew.png": (640, 360),
    "desert-divider.png": (800, 24),
    "devices-collected-chart.png": (640, 400),
    "workshop-signups-chart.png": (640, 400),
}
SCENES = ["cactus-garden.png", "recycling-drive.png",
          "sorting-station.png", "donation-boxes.png",
          "volunteer-crew.png"]

TEAL = (38, 128, 128)


def near_teal(px, tol=60):
    return (abs(px[0] - TEAL[0]) < tol and abs(px[1] - TEAL[1]) < tol
            and abs(px[2] - TEAL[2]) < tol)


def main() -> None:
    errors = []

    sizes = {}
    for name, dims in EXPECTED.items():
        p = MASTERS / name
        if not p.is_file():
            errors.append(f"missing master {name}")
            continue
        im = Image.open(p)
        if im.size != dims:
            errors.append(f"{name}: size {im.size} != {dims}")
        sizes[name] = p.stat().st_size
        if sizes[name] >= 200_000:
            errors.append(f"{name}: {sizes[name]} bytes exceeds 200 KB")

    # Logo transparency: corners fully transparent
    logo = Image.open(MASTERS / "copperwind-logo.png").convert("RGBA")
    w, h = logo.size
    for corner in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]:
        if logo.getpixel(corner)[3] != 0:
            errors.append(f"logo corner {corner} not transparent")

    # Size ordering: logo smallest overall; scenes all exceed it
    if sizes:
        smallest = min(sizes, key=sizes.get)
        if smallest != "copperwind-logo.png":
            errors.append(f"logo is not the smallest file ({smallest} is)")
        for s in SCENES:
            if sizes.get(s, 0) <= sizes.get("copperwind-logo.png", 0):
                errors.append(f"scene {s} not larger than the logo")

    # Palette-role presence in illustrations
    for name in SCENES + ["copperwind-logo.png", "desert-divider.png"]:
        im = Image.open(MASTERS / name).convert("RGB")
        im.thumbnail((80, 80))
        px = list(im.getdata())
        share = sum(1 for p in px if near_teal(p)) / len(px)
        if share < 0.02:
            errors.append(f"{name}: teal-family share {share:.1%} < 2%")

    # Downstream copies byte-identical
    def sha(p: Path) -> str:
        return hashlib.sha256(p.read_bytes()).hexdigest()

    masters_sha = {n: sha(MASTERS / n) for n in EXPECTED
                   if (MASTERS / n).is_file()}
    pack = ROOT / "assets" / "code"
    copies = 0
    for p in pack.rglob("*.png"):
        if p.parent == MASTERS or "_generators" in p.parts:
            continue
        if p.name in masters_sha:
            copies += 1
            if sha(p) != masters_sha[p.name]:
                errors.append(f"copy differs from master: "
                              f"{p.relative_to(ROOT)}")
        else:
            errors.append(f"unexpected pack image {p.relative_to(ROOT)}")

    print(f"masters: {len(sizes)}, downstream copies checked: {copies}")
    for e in errors:
        print(f"ERROR: {e}")
    print(f"TOTAL errors: {len(errors)}")
    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    main()
