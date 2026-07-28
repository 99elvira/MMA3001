"""
Utility functions for the Sphero Monash Student project.
"""

import csv
import json
import logging
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


def setup_logging(level: int = logging.INFO) -> None:
    """Configure logging for the project.

    Args:
        level: Logging level (default: INFO).
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def save_to_csv(data: list[dict[str, Any]], filepath: str | Path) -> None:
    """Save a list of dictionaries to a CSV file.

    Args:
        data: List of dictionaries to save.
        filepath: Output file path.
    """
    filepath = Path(filepath)
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
    logger.info(f"Data saved to {filepath}")


def load_from_csv(filepath: str | Path) -> pd.DataFrame:
    """Load data from a CSV file into a DataFrame.

    Args:
        filepath: Path to the CSV file.

    Returns:
        DataFrame containing the data.
    """
    df = pd.read_csv(Path(filepath))
    logger.info(f"Data loaded from {filepath}: {len(df)} rows")
    return df


def cartesian_to_polar(x: float, y: float) -> tuple[float, float]:
    """Convert cartesian coordinates to polar.

    Args:
        x: X coordinate.
        y: Y coordinate.

    Returns:
        Tuple of (radius, angle_in_degrees).
    """
    radius = np.sqrt(x**2 + y**2)
    angle = np.degrees(np.arctan2(y, x))
    return radius, angle
