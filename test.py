# rock 4c plus
# adafruit 
# https://github.com/adafruit/Adafruit_Python_Extended_Bus

import time
import board
import digitalio
import adafruit_max31855
from adafruit_extended_bus import ExtendedSPI as SPI

spi = SPI(1, 0)
cs = digitalio.DigitalInOut(board.D29)

max31855 = adafruit_max31855.MAX31855(spi, cs)
while True:
    tempC = max31855.temperature
    tempF = tempC * 9 / 5 + 32
    print("Temperature: {} C {} F ".format(tempC, tempF))
    time.sleep(2.0)