import math

## Problem 1
mass = 75
newAccel = 2.1 # Changing variable
gravity = 9.8
changeAccel = gravity - newAccel
force = mass * changeAccel
print("1: ", force)


## Problem 2
mass = 10100000 # Changing variable
force = 750000
acceleration = force / mass
# print("acceleration:", acceleration)
v = 22.2222 # 80km/h = 22.2222 m/s
v0 = 0
a = acceleration
#v = v0 + a * t
#v - v0 = a * t
# (v - v0) / a = t
t = (v - v0) / a
print("2: ", t)


## Problem 3
mass = 1286 #changing variable
a = 2.5
theta = 18
g = 9.807

# Part (a)
tension1 = mass * a
tension2 = mass * g * math.sin(math.radians(18))
tensionNet = tension1 + tension2
print("3a: ", tensionNet)

# Part (b)
normal = mass * g * math.cos(math.radians(18))
print("3b: ", normal)


## Problem 4
theta = 20.1 # changing variable
a = g * math.tan(math.radians(theta))
print("4: ", a)



## Problem 5
mass = 14.5

# Part (a)
force = mass * g
print("5a: ", force)

# Part (b)
mass2 = 5.6
netMass = mass - mass2
force = netMass * g
print("5b: ", force)

# part (c)
print("5c: ", 0) # 0 since the block is no longer on the floor



## Problem 6
locomotive = 4300
car1 = 12700
car2 = 16300
a = 0.392

# Part (a)
tension = car2 * a
print("6a: ", tension)

# Part (b)
tension = (car1 + car2) * a
print("6b: ", tension)

# Part (с)
force = (locomotive + car1 + car2) * a
print("6c: ", force)



## Problem 7
m1 = 15.7 # changing var
m2 = 4.0 # changing var

# Part (a)