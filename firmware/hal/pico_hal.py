# firmware/hal/pico_hal.py
#
# Pico W hardware HAL — CircuitPython 9.x implementation.
# Runs on the Raspberry Pi Pico W only; never imported by the desktop simulator.
#
# Pin assignments per specification.md §3 and D-008 (Q-001 resolution):
#   GP8 / GP9   — consumed by Kitronik 5329 I2C bus; DO NOT USE
#   GP10        — IR sensor, left emitter/detector  (DS3)
#   GP11        — IR sensor, right emitter/detector (DS3)
#   GP12–GP19   — QTRX-MD-08RC, 8 sensor elements  (DS5, Phase 3)
#   GP20        — speed sensor, left wheel          (DS7, Phase 4)
#   GP21        — speed sensor, right wheel         (DS7, Phase 4)
#
# Motor control uses the Kitronik 5329 I2C/PCA9685 PWM driver.
# Motor methods are stubbed until the Kitronik CircuitPython library
# is confirmed and integrated in Phase 2.

import board
import digitalio

from firmware.hal.base import MotorHAL, SensorHAL


class PicoSensorHAL(SensorHAL):

    def __init__(self):
        self._ir_left = digitalio.DigitalInOut(board.GP10)
        self._ir_left.direction = digitalio.Direction.INPUT

        self._ir_right = digitalio.DigitalInOut(board.GP11)
        self._ir_right.direction = digitalio.Direction.INPUT

    def read_ir_pair(self):
        # Returns: tuple(bool, bool) — (left_on_line, right_on_line)
        # True = sensor over dark line.
        #
        # NOTE: polarity confirmed in Week 4 hardware test.
        # Assumption: phototransistor + pull-up → GPIO HIGH when over dark line.
        # If readings are inverted on hardware, swap to: not self._ir_left.value
        return (self._ir_left.value, self._ir_right.value)

    def read_reflectance_array(self):
        # Returns: list[float] — 8 normalized readings, 0.0 = white, 1.0 = black
        # Stub — implemented in Phase 3 (Week 11) using GP12–GP19.
        return [0.0] * 8

    def read_wheel_speeds(self):
        # Returns: tuple(float, float) — (left_rpm, right_rpm)
        # Stub — implemented in Phase 4 (Week 14) via interrupt counting on GP20/GP21.
        return (0.0, 0.0)


class PicoMotorHAL(MotorHAL):

    def __init__(self):
        # Stub — Kitronik 5329 drives motors via I2C (GP8/GP9) → PCA9685 PWM chip.
        # Full init implemented in Phase 2 using the Kitronik CircuitPython library.
        pass

    def set_speeds(self, left, right):
        # left, right: float in [-1.0, 1.0]; -1.0 = full reverse, 1.0 = full forward
        # Stub — implemented in Phase 2.
        pass

    def stop(self):
        # Bring both motors to a halt immediately.
        # Stub — implemented in Phase 2.
        pass
