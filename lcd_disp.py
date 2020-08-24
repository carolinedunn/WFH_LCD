import i2c_lcd_driver
from time import *

mylcd = i2c_lcd_driver.lcd()

mylcd.lcd_display_string("Welcome to", 1)
mylcd.lcd_display_string("Tom's Hardware!", 2)
