#
#			duty cycle=T1/(T1+T2) * 100 == % value of T1
#

import RPi.GPIO as a
from time import sleep	#WE USE sleep(1) instead of time.sleep(1)
a.setwarnings(False)
a.setmode(a.BCM)
######################################
a.setup(22,a.OUT)		#SETTING IT TO OUTPUT MODE
######################################
a.output(22,0)			#INITIALLY SETTING IT TO 0,OFF STATE
######################################
s=a.PWM(22,1700)			#@1.7KHZ frequency on pin 22 having pwm function
s.start(50)					#it is compulsory to give initial value to run pwm initially here it will start by taking 50% duty cycle.
try:						#exception handling condition
	while 1:
		s.ChangeDutyCycle(5)		#5 here is duty cycle percentage
		print "Duty cycle is set to 5 on pin 22"
		sleep(1)
		s.ChangeDutyCycle(20)
		print "Duty cycle is set to 20 on pin 22"
		sleep(1)
		s.ChangeDutyCycle(40)
		print "Duty cycle is set to 40 on pin 22"
		sleep(1)
		s.ChangeDutyCycle(55)
		print "Duty cycle is set to 55 on pin 22"
		sleep(1)
		s.ChangeDutyCycle(70)
		print "Duty cycle is set to 70 on pin 22"
		sleep(1)
		s.ChangeDutyCycle(86)
		print "Duty cycle is set to 86 on pin 22"
		sleep(1)
		s.ChangeDutyCycle(98)
		print "Duty cycle is set to 98 on pin 22"
		sleep(1)
		s.ChangeDutyCycle(98)
		print "Duty cycle is set to 98 on pin 22"
		sleep(1)
		s.ChangeDutyCycle(86)
		print "Duty cycle is set to 86 on pin 22"
		sleep(1)
		s.ChangeDutyCycle(70)
		print "Duty cycle is set to 70 on pin 22"
		sleep(1)
		s.ChangeDutyCycle(55)
		print "Duty cycle is set to 55 on pin 22"
		sleep(1)
		s.ChangeDutyCycle(40)
		print "Duty cycle is set to 40 on pin 22"
		sleep(1)
		s.ChangeDutyCycle(20)
		print "Duty cycle is set to 20 on pin 22"
		sleep(1)

except KeyboardInterrupt:

	a.output(22,0)
	print " "
	print "someone has pressed ctrl + c !!!!"
	print " good bye!!!"
	print " "