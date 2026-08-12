"""Unit tests for the Robot class."""

import pytest
from sphero_monash_student import Robot


class TestRobot:
    def test_robot_initialization(self):
        robot = Robot()
        assert robot.connected is False
        assert robot.port is None

    def test_robot_with_port(self):
        robot = Robot(port="/dev/ttyUSB0")
        assert robot.port == "/dev/ttyUSB0"

    def test_drive_without_connection_raises(self):
        robot = Robot()
        with pytest.raises(ConnectionError):
            robot.drive(0, 50)

    def test_stop_without_connection_raises(self):
        robot = Robot()
        with pytest.raises(ConnectionError):
            robot.stop()

    def test_connect_and_disconnect(self):
        robot = Robot()
        assert robot.connect() is True
        assert robot.connected is True
        robot.disconnect()
        assert robot.connected is False
