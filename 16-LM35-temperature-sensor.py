#!/usr/bin/env python
import time 
import Netmaxiot

while True:
	valueread=Netmaxiot.analogRead(0)
	print " Value of analog to digital converter is = %d " %valueread
	voltage=valueread * 4.887
	print " Vlotage in mV is = %0.2f " %voltage
	temp=voltage/10
	print " Temperature now is = %0.2f " %temp
	time.sleep (0.8)

