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
G = 9.8


#=======================================================#


## Problem 1
mass = 1050 # kg
speed = 123 / 3.6 # km/g to m/s ## changing var

### Part a
p1 = mass * speed
p2 = mass * 0
changeP = p1 - p2
print("1a: ", changeP)

### Part b
k1 = (1/2) * mass * (speed**2)
k2 = (1/2) * mass * (0**2)
changeK = k1 - k2
print("1b: ", changeK)


print("")


#=======================================================#


## Problem 2
mass = 61.6 / 1000 # g to kg
height = 1.51 # m ## changing var
percent_of_h = 88.5 / 100 # %
new_height = height * percent_of_h # m

### Part a
v1 = sqrt(2 * G * height)
v2 = sqrt(2 * G * new_height)
p1 = mass * v1
p2 = mass * v2
changeP = p1 + p2
print("2a: ", changeP)

### Part b
v1 = sqrt(2 * G * height)
v2 = 0
p1 = mass * v1
p2 = mass * v2
changeP = p1 - p2
print("2b: ", changeP)


print("")


#=======================================================#


## Problem 3
mass1 = 5.21 / 1000 # g to kg
mass2 = 14.8 # kg
speed = 526 # m/s ## changing var

### Part a
Pi = (mass1 * speed) + (mass2 * 0)
combined_mass = mass2 + mass1
vf = (mass1 / (mass1 + mass2)) * speed
print("3a: ", vf)

### Part b
pf = vf * combined_mass
print("3b: ", pf)

### Part c / d
kf = (1/2) * combined_mass * (vf**2)
print("3c/d: ", kf)

### Part e/f
ki_bullet = (1/2) * mass1 * (speed**2)
w_bullet = kf - ki_bullet
print("3e/f: ", w_bullet)



print("")