#!/usr/bin/python3

from phue import Bridge

print("Imported library")
b = Bridge('192.168.1.124')
print("Defined bridge")

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
#b.connect()
#print("Connect has run")

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

lightArray = []

light_names = b.get_light_objects('name')
for light in light_names:
	light_names[light].on = True
	print("Turned off" + str(light))
	lightArray

print(light_names)
