#!/usr/bin/python

import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.ADC as ADC

ADC.setup()

#92,86

Throttle = "P8_13"
Yaw = "P9_14"
Pitch = "P9_21"
Roll = "P9_42"

Max = 95
Min = 85
mean = (Min + Max)/2
print(mean)

PWM.start(Throttle,Max,66,1)
PWM.start(Yaw,Min,66,1)
PWM.start(Roll,mean,66,1)
PWM.start(Pitch,mean,66,1)

try:
	input("Press Enter")
except SyntaxError:
	pass

PWM.set_duty_cycle(Yaw,mean)

try:
	while True:
		value = ADC.read("P9_39")

		adder = ((Max-Min)*(value))+Min
		print(adder)
		PWM.set_duty_cycle(Throttle,adder)
except KeyboardInterrupt:
	pass


PWM.stop(Throttle)
PWM.stop(Yaw)
PWM.stop(Pitch)
PWM.stop(Roll)
PWM.cleanup()

