import serial
import re
import urllib.request
#print(ser.name)         # check which port was really used
ser = serial.Serial('/dev/ttyACM0')  # open serial port
#ser.write(b'hello')     # write a string
while 1:
	line = ser.readline()
	str = line.decode()
	line = str.replace('\r', '')
	#print(str)
	sensor_array = str.split(' ')
	print(sensor_array)
	#u = urllib.request.urlopen("http://18.236.130.246/smider_open.php?humidity="+sensor_array[0]+"&temp="+sensor_array[1]+"&light="+sensor_array[2]+"&pressure="+sensor_array[3]+"&obstacle="+sensor_array[4])
	#print(request)
	#response = urllib.request.urlopen(request)
	#response.close()
ser.close()
