import numpy as np
import pylab as pyl

N=1000

x=[]
y=[]

n=[]

filename=raw_input('filename? .txt:')

f=open("data/"+filename+".txt","w")

for i in range(N):
    n.append(float(0.0+i*2*np.pi/N))

for i in range(0,N):
    x.append(np.cos(n[i]))
    y.append(np.sin(n[i]))
    f.write("%f, %f \n" % (np.cos(n[i]), np.sin(n[i])))

f.close()

x.append(1)
y.append(0)

pyl.plot(x,y)
pyl.show()
