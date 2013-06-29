import numpy as np
import pylab as pyl

def angle(x,y):
    a=np.array([x,y])
    b=np.array([0,1])
    tmp=float(np.arccos(np.dot(a,b)/np.linalg.norm(a))*180/np.pi)
    if x>=0:
        return 180.+tmp
    else:
        return tmp
filename=raw_input('load data in data/ ?.txt ...')
data=np.loadtxt('data/'+filename+'.txt', delimiter=',')

x=data[:,0]
y=data[:,1]
p=data[:,2]

tmp_x=x[0]
tmp_y=y[0]

angles=[]

for i in range(0,x.size-1):
     if tmp_x!=x[i] or tmp_y!=y[i]:
         print "%d: %f, %f :: %f" % (i, x[i]-tmp_x, y[i]-tmp_y, angle(x[i]-tmp_x, y[i]-tmp_y)) 
         angles.append(angle(x[i]-tmp_x,y[i]-tmp_y))
         tmp_x=x[i]
         tmp_y=y[i]

pyl.clf()

pyl.hist(angles, bins=60)
pyl.xlim([0,360])
pyl.title(filename)
pyl.xlabel('degree')
pyl.ylabel('frequency')
pyl.savefig(filename+'.png')
