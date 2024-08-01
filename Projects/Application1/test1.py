#Partie1
import mcp
import numpy as np


#1
x=np.arange(-2,3)
y=np.array([1.5,-1,1,5,8.5])
print("coefficients ajustement lineaire : ",mcp.fit(x,y,1))

input("continue ...")
#2
n=int(input("saisir degré : "))
mcp.traceFit(x,y,n)

