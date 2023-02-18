import time

import fibre
import odrive
from odrive.enums import *


def set_motor_configurations(drive: odrive):
    drive.axis0.motor.config.current_lim = 8
    time.sleep(0.25)
    drive.axis0.motor.config.current_lim = 8
    time.sleep(0.25)
    drive.axis0.controller.config.vel_limit = 30
    time.sleep(0.25)
    drive.config.enable_brake_resistor = True
    time.sleep(0.25)
    drive.config.brake_resistance = 2.0
    time.sleep(0.25)
    drive.config.dc_max_negative_current = -0.01
    time.sleep(0.25)
    drive.axis0.motor.config.pole_pairs = 7
    time.sleep(0.25)
    drive.axis0.motor.config.torque_constant = 0.02468656716
    time.sleep(0.25)
    drive.axis0.motor.config.motor_type = 0
    time.sleep(0.25)
    drive.axis0.encoder.config.cpr = 8192
    time.sleep(0.25)


# https://docs.odriverobotics.com/v/0.5.5/control-modes.html#velocity-control
if __name__ == "__main__":

    drive_serial = '209034615333'
    drive0 = odrive.find_any(serial_number=drive_serial)

    set_motor_configurations(drive0)
    drive0.axis0.requested_state = AxisState.FULL_CALIBRATION_SEQUENCE
    time.sleep(1)

    print_state = True
    while drive0.axis0.current_state != AxisState.IDLE:
        if print_state:
            print(f"Calibrating. State: [{drive0.axis0.current_state}]")
            print_state = False
        time.sleep(1)
    print(f"Done calibrating. State: [{drive0.axis0.current_state}]")

    time.sleep(1)
    drive0.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL

    time.sleep(2)
    drive0.axis0.requested_state = AxisState.IDLE

    time.sleep(1)
    drive0.axis0.motor.config.pre_calibrated = True
    try:
        drive0.save_configuration()

    # except fibre.libfibre.ObjectLostError:  # TODO Cannot find module
    except:
        pass

    print("Done calibrating motor on axis 0")
