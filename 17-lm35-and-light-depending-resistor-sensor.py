#!/usr/bin/env python
import time 
import Netmaxiot

while True:
	valueread=Netmaxiot.analogRead(0)				#LM35 IS ATTACHED ON ANALOG PIN 0
	valueread1=Netmaxiot.analogRead(1)				#DHT11 IS ATTACHED ON ANALOG PIN 1
	print " Value of analog to digital converter is = %d " %valueread
	voltage=valueread * 4.887							#AS 5000mV /1023 = 4.887 
	print " Vlotage in mV is = %0.2f " %voltage
	temp=voltage/10										#AS 10mV = 1 *Celsius
	print " Temperature now is = %0.2f " %temp
	voltage1 = valueread1 * 4.887
	light = voltage1/5000
	print " The value of light is = %0.2f" %(light * 100)
	time.sleep (0.8)

