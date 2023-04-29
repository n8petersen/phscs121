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



## Problem 1
mass = 1.80 # kg
radius = 35 / 100 #cm to m
force = 45.1 # N ## changing var


### Part a
torque = force * radius
print("1a: ", torque)


### Part b
# f = m * a
# a = f / m
accelTan = force / mass
#aTan = radius * aAng
accelAng = accelTan / radius
print("1b: ", accelAng)

print("")



#=======================================================#



## Problem 2
radius_wheel = 32 / 100 # cm to m
mass = 1.82 # kg
friction = 117 # N ## changing var
accelAng = 4.5 # rad/s^2


### Part a
radius_sprocket = 4.53 / 100 # cm to m
torque = mass * (radius_wheel **2) * accelAng
force_applied = (torque + (radius_wheel * friction)) / radius_sprocket
print("2a: ", force_applied)


### Part b
radius_sprocket = 2.88 / 100 # cm to m
torque = mass * (radius_wheel **2) * accelAng
force_applied = (torque + (radius_wheel * friction)) / radius_sprocket
print("2b: ", force_applied)


### Part c
arclength = radius_wheel * accelAng
massBike = friction / arclength
print("2c: ", massBike)

print("")



#=======================================================#



## Problem 3
inertia_ratio = 5520
theta_probe = 32.6
theta_rotor = (inertia_ratio) * theta_probe
rotations_rotor = theta_rotor / 360
print("3: ", rotations_rotor)

print("")



#=======================================================#



## Problem 4

mass_rod = 2 # kg
length = 75 / 100 # cm to m
vel_a = 10
mass_point = 0.547 # kg ## changing var

distance_a = 0
distance_b = length / 4
distance_c = length / 2

inertia_bar = (1/12) * mass_rod * (length **2)
inertia_mass_a = mass_point * (distance_a**2)
inertia_mass_b = mass_point * (distance_b**2)
inertia_mass_c = mass_point * (distance_c**2)

inertia_a = inertia_bar + 2*inertia_mass_a
inertia_b = inertia_bar + 2*inertia_mass_b
inertia_c = inertia_bar + 2*inertia_mass_c

### Part a
# using conservation of angular momentum
vel_b = (inertia_a * vel_a) / inertia_b
print("4a: ", vel_b)

### Part b
k_r_a = (1/2) * (inertia_a) * (vel_a**2)
k_r_b = (1/2) * (inertia_b) * (vel_b**2)
k_ratio_ba = k_r_b / k_r_a
print("4b: ", k_ratio_ba)

### Part c
# using conservation of angular momentum
vel_c = (inertia_a * vel_a) / inertia_c
print("4c: ", vel_c)

print("")


#=======================================================#



## Problem 5
mass = 2180
radius = 131 * 1000 # km to m
velocity = 248 / 3.6 # km/hr to m/s

### Part a
momentum_linear = mass * velocity
momentum_angular = radius * momentum_linear
print("5a: ", momentum_angular)

### Part b
momentum_linear = mass * velocity
momentum_angular = radius * momentum_linear * sin(rad(45))
print("5b: ", momentum_angular)

print("")