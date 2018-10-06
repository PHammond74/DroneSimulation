'''
SIT374 - Team Symbiosis

Drone flight simulation to mimick prototype flight-control methodology.

Written by:
Paul Hammond
216171484
'''

import time
import math

x = 4
y = 5
z = 1.6
initVelocityDrone = 0.5
s = 0
h = 0
height = 0
droneRotation = 0

# Equations
angle = math.degrees(math.atan(y / x))
distance = math.sqrt((x * x + y * y))
travelTime = (round)(distance / initVelocityDrone)      # Get time as an integer value
newVelocityDrone = distance / travelTime                # Recalculate drone velocity


# Outputs
print("Angle is: %f deg" %angle)
print("Distance to travel is: %f m" %distance)
print("Flight time is: %f s\n" %travelTime)

# Drone flight
# Takeoff
print("Drone is taking off: current height is %f m" %height)
time.sleep(1)
for z in range(10 + 1):
    height = z * 0.02
    print(height)
    time.sleep((0.1))   # seconds

# Hover
print("\nDrone is hovering at height of %f m\n" %height)
time.sleep(2)

# Rotate
print("Drone is commencing rotation")
time.sleep(1)
yawTime = 2
yawRate = angle / yawTime
for t in range(yawTime * 10 + 1):
    droneRotation = t / 10 * yawRate
    print(droneRotation)
    time.sleep((0.1))   # seconds
print("\nDrone has rotated %f deg\n" %droneRotation)
time.sleep(2)

# Traverse Flight Path
print("Drone is travelling to waypoint...")
time.sleep(1)
for timeT in range(travelTime * 10):
    s += (newVelocityDrone / 10)
    height += 0.1 / 10
    print("Distance: %f\t\tHeight: %f" %(s, height))
    time.sleep(0.1)     # seconds

print("\nDrone has reached its destination")
print("Total Distance travelled: %f m" %s)
print("Average speed: %f m/s\n" %(s/travelTime))

# Hover for 10 seconds
print("Drone is hovering at height of %f m" %height)
for t in range(10):
    print("Hovering...%d sec" %(t + 1))
    time.sleep(1)

# Reverse Flight Path
print("\nDrone is travelling to origin...")
time.sleep(1)
for timeT in range(travelTime * 10):
    s -= (newVelocityDrone / 10)
    height -= 0.1 / 10
    print("Distance: %f\t\tHeight: %f" %(s, height))
    time.sleep(0.1)     # seconds

print("\nDrone has reached the origin\n")

# Reverse Rotate
print("Drone is commencing reverse rotation")
time.sleep(1)
yawTime = 2
yawRate = angle / yawTime
startAngle = angle
for t in range(yawTime * 10 + 1):
    droneRotation = t / 10 * -yawRate
    print(droneRotation)
    time.sleep((0.1))   # seconds
print("Drone has rotated %f deg" %droneRotation)
print("Current angle is %f deg\n" %(startAngle + droneRotation))
time.sleep(2)

'''
Landing
'''
print("Drone is landing: current height is %f m" %height)
time.sleep(1)
for z in range(10 + 1):
    height = (10 - z) * 0.02
    print(height)
    time.sleep((0.1))   # seconds

if (height == 0):
    print("\nDrone has landed - engines shutdown")
else:
    print("\nDrone has crashed!!")





