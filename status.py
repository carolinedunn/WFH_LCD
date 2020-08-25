#!/usr/bin/env python

import i2c_lcd_driver
from time import sleep
from flask import Flask, jsonify, make_response, request
from datetime import datetime
mylcd = i2c_lcd_driver.lcd()

app = Flask(__name__)

def currentTime():
	dateraw=datetime.now()
	timeFormat=dateraw.strftime("%-I:%M %p")
	return timeFormat

def switchTH() :
	mylcd.lcd_clear()
	mylcd.lcd_display_string("Welcome to", 1)
	mylcd.lcd_display_string("Tom's Hardware!", 2)
	sleep(1)
	
def switchAvailable() :
	cT=currentTime()
	mylcd.lcd_clear()
	mylcd.lcd_display_string("Status:Available", 1)
	mylcd.lcd_display_string("as of "+cT, 2)
	sleep(1)

def switchBusy() :
	cT=currentTime()
	mylcd.lcd_clear()
	mylcd.lcd_display_string("Status: Busy", 1)
	mylcd.lcd_display_string("as of "+cT, 2)
	sleep(1)
	
def switchAway() :
	cT=currentTime()
	mylcd.lcd_clear()
	mylcd.lcd_display_string("Status: Away", 1)
	mylcd.lcd_display_string("as of "+cT, 2)
	sleep(1)
	
def switchMeeting() :
	cT=currentTime()
	mylcd.lcd_clear()
	mylcd.lcd_display_string("In a meeting", 1)
	mylcd.lcd_display_string("as of "+cT, 2)
	sleep(1)
	
def switchPhone() :
	cT=currentTime()
	mylcd.lcd_clear()
	mylcd.lcd_display_string("On the phone", 1)
	mylcd.lcd_display_string("as of "+cT, 2)
	sleep(1)
	
def switchGrading() :
	cT=currentTime()
	mylcd.lcd_clear()
	mylcd.lcd_display_string("Grading papers", 1)
	mylcd.lcd_display_string("as of "+cT, 2)
	sleep(1)
	
def switchEmail() :
	cT=currentTime()
	mylcd.lcd_clear()
	mylcd.lcd_display_string("Sending Emails", 1)
	mylcd.lcd_display_string("as of "+cT, 2)
	sleep(1)
	
def switchVideo() :
	cT=currentTime()
	mylcd.lcd_clear()
	mylcd.lcd_display_string("On a video call", 1)
	mylcd.lcd_display_string("as of "+cT, 2)
	sleep(1)
	


def switchClear() :
	mylcd.lcd_clear()
	sleep(1)

# API TH
@app.route('/api/th', methods=['GET'])
def apiTH() :
	switchTH()
	return jsonify({})
	
# API switchAvailable
@app.route('/api/available', methods=['GET'])
def apiavailable() :
	switchAvailable()
	return jsonify({})
	
# API Busy
@app.route('/api/busy', methods=['GET'])
def apiBusy() :
	switchBusy()
	return jsonify({})
	
# API Away
@app.route('/api/away', methods=['GET'])
def apiAway() :
	switchAway()
	return jsonify({})
	
# API switchMeeting
@app.route('/api/meeting', methods=['GET'])
def apiMeeting() :
	switchMeeting()
	return jsonify({})
	
# API switchPhone
@app.route('/api/phone', methods=['GET'])
def apiPhone() :
	global globalLastCalledApi
	globalLastCalledApi = '/api/Phone'
	switchPhone()
	return jsonify({})
	
# API switchGrading
@app.route('/api/grading', methods=['GET'])
def apiGrading() :
	switchGrading()
	return jsonify({})
	
# API switchEmail
@app.route('/api/email', methods=['GET'])
def apiEmail() :
	switchEmail()
	return jsonify({})
	
# API switchVideo
@app.route('/api/video', methods=['GET'])
def apiVideo() :
	switchVideo()
	return jsonify({})
	
# API clear
@app.route('/api/clear', methods=['GET'])
def apiClear() :
	switchClear()
	return jsonify({})

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=False)
