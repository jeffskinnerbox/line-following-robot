# tests/unit/test_ir_sensor.py
#
# Covers all four IR pair input combinations for read_ir_pair().
# Uses a stub SensorHAL so no hardware is required.

from firmware.hal.base import SensorHAL
from firmware.sensors.ir_sensor import read_ir_pair


class _StubSensorHAL(SensorHAL):

    def __init__(self, ir_pair):
        self._ir_pair = ir_pair

    def read_ir_pair(self):
        return self._ir_pair

    def read_reflectance_array(self):
        return [0.0] * 8

    def read_wheel_speeds(self):
        return (0.0, 0.0)


def test_both_off_line():
    # Both sensors see white — robot has lost the line.
    assert read_ir_pair(_StubSensorHAL((False, False))) == (False, False)


def test_left_on_line():
    # Left sensor over dark line — robot drifted right; must turn left.
    assert read_ir_pair(_StubSensorHAL((True, False))) == (True, False)


def test_right_on_line():
    # Right sensor over dark line — robot drifted left; must turn right.
    assert read_ir_pair(_StubSensorHAL((False, True))) == (False, True)


def test_both_on_line():
    # Both sensors over line — robot is centred; go straight.
    assert read_ir_pair(_StubSensorHAL((True, True))) == (True, True)
