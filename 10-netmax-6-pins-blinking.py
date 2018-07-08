#! /usr/bin/env python


import Netmaxiot		#Netmax Shield library
from time import sleep	

led1 = 2				#working 0n pin 2,3,4 of digital I/O available on netmax shield
led2 = 3				#pin 1 and 2 are only for input purposes
led3 = 4
led4 = 5
led5 = 6
led6 = 7

Netmaxiot.pinMode(led1,"OUTPUT")			#ALL Functions in the library netmax are inherited from Arduino library
Netmaxiot.pinMode(led2,"OUTPUT")
Netmaxiot.pinMode(led3,"OUTPUT")
Netmaxiot.pinMode(led4,"OUTPUT")
Netmaxiot.pinMode(led5,"OUTPUT")
Netmaxiot.pinMode(led6,"OUTPUT")


try:											#TO HANDLE EXCEPTIONS
	while True:
		Netmaxiot.digitalWrite(led1,1)			#TO TURN ON THE LED ON PIN 2,3,4
		Netmaxiot.digitalWrite(led2,1)
		Netmaxiot.digitalWrite(led3,1)
		Netmaxiot.digitalWrite(led4,1)
		Netmaxiot.digitalWrite(led5,1)
		Netmaxiot.digitalWrite(led6,1)
		print " LED ON HAI !!!!"
		sleep(0.2)								 
		Netmaxiot.digitalWrite(led1,0)
		Netmaxiot.digitalWrite(led2,0)
		Netmaxiot.digitalWrite(led3,0)
		Netmaxiot.digitalWrite(led4,0)
		Netmaxiot.digitalWrite(led5,0)
		Netmaxiot.digitalWrite(led6,0)
		print " LED OFF HAI !!!!"
		sleep(0.2)

except IOError:
	print "ERROR COMES"
except KeyboardInterrupt:
	print " "
	print " SOMEONE HAS PRESSED CTRL + C "
	print " "