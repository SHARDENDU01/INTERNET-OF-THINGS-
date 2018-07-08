#
#			duty cycle=T1/(T1+T2) * 100 == % value of T1
#

import RPi.GPIO as a
from time import sleep	#WE USE sleep(1) instead of time.sleep(1)
a.setwarnings(False)
a.setmode(a.BCM)
######################################
a.setup(17,a.OUT)
a.setup(22,a.OUT)		#SETTING IT TO OUTPUT MODE
a.setup(27,a.OUT)
######################################
a.output(17,0)
a.output(22,0)			#INITIALLY SETTING IT TO 0,OFF STATE
a.output(27,0)
######################################
r=a.PWM(17,900)
s=a.PWM(22,700)			#@700 HZ frequency on pin 22 having pwm function
t=a.PWM(27,1000)
r.start(0)
s.start(10)					#it is compulsory to give initial value to run pwm initially here it will start by taking 50% duty cycle.
t.start(50)

try:						#exception handling condition
	while 1:
		r.ChangeDutyCycle(98)
		print "Duty cycle is set to 98 on pin 17"
		sleep(1)
		r.ChangeDutyCycle(86)
		print "Duty cycle is set to 86 on pin 17"
		sleep(1)
		r.ChangeDutyCycle(70)
		print "Duty cycle is set to 70 on pin 17"
		sleep(1)
		r.ChangeDutyCycle(55)
		print "Duty cycle is set to 55 on pin 17"
		sleep(1)
		r.ChangeDutyCycle(40)
		print "Duty cycle is set to 40 on pin 17"
		sleep(1)
		r.ChangeDutyCycle(20)
		print "Duty cycle is set to 20 on pin 17"
		sleep(1)
		r.ChangeDutyCycle(5)		#5 here is duty cycle percentage
		print "Duty cycle is set to 5 on pin 17"
		sleep(1)
		r.ChangeDutyCycle(0)
		print "Duty cycle is set to 0 on pin 17"
		sleep(1)

		s.ChangeDutyCycle(0)
		print "Duty cycle is set to 0 on pin 22"
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



		t.ChangeDutyCycle(98)
		print "Duty cycle is set to 98 on pin 27"
		sleep(1)
		t.ChangeDutyCycle(86)
		print "Duty cycle is set to 86 on pin 27"
		sleep(1)
		t.ChangeDutyCycle(70)
		print "Duty cycle is set to 70 on pin 27"
		sleep(1)
		t.ChangeDutyCycle(55)
		print "Duty cycle is set to 55 on pin 27"
		sleep(1)
		t.ChangeDutyCycle(40)
		print "Duty cycle is set to 40 on pin 27"
		sleep(1)
		t.ChangeDutyCycle(20)
		print "Duty cycle is set to 20 on pin 27"
		sleep(1)
		t.ChangeDutyCycle(0)
		print "Duty cycle is set to 0 on pin 27"
		sleep(1)

except KeyboardInterrupt:
	a.output(17,0)
	a.output(27,0)
	a.output(22,0)
	print " "
	print "someone has pressed ctrl + c !!!!"
	print " good bye!!!"
	print " "