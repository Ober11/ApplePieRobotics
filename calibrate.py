#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
g = GyroSensor("in2")
g.calibrate()
g.reset()