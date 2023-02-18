import time
import odrive
from odrive.enums import *
from odrive.utils import *

# https://docs.odriverobotics.com/v/latest/troubleshooting.html
if __name__ == "__main__":
    drive0 = odrive.find_any()

    dump_errors(drive0, False)  # Print in rich text

    error = odrive.utils.format_errors(drive0)  # Get errors as RichText object
    for segment in error.segments:
        print(segment)

    axis_error = drive0.axis0.error  # 0 if no error, https://docs.odriverobotics.com/v/devel/fibre_types/com_odriverobotics_ODrive.html#ODrive.Error
    print(f"\n Current error on axis0: {axis_error}")


###############################################################################################
# ('system: ', <Color.DEFAULT: 1>, <Color.DEFAULT: 1>, <Style.NONE: 0>)
# ('no error', <Color.GREEN: 5>, <Color.DEFAULT: 1>, <Style.BOLD: 1>)
# ('\naxis0\n  axis: ', <Color.DEFAULT: 1>, <Color.DEFAULT: 1>, <Style.NONE: 0>)
# ('Error(s):', <Color.RED: 3>, <Color.DEFAULT: 1>, <Style.BOLD: 1>)
# ('\n    ', <Color.DEFAULT: 1>, <Color.DEFAULT: 1>, <Style.NONE: 0>)
# ('AxisError.MIN_ENDSTOP_PRESSED', <Color.RED: 3>, <Color.DEFAULT: 1>, <Style.BOLD: 1>)
# ('\n    ', <Color.DEFAULT: 1>, <Color.DEFAULT: 1>, <Style.NONE: 0>)
# ('AxisError.MAX_ENDSTOP_PRESSED', <Color.RED: 3>, <Color.DEFAULT: 1>, <Style.BOLD: 1>)
# ('\n  motor: ', <Color.DEFAULT: 1>, <Color.DEFAULT: 1>, <Style.NONE: 0>)
# ('no error', <Color.GREEN: 5>, <Color.DEFAULT: 1>, <Style.BOLD: 1>)
# ('\n  DRV fault: ', <Color.DEFAULT: 1>, <Color.DEFAULT: 1>, <Style.NONE: 0>)
# ('none', <Color.GREEN: 5>, <Color.DEFAULT: 1>, <Style.BOLD: 1>)
# ('\n  sensorless_estimator: ', <Color.DEFAULT: 1>, <Color.DEFAULT: 1>, <Style.NONE: 0>)
# ('no error', <Color.GREEN: 5>, <Color.DEFAULT: 1>, <Style.BOLD: 1>)
# ('\n  encoder: ', <Color.DEFAULT: 1>, <Color.DEFAULT: 1>, <Style.NONE: 0>)
# ('no error', <Color.GREEN: 5>, <Color.DEFAULT: 1>, <Style.BOLD: 1>)
# ('\n  controller: ', <Color.DEFAULT: 1>, <Color.DEFAULT: 1>, <Style.NONE: 0>)
# ('no error', <Color.GREEN: 5>, <Color.DEFAULT: 1>, <Style.BOLD: 1>)
# ('\naxis1\n  axis: ', <Color.DEFAULT: 1>, <Color.DEFAULT: 1>, <Style.NONE: 0>)
# ('no error', <Color.GREEN: 5>, <Color.DEFAULT: 1>, <Style.BOLD: 1>)
# ('\n  motor: ', <Color.DEFAULT: 1>, <Color.DEFAULT: 1>, <Style.NONE: 0>)
# ('no error', <Color.GREEN: 5>, <Color.DEFAULT: 1>, <Style.BOLD: 1>)
# ('\n  DRV fault: ', <Color.DEFAULT: 1>, <Color.DEFAULT: 1>, <Style.NONE: 0>)
# ('none', <Color.GREEN: 5>, <Color.DEFAULT: 1>, <Style.BOLD: 1>)
# ('\n  sensorless_estimator: ', <Color.DEFAULT: 1>, <Color.DEFAULT: 1>, <Style.NONE: 0>)
# ('no error', <Color.GREEN: 5>, <Color.DEFAULT: 1>, <Style.BOLD: 1>)
# ('\n  encoder: ', <Color.DEFAULT: 1>, <Color.DEFAULT: 1>, <Style.NONE: 0>)
# ('no error', <Color.GREEN: 5>, <Color.DEFAULT: 1>, <Style.BOLD: 1>)
# ('\n  controller: ', <Color.DEFAULT: 1>, <Color.DEFAULT: 1>, <Style.NONE: 0>)
# ('no error', <Color.GREEN: 5>, <Color.DEFAULT: 1>, <Style.BOLD: 1>)
#################################################################################################
