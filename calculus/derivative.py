
def derivative(f,x,h=0.00001):
    
    return (f(x+h)-f(x))/h

def f(x):
    return x**2
