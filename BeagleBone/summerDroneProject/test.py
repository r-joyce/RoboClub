#!/usr/bin/python

import time
import Adafruit_BBIO.PWM as PWM
PWM.start("P8_13",86.67,66,1)
time.sleep(3)

PWM.start("P8_13",75,66,1)
time.sleep(5)
PWM.stop("P8_13")

