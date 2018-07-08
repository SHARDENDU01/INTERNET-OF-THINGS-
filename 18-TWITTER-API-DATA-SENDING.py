#in pi download the twitter library i.e, ]# pip install python-twitter 
#Go to apps.twitter.com and create a app and generate its consumer key,consumer secret, access token, access token secret 
#note that a mobile number should be linked on to the twitter account
#and twitter account should be in active state.

import Netmaxiot
import time
import twitter

my_str= "this is an iot tweet @Rocker_Ritesh @OfficialPU today's tempearture and lightintensity is"
api= twitter.Api(consumer_key ='b7H1kpcf2qg9LqlAzWVNSwase', 
	consumer_secret= '2knWXecooJHYM3pNO3ns6NPsBfLGIguRpzpnsAmOJfwHGj7En3',
	access_token_key='912784235055816704-eiswVPv36pd3eXouD7fne2MlB0TmlSs',
	access_token_secret= '5HPmGANFGjmVbMzzJz8Y75BOVBjWIIfKmP46zKGxmPZrn')

while True:
	try:
		valueread=Netmaxiot.analogRead(0)				#LM35 IS ATTACHED ON ANALOG PIN 0
		valueread1=Netmaxiot.analogRead(1)				#DHT11 IS ATTACHED ON ANALOG PIN 1
		print " Value of analog to digital converter is = %d " %valueread
		voltage=valueread * 4.887							#AS 5000mV /1023 = 4.887 
		print " Vlotage in mV is = %0.2f " %voltage
		temp=voltage/10										#AS 10mV = 1 *Celsius
		print " Temperature now is = %0.2f " %temp
		voltage1 = valueread1 * 4.887
		light = voltage1/50
		print " The value of light is = %0.2f" %(light)
		time.sleep(1)
		print "sending value to twitter "
		send_string= u"%s , temp: %0.2f, degree Celsius,light: %0.2f percent" %(my_str,temp,light)
		time.sleep (40)
		print "----------------------------------------------------"
		print (send_string)
		api.PostUpdate(send_string)
		print "tweet sended"
		time.sleep(50)
	except KeyboardInterrupt:
		print "Some one has pressed CTRL + C"

