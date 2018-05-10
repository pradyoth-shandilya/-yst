import serial
import re
import urllib.request
ser = serial.Serial('/dev/ttyUSB0')  # open serial port
#print(ser.name)         # check which port was really used
#ser.write(b'hello')     # write a string
while 1:
	
	line = ser.readline()
	str = line.decode()
	line = str.replace('\r', '')
	#print(str)
	sensor_array = str.split(' ')
	print(sensor_array[0])
	request = "http://18.236.130.246/smider_open.php?humidity="+sensor_array[0]+"&temp="+sensor_array[1]+"&light="+sensor_array[2]+"&pressure="+sensor_array[3]+"&obstacle="+sensor_array[4];
	print(request)
	response = urllib.request.urlopen(request)
	response.close()
ser.close()    
