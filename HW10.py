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
m1 = 5.21 / 1000 # g to kg
v1 = 352 # m/s  ## changing var
m2 = 14.8 # kg
v2i = 0 # m/s

### Part a
v2f = (((2 * m1) / (m1 + m2)* v1) + (((m2 - m1) / (m2 + m1)) * v2i))
print("1a: ", v2f)

### Part b
impulse = ((m2 * v2f) + (m2 * v2i))
print("1b: ", impulse)

print("")


#=======================================================#


## Problem 2
m1 = 1310 # kg ## changing var
v1i = 25 # m/s
v1f = 18 # m/s
m2 = 9000 # kg
v2i = 20 # m/s

### Part a
v2f = ((m1 * v1i) + (m2 * v2i) - (m1 * v1f)) / m2
print("2a: ", v2f)

### Part b
vfX = (m1 * v1i) / ((m1 + m2) * cos(rad(0)))
vfY = (m2 * v2i) / ((m1 + m2) * sin(rad(90)))
vf = sqrt((vfX**2) + (vfY**2))
print("2b: ", vf)


### Part c
angle_after = deg(atan((m1 * v1i) / (m2 * v2i)))
print("2c: ", angle_after)

print("")


#=======================================================#


## Problem 3
m1 = 0.00512 # kg
v1 = 243 # m/s ## changing var
ang1 = 21.3 # degrees
m2 = 0.00305 # kg
v2 = 282 # m/s
ang2 = 15.4 # degrees

v1X = v1 * cos(rad(ang1))
v1Y = v1 * sin(rad(ang1))

v2X = v2 * cos(rad(ang2))
v2Y = v2 * sin(rad(ang2))

mF = m1 + m2

vFX = ((m1 * v1X) - (m2 * v2X)) / mF
vFY = ((m1 * v1Y) + (m2 * v2Y)) / mF
vF = sqrt((vFX**2) + (vFY**2))
print("3a: ", vF)

angleF = 90 - deg(atan((vFX) / (vFY)))
print("3b: ", angleF)

k1 = (1/2) * m1 * v1**2
k2 = (1/2) * m2 * v2**2
ki = k1 + k2
kf = (1/2) * mF * vF**2
kdiff = ki - kf
lossKFraction = kdiff / ki
print("3c: ", lossKFraction)

print("")


#=======================================================#


## Problem 4
earth_mass = 5.98E+24
moon_mass = 7.36E+22
sun_mass = 1.99E+30
jupiter_mass = 1.90E+27

moon_d_from_Earth = 3.84E+08
earth_d_from_Sun = 1.496E+11
jupter_d_from_Sun = 7.78E+11

earth_radius = 6.37E+06
sun_radius = 6.96E+08

earth_and_Moon = (((earth_mass * 0) + (moon_mass * moon_d_from_Earth)) / (earth_mass + moon_mass))
ratio_Earth_radius = earth_and_Moon / earth_radius
print("4a: ", ratio_Earth_radius)

sun_and_Earth = (((sun_mass * 0) + (earth_mass * earth_d_from_Sun)) / (earth_mass + sun_mass))
ratio_Sun_radius = sun_and_Earth / sun_radius
print("4b: ", ratio_Sun_radius)

sun_and_Jupiter = (((sun_mass * 0) + (jupiter_mass * jupter_d_from_Sun)) / (sun_mass + jupiter_mass))
ratio_Sun_radius = sun_and_Jupiter / sun_radius
print("4c: ", ratio_Sun_radius)


print("")


#=======================================================#


## Problem 5
v0 = 9.9 # m/s ## changing var
# angle = 30 # degrees

u1 = ((2 * sqrt(3)) / 5) * v0
print("5a: ", u1)

v2 = -(1/5) * v0
print("5b: ", v2)

print("HW10 Finished.")