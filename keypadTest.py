from Keypad import Keypad
import time

test = Keypad(4, 14, 15, 17, 18, 21, 22)
print("made the keypad object")

while(1):
	print(test.value())
	time.sleep(0.1)
