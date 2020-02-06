#Jonathan Robinson for UNM CS 500 (Complex Adaptive Systems)
#Plot time series graph (Logistic Map)


from pylab import show, scatter, xlim, ylim, plot, xlabel, ylabel
import numpy

xVal = []
time = []
xNew = 0.2 #initialized value for X[0]

#Logisitic map function
def logMap(r,x):
    return r*x*(1-x)

#iterate through each time step, calculate X[t]
#r value can be changed (first param of logMap() function
for i in numpy.arange(0, 1000, 0.01):
    xNew = logMap(3.9, xNew)
    print(xNew)
    xVal.append(xNew)
    time.append(i)

#create graph
scatter(time, xVal, s = .2)
plot(time, xVal)
xlim(0.001, 10)
ylim(-0.1,1.1)
xlabel("Time")
ylabel("X[t]")
show()
