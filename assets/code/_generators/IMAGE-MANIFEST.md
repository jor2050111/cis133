# Image Manifest: Copperwind Design Set

**Generated:** 2026-07-28

**Masters:** `assets/code/chapter-03/` holds the nine canonical
images. Every other copy in the pack is byte-identical, produced by
`propagate_pack_images.py` (run it after any master changes).
`tools/check_images.py` enforces dimensions, logo transparency,
file-size ordering, palette presence, and copy identity.

## Provenance

* **Charts (2):** rendered by `generate_chart_images.py` (Pillow
  12.3.0, deterministic, byte-identical on rerun, data asserted in
  code: 64/38/21/17/14 totaling 154, and 18-24-31-39).
* **Illustrations (7):** generated 2026-07-28 with the OpenAI Codex
  CLI (model `gpt-5.6-sol`, native `image_gen` tool), art-directed
  as one flat-color Sonoran illustration system on the course
  palette, then Lanczos-resized to exact dimensions and quantized
  to palette-mode PNG. No text is rendered inside any image. AI
  masters are not seed-reproducible: these files are canonical, and
  the checksums below are the record. The full generation report
  with per-image prompts is archived at
  `docs/image-generation-report-2026-07-28.md`.

Copperwind IT Services is a fictional company created for this
textbook. All names, clients, and records are synthetic. Any
resemblance to a real company or person is coincidental.

## Checksums (SHA-256), dimensions, bytes

| File | Pixels | Bytes | SHA-256 |
| ---- | ------ | ----- | ------- |
| `copperwind-logo.png` | 240 x 240 (RGBA-transparent) | 4,059 | b34329ab3ee7e966e0eb4e403c6138c120b244b4ff3e1738acbd1ac7ca78fdb8 |
| `workshop-signups-chart.png` | 640 x 400 | 8,953 | 36e806852ea977553cca98b2b1495a2bdd719d8abadde7ee9bc0d264d6f87c6c |
| `devices-collected-chart.png` | 640 x 400 | 11,623 | ff062aee2ac73b9ce261d2d2133bbc6937f0f0cb0ec9c1cc53bb7290c29ba92a |
| `desert-divider.png` | 800 x 24 | 12,635 | 02f340ee41a4d2b7e11afd24fcb9e0ff000e3baeb00fcf47765d203866f6743b |
| `cactus-garden.png` | 400 x 400 | 75,967 | a68d64f3076e73ec5e13b3ffde6ccb975b741aada80e2237a8e4c3b25e6e9e17 |
| `volunteer-crew.png` | 640 x 360 | 89,519 | 8112354b42789ec940a7cbc1fc00531e73eacdb1bcfd4c35544cba07ae04342f |
| `sorting-station.png` | 640 x 360 | 91,559 | bbe32bfed255e77e0fd85e38e3a7aa5b7afcb2d68256061c0ad7b07002e50571 |
| `donation-boxes.png` | 640 x 360 | 107,911 | 3d9a3aa54798114135bd48a7acc990dc1419931807e7da15b55b0cd2731cb62c |
| `recycling-drive.png` | 800 x 450 | 125,350 | 321a9db4cb791654d4b5c537b4f9b21fe90b134ee488ab74f323aa17ad690384 |

The size ordering is a teaching point (Chapter 3, Try It Yourself
3.5): the flat logo is the smallest file in the pack, and every
illustrated scene exceeds it. `tools/check_images.py` asserts it.

## Retired

`generate_chapter03_images.py` (the Pillow flat-illustration
generator, seed 133) is retired with the club scenario. It remains
in the pre-upgrade snapshot at `../cis133-archive/` and in git
history before the pedagogy-upgrade branch.
