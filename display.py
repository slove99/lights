from signal import signal, SIGTERM, SIGHUP, pause
from Display import LCD
lcd = LCD()
import time
def safe_exit(signum, frame):
    exit(1)
try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    lcd.text("Hello,", 1)
    lcd.text("Raspberry Pi!", 2)
    lcd.text("Testing row 3", 3)
    lcd.text("FJIDSFJ*(£*JF*", 4)
    time.sleep(3)
    for i in range(5):
        lcd.backlight(0)
        time.sleep(1)
        lcd.backlight(1)
        time.sleep(1)
    #lcd.text(" ",1)
    print("fin")
except KeyboardInterrupt:
    pass
