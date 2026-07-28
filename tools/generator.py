"""Synthetic noisy‑image generator.

Creates a batch of PNG images containing centred text overlaid with
Gaussian noise.  These images are intended as test inputs for the
``averager.py`` module, which demonstrates noise reduction through
image stacking and averaging.
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os


def generate_noisy_images(
    output_dir: str,
    n_images: int = 20,
    width: int = 800,
    height: int = 400,
    noise_level: float = 0.25,
) -> None:
    """Generate PNG images with centred text and additive Gaussian noise.

    Each image is an 800×400 (default) white canvas with the word
    ``"MMA3001"`` drawn in black at the centre.  Gaussian noise with a
    standard deviation of ``255 × noise_level`` is then added to every
    colour channel independently, producing a set of noisy observations
    of the same underlying signal.

    Args:
        output_dir: Directory in which to save the generated images.
            Created automatically if it does not exist.
        n_images: Number of noisy images to generate.  Defaults to 20.
        width: Image width in pixels.  Defaults to 800.
        height: Image height in pixels.  Defaults to 400.
        noise_level: Multiplier controlling noise intensity.
            0.0 = no noise; 1.0 = very strong noise (±255 per channel).
            Defaults to 0.25.

    Example:
        >>> from generator import generate_noisy_images
        >>> generate_noisy_images("images/", n_images=50, noise_level=0.3)
        Generated 50 noisy images in images/
    """
    # Ensure the output folder exists (idempotent if it already does)
    os.makedirs(output_dir, exist_ok=True)

    # Try to load a TrueType font for nicer rendering; fall back to the
    # default bitmap font if Arial isn't available on this system.
    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except OSError:
        font = ImageFont.load_default()

    for i in range(n_images):
        # Create a fresh white canvas for each image
        img = Image.new("RGB", (width, height), color="white")
        draw = ImageDraw.Draw(img)

        text = "MMA3001"

        # Measure the bounding box of the text so we can centre it
        # precisely on the canvas.
        bbox = draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]

        # Compute top‑left corner such that the text is centred
        pos = ((width - text_w) // 2, (height - text_h) // 2)

        # Render the centred text in solid black
        draw.text(pos, text, fill="black", font=font)

        # Add zero‑mean Gaussian noise scaled by noise_level.
        # np.random.randn produces values ~ N(0, 1); multiplying by
        # 255 * noise_level scales to the pixel intensity range.
        noise = np.random.randn(height, width, 3) * 255 * noise_level

        # Add noise to the image and clip to valid 8‑bit range [0, 255]
        noisy = np.clip(np.array(img) + noise, 0, 255).astype(np.uint8)

        noisy_img = Image.fromarray(noisy)

        # Save with zero‑padded numbering so file‑system sorting is
        # consistent (e.g. noisy_000.png, noisy_001.png, …).
        noisy_img.save(os.path.join(output_dir, f"noisy_{i:03d}.png"))

    print(f"Generated {n_images} noisy images in {output_dir}")
