import time
import threading
from gpiozero import InputDevice
from gpiozero import OutputDevice

# Scan for pressed column
# Rows act as ground
# Column act as buttons



class Keypad:

	# Keypad display
	_keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
	_value = None
	_updateRate = 100 # Update rate for thread
	_r0 =_r1 =_r2 =_r3 =_c0 =_c1 =_c2 = None # Matrix pins
	_scanThread = None #threading.Thread(target=self.__keyScanner)

	def __init__(self, r0, r1, r2, r3, c0, c1, c2, updateRate=10):
		self._r0 = r0
		self._r1 = r1
		self._r2 = r2
		self._r3 = r3
		self._c0 = c0
		self._c1 = c1
		self._c2 = c2
		self._updateRate = updateRate
		self._scanThread = threading.Thread(target=self.__keyScanner).start()

	def __closePins(self):
		#global r0,r1,r2,r3,c0,c1,c2
		# Close old pins
		self._r0.close()
		self._r1.close()
		self._r2.close()
		self._r3.close()
		self._c0.close()
		self._c1.close()
		self._c2.close()


	def __setPinsRow(self):
		#global r0,r1,r2,r3,c0,c1,c2
		self._c0 = OutputDevice(18, active_high = False)
		self._c1 = OutputDevice(22, active_high = False)
		self._c2 = OutputDevice(15, active_high = False)
		self._r0 = InputDevice(21)
		self._r1 = InputDevice(14)
		self._r2 = InputDevice(4)
		self._r3 = InputDevice(17)


	def __setPinsCol(self):
		#global r0,r1,r2,r3,c0,c1,c2
		self._r0 = OutputDevice(21, active_high = False)
		self._r1 = OutputDevice(14, active_high = False)
		self._r2 = OutputDevice(4, active_high = False)
		self._r3 = OutputDevice(17, active_high = False)
		self._c0 = InputDevice(18)
		self._c1 = InputDevice(22)
		self._c2 = InputDevice(15)



	def value(self):
		return self._value

	def __keyScanner(self):
		while(1):
			self.__setPinsCol()
			cols = [self._c0.value, self._c1.value, self._c2.value]
			if(sum(cols) > 0):
				flagCol = cols.index(max(cols))
				self.__closePins() # Close pins
				self.__setPinsRow() # Swap pins
				# Scan rows
				rows = [self._r0.value, self._r1.value, self._r2.value, self._r3.value]
				if(sum(rows) != 0):
					flagRow = rows.index(max(rows))
					self._value = self._keypad[flagRow][flagCol]
			else:
				self._value = None
			time.sleep(1 / self._updateRate)
			self.__closePins()
