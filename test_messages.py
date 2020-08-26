#!/usr/bin/env python

import i2c_lcd_driver
from time import sleep
from datetime import datetime

mylcd = i2c_lcd_driver.lcd()

#currentTime function pulls the current Time
#and formats to hour:minute AM/PM i.e. 9:36 AM
def currentTime():
    dateraw=datetime.now()
    timeFormat=dateraw.strftime("%-I:%M %p")
    return timeFormat
    
#Until Ctrl-C is pressed, this code cycles through
#each of these messages for 2 seconds each    
while True: 
    cT=currentTime();
    mylcd.lcd_display_string("Welcome to", 1) #Line 1
    mylcd.lcd_display_string("Tom's Hardware!", 2) #Line 2
    sleep(2)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Status: Busy", 1) #Line 1
    mylcd.lcd_display_string("as of "+cT, 2) #Line 2 displays the current time i.e. "as of 9:36 AM"
    sleep(2)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("On the phone", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(2)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("On a video call", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(2)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("In a meeting", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(2)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Grading papers", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(2)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Sending Emails", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(2)
    mylcd.lcd_clear()
