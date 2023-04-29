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
## Problem 1
mass1 = 45
distance1 = 3.5
mass2 = 55
distance2 = 2.5
mass3 = 33.9  #  changing var

# m1 * d1 = m2 * d2 + m3 * d3
# (m1 * d1) - (m2 * m2) = m3 * d3
# (m1 * d1) - (m2 * m2) / m3 * d3

person1 = mass1 * distance1
person2 = mass2 * distance2

distance3 = (person1 - person2) / mass3
print("1: ", distance3)
print("")



#=======================================================#
## Problem 2
mass = 67.4 # kg  ## changing var
length = 2.5 # meters
angle = 60 # degrees

weight = mass * grav

# tension_y = cos(theta) * tension
# weight_y = tension_y
# sin(theta) * weight  = cos(theta) * tension
# tension = (sin(theta) / cos(theta)) * w
tension = tan(rad(angle)) * weight
print("2: ", tension)
print("")



#=======================================================#
## Problem 3
length = 12.3 / 100 # cm to m
force = 144 # N  ## changing var
distance = 5.2 / 100 # cm to m

force_nail = (force * distance * 2) / length

print("3: ", force_nail)
print("")



#=======================================================#
## Problem 4
mass = 3.51 # kg ## changing var
angle1 = rad(60)
angle2 = rad(13.5)

tension1 = (mass * grav) / (sin(angle1) + sin(angle2) * cos(angle1) / cos(angle2))
tension2 = cos(angle1) / cos(angle2) * tension1



print("4a: ", tension1)
print("4b: ", tension2)
print("")