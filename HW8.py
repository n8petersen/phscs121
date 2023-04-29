import math
from math import cos
from math import sin
from math import tan
from math import radians
from math import sqrt
from Physics import quadratic_roots

G = 9.8


## Problem 1
v_0 = 4.01 # changing var
l = 1.54
angle = 21.7

h1 = l
h2 = 1.54 * sin(radians(angle))

v_f = sqrt(2*((0.5) * v_0**2 + G * h1 - G * h2))
print("1: ", v_f)

print("")



## Problem 2
angle = 53.2
h_0 = 182000 # 182km = 182000 m
v_0 = 1010 # 1.55 km/s = 1550 m/s  # changing var
accel = 9.8

v_f = sqrt(v_0**2 + accel * h_0)
print("2: ", v_f)



## Problem 3
m1 = 5.55 # changing var
m2 = 3.52
v1_i = 2.13
h = 2.47

# vf = sqrt(v1_i**2 + 2 * a * h)

vf = sqrt((v1_i**2 * (m1 + m2) + 2*G*h*(m1-m2))/(m1+m2))
print("3: ", vf)