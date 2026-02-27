# firmware/config.py
#
# Central store for all tunable parameters.
# Loaded at startup; updated at runtime via configure() calls from web_server.py.
#
# WIFI_SSID: change the trailing digit per robot (LFR-1 through LFR-6).
# All other defaults match specification.md Section 5.

CONTROLLER    = "bang_bang"   # active controller module name
BASE_SPEED    = 0.5           # nominal forward speed (0.0–1.0)
SENSOR_TYPE   = "ir_pair"     # "ir_pair" or "reflectance_array"

WIFI_SSID     = "LFR-1"       # per-robot unique SSID; update before flashing
WIFI_PASSWORD = "lfr12345"

PID_KP        = 1.0           # proportional gain
PID_KI        = 0.0           # integral gain
PID_KD        = 0.1           # derivative gain

KALMAN_Q      = 0.01          # process noise covariance
KALMAN_R      = 0.1           # measurement noise covariance

QL_ALPHA      = 0.1           # Q-Learning learning rate
QL_GAMMA      = 0.9           # Q-Learning discount factor
QL_EPSILON    = 0.1           # Q-Learning exploration rate
