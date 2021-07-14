from gpiozero import Button
from gpiozero import RotaryEncoder
rotor = RotaryEncoder(24,10)
button = Button(23)
while(1):
	#print(rotor.value)
	if(button.value == 1):
		print("button pressed")
		print(rotor.value)
