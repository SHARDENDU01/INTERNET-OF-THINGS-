#!/usr/bin/env python
import time
import Netmaxiot as net
#Connect the netmax button to digital port on netmax shield
#WHEN BUTTON IS PRESSED OUTPUT IS 0 AND WHEN IN IDEAL SITUTATION IT IS 1
button = 9
net.pinMode(button,"INPUT")
while True:
	try:
		a=net.digitalRead(button)
		print a
		time.sleep(1)
	except KeyboardInterrupt:
		print "Someone has pressed CTRL + C "
		break