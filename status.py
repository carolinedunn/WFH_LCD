#!/usr/bin/env python

import i2c_lcd_driver
from time import sleep
from flask import Flask, jsonify, make_response, request
mylcd = i2c_lcd_driver.lcd()

app = Flask(__name__)

def switchTH() :
	mylcd.lcd_clear()
	mylcd.lcd_display_string("Welcome to", 1)
	mylcd.lcd_display_string("Tom's Hardware!", 2)
	sleep(1)
	
def switchAvailable() :
	mylcd.lcd_clear()
	mylcd.lcd_display_string("Caroline is", 1)
	mylcd.lcd_display_string("available", 2)
	sleep(1)

def switchBusy() :
	mylcd.lcd_clear()
	mylcd.lcd_display_string("Caroline is", 1)
	mylcd.lcd_display_string("busy", 2)
	sleep(1)
	
def switchMeeting() :
	mylcd.lcd_clear()
	mylcd.lcd_display_string("Caroline is", 1)
	mylcd.lcd_display_string("in a meeting", 2)
	sleep(1)
	
def switchPhone() :
	mylcd.lcd_clear()
	mylcd.lcd_display_string("Caroline is", 1)
	mylcd.lcd_display_string("on the phone", 2)
	sleep(1)
	
def switchGrading() :
	mylcd.lcd_clear()
	mylcd.lcd_display_string("Dad is", 1)
	mylcd.lcd_display_string("grading papers", 2)
	sleep(1)
	
def switchEmail() :
	mylcd.lcd_clear()
	mylcd.lcd_display_string("Mom is replying", 1)
	mylcd.lcd_display_string("to emails", 2)
	sleep(1)
	
def switchVideo() :
	mylcd.lcd_clear()
	mylcd.lcd_display_string("Caroline is", 1)
	mylcd.lcd_display_string("on a video call", 2)
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
