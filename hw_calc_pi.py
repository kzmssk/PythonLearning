from pylab import * 

def wallis(n):
    my_pi=1
    for i in range(1,n+1):
        my_pi*=4*i**2/float(4*i**2-1)
    return float(my_pi*2)

x=arange(1,1000,10)
y=zeros(x.size)

j=0

for k in x:
   y[j]=wallis(j)
   j+=1

print y[x.size-1]
plot(x,y,label='wallis formula')
l=plt.axhline(y=pi,color='r',label='pi')

title("wallis's formula",fontsize=20) 
xlabel('times',fontsize=15)
ylabel('result',fontsize=15)

legend(loc=7)
show()
