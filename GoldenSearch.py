import numpy as np
import numpy as np

a = a_start = -10
b = b_start = 10

def f(x):
    return x**2 + 10*np.sin(x)

tau = (np.sqrt(5) - 1)/2
m1 = a + (1-tau)*(b-a)
f1 = f(m1)
m2 = a + tau*(b-a)
f2 = f(m2)
brackets = [[a,m1,m2,b]]
while((b-a) > 10**-5):
    if(f1 > f2):
        a = m1
        m1 = m2
        f1 = f2
        m2 = a + tau*(b-a)
        f2 = f(m2)
    else:
        b = m2
        m2 = m1
        f2 = f1
        m1 = a + (1-tau)*(b-a)
        f1 = f(m1)
    brackets.append([a, m1, m2, b])
 
# plotting code below
import matplotlib.pyplot as pt
x = np.linspace(-10, 10)
pt.plot(x, f(x))

brackets = np.array(brackets)
for i in range(4):
    pt.plot(brackets[:, i], 3*np.arange(len(brackets)), "o-")
    pt.show()
    
