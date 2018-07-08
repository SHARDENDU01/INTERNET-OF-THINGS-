											#	o 	3.3 V
											#	|
											#	|
											#	|
											#	<
											#	>	10 ohm
											#	<
											#	>								IF SWITCH IS ON(pressed),THEN Vout = 0V
											#	o--------------PIN(out)			else it is 3.3V
											#	|
											#	|
											#	o
											#  \	SWITCH 	
											#	\
											#	o
											#	|
											#	|
											# ======	GND 0V
											#  ====	



															

import RPi.GPIO as NET
import time
NET.setmode(NET.BCM)
NET.setwarnings(False)
###############################
NET.setup(23,NET.IN)
NET.setup(24,NET.IN)		#SET SWITCH TO INPUT MEANS 23rd,24th PIN IS TO BE CONNECTED WITH SWITCH
############################
NET.setup(17,NET.OUT)		#SET LED AS OUTPUT PORT
NET.setup(22,NET.OUT)		#PIN 17,27,22 ARE TO BE CONNECTED WITH LED'S
NET.setup(27,NET.OUT)
###############################

NET.output(17,0)			#SETTING ALL THE OUTPUT PINS IN OFF POSITION AT THE BEGINNING
NET.output(22,0)
NET.output(27,0)

###############################

while 1:
	if NET.input(24)==0:			#WHEN THE SWITCH (24) IS NOT PRESSED i.e, (24)==0 then,THE VOLTAGE AT THE TERMINAL IS HIGH i.e, IN ELSE CASE WHEN Vout=3.3V (HIGH)
		NET.output(17,1)
		NET.output(22,1)
		NET.output(27,1)
		print "PIN 24 IS NOT PRESSED (INPUT IS LOW) && OUTPUT IS HAVING 3.3V!!!!"
	elif NET.input(23)==0 and NET.input(24)==1:   #WHEN PIN 23 IS NOT PRESSED i.e,(23)==0 AND PIN 24 IS PRESSED i.e, (24)==1 
		NET.output(17,1)
		NET.output(22,0)
		NET.output(27,1)
		print "PIN 24(SWITCH) IS PRESSED AND 23(SWITCH) IS NOT PRESSED && OUTPUT IS HAVING PARTIAL VALUES"
	else:
		NET.output(17,0)				#IN CASE WHEN 23 IS ON AND WHATEVER 24 IS ON or OFF THIS CASE WILL RUN
		NET.output(22,0)
		NET.output(27,0)
		print "NO PIN IS PRESSED(INPUT IS HIGH) && OUTPUT IS HAVING 0 V "

	time.sleep(1)


