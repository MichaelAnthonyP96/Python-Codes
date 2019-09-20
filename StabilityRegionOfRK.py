import numpy as np
import matplotlib.pyplot as plt

xcoords = np.linspace(0,-3,200)
ycoords = np.linspace(3,-3,200)

xvals, yvals = np.meshgrid(xcoords, ycoords)
# This line creates a 2D grid of values of λ
lambdas = xvals + 1j * yvals
deltaT = 1
epsilon = 10**-6
f_euler = np.ones((len(xcoords), len(ycoords)))
f_implicit_euler = np.ones((len(xcoords), len(ycoords)))
f_rk2 = np.ones((len(xcoords), len(ycoords)))
f_rk3 = np.ones((len(xcoords), len(ycoords)))

def g(y10):
    ret = np.zeros(np.shape(y10))
    for i in range(np.shape(y10)[0]):
        for j in range(np.shape(y10)[1]):
            if( np.linalg.norm(y10[i][j]) <= (1 + epsilon)):
                ret[i][j] = 1
            else:
                ret[i][j] = 0
    return ret

def f(lamb,y,t):
    return lamb * y

yE = 1
for k in range(10):
    f_euler = lambdas*f_euler + f_euler
    f_implicit_euler = f_implicit_euler/(1-lambdas)
    K21 = f(lambdas,f_rk2,1)
    K22 = f(lambdas,(f_rk2 + 1 * K21),1)
    f_rk2 = f_rk2 + (1/2 * (K21 + K22))
    K31 = f(lambdas,f_rk3,1)
    K32 = f(lambdas,(f_rk3 + (1/2) * K31),1)
    K33 = f(lambdas,(f_rk3 - K31 + (2 * K32)),1)
    f_rk3 = f_rk3 + (1/6) * (K31 + (4 * K32) + K33)

f_euler = g(f_euler)
f_implicit_euler = g(f_implicit_euler)
f_rk2 = g(f_rk2)
f_rk3 = g(f_rk3)
#plot the first figure of the Euler Method
plt.figure()
plt.contourf(xvals,yvals,f_euler)
plt.ylabel('Imaginary Lambda components')
plt.xlabel('Negative Real Lambda components')
plt.title('Stability Region for Euler Method')
plt.show()

#Plot the second figure of the backward Euler Method
plt.figure()
plt.contourf(xvals,yvals,f_implicit_euler)
plt.ylabel('Imaginary Lambda components')
plt.xlabel('Negative Real Lambda components')
plt.title('Stability Region for Implicit Euler Method')
plt.show()

#Plot the third figure of the RK2 method
plt.figure()
plt.contourf(xvals,yvals,f_rk2)
plt.ylabel('Imaginary Lambda components')
plt.xlabel('Negative Real Lambda components')
plt.title('Stability Region for RK2 method')
plt.show()

#Plot the fourth figure of the RK3 method
plt.figure()
plt.contourf(xvals,yvals,f_rk3)
plt.ylabel('Imaginary Lambda components')
plt.xlabel('Negative Real Lambda components')
plt.title('Stability Region for RK3 method')
plt.show()
