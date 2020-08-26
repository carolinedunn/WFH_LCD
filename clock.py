#!/usr/bin/env python

import i2c_lcd_driver
from time import sleep
from datetime import datetime

mylcd = i2c_lcd_driver.lcd()

def currentTime():
    dateraw=datetime.now()
    timeFormat=dateraw.strftime("%-I:%M %p")
    return timeFormat
    
while True: 
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Current Time:", 1)
    mylcd.lcd_display_string(cT, 2)
    sleep(10)
