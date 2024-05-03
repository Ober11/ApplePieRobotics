#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.button import *
import time
from threading import Thread
mt = MoveTank("outA", "outD",)
ms = MoveSteering("outA", "outD",)
mr = LargeMotor("outA")
ml = LargeMotor("outD")
kr = MediumMotor("outB")
kl = MediumMotor("outC")
g = GyroSensor("in2")
#c1 = ColorSensor("in1")
c2 = ColorSensor("in4")

g.reset()
time.sleep(0.2)
global blocked
global x, y, nextstartposition, firstnavloop
firstnavloop = True

# 100 cordinate units == 5.08 cm
# 1 cordinate unit = 0.0508 cm


class Navigation():
    def GetNumberInCordinates(centimeters):
        cordinates = centimeters / 0.0508
        return cordinates
    def CordinateUpdates():
        global x, y, nextstartposition, firstnavloop
        print("a")
        while True:
            if firstnavloop:
                motorpositionstart = (ml.position*mr.position)/2
                firstnavloop = False
            elif not firstnavloop:
                motorpositionstart = nextstartposition
            motorpositionfinish = (ml.position*mr.position)/2
            robotangle = GyroSensor("in2").angle
            nextstartposition = (ml.position*mr.position)/2
            motorpositionchange = motorpositionfinish - motorpositionstart
            xcordinatechange = motorpositionchange * math.sin(robotangle)
            ycordinatechange = motorpositionchange * math.cos(robotangle)

            x += xcordinatechange
            y += ycordinatechange
               
    def MoveTo(X, Y, enddegrees, force=False):
        print("a")
        start_point = [x, y]
        end_point = [X, Y]

        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        
        distance = Navigation.dist(start_point, end_point)
        angle_radians = math.atan2(delta_y, delta_x)
        angle_degrees = math.degrees(angle_radians)
        
        turn(angle_degrees-90)
        forandbackward(30, distance, angle_degrees)
        turn(enddegrees+90)
            
def forandbackward(speed, distance, target=None, multiplier = 0.8, stop = True):
    if target == None:
        target = g.angle
    start_degrees = (ml.position+mr.position)/2
    if distance < 0:
        target_distance = start_degrees + distance
    else:
        target_distance = start_degrees + distance
    originalspeed = speed
    completed_degrees = start_degrees
    remaining_degrees = target_distance - completed_degrees
    original_remaining_degrees = remaining_degrees
    while remaining_degrees * (1 if distance >= 0 else -1) > 0:
        iteration_completed_degrees = (ml.position+mr.position)/2-start_degrees
        remaining_degrees = original_remaining_degrees - iteration_completed_degrees
        if abs(iteration_completed_degrees) < 50:
            speed = max(abs(iteration_completed_degrees) * (originalspeed*0.02), 10)
        remaining = target-g.angle
        correction = remaining*multiplier
        correction = min(max(correction, -100), 100)
        if stop == True and abs(remaining_degrees) < 100:
            speed = max(originalspeed*(abs(remaining_degrees)*0.01), 10)
        ms.on(correction if distance >= 0 else -correction, speed if distance >= 0 else -speed)
        print(remaining, g.angle, (ml.position+mr.position)/2<target_distance, ml.position, mr.position)
    if stop == True:
        print("Motors turning off") 
        ms.off()
    return 0



def turn(target, multiplier=0.7, timeout=None):
    #modulo modifiers for efficiency
    if target < 0:
        target=target*-1
        target=target%360
        target=target*-1
    elif target >= 0: 
        target=target%360  
    #starting timeout if needed
    start_time = time.time() if timeout else None

    #looping until the target is reached
    while target != g.angle:
        # Check for timeout
        if timeout:
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout:
                print("Timeout reached. Exiting the loop.")
                break
        # Calculating the difference between the target and the current angle
        diff = target - g.angle
        #multiplier for the speed of the motors
        diff *= multiplier
        #limiting the speed of the motors
        if diff > 100:
            diff = 100
        elif diff < -100: 
            diff = -100
        #turning the motors
        mt.on(diff, -diff)
        #print test
        print(diff, target, g.angle)
    #stopping the motors
    mt.stop()
    time.sleep(0.3)

kl.on_for_seconds(-50, 1)
time.sleep(0.5)
kl.on_for_degrees(100, 150)
forandbackward(30, 100)
time.sleep(0.75)
kl.on_for_degrees(100, 125)
forandbackward(30, 100)
time.sleep(0.75)
forandbackward(30, 100)
kl.on_for_degrees(100, 150)
time.sleep(0.75)
forandbackward(30, 100)
kl.on_for_degrees(100, 125)
time.sleep(0.75)