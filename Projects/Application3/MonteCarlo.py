import numpy as np
import matplotlib.pyplot as plt
from numpy.random import rand


#1.
n=200
XY=rand(n,2)
print(XY)
input("Taper Enter pour continuer")


#2.
#prop=mean(XY[:,0]**2+XY[:,1]**2<1)
D=XY[XY[:,0]**2+XY[:,1]**2<1]

prop=len(D)/n
PI=4*prop
print(f"Approximation de pi par {n} simulations : {PI:.6f}")


input("Taper Enter pour continuer")

#3.
M=10; n=200
print("les approximations  sont :")
print("===============================")
for j in range(M):
    XY=rand(n,2)
    #prop=mean(XY_mat[:,0]**2+XY_mat[:,1]**2<1)
    D=XY[XY[:,0]**2+XY[:,1]**2<1]
    prop=len(D)/n
    PI=4*prop
    diff=np.pi-PI
    print(f"{n:d}\t{PI:f}\t{diff:f}")
    n=2*n

input("Taper Enter pour continuer")


#4.
n=200
XY=rand(n,2)
plt.axes(aspect='equal')
plt.plot(XY[:,0],XY[:,1],'ko')
t=np.linspace(0,np.pi/2,100)
x=np.cos(t);y=np.sin(t)
plt.plot(x,y,'r',lw=3)
plt.xlabel('X'); plt.ylabel('Y')
plt.show()
#plt.savefig("mcFig1.png")


input("Taper Enter pour continuer")

#5.
plt.clf()
pp=XY[XY[:,0]**2+XY[:,1]**2<1]
plt.axes(aspect='equal')
plt.plot(x,y,'r')
plt.plot(pp[:,0],pp[:,1],'go')
#show()
plt.savefig("mcFig2.png")


input("Taper Enter pour conti")



#6
plt.clf()

n=[200,500,1000,2000]
j=1
for k in n:
    XY=rand(k,2)
    plt.subplot(2,2,j)
    pp=XY[XY[:,0]**2+XY[:,1]**2<1]
    plt.plot(x,y,'r')
    plt.plot(pp[:,1],pp[:,0],'go')
    plt.title(r'$n=$%d'%k)
    j=j+1
plt.subplots_adjust(hspace=0.8,wspace=0.8)
plt.show()


