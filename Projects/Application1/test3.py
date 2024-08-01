import mcp
#import numpy as np
import numpy.random as rd
import matplotlib.pyplot as pl



#3.1
input("Question 3.1")
X=rd.rand(50)
epsi=rd.randn(50)
print("epsi ",epsi)
Y=2-4*X+0.5*epsi
print("X= ",X)
print("Y= ",Y)


#3.2
input("Question 3.2")
mcp.traceMC(X,Y,1)
pl.show()


#3.3
input("Question 3.3")
k=0
for n in [10,100,1000,10000]:
    X=rd.rand(n)
    epsi=rd.randn(n)
    Y=2-4*X+0.5*epsi
    k=k+1
    pl.subplot(2,2,k)
    mcp.traceMC(X,Y,1)
    pl.title(f"$n={n:d}$")
pl.subplots_adjust(hspace=0.6)
pl.show()



input("Question 3.5")

import linamod

n=100
X=rd.rand(n)
#epsi=sp.randn(n)
#a,b,c=2,-4,0.5
a,b,c=eval(input("donner les coefficients du modele a,b,c : "))
#Y=a+b*X+c*epsi
linamod.nuage(X,a,b,c)

