import odrive
from odrive.enums import *


if __name__ == "__main__":
    drive_serial = '209034615333'
    drive0 = odrive.find_any(serial_number=drive_serial)
    drive0.axis0.requested_state = AxisState.FULL_CALIBRATION_SEQUENCE
