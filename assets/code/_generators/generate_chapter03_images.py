"""Generate the Chapter 3 image assets for the CIS133 data pack.

Renders every PNG in assets/code/chapter-03/ in one consistent
flat-illustration style, so the pack reads as a single design set
for the fictional PC Computer Club. Each image depicts exactly the
scene its alt text names in the chapter and the lab answer key.

Deterministic: pure drawing code plus one seeded Random for pebble
scatter. Rerunning produces byte-identical files (verified by the
double-render assert at the bottom). Base seed: 133.

Run from the repo root:
    python3 assets/code/_generators/generate_chapter03_images.py
"""

import hashlib
import io
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BASE_SEED = 133
OUT_DIR = Path(__file__).resolve().parents[1] / "chapter-03"

# One palette across all nine images keeps the set coherent
SKY = (244, 162, 89)        # desert sunset orange
SKY_LIGHT = (250, 199, 141)
GROUND = (222, 184, 135)    # sandy tan
GRAVEL = (201, 162, 118)
CACTUS = (94, 153, 89)      # saguaro green
CACTUS_DARK = (72, 122, 70)
CLUB_TEAL = (38, 128, 128)  # club brand color
CLUB_TEAL_DARK = (26, 94, 94)
BIN_GREEN = (94, 153, 89)
BIN_BLUE = (74, 122, 178)
BIN_YELLOW = (233, 196, 106)
CARDBOARD = (196, 154, 108)
CARDBOARD_DARK = (166, 124, 82)
TABLE = (140, 100, 70)
WHITE = (255, 255, 255)
INK = (51, 51, 51)          # dark gray for text and outlines
SHIRT_COLORS = [(74, 122, 178), (233, 196, 106),
                (94, 153, 89), (196, 108, 94)]
SKIN_TONES = [(224, 172, 105), (141, 85, 36),
              (255, 219, 172), (198, 134, 66)]

# Chart data cited in the Skills Lab. The order is descending so
# the bar chart reads left to right without sorting.
CHART_ITEMS = [
    ("Cables", 64),
    ("Phones", 38),
    ("Laptops", 21),
    ("Small elec.", 17),
    ("Tablets", 14),
]
CHART_TOTAL = 154

# Chapter-only practice chart for the figure/figcaption worked
# example. Kept separate from the lab chart so the chapter never
# hands students the alt text their lab grades them on. The 18 and
# 39 endpoints are cited in the chapter's example alt text.
MEMBERSHIP_ITEMS = [
    ("Fall 2024", 18),
    ("Spring 2025", 24),
    ("Fall 2025", 31),
    ("Spring 2026", 39),
]


def font(size):
    """Pillow's built-in scalable default font, so the script has no
    font-file dependency and renders the same on every machine."""
    return ImageFont.load_default(size=size)


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill,
                           outline=outline, width=width)


def draw_cactus(draw, x, base_y, height, trunk_w=None):
    """A saguaro: rounded trunk plus two L-shaped side arms that
    hug the trunk, left arm higher than the right."""
    trunk_w = trunk_w or max(14, height // 5)
    top_y = base_y - height
    arm_w = max(10, int(trunk_w * 0.75))
    rise = int(height * 0.28)

    def arm(attach_y, side):
        gap = int(trunk_w * 0.55)
        if side == "left":
            ax = x - gap - arm_w
            connector = (ax, attach_y, x + 2, attach_y + arm_w)
        else:
            ax = x + trunk_w + gap
            connector = (x + trunk_w - 2, attach_y,
                         ax + arm_w, attach_y + arm_w)
        rounded(draw, connector, arm_w // 2, CACTUS)
        rounded(draw, (ax, attach_y - rise, ax + arm_w,
                       attach_y + arm_w), arm_w // 2, CACTUS)

    arm(top_y + int(height * 0.30), "left")
    arm(top_y + int(height * 0.48), "right")
    rounded(draw, (x, top_y, x + trunk_w, base_y),
            trunk_w // 2, CACTUS)
    # Vertical ridge line gives the trunk depth
    cx = x + trunk_w // 2
    draw.line((cx, top_y + trunk_w // 2, cx, base_y - 6),
              fill=CACTUS_DARK, width=2)


def draw_person(draw, cx, base_y, scale, shirt, skin):
    """A flat-style figure: round head, rounded-rectangle torso."""
    head_r = int(11 * scale)
    torso_w = int(34 * scale)
    torso_h = int(42 * scale)
    head_cy = base_y - torso_h - head_r
    draw.ellipse((cx - head_r, head_cy - head_r,
                  cx + head_r, head_cy + head_r), fill=skin)
    rounded(draw, (cx - torso_w // 2, base_y - torso_h,
                   cx + torso_w // 2, base_y),
            int(10 * scale), shirt)


def draw_bin(draw, x, y, w, h, color, label=None, label_size=14):
    """An open-top collection bin with a label plate."""
    draw.polygon([(x, y), (x + w, y), (x + w - w // 10, y + h),
                  (x + w // 10, y + h)], fill=color)
    draw.rectangle((x - 4, y - 8, x + w + 4, y + 6), fill=color)
    if label:
        f = font(label_size)
        tw = draw.textlength(label, font=f)
        pad = 6
        lx = x + (w - tw) / 2
        ly = y + h * 0.35
        rounded(draw, (lx - pad, ly - pad,
                       lx + tw + pad, ly + label_size + pad),
                4, WHITE)
        draw.text((lx, ly), label, font=f, fill=INK)


def draw_box(draw, x, y, w, h, open_flaps=True):
    """A cardboard box, flaps out, for the donation piles."""
    draw.rectangle((x, y, x + w, y + h), fill=CARDBOARD,
                   outline=CARDBOARD_DARK, width=2)
    if open_flaps:
        draw.polygon([(x, y), (x - w // 5, y - h // 4),
                      (x + w // 8, y)], fill=CARDBOARD_DARK)
        draw.polygon([(x + w, y), (x + w + w // 5, y - h // 4),
                      (x + w - w // 8, y)], fill=CARDBOARD_DARK)
    draw.line((x, y + h // 2, x + w, y + h // 2),
              fill=CARDBOARD_DARK, width=2)


def draw_phone(draw, x, y, s=1.0, body=INK):
    w, h = int(16 * s), int(28 * s)
    rounded(draw, (x, y, x + w, y + h), int(4 * s), body)
    draw.rectangle((x + 3, y + 5, x + w - 3, y + h - 7),
                   fill=(120, 170, 190))


def draw_laptop(draw, x, y, s=1.0):
    w, h = int(44 * s), int(26 * s)
    rounded(draw, (x, y, x + w, y + h), 3, (90, 90, 95))
    draw.rectangle((x + 4, y + 4, x + w - 4, y + h - 4),
                   fill=(120, 170, 190))
    rounded(draw, (x - int(4 * s), y + h,
                   x + w + int(4 * s), y + h + int(6 * s)),
            3, (60, 60, 65))


def draw_cable(draw, x, y, s=1.0, color=(80, 80, 85)):
    r = int(12 * s)
    for i in range(3):
        rr = r - i * int(4 * s)
        draw.ellipse((x - rr, y - rr, x + rr, y + rr),
                     outline=color, width=max(2, int(3 * s)))


def desert_backdrop(draw, w, h, horizon, rng, pebbles=40):
    """Orange sky over sandy ground, with a seeded pebble scatter."""
    draw.rectangle((0, 0, w, horizon), fill=SKY)
    draw.ellipse((w * 0.72, h * 0.06, w * 0.86, h * 0.06 + w * 0.14),
                 fill=SKY_LIGHT)
    draw.rectangle((0, horizon, w, h), fill=GROUND)
    for _ in range(pebbles):
        px = rng.randint(0, w)
        py = rng.randint(horizon + 10, h - 6)
        pr = rng.randint(2, 5)
        draw.ellipse((px, py, px + pr * 2, py + pr),
                     fill=GRAVEL)


def make_club_logo():
    """240x240 transparent logo: teal disk, monitor, three chasing
    arrows. Transparency is the chapter's PNG teaching point."""
    img = Image.new("RGBA", (240, 240), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((10, 10, 230, 230), fill=CLUB_TEAL + (255,))
    d.ellipse((22, 22, 218, 218), outline=WHITE + (255,), width=4)
    # Monitor silhouette
    rounded(d, (70, 78, 170, 142), 8, WHITE + (255,))
    d.rectangle((78, 86, 162, 134), fill=CLUB_TEAL + (255,))
    d.rectangle((112, 142, 128, 156), fill=WHITE + (255,))
    d.rectangle((94, 156, 146, 164), fill=WHITE + (255,))
    # Three chasing arrows circling the monitor
    for start in (200, 320, 80):
        d.arc((44, 44, 196, 196), start=start, end=start + 75,
              fill=WHITE + (255,), width=10)
        # Arrowhead at each arc's end
        import math
        ang = math.radians(start + 75)
        cx, cy, r = 120, 120, 76
        ax = cx + r * math.cos(ang)
        ay = cy + r * math.sin(ang)
        tang = ang + math.pi / 2
        pts = []
        for da, dr in ((0, 16), (math.pi / 2, 10),
                       (-math.pi / 2, 10)):
            pts.append((ax + dr * math.cos(tang + da),
                        ay + dr * math.sin(tang + da)))
        d.polygon(pts, fill=WHITE + (255,))
    return img


def make_cactus_garden():
    """400x400 practice image: three cacti in a gravel garden under
    an orange desert sky. Square on purpose, so the width/height
    distortion exercise is impossible to miss."""
    rng = random.Random(BASE_SEED)
    img = Image.new("RGB", (400, 400), WHITE)
    d = ImageDraw.Draw(img)
    desert_backdrop(d, 400, 400, horizon=260, rng=rng, pebbles=48)
    draw_cactus(d, 60, 335, 140)
    draw_cactus(d, 195, 355, 190, trunk_w=30)
    draw_cactus(d, 330, 325, 115)
    return img


def make_recycling_drive():
    """800x450 scene: students drop old electronics into labeled
    bins at the club's collection table."""
    rng = random.Random(BASE_SEED + 1)
    img = Image.new("RGB", (800, 450), WHITE)
    d = ImageDraw.Draw(img)
    desert_backdrop(d, 800, 450, horizon=300, rng=rng, pebbles=30)
    # Banner above the table
    rounded(d, (250, 60, 640, 108), 10, CLUB_TEAL)
    d.text((280, 72), "RECYCLING DRIVE TODAY", font=font(26),
           fill=WHITE)
    # Volunteer first, so the table occludes their lower half
    draw_person(d, 450, 330, 1.1, CLUB_TEAL, SKIN_TONES[1])
    # Collection table with devices on top
    d.rectangle((240, 300, 650, 316), fill=TABLE)
    d.rectangle((256, 316, 276, 390), fill=TABLE)
    d.rectangle((614, 316, 634, 390), fill=TABLE)
    draw_laptop(d, 300, 274)
    draw_phone(d, 380, 272)
    draw_phone(d, 410, 272)
    draw_cable(d, 490, 292)
    draw_laptop(d, 530, 274, s=0.9)
    # Labeled bins beside the table, students walking up between
    # the bins and the table so no label is covered
    draw_bin(d, 60, 320, 130, 100, BIN_GREEN, "PHONES")
    draw_bin(d, 680, 320, 110, 100, BIN_BLUE, "CABLES")
    draw_person(d, 218, 430, 1.3, SHIRT_COLORS[0], SKIN_TONES[0])
    draw_person(d, 660, 430, 1.3, SHIRT_COLORS[3], SKIN_TONES[2])
    return img


def draw_bar_chart(items, title, note=None, colors=None):
    """640x400 bar chart drawn with PIL, not matplotlib, so the
    bytes stay deterministic and the numbers are pinned by the
    items list."""
    img = Image.new("RGB", (640, 400), WHITE)
    d = ImageDraw.Draw(img)
    title_f, label_f, value_f = font(22), font(16), font(18)
    d.text((40, 18), title, font=title_f, fill=INK)
    base_y, top_y = 330, 80
    left, right = 60, 610
    d.line((left, base_y, right, base_y), fill=INK, width=2)
    max_val = max(val for _, val in items)
    colors = colors or [CLUB_TEAL, BIN_GREEN, BIN_BLUE,
                        BIN_YELLOW, CARDBOARD]
    n = len(items)
    slot = (right - left) // n
    bar_w = int(slot * 0.62)
    for i, (name, val) in enumerate(items):
        x = left + i * slot + (slot - bar_w) // 2
        h = int((base_y - top_y) * (val / max_val))
        d.rectangle((x, base_y - h, x + bar_w, base_y),
                    fill=colors[i % len(colors)])
        vw = d.textlength(str(val), font=value_f)
        d.text((x + (bar_w - vw) / 2, base_y - h - 26), str(val),
               font=value_f, fill=INK)
        lw = d.textlength(name, font=label_f)
        d.text((x + (bar_w - lw) / 2, base_y + 10), name,
               font=label_f, fill=INK)
    if note:
        d.text((40, 364), note, font=label_f, fill=INK)
    return img


def make_chart():
    return draw_bar_chart(CHART_ITEMS,
                          "Items Collected at the Spring Drive",
                          note=f"Total: {CHART_TOTAL} items")


def make_membership_chart():
    return draw_bar_chart(MEMBERSHIP_ITEMS,
                          "Club Membership by Semester",
                          colors=[CLUB_TEAL])


def make_divider():
    """800x24 decorative strip: alternating cactus diamonds. Exists
    to teach alt="" for decoration."""
    img = Image.new("RGB", (800, 24), CLUB_TEAL)
    d = ImageDraw.Draw(img)
    for i, x in enumerate(range(10, 800, 40)):
        c = WHITE if i % 2 == 0 else BIN_YELLOW
        d.polygon([(x + 10, 4), (x + 20, 12), (x + 10, 20),
                   (x, 12)], fill=c)
    return img


def make_sorting_station():
    """640x360 gallery image: a volunteer sorts donated phones and
    laptops into three labeled bins."""
    rng = random.Random(BASE_SEED + 2)
    img = Image.new("RGB", (640, 360), WHITE)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 640, 240), fill=(235, 226, 214))  # indoor wall
    d.rectangle((0, 240, 640, 360), fill=(214, 202, 186))
    rounded(d, (200, 30, 450, 66), 8, CLUB_TEAL)
    d.text((222, 38), "SORTING STATION", font=font(20), fill=WHITE)
    d.rectangle((60, 250, 580, 264), fill=TABLE)
    d.rectangle((80, 264, 98, 330), fill=TABLE)
    d.rectangle((542, 264, 560, 330), fill=TABLE)
    draw_bin(d, 110, 160, 110, 84, BIN_GREEN, "PHONES", 13)
    draw_bin(d, 260, 160, 110, 84, BIN_BLUE, "LAPTOPS", 13)
    draw_bin(d, 410, 160, 110, 84, BIN_YELLOW, "CABLES", 13)
    draw_phone(d, 150, 222)
    draw_laptop(d, 286, 224, s=0.8)
    draw_cable(d, 470, 236, s=0.9)
    draw_person(d, 560, 250, 1.15, CLUB_TEAL, SKIN_TONES[3])
    for _ in range(6):
        draw_phone(d, rng.randint(120, 500), 236, s=0.7)
    return img


def make_donation_boxes():
    """640x360 gallery image: cardboard donation boxes filled with
    tangled cables and chargers."""
    rng = random.Random(BASE_SEED + 3)
    img = Image.new("RGB", (640, 360), WHITE)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 640, 250), fill=(235, 226, 214))
    d.rectangle((0, 250, 640, 360), fill=(214, 202, 186))
    for bx, by, bw, bh in ((70, 190, 160, 110), (270, 210, 180, 100),
                           (490, 195, 120, 105)):
        draw_box(d, bx, by, bw, bh)
        for _ in range(4):
            draw_cable(d, rng.randint(bx + 24, bx + bw - 24),
                       by + rng.randint(4, 16), s=0.9,
                       color=(70, 70, 75))
    return img


def make_volunteer_crew():
    """640x360 gallery image: four club volunteers stand behind the
    drive's welcome table."""
    img = Image.new("RGB", (640, 360), WHITE)
    d = ImageDraw.Draw(img)
    rng = random.Random(BASE_SEED + 4)
    desert_backdrop(d, 640, 360, horizon=250, rng=rng, pebbles=20)
    rounded(d, (170, 40, 470, 84), 10, CLUB_TEAL)
    d.text((196, 50), "PC COMPUTER CLUB", font=font(22),
           fill=WHITE)
    for i, cx in enumerate((160, 270, 380, 490)):
        draw_person(d, cx, 300, 1.4, SHIRT_COLORS[i],
                    SKIN_TONES[i])
    d.rectangle((90, 300, 560, 318), fill=TABLE)
    d.rectangle((108, 318, 128, 356), fill=TABLE)
    d.rectangle((522, 318, 542, 356), fill=TABLE)
    return img


IMAGES = {
    "club-logo.png": (make_club_logo, (240, 240)),
    "cactus-garden.png": (make_cactus_garden, (400, 400)),
    "recycling-drive.png": (make_recycling_drive, (800, 450)),
    "devices-collected-chart.png": (make_chart, (640, 400)),
    "membership-chart.png": (make_membership_chart, (640, 400)),
    "desert-divider.png": (make_divider, (800, 24)),
    "sorting-station.png": (make_sorting_station, (640, 360)),
    "donation-boxes.png": (make_donation_boxes, (640, 360)),
    "volunteer-crew.png": (make_volunteer_crew, (640, 360)),
}


def render_all():
    """Render every image to bytes. Returns {name: bytes}."""
    rendered = {}
    for name, (maker, size) in IMAGES.items():
        img = maker()
        assert img.size == size, (
            f"{name}: got {img.size}, expected {size}")
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        rendered[name] = buf.getvalue()
    return rendered


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    first = render_all()
    second = render_all()
    # Engineered-property asserts
    for name in IMAGES:
        a = hashlib.sha256(first[name]).hexdigest()
        b = hashlib.sha256(second[name]).hexdigest()
        assert a == b, f"{name}: render is not deterministic"
    logo = Image.open(io.BytesIO(first["club-logo.png"]))
    assert logo.mode == "RGBA", "logo must carry an alpha channel"
    corner_alpha = logo.getpixel((0, 0))[3]
    assert corner_alpha == 0, "logo corners must be transparent"
    assert sum(v for _, v in CHART_ITEMS) == CHART_TOTAL, (
        "chart values must sum to the cited total")
    memb = [v for _, v in MEMBERSHIP_ITEMS]
    assert memb == sorted(memb) and memb[0] == 18 and memb[-1] == 39, (
        "membership chart must grow every term from 18 to 39, as the"
        " chapter's example alt text states")
    # The lab's file-size comparison needs the flat logo to be much
    # smaller than the detailed scene, both being PNGs
    assert len(first["club-logo.png"]) < len(
        first["recycling-drive.png"]), (
        "size-comparison teaching point requires logo < drive scene")
    for name, data in first.items():
        (OUT_DIR / name).write_bytes(data)
        print(f"wrote {name}: {len(data):,} bytes")
    print("all asserts passed")


if __name__ == "__main__":
    main()
