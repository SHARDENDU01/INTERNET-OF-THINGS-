import os			
import requests
import time
from w1thermsensor import W1ThermSensor

#####################################################
sensor = W1ThermSensor()
def read_temp():
	temp_c= sensor.get_temperature()
	temp_f= temp_c * 9.0 /5.0 + 32
	print  "========================================"
	print temp_c
	time.sleep(0.8)
	print temp_f
	print  "========================================"
	print " The temperature in celcius is = %0.2f *C" %temp_c
	print " The temperature in farenheit is = %0.2f *F" %temp_f
	time.sleep(3)
	payload = {'temperature_celcius':temp_c,'temperature_farenheit':temp_f}
	return payload
#####################################################

while True:
	try:
		r=requests.post('http://things.ubidots.com/api/v1.6/devices/rspberry/?token=A1E-3l65kX2jKmxRQGZwYHeL8EixzmTsm6',data = read_temp())
		print "Posting data in ubidots"
		print (read_temp())
	except:
		print "Something goes wrong please do it correct"
		time.sleep(5)
