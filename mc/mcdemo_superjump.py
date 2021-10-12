#Everleigh pierce
#Super jump


from mcpi.minecraft import Minecraft
mc = Minecraft.create()


import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(6) == GPIO.LOW:
        pos = mc.player.getTilePos()
        blockData = mc.getBlock(pos.x, pos.y -1, pos.z)
        print(blockData)
        if blockData == 57:
            mc.player.setTilePos(pos.x, pos.y - 20, pos.z)
        #if the blockData is a Diamond block,
        #change the player's position to it current position
        #plus 20 to the y position
        

   
