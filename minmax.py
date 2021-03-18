import math
#not stable :(

def f(x):
	return x**3 + 3*x**2 - x - 5

def deriv(f, a, n):
	return (f(a + (10**-n)) - f(a - (10**-n)))/(2*(10**-n))

def minmax(f, x_0, t):
	y = f(x_0)
	m_0 = deriv(f, x_0, 5)
	x_1 = x_0 + m_0/y
	m_1 = deriv(f, x_1, 5)
	if math.fabs(m_1 - m_0) > t:
		x_1 = minmax(f, x_1, t)
	return x_1

print(minmax(f, -2, 0.00001))