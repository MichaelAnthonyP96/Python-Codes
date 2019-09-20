import numpy as np
#backward subsitution Ux = b
U = np.array([[1,3,5],[0,3,4],[0,0,6]])
print(U)
b = np.array([1,5,6])
x = np.linalg.solve(U,b)
#print(x)
X = np.zeros(U.shape[0])
for j in range(U.shape[0]-1,-1,-1):
    if (U[j,j] == 0):
        break
    X[j] = b[j]/U[j,j]
    for i in range(0,j):
        b[i] = b[i] - U[i,j]*X[j]
    #print(X)
