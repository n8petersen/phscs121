import math
import cmath


# Problem 3-4
x = 25.1 # Changing Variable
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