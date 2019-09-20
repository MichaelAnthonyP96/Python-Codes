import numpy as np
Ax = np.zeros(4)
#V : Non-zero values in A.
#IA: Row start pointers.
#JA: Column indices for the non-zero values.
#x : Vector to multiply A with.
V = np.array([5,8,3,6])
IA = np.array([0,0,2,3,4])
JA = np.array([0,1,2,1])
x = np.array([1,1,1,1])
for i in range(len(IA)-1):
    rowCount = IA[i+1] - IA[i]
    for j in range(IA[i], IA[i] + rowCount):
        Ax[i] = Ax[i] + x[JA[j]] * V[j]
print(Ax)
