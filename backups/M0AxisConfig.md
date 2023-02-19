
$$ k_t = \frac{15\sqrt{3}}{\pi K_V}$$

Motor parameters

    Measured phase resitance R_A = R_B = R_C =~ 0.3 Ohm
    Estimated phase resitance = 0.10922777652740479 Ohm
    Estimated phase inductance = 2.947691609733738e-05
    KV = 335
    Torue conastant = 8.27 / (KV) = 8.27/335 = 0.02468656716
    Max distance is about -12.691797256469727 turns
    Min distance is about -0.037105560302734375 turns

    Moving to the right is negative and moving towards the left is positiv
    --> (-)
    <-- (+)

Config variables

    dev0.axis0.motor.config.current_lim = 8 [A]
    dev0.axis0.motor.config.current_lim = 8 [A]
    dev0.axis0.controller.config.vel_limit = 30 [A]
    dev0.config.enable_brake_resistor = True
    dev0.config.brake_resistance = 2.0 [Ohm]
    dev0.config.dc_max_negative_current = -0.01 [A]
    dev0.axis0.motor.config.pole_pairs = 7 [-]
    dev0.axis0.motor.config.torque_constant = 0.02468656716 [Nm]
    dev0.axis0.motor.config.motor_type = 0 [MOTOR_TYPE_HIGH_CURRENT]
    dev0.axis0.encoder.config.cpr = 8192 [cpr]


## M0 Axis config ##
Use these commands so set the motor ready for FULL_CALIBRATION_SEQUENCE
to perform the necessary motor calibration. 

    dev0.axis0.motor.config.current_lim = 8
    dev0.axis0.motor.config.current_lim = 8
    dev0.axis0.controller.config.vel_limit = 30
    dev0.config.enable_brake_resistor = True
    dev0.config.brake_resistance = 2.0
    dev0.config.dc_max_negative_current = -0.01
    dev0.axis0.motor.config.pole_pairs = 7
    dev0.axis0.motor.config.torque_constant = 0.02468656716
    dev0.axis0.motor.config.motor_type = 0
    dev0.axis0.encoder.config.cpr = 8192

Then run the full calibration sequence

    dev0.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE

Don't forget to store the result to avoid having to perform the motor calibration on startup of the ODrive

    dev0.axis0.motor.config.pre_calibrated = True
    dev0.axis0.encoder.config.pre_calibrated = True
    dev0.save_configuration()


## End stop setup and calibration ##

**Min end stop (left side) - GPIO 8** 

    dev0.config.gpio8_mode = GPIO_MODE_DIGITAL
    dev0.axis0.min_endstop.config.gpio_num = 8
    dev0.axis0.min_endstop.config.is_active_high = False
    dev0.axis0.min_endstop.config.offset = 0.0
    dev0.axis0.min_endstop.config.enabled = True

**Max end stop (right side) - GPIO 7**

    dev0.config.gpio7_mode = GPIO_MODE_DIGITAL
    dev0.axis0.max_endstop.config.gpio_num = 7
    dev0.axis0.max_endstop.config.is_active_high = False
    dev0.axis0.max_endstop.config.offset = 0.0
    dev0.axis0.max_endstop.config.enabled = True

The internal pull/down is not used due to the end switch having an onboard pull down.

**Setting homing direction**

    dev0.axis0.controller.config.homing_speed = -6.346
    dev0.axis0.config.startup_homing = True


## On startup ##

Run the index calibration before starting:

    dev0.axis0.requested_state = AXIS_STATE_ENCODER_INDEX_SEARCH    
    dev0.axis0.requested_state = AXIS_STATE_ENCODER_OFFSET_CALIBRATION

Then the motor is ready to be used.

## MISC ##

Motor information is inside of

    dev0.axis0.motor.config

i.e

    dev0.axis0.motor.config.phase_resistance


To save the configuration to a file on the PC, run

    odrivetool backup-config my_config.json

To restore the configuration form such a file, run

    odrivetool restore-config my_config.json


Check the current set points

    dev0.axis0.controller.pos_setpoint
    dev0.axis0.controller.torque_setpoint
    dev0.axis0.controller.vel_setpoint  