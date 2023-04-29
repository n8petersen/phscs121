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

print("")


#=======================================================#


## Problem 2
#a = ?
wf = 75.9
t = 4.01 # changing var
theta_f = 37 * 2 * pi
theta_i = 0
theta = theta_f - theta_i

# wf = w_i + a*t
# wf - w_i / t = a

    # (w_i + wf / 2) = w_avg
    # w_i + wf = 2 * w_avg
    # w_i = 2 * w_avg   -  wf

        # θ = wavg * t
        # θ / t = wavg
theta = theta_f - theta_i

# wf = w_i + a*t
# wf - w_i / t = a

    # (w_i + wf / 2) = w_avg
    # w_i + wf = 2 * w_avg
    # w_i = 2 * w_avg   -  wf

        # θ = wavg * t
        # θ / t = wavg

w_avg = theta / t
w_i = 2 * w_avg   -  wf
w_avg = theta / t
w_i = 2 * w_avg   -  wf

a = (wf - w_i) / t
a = (wf - w_i) / t
print("2: ", a)

print("")


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

print("")

#=======================================================#


## Problem 4
# No mass or radius given?? How do we calculate without these?
d = 6.02 # changing var
angle = 35
h = d * sin(rad(angle))

### Part a
v = sqrt(G * h)
print("4a: ", v)


### Part b
v = sqrt((4 * G * h) / 3)
print("4b: ", v)

print("")



#=======================================================#


## Problem 5
m = 500     / 1000                  # g to kg
r = 1.48    / 100 # chaning var     # cm to m
h = 49.5    / 100 # changing var    # cm to m

i = (2*m * r**2) / 5
print("5a: ", i)

v = sqrt(10 * G * h / 7)
print("5b: ", v)

print("")


#=======================================================#


## Problem 6
v = 80.7    / 3.6 # changing var    # km/h to m/s
r = 38.4    / 100                   # cm to m
w = v / r
print("6a: ", w)

a_c = v**2 / r
print("6b: ", a_c)