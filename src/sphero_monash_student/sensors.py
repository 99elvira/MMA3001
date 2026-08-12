"""
Sensor data collection module for Sphero RVR.
"""

import logging
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class SensorData:
    """Container for sensor readings from the Sphero RVR.

    Attributes:
        accelerometer: (x, y, z) accelerometer values.
        gyroscope: (x, y, z) gyroscope values.
        encoder_left: Left encoder count.
        encoder_right: Right encoder count.
        battery_percentage: Battery level as percentage.
    """

    accelerometer: Optional[tuple] = None
    gyroscope: Optional[tuple] = None
    encoder_left: Optional[int] = None
    encoder_right: Optional[int] = None
    battery_percentage: Optional[float] = None


class SensorCollector:
    """Collects and processes sensor data from the Sphero RVR."""

    def __init__(self):
        self.data_buffer: list[SensorData] = []

    def read_sensors(self) -> SensorData:
        """Read current sensor values from the robot.

        Returns:
            SensorData object with current readings.
        """
        # TODO: Implement sensor reading via Sphero SDK
        data = SensorData()
        self.data_buffer.append(data)
        logger.debug(f"Read sensor data: {data}")
        return data

    def clear_buffer(self) -> None:
        """Clear the sensor data buffer."""
        self.data_buffer.clear()

    def get_buffer(self) -> list[SensorData]:
        """Get all buffered sensor readings.

        Returns:
            List of SensorData objects.
        """
        return self.data_buffer.copy()
