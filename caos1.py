from pylab import *

def calc(r,x,n):
    values=[]
    f=lambda r,x:r*x*(1.0-x)
    for i in xrange(n):
        x=f(r,x)
        values.append(x)
    return values

n=100
x=0.4
for r in arange(2.8,4.0,0.001):
    plot([r for i in xrange(n-n//10)],calc(r,x,n)[n//10:],"b.",markersize=2)
axis([2.8,4.0,0.0,1.0])
xlabel(r"$r$",fontsize=20)
ylabel(r"$x$",fontsize=20)
show()
