#!/usr/bin/python3

from phue import Bridge

def rgb_to_xy(red, green, blue):
    """ conversion of RGB colors to CIE1931 XY colors
    Formulas implemented from: https://gist.github.com/popcorn245/30afa0f98eea1c2fd34d
    Args: 
        red (float): a number between 0.0 and 1.0 representing red in the RGB space
        green (float): a number between 0.0 and 1.0 representing green in the RGB space
        blue (float): a number between 0.0 and 1.0 representing blue in the RGB space
    Returns:
        xy (list): x and y
    """

    # gamma correction
    red = pow((red + 0.055) / (1.0 + 0.055), 2.4) if red > 0.04045 else (red / 12.92)
    green = pow((green + 0.055) / (1.0 + 0.055), 2.4) if green > 0.04045 else (green / 12.92)
    blue =  pow((blue + 0.055) / (1.0 + 0.055), 2.4) if blue > 0.04045 else (blue / 12.92)

    # convert rgb to xyz
    x = red * 0.649926 + green * 0.103455 + blue * 0.197109
    y = red * 0.234327 + green * 0.743075 + blue * 0.022598
    z = green * 0.053077 + blue * 1.035763

    # convert xyz to xy
    x = x / (x + y + z)
    y = y / (x + y + z)

    return [x, y]

print("Imported library")
b = Bridge('192.168.1.124')
print("Defined bridge\n")

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
#b.connect()
#print("Connect has run")

# Get the bridge state
b.get_api()

# Array to store light states
lightArray = []

# Create light object dictionary
light_names = b.get_light_objects('name')



# Print a list of lights and their status
for light in light_names:
	if light_names[light].reachable == True:
		lightArray.append(str(light))
		print('{0: <20}'.format("Found %s " % str(light)) + "Reachable")
	else:
		print('{0: <20}'.format("Found %s " % str(light)) + "Unreachable")
	light_names[light].on = True

for i in range(len(lightArray)):
	print("\n%d. %s" % (i, lightArray[i]))

# Select a reachable light
selectedLight = int(input("Select a light"))
print("Selected %s " % lightArray[selectedLight])
selectedLightID = lightArray[selectedLight]

# Chosen light modification parameter (brightness, warmth, colour)
lightMode = 0

# Adjustments for a specific parameter
lightAdjustment = 0

while(lightMode != -1):
	lightMode = int(input(""))
	#Brightness
	if(lightMode == 1):
		curBrightness = int(light_names[selectedLightID].brightness)
		light_names[selectedLightID].brightness = min(curBrightness + 20, 255)
	elif(lightMode == 2):
                curBrightness = int(light_names[selectedLightID].brightness)
                light_names[selectedLightID].brightness = max(curBrightness - 20, 0)
	#X
	elif(lightMode == 3):
		curXY = light_names[selectedLightID].xy
		newXY = [min(curXY[0] + 0.1, 1), curXY[1]]
		light_names[selectedLightID].xy = newXY
	elif(lightMode == 4):
		curXY = light_names[selectedLightID].xy
		newXY = [max(curXY[0] - 0.1, 0), curXY[1]]
		light_names[selectedLightID].xy = newXY
	#Y
	elif(lightMode == 5):
		curXY = light_names[selectedLightID].xy
		newXY = [curXY[0], min(curXY[1] + 0.1, 1)]
		light_names[selectedLightID].xy = newXY
	elif(lightMode == 6):
		curXY = light_names[selectedLightID].xy
		newXY = [curXY[0], max(curXY[1] - 0.1, 0)]
		light_names[selectedLightID].xy = newXY

	#Temperature
	elif(lightMode == 7):
		curTemp = int(light_names[selectedLightID].colortemp_k)
		light_names[selectedLightID].colortemp_k = min(curTemp + 200, 6500)
	elif(lightMode == 8):
		curTemp = int(light_names[selectedLightID].colortemp_k)
		light_names[selectedLightID].colortemp_k = max(curTemp - 200, 2000)



print(vars(light_names["DeskR"]))


print("\nFound %d lights" % (len(lightArray)))
#print(light_names)
