import time
import Netmaxiot

while True:
	a=Netmaxiot.analogRead(0)
	print " "
	print "voltage in analog value now is = %d :)" %a
	print " "
	time.sleep(0.8)
