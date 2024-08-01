
import eqdiff as eqd
import matplotlib.pyplot as pl
from numpy import sin

#4a
fa=lambda t,x,y: -x
eqd.Euler(fa,0,40,1,0,10000)
pl.show()
#pl.savefig("Euler_4a.png")

#4b
fb=lambda t,x,y: -x-y*(x**2-1)
eqd.Euler(fb,0,30,1,0,10000)
pl.show()
#pl.savefig("Euler_4b.png")

#4c
fc=lambda t,x,y:-y/5+sin(x)
eqd.Euler(fc,0,30,1,0,10000)
pl.show()
#pl.savefig("Euler_4c.png")
#====================================


input("continue ... ")


#6a
pl.clf()

t0,T,n=0,30,500
Lc=[[0,-1],[-3,4],[3,3],[3,-2]]

eqd.EulerPhase(fb,t0,T,Lc,n)
pl.legend([str(Lc[i]) for i in range(len(Lc))])
pl.show()
#pl.savefig("Phase_6a.png")


#6b

Lc=[[0,1.5],[0,2.5],[0,4],[0,6],[0,7.5]]

eqd.EulerPhase(fc,t0,T,Lc,n)
pl.legend([str(Lc[i]) for i in range(len(Lc))])
pl.show()
#pl.savefig("Phase_6b.png")


