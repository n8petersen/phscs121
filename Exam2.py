import math
from math import cos
from math import sin
from math import tan
from math import radians
from math import sqrt
from Physics import quadratic_roots

G = 9.8

mass = 0.812
angle = radians(35.3)
springConstK = 1140
d = 0.248 # changing var
mu_k = 0.195

# Epot = (1/2) * (springConstK) * x**2

energyChange = mass * G * d * sin(angle)

energyLostFriction = mu_k * mass * G * cos(angle) * d

# (1/2) * springConstK * x**2 = energyChange + energyLostFriction
# x**2 = (energyChange + energyLostFriction) / (1/2) * springConstK
x = sqrt(((energyChange + energyLostFriction) / ((1/2) * springConstK)))


print("Answer:", x)