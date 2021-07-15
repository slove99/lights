import time
from gpiozero import Button
from gpiozero import RotaryEncoder
from Keypad import Keypad

rotor1 = RotaryEncoder(24,10)
rotor2 = RotaryEncoder(25,11)
rotor3 = RotaryEncoder(8,7)
keypad = Keypad(4,14,15,17,18,21,22)

button = Button(23)
while(1):
	#print(rotor.value)
	if(button.value == 1):
		print("button pressed")
	print(rotor1.value, rotor2.value, rotor3.value)
	if(keypad.value != None):
		print(keypad.value)

	time.sleep(0.1)
