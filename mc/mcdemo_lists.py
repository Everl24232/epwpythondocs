#Everleigh Pierce
#Places a randomly colored wool block

'''
Set up program for mc and tweo buttons
Create a 'counter' variable that starts at 0
Create a list of blockdata numbers for differe color wool
Defien a function called placeNext
    - it takes one argument called direction
    - it changes the counter by adding the direction argument
    - place a wool block of the color from the list where the index matchs the counter variable
    -if the counter is out of bound of the index, reset it
In a forever loop:
    - if the first button was pressed, placeNext(1)
    - if the second button was pressed, placeNext(-1)


'''
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = 0
woolColors = [6, 5, 10]

def placeNext(direction):
    global counter
    counter += direction
    import time 
    mc.setBlock(-13, 4, 64, 35, woolColors[counter])
    
while True:
    if GPIO.input(6) == GPIO.LOW:
        placeNext(1)
    if GPIO.input(13) == GPIO.LOW:
        placeNext(-1)
    
