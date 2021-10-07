#Everleigh p
#4button minecraft
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import requests


playerPosition = mc.player.getTilePos()
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
if GPIO.input(6) == GPIO.LOW:
        print(mc.postToChat(playerPosition))