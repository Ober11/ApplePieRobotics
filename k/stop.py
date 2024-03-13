#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
mt = MoveTank("outA", "outD",)
ms = MoveSteering("outA", "outD",)
mr = LargeMotor("outA")
ml = LargeMotor("outD")
kr = MediumMotor("outB")
kl = MediumMotor("outC")
g = GyroSensor("in2")
c2 = ColorSensor("in4")
mt.off(brake=False)
print("a")
ms.off(brake=False)
print("b")
kl.off(brake=False)
print("c")
kr.off(brake=False)
print("d")
