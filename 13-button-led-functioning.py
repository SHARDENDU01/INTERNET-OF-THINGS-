#! /usr/bin/env python


import Netmaxiot		#Netmax Shield library
from time import sleep	

led1 = 2				#working 0n pin 2,3,4 of digital I/O available on netmax shield
led2 = 3				#pin 1 and 2 are only for input purposes
led3 = 4
button1 = 8
button2 = 9

Netmaxiot.pinMode(button1,"INPUT")
Netmaxiot.pinMode(button2,"INPUT")
Netmaxiot.pinMode(led1,"OUTPUT")			#ALL Functions in the library netmax are inherited from Arduino library
Netmaxiot.pinMode(led2,"OUTPUT")
Netmaxiot.pinMode(led3,"OUTPUT")


while True:
	try:	
		a=Netmaxiot.digitalRead(button1)
		b=Netmaxiot.digitalRead(button2)	
		if a==0:
			Netmaxiot.digitalWrite(led1,1)			#TO TURN ON THE LED ON PIN 2,3,4
			Netmaxiot.digitalWrite(led2,1)
			Netmaxiot.digitalWrite(led3,1)
			print " BUTTON 1 PRESSED LED ON HAI !!!!"
			sleep(0.2)
			Netmaxiot.digitalWrite(led1,0)			#TO TURN ON THE LED ON PIN 2,3,4
			Netmaxiot.digitalWrite(led2,0)
			Netmaxiot.digitalWrite(led3,0)
			print " BUTTON 1 PRESSED LED OFF HAI !!!!"
			sleep(0.2)

		elif b==0:
			Netmaxiot.digitalWrite(led1,1)
			Netmaxiot.digitalWrite(led2,0)
			Netmaxiot.digitalWrite(led3,1)
			print " BUTTON 2 PRESSED LED ON HAI !!!!"
			sleep(0.2)
			Netmaxiot.digitalWrite(led1,0)			#TO TURN ON THE LED ON PIN 2,3,4
			Netmaxiot.digitalWrite(led2,1)
			Netmaxiot.digitalWrite(led3,0)
			print " BUTTON 2 PRESSED LED OFF HAI !!!!"
			sleep(0.2)

		else:
			Netmaxiot.digitalWrite(led1,1)			#TO TURN ON THE LED ON PIN 2,3,4
			Netmaxiot.digitalWrite(led2,0)
			Netmaxiot.digitalWrite(led3,0)
			print " NO BUTTON PRESSED LED ON HAI !!!!"
			sleep(0.2)
			Netmaxiot.digitalWrite(led1,0)			#TO TURN ON THE LED ON PIN 2,3,4
			Netmaxiot.digitalWrite(led2,0)
			Netmaxiot.digitalWrite(led3,1)
			print " NO BUTTON PRESSED LED OFF HAI !!!!"
			sleep(0.2)

	except IOError:
		print "ERROR COMES"
		break
	except KeyboardInterrupt:
		print " "
		print " SOMEONE HAS PRESSED CTRL + C "
		print " "
		break