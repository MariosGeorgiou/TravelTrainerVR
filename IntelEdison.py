import time
from time import gmtime, strftime
import mraa
import sys
import math
import pyupm_i2clcd as lcd

button = mraa.Gpio(3)
button.dir(mraa.DIR_IN)

led = mraa.Gpio(13)
led.dir(mraa.DIR_OUT)

lightPin=1
lum = mraa.Aio(lightPin)
lumVal = 0

tmpPin=2
tmp = mraa.Aio(tmpPin)
tmpVal = 0

lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.setColor(255,100,0)
while 1:
    while button.read() == 1:
        led.write(1)

        lumVal = float(lum.read())
        dn = "Day"
        if lumVal < 35:
            dn = "Night"

        tmp1Val = float(tmp.read())
        bVal = 3975
    	resistanceVal = (1023 - tmp1Val) * 10000 / tmp1Val
        celsiusVal = 1 / (math.log(resistanceVal / 10000) / bVal + 1 / 298.15) - 273.15
        tempVal = int(celsiusVal)

        hello =  dn +"(L:"+str(int(lumVal)) +")        "
        lcdDisplay.setCursor(1, 0)
        lcdDisplay.write(hello)
        lcdDisplay.setCursor(0, 0)
        lcdDisplay.write(strftime("%H:%M:%S", gmtime()) + " temp:"+str(tempVal))
        time.sleep(3)

    led.write(0)
    lcdDisplay.setCursor(0, 0)
    lcdDisplay.write("                      ")
    lcdDisplay.setCursor(1, 0)
    lcdDisplay.write("                      ")
    