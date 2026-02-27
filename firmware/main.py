# firmware/main.py
#
# Entry point for the Raspberry Pi Pico W (CircuitPython 9.x).
# Not imported by the desktop simulator — the simulator has simulator/main.py.
#
# Controller dispatch is added in Phase 2 once bang_bang.py is complete.

import firmware.config as config
from firmware.hal.pico_hal import PicoMotorHAL, PicoSensorHAL

sensor_hal = PicoSensorHAL()
motor_hal = PicoMotorHAL()

while True:
    pass
