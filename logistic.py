# DATE: 9/AGOSTO/2016 
#
# This code will solve the logistic map problem 
#
# Author: Introduction to the scientific computing Class

import numpy 
import matplotlib.pyplot as plt


x0=0.1
r=0.9 
Nmax=10

n = numpy.zeros(Nmax + 1)
x = numpy.zeros(Nmax + 1)

print x0
for i in range(0,Nmax):	
	y = r * x0 * (1 - x0)
	x0=y
	n[i]=i
	x[i]=y


        
plt.plot(n,x)
plt.show()
	
	
