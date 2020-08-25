import i2c_lcd_driver
from time import sleep
from datetime import datetime

mylcd = i2c_lcd_driver.lcd()

def currentTime():
	dateraw=datetime.now()
	timeFormat=dateraw.strftime("%-I:%M %p")
	return timeFormat
	
while True: 
	cT=currentTime();
	mylcd.lcd_display_string("Welcome to", 1)
	mylcd.lcd_display_string("Tom's Hardware!", 2)
	sleep(2)
	mylcd.lcd_clear()
	mylcd.lcd_display_string("Status: Busy", 1)
	mylcd.lcd_display_string("as of "+cT, 2)
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
