import mcp
import numpy as np
import matplotlib.pyplot as pl



#2.1
input("question 2.1")
x=np.array([1,2,5,-1,6])
M=mcp.matMC(x,2)
print(M)

#2.2
input("question 2.2/2.3")
x=np.array([-2,-1,0,1,2]); y=np.array([3/2,-1,1,5,17/2])
a,b=mcp.ajustMC(x,y,1)[0],mcp.ajustMC(x,y,1)[1]
print(f"coefficients ajustements :",mcp.ajustMC(x,y,1))

#2.3

n=int(input("donner degré :"))
mcp.traceMC(x,y,n)
   

#2.4
input("Question 2.4")
j=0
for n in range(1,5):
    j+=1
    pl.subplot(2,2,j)
    mcp.traceMC(x,y,n)
pl.subplots_adjust(hspace=0.5,wspace=0.3)
pl.show()
