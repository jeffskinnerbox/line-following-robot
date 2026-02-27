# firmware/sensors/ir_sensor.py
#
# IR emitter/phototransistor pair reader.
# Reads one sensor pair through the SensorHAL interface.
#
# The four possible states returned by read_ir_pair():
#   (False, False) — both sensors off line; robot has lost track
#   (True,  False) — left sensor on line; turn left to correct
#   (False, True)  — right sensor on line; turn right to correct
#   (True,  True)  — both sensors on line; robot is centred


def read_ir_pair(sensor):
    # sensor: SensorHAL instance
    # Returns: tuple(bool, bool) — (left_on_line, right_on_line)
    return sensor.read_ir_pair()
