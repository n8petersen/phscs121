import math
from math import cos
from math import sin
from math import tan
from math import radians as rad
from math import sqrt
from math import pi
from Physics import quadratic_roots
G = 9.8



#=======================================================#



## Problem 2 ( From HW 2)
x_man = 3.01
v0_man = 0
a_man = 9.8

v_horse = 9.28
a_horse = 0

### Part b (easier to do b first, then a)
# x = v0 * t + 1/2 * a * t**2
# 3.01 = 0 * t + 1/2 * 9.8 * t**2
# 3.01 = 1/2 * 9.8 * t**2
t = sqrt((2 * x_man) / a_man)

### Part a
x = v_horse * t 


print("2a: ", x)
print("2b: ", t)

print("")




#=======================================================#



## Problem 20
a = 0.2
x = 380000
# x = x_not + v_not * t + 1/2 * a * t**2
# x = 1/2 * a * t**2
# x / (1/2 * a) = t**2
t = sqrt(x / (1/2 * a))
print("20: ", t / 60)

print("")




#=======================================================#



## Problem 24



v = sqrt(2 * 6.67E-11 * 5.98E24 * ((1 / 6370000) - (1 / 3860000)) / 60) 
print("24: ", v)