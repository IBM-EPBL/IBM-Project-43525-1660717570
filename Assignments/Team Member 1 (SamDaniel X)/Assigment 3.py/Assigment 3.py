
# Write a python code for blinking LED and Traffic lights for Raspberry pi.

# Blinking LED:
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and
set initial value to low (off)
while True: # Run forever
 GPIO.output(8, GPIO.HIGH) # Turn on
 sleep(1) # Sleep for 1 second
 GPIO.output(8, GPIO.LOW) # Turn off
 sleep(1)

# Traffic Light:
from gpiozero import LED
red = LED(22)
amber = LED(27)
green = LED(17)
red.blink(1, 1)
amber.blink(2, 2)
green.blink(3, 3)
