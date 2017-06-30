def derivative(dx,c,f):
	slope = (f(c+dx)-f(c))/dx
	return slope
print (derivative (0.01,5,lambda x: x**2))
