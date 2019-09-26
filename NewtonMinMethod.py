import numpy as np
x0 = 1
xnext = 0
xold = x0
count = 0

def fp(x):
    return 46*x -4
    
def fpp(x):
    return 46
    
while(np.abs(xnext - xold) > 10**-10):
    xnext = xold - fp(xold)/fpp(xold)
    count = count +1
    xold = xnext
    print(xnext)
print(count)
