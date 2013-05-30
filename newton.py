import math

def f(x):
    return x**3-x+1

def g(x):
    return 3*x**2-1

eps=1e-8
LIMIT=50

x=-2.0

for k in range(1,LIMIT):
    dx=x
    x=x-f(x)/g(x)
    if math.fabs(x-dx)<math.fabs(dx)*eps:
        print "x=%f" % x
        break

if k>LIMIT:
    print "error. it doesn't convergence."



