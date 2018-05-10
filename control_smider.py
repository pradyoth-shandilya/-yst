import time
import serial
import re
import io
import urllib.request
ser = serial.Serial('/dev/ttyACM1', 9600, timeout = 1)  # open serial port
#print(ser.name)         # check which port was really used
#ser.write(b'hello')     # write a string
a = '1'.encode()
b = '2'.encode()
u = urllib.request.urlopen("http://127.0.0.1/test.txt")
while 1:
	u = urllib.request.urlopen("http://127.0.0.1/test.txt")
	f = io.TextIOWrapper(u,encoding='utf-8')
	smider_status = f.read()
	print(smider_status)
	if smider_status == "100":
		print("Open")
		ser.write(a)
	if smider_status is "0":
		print("Close")
		ser.write(b)
	#print(request)

ser.close()    
u.close()
