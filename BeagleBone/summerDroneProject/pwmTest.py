#!/usr/bin/python

import time
import Adafruit_BBIO.PWM as PWM

print "Welcome to the PWM Program: Version 1.01"

PWM.start("P8_13",86.67,66,1);
time.sleep(3)

duty = 37
for num in range(0,27):
	var = 100-(duty - num)
	PWM.set_duty_cycle("P8_13",var)
	print var
	time.sleep(2)

PWM.stop("P9_14")
PWM.cleanup()
