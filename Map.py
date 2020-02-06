#Jonathan Robinson for UNM CS 500 (Complex Adaptive Systems)
#Plot bifercation graph (Logistic Map)
#Based on matlab code discussed in https://www.youtube.com/watch?v=_BvAkyuWhOI

from pylab import show, scatter, xlim, ylim
import numpy

#these will be used to store values for graph
xvals = []
yvals = []


#iterate over range 0-4, increment by .001 (decreaseing interval increases resolution of graph
# as well as computation time)
for beta in numpy.arange(0,9/10,0.001):
    print(beta)
    xold = 0.5
    #transient, itereate and update xnew value
    for i in range(1,5000,1):
        xnew = ((xold - (xold ** 2)) * beta)
        xold = xnew
    xss = xnew
    #iterate again, store beta and xnew values
    for i in range(1,5000,1):
        xnew = ((xold - (xold ** 2)) * beta)
        xold = xnew
        xvals.append(beta)
        yvals.append((xnew))
        print(xnew-xss)
        #if difference in values is very small, break
        if(abs(xnew - xss)<0.001):
            break

#create graph
scatter(xvals, yvals, s = .2)
xlim(0.01, 4.1)
ylim(-0.1,1.1)
show()


