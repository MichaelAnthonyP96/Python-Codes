#f, the function to be integrated
#n, the number of nodes to be used in Gaussian quadrature
#tol, a tolerance used for stopping criteria
#I, the value of the integral on (0,1).

import numpy as np
import matplotlib.pyplot as pt

intv_ends = []

def Gauss(f,a,b):
    m = (a + b)/2
    samples, weights = np.polynomial.legendre.leggauss(n)
    bigSum = ((b-a)/2) * np.sum(weights * f( ( (b-a)*samples + a + b) /2) )
    leftSum = ((m-a)/2) * np.sum(weights * f( ( (m-a)*samples + a + m) /2) )
    rightSum = ((b-m)/2) * np.sum(weights * f( ( (b-m)*samples + m + b) /2) )
    if( (bigSum - (leftSum + rightSum)) < tol):
        intv_ends.append(b)
        return leftSum + rightSum
    else:
        intv_ends.append(m)
        return Gauss(f,a,m) + Gauss(f,m,b)

I = Gauss(f,0,1)
print(I)
intv_ends = np.asarray(intv_ends)
print(intv_ends)
pt.plot(np.linspace(0,1,2000),f(np.linspace(0,1,2000)),'b')
pt.plot(intv_ends, f(intv_ends), "o")

def f(x):
    return 1 + x**2

samples, weights = np.polynomial.legendre.leggauss(2)
print(samples, weights)

a = 0
b = 1
bigSum = ((b-a)/2) * np.sum(weights * f( ( (b-a)*samples + a + b) /2) )
print(bigSum)
