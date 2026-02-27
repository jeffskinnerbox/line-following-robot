# tests/unit/test_hal_base.py
#
# Verify that SensorHAL, MotorHAL, and ControllerBase cannot be instantiated
# directly — they must raise TypeError (abstract class enforcement).

import pytest
from firmware.hal.base import ControllerBase, MotorHAL, SensorHAL


def test_sensor_hal_is_abstract():
    with pytest.raises(TypeError):
        SensorHAL()


def test_motor_hal_is_abstract():
    with pytest.raises(TypeError):
        MotorHAL()


def test_controller_base_is_abstract():
    with pytest.raises(TypeError):
        ControllerBase()
