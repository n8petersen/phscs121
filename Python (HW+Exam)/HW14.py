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
G_const = 6.67e-11



#=======================================================#
## Problem 1
mass = 5 # kg
k = 89.5 # N/m

period = 2 * pi * sqrt(mass / k)
print("1: ", period)
print("")



#=======================================================#



## Problem 2
# x(t) = c1 * cos((c2 * t) + c3)
c1 = 0.0337 # 0.0252 # Amplitude
c2 = 333 # Hz # 
c3 = 1.22 # radians

amplitude = c1
angular_freq = c2
phase_shift = c3

period = (2 * pi) / angular_freq
freq = 1 / period

print("2a: Amplitude (m):", amplitude)
print("2b: Angular Freq (rad/s):", angular_freq)
print("2c: Frequency (Hz):", freq)
print("2d: Period (s):", period)
print("2e: Phase Shift/Constant (rad):", phase_shift)
print("    for other parts, see desmos")
print("    https://www.desmos.com/calculator/kmjka9jqfr")
print("")



#=======================================================#



## Problem 3
period_initial = 2.68 # s ## changing var
g_i = 9.8 # m/s^2

### Part a
# T = 2 * pi * sqrt(length / g)
# T / (2 * pi) = sqrt(length / g)
# (T / (2 * pi))**2 = length / g
# g * (T / (2 * pi))**2 = length
length =  g_i * (period_initial / (2 * pi))**2
print("3a: ", length)

### Part b
g = 1.67  # m/s^2
period = 2 * pi * sqrt(length / g)
print("3b: ", period)


### Part c
g_new = 9.79
period_new = 2 * pi * sqrt(length / g_new)
period_diff = period_new - period_initial
print("3c: ", period_diff)

print("")



#=======================================================#



## Problem 4
mass_rod = 1.23 # kg
length_rod = 1.25 # m
mass_weight = 0.71 # kg ## changing var
x_weight = 1
mass_total = mass_rod + mass_weight

inertia_rod = mass_rod * ((length_rod**2) / 3)
inertia_mass = mass_weight * (x_weight**2)
inertia_total = inertia_rod + inertia_mass

length_cm = (mass_rod * (length_rod / 2) + mass_weight * x_weight) / (mass_rod + mass_weight)

period = 2 * pi * sqrt(inertia_total / (mass_total * grav * length_cm))
print("4: ", period)

print("")



#=======================================================#



## Problem 5
mass_earth = 5.98e24 # kg
radius_earth = 6370 * 1000 # km to m
height_sat = 8.7e3 * 1000 # km to m ## changing var

### Part a
radius_total = radius_earth + height_sat
g = G_const * (mass_earth / (radius_total**2))
v = sqrt(g * radius_total)
print("5a: ", v / 1000)

### Part b
period = (2 * pi * radius_total) / v
print("5b: ", period / 60 / 60)

print("")



#=======================================================#



## Problem 6
v_p = 55 # km/s
r_p = 0.586 # AU
r_a = 17.8 # AU

v_a = r_p * v_p / r_a
print("6: ", v_a)

print("")



#=======================================================#



## Problem 7
period = 18.3 # days
speed = 220 # km/s

period = period * 24 * 60 * 60 # days to seconds
speed = speed * 1000 # km/s to m/s

radius = (period * speed ) / (2 * pi)
mass = ((speed**2 * 2 * radius) / G_const) * 2
print("7: ", mass)

print("")



#=======================================================#



## Problem 8
r = 806e6 * 1000 # km to m ## changing var
v = 14.4 * 1000 # km/s to m/s ## changing var

mass = (v**2 * r) / G_const
print("8: ", mass)