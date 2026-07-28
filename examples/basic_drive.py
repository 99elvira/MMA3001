"""
Example: Connect and drive the Sphero RVR.
"""

import logging
from sphero_monash_student import Robot
from sphero_monash_student.utils import setup_logging


def main():
    setup_logging(level=logging.INFO)
    logger = logging.getLogger(__name__)

    robot = Robot()

    try:
        logger.info("Connecting to robot...")
        robot.connect()

        logger.info("Driving forward...")
        robot.drive(heading=0, speed=50)

        input("Press Enter to stop...")

    except KeyboardInterrupt:
        logger.info("Interrupted by user")
    finally:
        robot.stop()
        robot.disconnect()
        logger.info("Done.")


if __name__ == "__main__":
    main()
