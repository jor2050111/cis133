"""Generate two deterministic charts for the Copperwind data pack.

The script uses fixed source data and Pillow drawing primitives only.
It does not read the clock, add PNG metadata, or use random values.
Each chart renders twice in memory and must produce byte-identical PNGs.

Pillow 12.3.0 is required because Pillow's bundled default scalable font
is part of the deterministic rendering contract.
"""

import hashlib
import io
from pathlib import Path

import PIL
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageStat


PILLOW_VERSION = "12.3.0"
OUTPUT_SIZE = (640, 400)
SCALE = 2
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "chapter-03"

TEAL = (38, 128, 128)          # #268080
DEEP_TEAL = (26, 94, 94)      # #1a5e5e
SUNSET = (244, 162, 89)        # #f4a259
SAND = (222, 184, 135)         # #deb887
INK = (51, 51, 51)             # #333333
WHITE = (255, 255, 255)
BACKGROUND = (252, 249, 244)
GRID = (226, 221, 213)
TRACK = (239, 235, 228)
AREA = (246, 226, 201)

DEVICE_ITEMS = (
    ("Cables", 64),
    ("Phones", 38),
    ("Laptops", 21),
    ("Small electronics", 17),
    ("Tablets", 14),
)
DEVICE_TOTAL = 154

WORKSHOP_SIGNUPS = (
    ("January", 18),
    ("February", 24),
    ("March", 31),
    ("April", 39),
)


def scaled(value):
    """Convert a final-size coordinate to the supersampled canvas."""
    return int(round(value * SCALE))


def scaled_box(box):
    return tuple(scaled(value) for value in box)


def font(size):
    """Use Pillow's built-in scalable default, matching the reference."""
    return ImageFont.load_default(size=scaled(size))


def draw_text(draw, position, text, text_font, fill=INK, anchor=None):
    draw.text(
        (scaled(position[0]), scaled(position[1])),
        text,
        font=text_font,
        fill=fill,
        anchor=anchor,
    )


def draw_line(draw, points, fill, width=1, joint=None):
    draw.line(
        tuple(scaled(value) for point in points for value in point),
        fill=fill,
        width=scaled(width),
        joint=joint,
    )


def draw_rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(
        scaled_box(box),
        radius=scaled(radius),
        fill=fill,
        outline=outline,
        width=scaled(width),
    )


def new_canvas():
    return Image.new(
        "RGB",
        (scaled(OUTPUT_SIZE[0]), scaled(OUTPUT_SIZE[1])),
        BACKGROUND,
    )


def finalize_chart(image):
    """Downsample, then use a compact deterministic palette."""
    downsampled = image.resize(OUTPUT_SIZE, Image.Resampling.LANCZOS)
    quantized = downsampled.quantize(
        colors=128,
        method=Image.Quantize.MEDIANCUT,
        dither=Image.Dither.NONE,
    )

    # Palette mode saves space while keeping average channel error below
    # one RGB level for these flat charts.
    difference = ImageChops.difference(
        downsampled,
        quantized.convert("RGB"),
    )
    mean_error = max(ImageStat.Stat(difference).mean)
    assert mean_error < 1.0, (
        f"palette conversion error is too high: {mean_error:.3f}"
    )
    assert quantized.size == OUTPUT_SIZE
    assert quantized.mode == "P"
    return quantized


def make_devices_chart():
    """Render the five-category collection chart without a title."""
    image = new_canvas()
    draw = ImageDraw.Draw(image)
    label_font = font(16)
    value_font = font(16)
    tick_font = font(13)
    axis_font = font(14)

    plot_left = 170
    plot_right = 570
    plot_top = 34
    plot_bottom = 312
    maximum = 64
    tick_values = (0, 16, 32, 48, 64)

    for tick_value in tick_values:
        x_position = (
            plot_left
            + (plot_right - plot_left) * tick_value / maximum
        )
        draw_line(
            draw,
            ((x_position, plot_top), (x_position, plot_bottom)),
            GRID,
        )
        draw_text(
            draw,
            (x_position, 329),
            str(tick_value),
            tick_font,
            anchor="mm",
        )

    row_colors = (TEAL, DEEP_TEAL, SUNSET, SAND, TEAL)
    row_centers = (57, 111, 165, 219, 273)
    bar_height = 26

    for (label, value), color, center_y in zip(
        DEVICE_ITEMS,
        row_colors,
        row_centers,
        strict=True,
    ):
        draw_text(
            draw,
            (151, center_y),
            label,
            label_font,
            anchor="rm",
        )
        draw_rounded(
            draw,
            (
                plot_left,
                center_y - bar_height / 2,
                plot_right,
                center_y + bar_height / 2,
            ),
            bar_height / 2,
            TRACK,
        )
        bar_right = (
            plot_left
            + (plot_right - plot_left) * value / maximum
        )
        draw_rounded(
            draw,
            (
                plot_left,
                center_y - bar_height / 2,
                bar_right,
                center_y + bar_height / 2,
            ),
            bar_height / 2,
            color,
        )
        draw_text(
            draw,
            (bar_right + 10, center_y),
            str(value),
            value_font,
            anchor="lm",
        )

    draw_line(
        draw,
        ((plot_left, plot_bottom), (plot_right, plot_bottom)),
        DEEP_TEAL,
        width=2,
    )
    draw_text(
        draw,
        ((plot_left + plot_right) / 2, 367),
        "Items collected",
        axis_font,
        DEEP_TEAL,
        anchor="mm",
    )
    draw_text(
        draw,
        (616, 367),
        f"Total: {DEVICE_TOTAL} items",
        tick_font,
        INK,
        anchor="rm",
    )
    return finalize_chart(image)


def make_workshop_chart():
    """Render four months of workshop signup growth without a title."""
    image = new_canvas()
    draw = ImageDraw.Draw(image)
    tick_font = font(13)
    label_font = font(15)
    value_font = font(15)
    axis_font = font(14)

    plot_left = 78
    plot_right = 594
    plot_top = 36
    plot_bottom = 310
    chart_maximum = 45
    y_ticks = (0, 10, 20, 30, 40)

    def value_y(value):
        return (
            plot_bottom
            - (plot_bottom - plot_top) * value / chart_maximum
        )

    for tick_value in y_ticks:
        y_position = value_y(tick_value)
        draw_line(
            draw,
            ((plot_left, y_position), (plot_right, y_position)),
            GRID,
        )
        draw_text(
            draw,
            (60, y_position),
            str(tick_value),
            tick_font,
            anchor="rm",
        )

    x_positions = (100, 258, 416, 574)
    points = tuple(
        (x_position, value_y(value))
        for x_position, (_, value) in zip(
            x_positions,
            WORKSHOP_SIGNUPS,
            strict=True,
        )
    )

    area_points = (
        (points[0][0], plot_bottom),
        *points,
        (points[-1][0], plot_bottom),
    )
    draw.polygon(
        tuple(
            (scaled(x_position), scaled(y_position))
            for x_position, y_position in area_points
        ),
        fill=AREA,
    )
    draw_line(draw, points, DEEP_TEAL, width=4, joint="curve")

    for (month, value), (x_position, y_position) in zip(
        WORKSHOP_SIGNUPS,
        points,
        strict=True,
    ):
        draw.ellipse(
            scaled_box(
                (
                    x_position - 9,
                    y_position - 9,
                    x_position + 9,
                    y_position + 9,
                )
            ),
            fill=WHITE,
            outline=DEEP_TEAL,
            width=scaled(3),
        )
        draw.ellipse(
            scaled_box(
                (
                    x_position - 4,
                    y_position - 4,
                    x_position + 4,
                    y_position + 4,
                )
            ),
            fill=SUNSET,
        )
        draw_rounded(
            draw,
            (
                x_position - 18,
                y_position - 37,
                x_position + 18,
                y_position - 15,
            ),
            8,
            WHITE,
            outline=GRID,
        )
        draw_text(
            draw,
            (x_position, y_position - 26),
            str(value),
            value_font,
            anchor="mm",
        )
        draw_text(
            draw,
            (x_position, 337),
            month,
            label_font,
            anchor="mm",
        )

    draw_line(
        draw,
        ((plot_left, plot_bottom), (plot_right, plot_bottom)),
        DEEP_TEAL,
        width=2,
    )
    draw_text(
        draw,
        (24, 18),
        "Signups",
        axis_font,
        DEEP_TEAL,
        anchor="lm",
    )
    draw_text(
        draw,
        ((plot_left + plot_right) / 2, 375),
        "Month",
        axis_font,
        DEEP_TEAL,
        anchor="mm",
    )
    return finalize_chart(image)


IMAGES = {
    "devices-collected-chart.png": make_devices_chart,
    "workshop-signups-chart.png": make_workshop_chart,
}


def assert_source_data():
    """Pin every value named in the textbook data contract."""
    assert PIL.__version__ == PILLOW_VERSION, (
        f"requires Pillow {PILLOW_VERSION}, found {PIL.__version__}"
    )
    assert DEVICE_ITEMS == (
        ("Cables", 64),
        ("Phones", 38),
        ("Laptops", 21),
        ("Small electronics", 17),
        ("Tablets", 14),
    )
    assert sum(value for _, value in DEVICE_ITEMS) == DEVICE_TOTAL
    assert DEVICE_TOTAL == 154

    signup_values = tuple(value for _, value in WORKSHOP_SIGNUPS)
    assert len(signup_values) == 4
    assert signup_values == (18, 24, 31, 39)
    assert signup_values[0] == 18
    assert signup_values[-1] == 39
    assert all(
        earlier < later
        for earlier, later in zip(
            signup_values[:-1],
            signup_values[1:],
            strict=True,
        )
    )


def render_all():
    """Render all images to deterministic PNG byte strings."""
    rendered = {}
    for name, maker in IMAGES.items():
        image = maker()
        assert image.size == OUTPUT_SIZE, (
            f"{name}: got {image.size}, expected {OUTPUT_SIZE}"
        )
        buffer = io.BytesIO()
        # Pillow does not add a wall-clock timestamp. No pnginfo object is
        # supplied, so these files contain no date or other text metadata.
        image.save(
            buffer,
            format="PNG",
            optimize=True,
            compress_level=9,
        )
        rendered[name] = buffer.getvalue()
    return rendered


def main():
    assert_source_data()
    assert set(IMAGES) == {
        "devices-collected-chart.png",
        "workshop-signups-chart.png",
    }

    first_render = render_all()
    second_render = render_all()

    for name in IMAGES:
        first_hash = hashlib.sha256(first_render[name]).hexdigest()
        second_hash = hashlib.sha256(second_render[name]).hexdigest()
        assert first_hash == second_hash, (
            f"{name}: render is not deterministic"
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, data in first_render.items():
        output_path = OUTPUT_DIR / name
        output_path.write_bytes(data)
        with Image.open(io.BytesIO(data)) as saved_image:
            assert saved_image.size == OUTPUT_SIZE
        print(
            f"wrote {name}: {len(data):,} bytes "
            f"sha256={hashlib.sha256(data).hexdigest()}"
        )

    # chapter-03 holds other pack files, so assert presence of the
    # two charts rather than exclusive directory contents.
    for name in IMAGES:
        assert (OUTPUT_DIR / name).is_file(), f"missing output {name}"
    print("all asserts passed")


if __name__ == "__main__":
    main()
