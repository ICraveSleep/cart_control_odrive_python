import time
import odrive
from odrive.enums import *

# https://docs.odriverobotics.com/v/latest/control-modes.html#ramped-velocity-control
if __name__ == "__main__":
    calibrated = True  # Set False to run full calibration sequence
    drive0 = odrive.find_any()

    if not calibrated:
        drive0.axis0.requested_state = AxisState.FULL_CALIBRATION_SEQUENCE
        time.sleep(1)

    if drive0.axis0.current_state != AxisState.CLOSED_LOOP_CONTROL:
        while drive0.axis0.current_state != AxisState.IDLE:
            print(f"Still calibrating. State: [{drive0.axis0.current_state}]")
            time.sleep(1)
        print(f"Done calibrating. State: [{drive0.axis0.current_state}]")
        time.sleep(1)
        drive0.axis0.controller.config.control_mode = ControlMode.VELOCITY_CONTROL
        drive0.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL
        time.sleep(0.5)
    print(f"Velocity limit = {drive0.axis0.controller.config.vel_limit}")
    drive0.axis0.controller.input_vel = 10  # [turns/s]
    time.sleep(2.5)
    drive0.axis0.controller.input_vel = -10  # [turns/s]
    time.sleep(2.5)

    drive0.axis0.controller.input_vel = 0
    drive0.axis0.requested_state = AxisState.IDLE

    print("Finished running steps")
