 #Everleigh p
#Four Buttons, One LED

#Use a module for requesting data online
import requests

#Use a module to control time
import time

#Setup for buttons and leds
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)


 #Start an infinite loop
while True:
    #Wait for one second
    time.sleep(1)
    #Check the first button
    if GPIO.input(6) == GPIO.LOW:
        print("Button 6 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=up")
    elif GPIO.input(13) == GPIO.LOW:
        print("Button 13 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=down")
    elif GPIO.input(19) == GPIO.LOW:
        print("Button 19 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=wiggle")
    elif GPIO.input(26) == GPIO.LOW:
        print("Button 26 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=oops")