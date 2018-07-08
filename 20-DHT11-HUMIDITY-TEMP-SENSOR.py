#

#	visit google and type "adafruit raspberry pi dht11"select the first option of learn.adafruit.com  
# 	scroll down to youtube tab and below that video tab their is a "WIRING" tag click on it and then scroll down and click on "SOFTWARE INSTALL UPDATE"
#	install the packages written in it.
#	Use ]# git clone 	//whereever required.


import time
import Adafruit_DHT
sensor=Adafruit_DHT.DHT11
pin=18				#//sensor output pin is attached at pin no 18
while 1:
	humidity,temperature=Adafruit_DHT.read_retry(sensor,pin)
	if humidity is not None and temperature is not None:
		print "Temp: %0.2f *C, humidity: %0.2f " %(temperature,humidity)
	else:
		print " It is not working!!!"
time.sleep(1)