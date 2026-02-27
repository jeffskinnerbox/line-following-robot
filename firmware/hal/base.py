# firmware/hal/base.py
#
# Abstract base classes (ABCs) for the Hardware Abstraction Layer (HAL).
# All firmware modules access hardware exclusively through these interfaces.
# This allows the same controller code to run on both the Pico W and the
# desktop simulator — neither ever imports a hardware-specific library directly.
#
# Implementations:
#   pico_hal.py  — real GPIO on the Raspberry Pi Pico W (CircuitPython 9.x)
#   sim_hal.py   — delegates to simulator/physics.py (Python 3.12)
#
# CircuitPython compatibility: no typing module; no dataclasses; no walrus op.

from abc import ABC, abstractmethod


class SensorHAL(ABC):

    @abstractmethod
    def read_ir_pair(self):
        # Returns: tuple(bool, bool) — (left_on_line, right_on_line)
        # True = sensor over dark line.
        pass

    @abstractmethod
    def read_reflectance_array(self):
        # Returns: list[float] — 8 normalized readings.
        # 0.0 = white surface, 1.0 = black line.
        pass

    @abstractmethod
    def read_wheel_speeds(self):
        # Returns: tuple(float, float) — (left_rpm, right_rpm)
        # Positive = forward.
        pass


class MotorHAL(ABC):

    @abstractmethod
    def set_speeds(self, left, right):
        # left, right: float in [-1.0, 1.0]
        # -1.0 = full reverse, 1.0 = full forward.
        pass

    @abstractmethod
    def stop(self):
        # Bring both motors to a halt immediately.
        pass


class ControllerBase(ABC):

    @abstractmethod
    def compute(self, sensor, speed, dt):
        # Compute motor output.
        #
        # Args:
        #   sensor: list[float] — normalized sensor readings
        #           (length matches active sensor mode)
        #   speed:  tuple(float, float) — current (left_rpm, right_rpm)
        #   dt:     float — elapsed seconds since last call
        #
        # Returns: tuple(float, float) — (left_output, right_output)
        #          each in [-1.0, 1.0]
        pass

    @abstractmethod
    def configure(self, params):
        # Apply runtime tuning parameters.
        # params: dict — called from WiFi UI or config.py
        pass

    @abstractmethod
    def reset(self):
        # Reset internal state (integrators, Q-table replay, etc.).
        pass
