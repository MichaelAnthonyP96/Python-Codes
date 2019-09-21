#Denote the mass of each floor as m_i and the restoring force of each floor (Hooke's force) k_i. 
#The displacement of floor j is governed by the following differential equation:

#m_jx^″_j(t)=k_jx_(j−1)(t)−(k_j+k_(j+1))x_j(t)+k_(j+1)x_(j+1)(t)+m_jF(t)  <--- (*)

#Where F(t) is the forcing function. If we are at the first floor (j=1) we omit the first term 
#in the right hand side, since the foundation of the building has no displacement (relative to itself).
#If we are at the top floor (j=n), we omit x_(j+1) term since there is no floor above it. We also set 
#k_(j+1)=0 for the top floor, as there is no "restoring force" for the sky above.

#If we collect all these equations together, we can write the system of equations as:
#M_x^″(t)=Kx(t)+H(t)
#where M is a diagonal matrix with the masses of each floor mi placed along diagonal, K is a tridiagonal
#matrix that can be constructed from equation (∗) above, and H(t) is a column vector of the (m_j)'s,
#multiplied by the forcing function F(t).

#To use the methods you will learn in class and in the text, we require a first-order system of equations;
#this is second order. If we introduce an intermediate variable v(t)=x′(t), we can rewrite this as a 
#first-order system:
#x^′(t)=v(t)
#Mv^′(t)=Kx(t)+H(t)

#n: the number of floors
#w1: the first frequency of the forcing function.
#w2: the second frequency of the forcing function.

import numpy as np

w1 = 1
w2 = 2
n = 3
#define the forcing function
def force(w,t):
    return (-w**2)*0.05*np.cos(w*t)

def f(w,t,x):
    b[n:2*n] = force(w,t) * (10 * np.ones(n))
    return np.linalg.inv(LHS) @ RHS @ x + np.linalg.inv(LHS) @ b
#define the mass matrix, stiffness matrix and the time vector
M = np.diag(10 * np.ones(n) )
I = np.identity(n)
K = np.diag(-2000 * np.ones(n),0) + np.diag(1000 * np.ones(n-1),-1) + np.diag(1000 * np.ones(n-1),1)
K[-1][-1] = -1000
t = np.linspace(0,4,400)
#initialize the displacements
X1 = np.zeros((2*n,400))
X2 = np.zeros((2*n,400))
x1 = np.zeros((n,))
x2 = np.zeros((n,))
deltaT = t[1] - t[0]

#initialize the LHS and RHS matrices
LHS = np.zeros((2*n,2*n))
RHS = np.zeros((2*n,2*n))
b = np.zeros((2*n,))
#place the I and M matrices into the LHS
LHS[0:n,0:n] = I
LHS[n:2*n,n:2*n] = M
#place the RHS
RHS[n:2*n,0:n] = K
RHS[0:n,n:2*n] = I

#compute the initial 3 points using RK4
for g in range(0,2):
    K11 = deltaT * ( f(w1, t[g], X1[:,g]) )
    K12 = deltaT * ( f(w1, ( t[g] + ( deltaT/2 ) ),X1[:,g] + K11/2) )
    K13 = deltaT * ( f(w1, ( t[g] + ( deltaT/2 ) ),X1[:,g] + K12/2) )
    K14 = deltaT * ( f(w1, ( t[g] + ( deltaT ) ) ,X1[:,g] + K13) )
    #print(K11, K12, K13, K14)
    X1[:,g+1] = X1[:,g] + K11/6 + K12/3 + K13/3 + K14/6
    K21 = deltaT * ( f(w2, t[g], X2[:,n]) )
    K22 = deltaT * ( f(w2, ( t[g] + ( deltaT/2 ) ),X2[:,g] + K21/2 ) )
    K23 = deltaT * ( f(w2, ( t[g] + ( deltaT/2 ) ),X2[:,g] + K22/2 ) )
    K24 = deltaT * ( f(w2, ( t[g] + ( deltaT ) ),X2[:,g] ) + K23 )
    #print(K21, K22, K23, K24)
    X2[:,g+1] = X2[:,g] + K21/6 + K22/3 + K23/3 + K24/6
#print(X1[:,0:3])
#print(X2[:,0:3])

#compute the rest of the displacements
for h in range(3,400):
    X1[:,h] = X1[:,h-1] + (deltaT/12) * ( 23 * f(w1, t[h-1], X1[:,h-1]) - 16 * f(w1, t[h-2], X1[:,h-2]) + 5 * f(w1, t[h-3], X1[:,h-3]) )
    X2[:,h] = X2[:,h-1] + (deltaT/12) * ( 23 * f(w2, t[h-1], X2[:,h-1]) - 16 * f(w2, t[h-2], X2[:,h-2]) + 5 * f(w2, t[h-3], X2[:,h-3]) )
x1 = X1[:n,-1]
x2 = X2[:n,-1]

print(M)
print(K)
print(LHS)
print(RHS[0:n,0:n])
