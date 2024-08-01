

import numpy as np
import matplotlib.pyplot as pl


#question 3
def Euler(f,t0,T,x0,xp0,n):
    h=T/n
    Vt=np.linspace(t0,t0+T,n+1)
    
    x=np.zeros(n+1); xp=np.zeros(n+1)
    x[0]=x0; xp[0]=xp0
    for i in range(n):
        x[i+1]=x[i]+h*xp[i]
        xp[i+1]=xp[i]+h*f(Vt[i],x[i],xp[i])
        
    pl.clf()    
    pl.subplot(2,1,1)
    pl.plot(Vt,x,'r')
    pl.subplot(2,1,2)
    pl.plot(x,xp,'b')
    #pl.show()
    

#======================================================


    
def EulerPhase(f,t0,T,Lc,n):
    h=T/n
    Vt=np.linspace(t0,t0+T,n+1)
    x=np.zeros(n+1); xp=np.zeros(n+1)
    pl.clf()
    for C in Lc:
        x[0]=C[0]; xp[0]=C[1]
        for i in range(n):
            x[i+1]=x[i]+h*xp[i]
            xp[i+1]=xp[i]+h*f(Vt[i],x[i],xp[i])
        
        #pl.clf()
        pl.plot(x,xp)
    
