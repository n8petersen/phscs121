from Physics import quadratic_roots as quadratic
import cmath
import math


# Problem 3-1 (a) & (b)
degrees = 20.1 # changing variable
c = 3.10

a = (c * math.sin(math.radians(degrees)))
b = (c * math.cos(math.radians(degrees)))
print(f"3-1-a: {a:.5f} km north")
print(f"3-1-b: {b:.5f} km east")
print("")




# Problem 3-2
a_mag = 1.51 # Changing variable
a_dir_deg = 35
y = 3.38
y_not = 0
x_not = 0
v_not_y = -1.32

v_not = v_not_y
a_y = (a_mag * math.sin(math.radians(a_dir_deg)))
a_x = (a_mag * math.cos(math.radians(a_dir_deg)))


## Part (a)
### Formula: y = y_not + (v_not * t) + (1/2)(a)(t**2)
### use quadratic to solve for t
a = (1/2) * a_y
b = v_not
c = -y
t = 0
roots = quadratic(a, b, c)
for root in roots:
    if (root > 0): 
        t = root

print(f"3-2-a: {t:.5f} s at y(t) = 3.38m")
        

## TODO: Part (b)
### find pos_x at t



## TODO: Part (c)


## TODO: Part (d)


print("")





# Problem 3-3
v_not_mag = 50
v_not_deg = 41.3 # Changing variable
y_not = 75
y = 0
x_not = 0
g = 9.8

v_not_y = v_not_mag * math.sin(math.radians(v_not_deg))
v_not_x = v_not_mag * math.cos(math.radians(v_not_deg))
v_x = v_not_x 


## Part (a)
### Formula: y = y_not + (v_not_y * t) - (1/2)(g)(t**2)
a = -(1/2) * g
b = v_not_y
c = y_not
t = 0

roots = quadratic(a, b, c)
for root in roots:
    if (root > 0): 
        t = root

print(f"3-3-a: {t:.5f} s to hit ground")


## Part (b)
### Formula: x = x_not + v_x * t
x = x_not + v_x * t

print(f"3-3-b: {x:.5f} m from base of cliff")


## Part (c)
### Formula: v = v_not_y - g * t
v_y = v_not_y - g * t
print(f"3-3-c: {v_y:.5f} m/s = v_y")

## Part (d)
print(f"3-3-d: {v_x:.5f} m/s = v_x")
print("")



# Problem 3-4
x = 30.5 # Changing Variable
h = 3
x_not = 0
y_not = 0
v_not_mag = 20
v_not_deg = 53
g = 9.8

## Part (a)
### Find y where x = 25.1
### using y = y_not + (v_not_y * t) - (1/2)(g)(t**2)
### Find t, using x = x_not + v_x * t

v_not_y = v_not_mag * math.sin(math.radians(v_not_deg))
v_not_x = v_not_mag * math.cos(math.radians(v_not_deg))
v_x = v_not_x 

#x_not + (v_x * t) = x
#v_x * t = x - x_not
t = (x - x_not) / v_x

y = y_not + (v_not_y * t) - ((1/2)*(g)*(t**2))

y_clear = y - 3
print(f"3-4-a: {y_clear:.5f} m = the distance between the bar and the ball")


## Part (b)
### what is v_y at time t
### positive means ball is rising, negative means ball is falling.
### Use Formula: v_y = v_not_y - (g * t)
v_y = v_not_y - (g * t)
print(f"3-4-b: {v_y:.5f} m/s = v_y of the ball at t={t:.5f}")
print("")




# Problem 3-5
y_not = 0.860
y = 0
x_not = 0
x = 1.48 # Changing variable

g = 9.8
v_not_y = 0

## Part (a)
### Find v_x using: x = x_not + (v_x * t) 

### We can find t, because we know it fell 0.860m, with v_not_y = 0, and g = 9.8.
### y = y_not + v_not * t - (1/2) * g * t**2
### 0 = -4.9t^2 + 0t + 0.860

a = (-1/2) * (g)
b = v_not_y
c = y_not
t = 0

roots = quadratic(a, b, c)
for root in roots:
    if (root > 0): 
        t = root

# x_not + (v_x * t) = x
# v_x * t = x - x_not
v_x = (x - x_not) / t
print(f"3-5-a: {v_x:.5f} m/s = v_x as it leaves edge")


## Part (b)
### Find the angle of velocity at landing
### This requires both v_x and v_y. 
### We can finc v_y from: v_y = v_not_y - g * t
### We can get angle from arctan(v_y/v_x)
v_y = v_not_y - g * t
inner = v_y / v_x
v_rad = math.atan(inner)
v_deg = math.degrees(v_rad)
print(f"3-5-b: {v_deg:.5f} degrees as it hits the ground")
