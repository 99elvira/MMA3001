"""Image averaging utility for noise reduction.

This module provides a function to average multiple noisy images of the
same scene, producing a cleaner composite. It leverages the statistical
property that random noise cancels out when averaged across many samples.

Typical usage example:

    from averager import average_images
    average_images("path/to/noisy_images/", "output/clean.png")
"""

import numpy as np
from PIL import Image
import os
from glob import glob


def average_images(input_dir: str, output_path: str = "averaged.png") -> None:
    """Average all PNG images in a directory to produce a denoised composite.

    Reads every ``.png`` file in *input_dir*, accumulates them in a
    floating‑point array, then divides by the total count and saves the
    result to *output_path*.  This technique reduces zero‑mean random
    noise by a factor of √N (where N is the number of input images).

    Args:
        input_dir: Path to the directory containing source PNG images.
            Files are sorted alphabetically before processing so the
            result is deterministic.
        output_path: File path where the averaged PNG will be written.
            Defaults to ``"averaged.png"`` in the current directory.

    Raises:
        ValueError: If *input_dir* contains no ``.png`` files.

    Example:
        >>> average_images("noisy_frames/", "denoised.png")
        Averaged image saved to denoised.png
    """
    # Collect and sort all PNG paths in the input directory
    files = sorted(glob(os.path.join(input_dir, "*.png")))

    # Guard against an empty directory (could happen if the user
    # points to the wrong folder or the generator hasn't run yet)
    if not files:
        raise ValueError("No PNG images found in directory.")

    # Read the first image to determine dimensions for the accumulator
    first = np.array(Image.open(files[0]), dtype=np.float64)
    accumulator = np.zeros_like(first)

    # Sum every image pixel‑by‑pixel into the accumulator.
    # Using float64 prevents overflow during summation.
    for f in files:
        accumulator += np.array(Image.open(f), dtype=np.float64)

    # Divide by the number of images to get the per‑pixel mean,
    # then cast back to uint8 for saving as a standard PNG.
    averaged = (accumulator / len(files)).astype(np.uint8)

    # Convert the NumPy array back to a Pillow Image and persist it
    out_img = Image.fromarray(averaged)
    out_img.save(output_path)

    print(f"Averaged image saved to {output_path}")
