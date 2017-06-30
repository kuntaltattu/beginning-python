def integrate(l,u,n,f):
    dx = (u-l)/n
    area = 0
    x = l
    while (x <= u):
        area += f(x)*dx
        x += dx
    return area

print (integrate (0, 5.0, 10, lambda x: x**2))
