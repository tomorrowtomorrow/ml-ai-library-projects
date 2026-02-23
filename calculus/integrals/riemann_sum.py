
def poly(x):
    return x
def reiman_left(n,f,a,b):
    dx=(b-a)/n
    area=0
    for i in range(n):
        x=a +i * dx
        area+=f(x)
    return area *dx
