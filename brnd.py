import random
import math

x=0.
y=0.

def brnd(sig, m):
    global x
    global y
    r1=random.uniform(0,1)
    r2=random.uniform(0,1)
    x=sig*math.sqrt(-2*math.log(r1))*math.cos(2*3.14159*r2)+m
    y=sig*math.sqrt(-2*math.log(r1))*math.sin(2*3.14159*r2)+m

hist=[0]*100;

for i in range(0,1000):
    brnd(2.5,10.0)
    hist[int(x)]+=1
    hist[int(y)]+=1

for i in range(0,20):
    print "%d: I" % (i),
    for j in range(0,hist[i]/10):
        print "*",
    print "\n"

for i in range(100):
    print "%d, " % (hist[i]/10),

print "\n"

