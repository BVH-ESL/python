import dynamixel, time

portName = "/dev/ttyUSB0"

baudRate = 9600

serial = dynamixel.SerialStream(port = portName, baudrate = baudRate, timeout = 1)
print "connect"
net = dynamixel.DynamixelNetwork(serial)
net.scan(1, 1)

myActuators = list()
pos = 0
print "Scanning for Dynamixels..."
#print net.get_dynamixels()
for dyn in net.get_dynamixels():
    print dyn.id
    myActuators.append(net[dyn.id])
print "...Done"

for ac in myActuators:
    ac.moving_speed = 175
    ac.synchronized = True
    ac.torque_enable = True
    ac.torque_limit = 800
    ac.max_torque = 800

while (1):
    for ac in myActuators:
        ac.goal_position = pos
    net.synchronize()
    
#    for ac in myActuators:
#        ac.read_all()
#        time.sleep(0.01)

    time.sleep(2)

    if pos > 4095:
        pos = 0
    else:
        pos += 511
