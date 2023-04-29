import math

G = 9.807


# ## Problem 1
mass = 110.3 # Changing var
mu_s = 0.5
mu_k = 0.3

# ### Part (a)
Fn = mass * G
f_s_max = mu_s * Fn
print("1a: ", f_s_max)

# ### Part (b)
f_k = mu_k * Fn
Fnet = f_s_max - f_k
#F = ma
#F / m = a
a = Fnet / mass
print("1b: ", a)


print("")


# ## Problem 2
# mass = 2.5
# v = 0
# v0 = 0.6 # Changing var
# mu_k = 0.7
# angle = 25
# x0 = 0

# ### Part (a)
# weight = mass * G
# w_x = weight * math.sin(math.radians(angle))
# w_y = weight * math.cos(math.radians(angle))

# Fn = w_y
# f_k = -1 * mu_k * Fn
# Fnet = f_k + w_x
# a = Fnet / mass

# t =  (v - v0) / a
# x = x0 + v0 * t + (1/2) * a * (t**2)
# print("2a: ", x)

# ### Part (b)
# v_new = (v0 / 3)
# t = (v_new - v0) / a
# print("2b: ", t)



## Problem 3
mass = 7.5
a = 3.46 # changing var
mu_s = 0.443
mu_k = 0.312
angle = 25

## Part (a)
# N = mg*cos(theta) + Fsin(theta)
# ma = F*cos(theta) - m*g*sin(theta) - mu_k * N
# ma = F*cos(theta) - m*g*sin(theta) - mu_k * (mg*cos(theta) + Fsin(theta))
# F = (ma + mgsin(theta) + mu_kmgcos(theta)) / (cos(theta) - mu_k*sin(theta))
force = (mass * a + mass * G * math.sin(math.radians(angle)) + mu_k * mass * G * math.cos(math.radians(angle))) / (math.cos(math.radians(angle)) - mu_k * math.sin(math.radians(angle)))
print("3a: ", force)

## Part (b)
# N = mg*cos(theta) + Fsin(theta)
Fn = mass*G*math.cos(math.radians(angle)) + force * math.sin(math.radians(angle))
print("3b: ", Fn)

## Part (c)
friction = mu_k * Fn
print("3c: ", friction)




# ## Problem 4
# mass = 33.2 #changing var
# angle = 39.8 #changing var
# mu_k = 0.6

# weight = mass * G

# force = (mu_k * weight) / (math.cos(math.radians(angle)) + mu_k * math.sin(math.radians(angle)))


# print("4: ", force)




# print("Done!")
