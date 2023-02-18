# This file is used for development testing
import time

from cart_control.cart_control import CartControl

if __name__ == "__main__":

    cart = CartControl()
    cart.connect()
    cart.dump_errors(True)
    cart.calibrate()
    cart.homing()

    cart.set_position_control()
    print("Setting pos -3.0")
    cart.set_position(-3.0)
    time.sleep(3)
    print("Setting pos 0.0")
    cart.set_position(0.0)
    time.sleep(3)
    print("Setting pos 3.0")
    cart.set_position(3.0)
    time.sleep(3)
    print("Setting pos 0.0")
    cart.set_position(0.0)
    time.sleep(3)
    cart.set_state_idle()
