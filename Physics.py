import cmath

def quadratic_roots(a: float, b:float, c:float):

    #calculate the descriminate
    d = abs((b**2)) - (4*a*c)

    # find two solutions
    sol1 = (-b - cmath.sqrt(d))/(2*a)
    sol2 = (-b + cmath.sqrt(d))/(2*a)
    ans = [sol1.real, sol2.real]
    return ans