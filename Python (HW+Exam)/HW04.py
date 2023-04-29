import math
from math import cos
from math import sin
from math import tan
from math import atan
from math import radians as rad
from math import degrees as deg
from math import sqrt
from math import pi
from Physics import quadratic_roots
grav = 9.8



#=======================================================#
## Problem 3
mass = 0.1
length = 1.7
angle = rad(37)
period = 2.34
t = 0

freq = (2 * pi) / period
radius = length * sin(angle)
v_x = -radius * freq * sin(freq * t)
v_y = radius * freq * cos(freq * t)
v = sqrt(v_x**2 + v_y**2)

a_c = (v**2) / radius
print("3: ", a_c)