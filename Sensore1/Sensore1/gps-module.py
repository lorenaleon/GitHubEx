import os
import time
import serial
import pynmea2
import string
#loop for the gps

while True:
	port = "/dev/ttyAMA0"
	ser = serial.Serial(port, baudrate=9600, timeout=0.5)
	dataout = pynmea2.NMEAStreanReader()
	newdata = ser.readline()

	print ("Obtendo latitude e longetude")

	if newdata[0:6] == '$GPGGA':
		newmsg = pynmea2.parse(newdata)
		lat = newmsg.latitude
		print (lat)
		long = newmsg.longitude
		print (long)
		time.sleep()
