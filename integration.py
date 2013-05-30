import math
from decimal import Decimal

#print 'A,B ?'
a = 0
b = 2

n = 50
h = (b-a)/float(n)
x = a
s = 0.

def f(x):
    return math.sqrt(4-x**2)

for k in range(n):
    #print "%f, " % (x),
    x = x + h
    #print "%f, %f" % (x,h)
    if(x>2):
        print Decimal(x)
        x=2
    s = s + f(x)

sum= h*((f(a) + f(b))/2 + s)


print f(a),f(b)
print h
print '%f\n'%b
print '|sqrt(4 - x * x) = %f\n'%sum
print '%f\n'%a
