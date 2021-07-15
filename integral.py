import math
import numpy

def f(x):
    return x ** 2

#riemann integration
def riemm(f, a, b, n):
    dx = (b - a) / n
    x = a
    area = 0
    for p in range(n):
        y = f(x)
        area += y * dx
        x += dx
    return area

#trapezoid integration, generally more accurate
def trapez(f, a, b, n):
    dx = (b - a) / n
    x = a
    area = 0
    for p in range(n):
        y0 = f(x)
        y1 = f(x + dx)
        area += (y0 + y1) * dx / 2
        x += dx
    return area
