"""
Example: Collect sensor data from the Sphero RVR and save to CSV.
"""

import logging
import time
from datetime import datetime

from sphero_monash_student import Robot
from sphero_monash_student.sensors import SensorCollector
from sphero_monash_student.utils import setup_logging, save_to_csv


def main():
    setup_logging(level=logging.INFO)
    logger = logging.getLogger(__name__)

    robot = Robot()
    collector = SensorCollector()
    duration_seconds = 30
    sample_interval = 0.1  # 10 Hz

    try:
        robot.connect()
        logger.info(f"Collecting data for {duration_seconds}s at {1/sample_interval:.0f}Hz...")

        start = time.time()
        while time.time() - start < duration_seconds:
            data = collector.read_sensors()
            time.sleep(sample_interval)

        # Save results
        buffer = collector.get_buffer()
        rows = [
            {
                "timestamp": start + i * sample_interval,
                "enc_left": d.encoder_left,
                "enc_right": d.encoder_right,
                "battery": d.battery_percentage,
            }
            for i, d in enumerate(buffer)
        ]

        filename = f"../data/sensor_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        save_to_csv(rows, filename)
        logger.info(f"Saved {len(rows)} readings to {filename}")

    except KeyboardInterrupt:
        logger.info("Interrupted by user")
    finally:
        robot.stop()
        robot.disconnect()


if __name__ == "__main__":
    main()
