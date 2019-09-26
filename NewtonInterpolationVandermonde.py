import numpy as np
x = np.array([1,2,3])

V = np.zeros((len(x),len(x)))

def newTonBasis(a, X):
    sum = 1
    for k in range(len(X)):
        sum = sum * (a-X[k])
        print(sum)
    return sum

for i in range (len(x)):
    for j in range(i+1):
        V[i][j] = newTonBasis(x[i],x[0:j])

print(V)
