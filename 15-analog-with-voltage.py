import time
import Netmaxiot

while True:
	a=Netmaxiot.analogRead(0)
	print " "
	v=4.9 * a
	print "analog value of voltage is = %d :)" %a
	print "voltage now is = %0.2f :)" %v
	print " "
	time.sleep(0.8)
