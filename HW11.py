import math
from math import cos
from math import sin
from math import tan
from math import radians
from math import sqrt
from math import pi
from Physics import quadratic_roots
G = 9.8


#=======================================================#


## Problem 1
### Part a
periodDays = 365

periodHours = periodDays * 24
periodMinutes = periodHours * 60
periodSeconds = periodMinutes * 60
w = 2 * pi / (periodSeconds)
print("1a: ", w)

### Part a
periodDays = 27.3

periodHours = periodDays * 24
periodMinutes = periodHours * 60
periodSeconds = periodMinutes * 60
w = 2 * pi / (periodSeconds)
print("1b: ", w)


#=======================================================#


## Problem 2
#a = ?
wf = 75.9
t = 4.01 # changing var
theta_f = 37
theta_i = 0

## All the equations I have are missing 2?
a = "Uncomplete"

print("2: ", a)


#=======================================================#


## Problem 3
### Part a
rpm = 10000

radPerSec = 2 * pi * rpm * (1/60)
print("3a: ", radPerSec)


### Part b
w_i = radPerSec
w_f = 0
t = 4.13 # changing var

# w_f = w_i + alpha * t
# w_f - w_i = alpha * t
# (w_f - w_i) / t = alpha
alpha = (w_f - w_i) / t
print("3b: ", alpha)


### Part c
r = 8.13 / 100
theta_i = 0
theta_f = theta_i + w_i * t + (1/2) * alpha * (t**2)
# theta = s / r
# s = r * theta
s = r * theta_f
print("3c: ", s)


### Part d
v = w_i * r
a_c = (v**2) / r
print("3d: ", a_c)


### Part e
a_t = alpha * r
print("3e: ", a_t)