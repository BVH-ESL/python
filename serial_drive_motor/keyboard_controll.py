import serial
from time import sleep
import tty, sys

speed_a = 0
speed_b = 0
dir_a = 1
dir_b = 1

drive_command = "("+str(speed_a*dir_a)+","+str(speed_b*dir_b)+"):"

ser = serial.Serial('/dev/ttyACM0', 
					baudrate = 9600,
					bytesize=serial.EIGHTBITS,
					parity=serial.PARITY_NONE,
					stopbits=serial.STOPBITS_ONE,
					timeout=0.1)

		
sleep(1.0)
while ser.read():
	pass

tty.setraw(sys.stdin.fileno())
ser.write(drive_command)
while 1:
	ch = sys.stdin.read(1)
	if ch == 'e':
		break
	else if ch == 'w':
		
	drive_command = "("+str(speed_a*dir_a)+","+str(speed_b*dir_b)+"):"
	ser.write(drive_command)
