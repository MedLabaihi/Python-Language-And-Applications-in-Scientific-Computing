

import mcp
import matplotlib.pyplot as plt
import numpy.random as rd


def nuage(X,a,b,c):
    n=len(X)
    epsi=rd.randn(n)
    Y=a+b*X+c*epsi
    mcp.traceMC(X,Y,1)
    plt.show()
