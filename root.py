import math
import numpy as np

def f(x):
	return x**2 - x - 6

def g(x):
	return 0*x

"""See linsolv.py
Could've been made simpler because of the fact that the root finder is only trying to solve 2 variable linear equations"""
def twovar(cf, ct):
	coef = np.array(cf, np.float)
	const = np.array(ct, np.float)
	d = np.linalg.det(coef)
	if d != 0:
		unknowns = np.shape(coef)
		d_solutions = np.array([])
		i = 0 
		for x in range(unknowns[0]):
			a = np.ndarray(unknowns, np.float)
			for y in range(unknowns[0]):
				if y == i:
					a[y] = const
				else:
					a[y] = coef[:,y]
			d_solutions = np.append(d_solutions, np.linalg.det(a))
			i += 1
		return d_solutions / d
	else:
		raise ZeroDivisionError("Given coefficients have determinant 0")

def deriv(f, a, n):
	return (f(a + (10**-n)) - f(a - (10**-n)))/(2*(10**-n))


"""A variation of the Newton method for root finding"""
def newt(f, g, x_0, t):
	x = x_0
	m = deriv(g, x, 5)
	if m == 0:
		m = deriv(f, x, 5)
		y_1 = g(x)		
		x_1 = twovar([[0,1], [m, -1]], [y_1, m*x - f(x)])[0]
	else:
		y_1 = f(x)
		x_1 = twovar([[0,1], [m, -1]], [y_1, m*x - g(x)])[0]
		
	if math.fabs(x_1 - x_0) > t:
		x_1 = newt(f, g, x_1, t)
	return x_1

print(newt(f, g, 4, 0.00001))