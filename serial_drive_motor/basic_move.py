import serial
from time import sleep
speed = 100
command = "("+str(speed)+","+str(speed)+"):"
ser = serial.Serial('/dev/ttyACM0', 
					baudrate = 9600,
					bytesize=serial.EIGHTBITS,
					parity=serial.PARITY_NONE,
					stopbits=serial.STOPBITS_ONE,
					timeout=0.1)
sleep(1.0)
while ser.read():
	pass
sleep(1.0)


ser.write("(75,75):")
sleep(5)
ser.write("(0,0):")
sleep(0.5)
ser.write("(-75,-75):")
sleep(5)
ser.write("(0,0):")
sleep(0.5)
ser.write("(-75,75):")
sleep(5)
ser.write("(0,0):")
sleep(0.5)
ser.write("(75,-75):")
sleep(5)
ser.write("(0,0):")
sleep(0.5)
ser.close()
