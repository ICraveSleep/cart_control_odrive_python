import time
import odrive
from odrive.enums import *


def configure_min_end_stop(drive: odrive):
    drive.config.gpio8_mode = GpioMode.DIGITAL
    time.sleep(0.25)
    drive.axis0.min_endstop.config.gpio_num = 8
    time.sleep(0.25)
    drive.axis0.min_endstop.config.is_active_high = False
    time.sleep(0.25)
    drive.axis0.min_endstop.config.offset = 0.0
    time.sleep(0.25)
    drive.axis0.min_endstop.config.enabled = True
    time.sleep(0.25)


def configure_max_end_stop(drive: odrive):
    drive.config.gpio7_mode = GpioMode.DIGITAL
    time.sleep(0.25)
    drive.axis0.max_endstop.config.gpio_num = 7
    time.sleep(0.25)
    drive.axis0.max_endstop.config.is_active_high = False
    time.sleep(0.25)
    drive.axis0.max_endstop.config.offset = 0.0
    time.sleep(0.25)
    drive.axis0.max_endstop.config.enabled = True
    time.sleep(0.25)


if __name__ == "__main__":
    drive_serial = '209034615333'
    drive0 = odrive.find_any(serial_number=drive_serial)

    configure_min_end_stop(drive0)
    print("Configured min end stop")
    configure_max_end_stop(drive0)
    print("Configured max end stop")

    drive0.axis0.controller.config.homing_speed = -0.5

    try:
        drive0.save_configuration()
    except:
        pass
