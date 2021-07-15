# Adapted from  https://github.com/bogdal/rpi-lcd

from smbus import SMBus
from time import sleep

ALIGN_FUNC = {
    'left': 'ljust',
    'right': 'rjust',
    'center': 'center'}
CLEAR_DISPLAY = 0x01
ENABLE_BIT = 0b00000100
LINES = {
    1: 0x80,
    2: 0xC0,
    3: 0x94,
    4: 0xD4}


class LCD(object):
    BACKLIGHT_MODE = 0x08

    # Initialise the display
    def __init__(self, address=0x27, bus=0, width=20, rows=4):
        self.address = address
        self.bus = SMBus(bus)
        self.delay = 0.0005
        self.rows = rows
        self.width = width

        self.write(0x33)
        self.write(0x32)
        self.write(0x06)
        self.write(0x0C)
        self.write(0x28)
        self.write(CLEAR_DISPLAY)
        sleep(self.delay)

    # Enable / Disable the backlight (applies to future write commands)
    def backlight(self, mode):
        if(mode == 1):
            self.BACKLIGHT_MODE = 0x08
            self._write_byte(self.BACKLIGHT_MODE)
        elif(mode == 0):
            self.BACKLIGHT_MODE = 0x00
            self._write_byte(self.BACKLIGHT_MODE)
        else:
            print("Invalid mode")

    def _write_byte(self, byte):
        self.bus.write_byte(self.address, byte)
        self.bus.write_byte(self.address, (byte | ENABLE_BIT))
        sleep(self.delay)
        self.bus.write_byte(self.address,(byte & ~ENABLE_BIT))
        sleep(self.delay)

    def write(self, byte, mode=0):
        self._write_byte(mode | (byte & 0xF0) | self.BACKLIGHT_MODE)
        self._write_byte(mode | ((byte << 4) & 0xF0) | self.BACKLIGHT_MODE)

    def text(self, text, line, align='left'):
        self.write(LINES.get(line, LINES[1]))
        text, other_lines = self.get_text_line(text)
        text = getattr(text, ALIGN_FUNC.get(align, 'ljust'))(self.width)
        for char in text:
            self.write(ord(char), mode=1)
        if other_lines and line <= self.rows - 1:
            self.text(other_lines, line + 1, align=align)

    def get_text_line(self, text):
        line_break = self.width
        if len(text) > self.width:
            line_break = text[:self.width + 1].rfind(' ')
        if line_break < 0:
            line_break = self.width
        return text[:line_break], text[line_break:].strip()

    def clear(self):
        self.write(CLEAR_DISPLAY)
