import time
import odrive
from odrive.enums import *
from odrive.utils import *


class CartControl:

    def __init__(self):
        self.serial = '209034615333'
        self.drive: odrive = None

    def connect(self):
        self.drive = odrive.find_any(serial_number=self.serial)
        time.sleep(0.25)

    def calibrate(self):
        self.drive.axis0.requested_state = AxisState.ENCODER_INDEX_SEARCH
        time.sleep(0.25)
        while self.drive.axis0.current_state != AxisState.IDLE:
            time.sleep(0.25)
        time.sleep(0.25)
        self.drive.axis0.requested_state = AxisState.ENCODER_OFFSET_CALIBRATION
        time.sleep(0.25)
        while self.drive.axis0.current_state != AxisState.IDLE:
            time.sleep(0.25)
        time.sleep(0.25)

    def homing(self):
        self.drive.axis0.requested_state = AxisState.HOMING
        time.sleep(0.25)
        while self.drive.axis0.current_state != AxisState.IDLE:
            time.sleep(0.25)

    def set_state_idle(self):
        self.drive.axis0.requested_state = AxisState.IDLE

    def set_position_control(self):
        self.drive.axis0.controller.config.control_mode = ControlMode.POSITION_CONTROL
        time.sleep(0.25)
        self.drive.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL
        time.sleep(0.25)

    def set_position(self, position):
        full_rotation = 8192  # Encoder CPR
        start_pos = self.drive.axis0.encoder.pos_estimate
        step_size = 10

        for i in range(0, full_rotation+step_size, step_size):
            cal_pos = start_pos + i/full_rotation * (position - start_pos)
            self.drive.axis0.controller.input_pos = cal_pos
            time.sleep(0.0001)

    def dump_errors(self, clear_errors: bool = False):
        odrive.utils.dump_errors(self.drive, clear_errors)
