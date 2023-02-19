# This file is used for development testing

import time
from cart_control import CartControl


def test_position_control(controller: CartControl):
    controller.set_position_control()
    print("Setting pos -3.0")
    controller.set_position(-3.0)
    time.sleep(3)
    print("Setting pos 0.0")
    controller.set_position(0.0)
    time.sleep(3)
    print("Setting pos 3.0")
    controller.set_position(3.0)
    time.sleep(3)
    print("Setting pos 0.0")
    controller.set_position(0.0)
    time.sleep(3)
    controller.set_state_idle()


def test_velocity_control(controller: CartControl):
    controller.set_velocity_control()
    velocity_setpoint = 1.5
    print("Setting velocity to 0.2 [turn/s]")
    controller.set_velocity(velocity_setpoint)
    time.sleep(3)
    print("Setting velocity to 0.0 [turn/s]")
    controller.set_velocity(0.0)
    time.sleep(2)
    print("Setting velocity to -0.2 [turn/s]")
    controller.set_velocity(-velocity_setpoint)
    time.sleep(3)
    print("Setting velocity to 0.0 [turn/s]")
    controller.set_velocity(0.0)
    time.sleep(2)
    print("Setting velocity to -0.2 [turn/s]")
    controller.set_velocity(-velocity_setpoint)
    time.sleep(3)
    print("Setting velocity to 0.0 [turn/s]")
    controller.set_velocity(0.0)
    time.sleep(2)
    print("Setting velocity to 0.2 [turn/s]")
    controller.set_velocity(velocity_setpoint)
    time.sleep(3)
    print("Setting velocity to 0.0 [turn/s]")
    controller.set_velocity(0.0)
    time.sleep(2)
    controller.set_state_idle()


def test_torque_control(controller: CartControl):
    controller.set_torque_control()
    torque_setpoint = 0.035
    torque_time = 1.0
    print(f"Setting velocity to {torque_setpoint} [Nm]")
    controller.set_torque(torque_setpoint)
    time.sleep(torque_time)
    print("Setting velocity to 0.0 [Nm]")
    controller.set_torque(0.0)
    time.sleep(2)
    print(f"Setting velocity to {-torque_setpoint} [Nm]")
    controller.set_torque(-torque_setpoint)
    time.sleep(torque_time)
    print("Setting velocity to 0.0 [Nm]")
    controller.set_torque(0.0)
    time.sleep(2)
    print(f"Setting velocity to {-torque_setpoint} [Nm]")
    controller.set_torque(-torque_setpoint)
    time.sleep(torque_time)
    print("Setting velocity to 0.0 [Nm]")
    controller.set_torque(0.0)
    time.sleep(2)
    print(f"Setting velocity to {torque_setpoint} [Nm]")
    controller.set_torque(torque_setpoint)
    time.sleep(torque_time)
    print("Setting velocity to 0.0 [Nm]")
    controller.set_torque(0.0)
    time.sleep(2)
    controller.set_state_idle()


if __name__ == "__main__":

    cart = CartControl()
    cart.connect()
    cart.dump_errors(True)
    cart.calibrate()
    cart.homing()

    print("Performing position control test")
    test_position_control(cart)
    print("Performing velocity control test")
    test_velocity_control(cart)
    print("Performing torque control test")
    test_torque_control(cart)
