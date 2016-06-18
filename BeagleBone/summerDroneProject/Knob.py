#!/usr/bin/python 

import time
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.ADC as ADC

ADC.setup()

print "Syncing with the Drone"
PWM.start("P8_13",86,66,1)

try:
	input("Press Enter to Continue...")
except SyntaxError:
	pass


print "LOCKED ON"

try:
	while True:
		value = ADC.read("P9_39")
		adder = value *100
		print(adder)
		PWM.set_duty_cycle("P8_13",adder)
except KeyboardInterrupt:
	pass
PWM.stop("P9_14")
PWM.cleanup()
