# firmware/hal/sim_hal.py
#
# Simulator HAL — stub implementation for Phase 1.
# Returns safe zero/False values for all reads; motor calls are no-ops.
#
# Completed in Phase 2 (Week 6) once simulator/physics.py exists.
# At that point, sensor reads will sample the physics engine state and
# motor writes will update the simulated robot pose.

from firmware.hal.base import MotorHAL, SensorHAL


class SimSensorHAL(SensorHAL):

    def read_ir_pair(self):
        # Stub — returns (False, False) until physics.py is wired in Phase 2.
        # Returns: tuple(bool, bool) — (left_on_line, right_on_line)
        return (False, False)

    def read_reflectance_array(self):
        # Stub — returns all-white until physics.py is wired in Phase 2.
        # Returns: list[float] — 8 normalized readings, 0.0 = white
        return [0.0] * 8

    def read_wheel_speeds(self):
        # Stub — returns zero RPM until physics.py is wired in Phase 2.
        # Returns: tuple(float, float) — (left_rpm, right_rpm)
        return (0.0, 0.0)


class SimMotorHAL(MotorHAL):

    def set_speeds(self, left, right):
        # Stub — no-op until physics.py is wired in Phase 2.
        # left, right: float in [-1.0, 1.0]
        pass

    def stop(self):
        # Stub — no-op until physics.py is wired in Phase 2.
        pass
