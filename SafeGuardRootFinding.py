import numpy as np

x_star = 99.0

def f(x):
    global x_star

    return 2.0 / (1.0 + np.exp(-(x - x_star))) - 1.0

def df(x):
    global x_star

    return (2.0 * np.exp(x + x_star)) / (np.exp(x) + np.exp(x_star)) ** 2.0

left, right = np.array([-100.0, 100.0])
tol = 1.0e-8

a = left
b = right
x = np.zeros(1)
x[0] = a + (b-a)/2
print(x)

def newtonM(x0,f,df):
    x1 = x0 - (f(x0)/df(x0))
    return x1
    
def bisection(a,b):
    m = a + (b-a)/2
    if(np.sign(f(a)) == np.sign(f(m))):
        a = m
    else:
        b = m
    return (a, b)
X = newtonM(x[-1],f,df)
if((X <= b) and (X >= a)):
    x = np.append(x,X)
else:
    (a,b) = bisection(a,b)
    M = a + (b-a)/2
    x = np.append(x,M)
print(x)

while(np.abs((x[-1] - x[-2])) > tol):
    X = newtonM(x[-1],f,df)
    if((X <= b) and (X >= a)):
        x = np.append(x,X)
    else:
        (a,b) = bisection(a,b)
        M = a + (b-a)/2
        x = np.append(x,M)
