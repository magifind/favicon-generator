import cairosvg
import argparse
from PIL import Image, ImageOps
from io import BytesIO
import os


def hex_to_rgba(hex_color):
    # Convert a hex color string to an RGBA tuple
    hex_color = hex_color.lstrip("#")
    lv = len(hex_color)
    return tuple(int(hex_color[i : i + lv // 3], 16) for i in range(0, lv, lv // 3)) + (
        255,
    )


def create_favicons(filename, hex_color=None):
    # Load and convert the SVG file
    svg_file = os.path.join(os.getcwd(), "svg", f"{filename}.svg")
    png_data = cairosvg.svg2png(url=svg_file)
    svg_image = Image.open(BytesIO(png_data)).convert("RGBA")

    # Apply the color if specified
    if hex_color:
        rgba_color = hex_to_rgba(hex_color)
        svg_image = ImageOps.colorize(
            Image.new("L", svg_image.size, 0), (0, 0, 0, 0), rgba_color
        )

    # Define the sizes for the favicon
    sizes = [16, 32, 48, 64, 128, 256]

    # Create favicons
    for size in sizes:
        resized_svg = svg_image.resize((size, size), resample=Image.LANCZOS)

        # Create a new image with the same size as the resized SVG
        composite_image = Image.new("RGBA", resized_svg.size, (0, 0, 0, 0))
        composite_image.alpha_composite(resized_svg, (0, 0))

        # Save the composite image
        composite_image.save(os.path.join(os.getcwd(), f"{filename}-{size}x{size}.png"))


def main():
    parser = argparse.ArgumentParser(description="Create favicons from SVG.")
    parser.add_argument(
        "filename", type=str, help="Base name of the SVG file in the ./svg folder"
    )
    parser.add_argument(
        "--color", type=str, help="Hex color value for the icon, e.g., #FF5733"
    )
    args = parser.parse_args()
    create_favicons(args.filename, args.color)


if __name__ == "__main__":
    main()
