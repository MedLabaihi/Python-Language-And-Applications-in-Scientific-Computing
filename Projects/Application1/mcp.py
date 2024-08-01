
import numpy as np
import matplotlib.pyplot as pl

#Partie 1
#=========


def fit(x,y,n):
    c=np.polyfit(x,y,n)
    return(c)


def traceFit(x,y,n):
    a=fit(x,y,n)
    print(a)
    p=np.poly1d(a)
    t=np.arange(min(x)-0.1,max(x)+0.1,0.01)
    s=p(t)
    pl.plot(x,y,'.k',t,s,'r')
    pl.title(f"ajustement de degré ${n:d}$")
    #pl.show()
    

    

#Partie 2
#=========
import numpy.linalg as la

#2.1
def matMC(x,n):
    m=len(x)
    x.shape=(m,1)
    A=np.ones((m,1))
    for j in range(1,n+1):
        A=np.hstack((A,x**j))
    return(A)

#2.2
def ajustMC(x,y,n):
    A=matMC(x,n)
    M=np.dot(A.T,A)
    sol=la.solve(M,np.dot(A.T,y))
    return(sol[-1::-1])

#2.3
def traceMC(x,y,n):
    a=ajustMC(x,y,n)
    print(a)
    t=np.arange(min(x)-0.01,max(x)+0.01,0.01)
    p=np.poly1d(a)
    pl.plot(x,y,'k.',t,p(t),'r')
    pl.title(f"ajustement de degré ${n:d}$")
    #pl.show()
