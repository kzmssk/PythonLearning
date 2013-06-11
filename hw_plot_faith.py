import numpy as np
import pylab as pyl
import os, os.path

data=np.loadtxt('faithful.txt')

x=data[:,0]
y=data[:,1]

pyl.scatter(x,y,color="red",s=2)
pyl.title('faithful.txt')
pyl.grid(True)

pyl.show()
