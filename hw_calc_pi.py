import numpy as np
import pylab as pyl

def wallis(n):
    my_pi=1
    for i in range(1,n+1):
        my_pi*=4*i**2/float(4*i**2-1)
    return float(my_pi*2)

x=np.arange(1,1000,10)
y=np.zeros(x.size)

j=0

for k in x:
   y[j]=wallis(j)
   j+=1

print y[x.size-1]

pyl.plot(x,y,label='wallis formula')

l=pyl.axhline(y=np.pi,color='r',label='pi')

pyl.title("wallis's formula",fontsize=20) 
pyl.xlabel('trials',fontsize=15)
pyl.ylabel('result',fontsize=15)

pyl.legend(loc=7)

pyl.show()
