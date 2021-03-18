import numpy as np

"""a rather naive implementation of Cramer's rule using numpy"""
def solve(cf, ct):
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
