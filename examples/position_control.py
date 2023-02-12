import time
import odrive
from odrive.enums import *


if __name__ == "__main__":
    calibrated = True  # Set False to run full calibration sequence
    drive_serial = '209034615333'
    drive0 = odrive.find_any(serial_number=drive_serial)

    if not calibrated:
        drive0.axis0.requested_state = AxisState.FULL_CALIBRATION_SEQUENCE
        time.sleep(1)

    if drive0.axis0.current_state != AxisState.CLOSED_LOOP_CONTROL:
        while drive0.axis0.current_state != AxisState.IDLE:
            print(f"Still calibrating. State: [{drive0.axis0.current_state}]")
            time.sleep(1)
        print(f"Done calibrating. State: [{drive0.axis0.current_state}]")
        time.sleep(1)
        drive0.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL
        time.sleep(0.1)

    full_rotation = 8192
    no_of_turns = 50

    for i in range(full_rotation):
        drive0.axis0.controller.input_pos = i/full_rotation * no_of_turns
        time.sleep(0.001)

    # Go back
    for i in range(full_rotation):

        drive0.axis0.controller.input_pos = no_of_turns - (i / full_rotation * no_of_turns)
        time.sleep(0.001)

    print("Finished running steps")
