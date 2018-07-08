import RPi.GPIO as _a
import time
_a.setwarnings(False)
_a.setmode(_a.BCM)
_a.setup(17,_a.OUT)
_a.setup(27,_a.OUT)
_a.setup(22,_a.OUT)

_a.output(17,1)
_a.output(27,1)
_a.output(22,1)
print "led are high "
time.sleep(0.3)

_a.output(17,0)
_a.output(27,0)
_a.output(22,0)
print "led are low"


print "loop starts!!!!"

while 1:
	_a.output(17,1)
	_a.output(27,1)
	_a.output(22,1)
	print "check pins are high"
	time.sleep(1)

	_a.output(17,0)
	_a.output(27,0)
	_a.output(22,0)
	print "check pins are low"
	time.sleep(1.2)








