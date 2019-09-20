#optimizing the path of a robot around obstacles using steepest decent
#c1 and c2 are "weights" (constants) that determine the effect of each term on the value of F(xi).
#c1 controls the 'loss' the objective function suffers for getting close to the obstacles.
#c2 controls the 'loss' the objective function suffers for having very long line segments.
#k is the number of obstacles your robot must avoid.
#given an initial path matrix, X, comprised of n+1 vectors (each with 2 coordinates) x0,x1,x2,x3...xn. 
#The start and end points of your path are fixed, and are given by x0 and xn
#Given certain point obstacles (vectors with 2 coordinates), ri, in the obstacle matrix  R

Adding ϵ in the denominator prevents division by zero
import numpy as np
import numpy.linalg as npla

m = P.shape[0]
n = P.shape[1]
k = obstacles.shape[0]
G = np.zeros(P.shape)

#sum over all the paths
for i in range(m):
    #sum over all the points in the path
    for h in range(1,n-1):
        #sum over all the obstacles
        sum = 0
        for j in range(k):
            sum = sum + (2 * (P[i][h] - obstacles[j]) / (eps + (npla.norm((P[i][h] - obstacles[j]),2))**2)**2)
        G[i][h] = -c1 * sum + 2*c2*((P[i][h] - P[i][h-1]) - (P[i][h+1] - P[i][h]))
    
print(G)
