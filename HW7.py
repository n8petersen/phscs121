import math
from math import cos
from math import sin
from math import radians

G = 9.807


## Problem 1
mass = 100
speed = 53.8 # changing var
acceleration = -1.81 # changing var


### Part (a)
force = mass * acceleration
print("1a: ", abs(force))

### Part (b)
v = 0
v_0 = speed
a = acceleration
x_0 = 0
# (v**2) = (v_0 ** 2) + 2 * a * (x - x_0)
# (v**2) - (v_0 ** 2) = 2 * a * (x - x_0)
# ((v**2) - (v_0 ** 2)) / 2 * a = x - x_0
# (((v**2) - (v_0 ** 2)) / (2 * a)) + x_0 = x
distance = (((v**2) - (v_0 ** 2)) / (2 * a)) + x_0
print("1b: ", distance)

### Part (c)
work = force * distance
print("1c: ", abs(work))

### Part (d)
print("1d: ", "negative direction ")



## Problem 3
mass  = 9.3 # changing var
v_0 = 10
v_f = 25
# work = k_f - k_0
# k = (1/2) * m * v**2
k_f = (1/2) * mass * v_f**2
k_0 = (1/2) * mass * v_0**2
work = k_f - k_0
print("3: ", work)



## Problem 4
mass = 44 # changing var
distance = 6
angle = 30
mu = 0.25 # changing var


w = mass * 9.8
wy = w * cos(radians(angle))
wx = w * sin(radians(angle))
normal = wy
friction = mu * normal

## Part (a)
force = friction + wx
work = force * distance
print("4a: ", work)

## Part (b)
work = -friction * distance
print("4b: ", work)

## Part (c)
height = distance * sin(radians(angle))
work = w * height
print("4c: ", -work)



### Problem 5
v_i = 26.8224 # 60mph = 26.8224 m/s
v_f = 0
distance = 10 #changing var
mass = 73 #changing var

## Part (b)
#v^2 = v_0^2 + 2 * a * d
a = (v_f**2 - v_i**2) / (2 * distance)
#v = v_0 + a * t
# v - v_0 = a * t
# (v - v_0)/a = t
t = (v_f - v_i)/a
print("5b: ", t)

## Part (c)
# F = m * a
force = mass * a
print("5c: ", force)

## Part (d)
# W = F * d
work = force * distance
print("5d: ", work)



## Problem 6
length = 0.252 #changing var #convert from cm to m
mass = 0.168 # 168g is 0.168kg
angle = 65.4

## Part (a)
shortHeight = length * cos(radians(angle))
longHeight = length
distanceY = longHeight - shortHeight
print("6a: ", distanceY)

## Part (b)
weight = mass * G
work = weight * distanceY
print("6b: ", work)

## Part (b)
print("6c: ", 0)



## Problem 7
mass = 3
v_i = 11.9 #changing var
v_f = 0

## Part (a)
k = (1/2) * mass * v_i**2
print("7a: ", k)

## Part (b)
# When v = 0 (at peak), the kinetic energy is 0.
print("7b: ", 0)

## Part (c)
height = ((1/2) * (v_i**2)) / G
print("7c: ", height)

## Part (d)
# v_f = v_i + a*t
# (v_f - v_i) / a = t
a = -9.8
t = (v_f - v_i) / a
print("7d: ", t)

## Part (e)
x_0 = 0
# x = x_0 + v_i * t + (1/2) * a * (t**2)
x = x_0 + v_i * t + (1/2) * -G * (t**2)
print("7e: ", x)