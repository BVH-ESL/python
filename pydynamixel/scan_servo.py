import dynamixel, random, time

portName = "/dev/ttyUSB0"

baudRate = 9600

serial = dynamixel.SerialStream(port = portName, baudrate = baudRate, timeout = 1)
print "connect"
net = dynamixel.DynamixelNetwork(serial)
net.scan(1, 3)

myActuators = list()
pos = 0
print "Scanning for Dynamixels..."
#print net.get_dynamixels()
for dyn in net.get_dynamixels():
    print dyn.id
    myActuators.append(net[dyn.id])
print "...Done"

