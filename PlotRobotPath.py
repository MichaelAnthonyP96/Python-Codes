import scipy.optimize as sopt
import numpy as np
import matplotlib.pyplot as pt

x = init_path
c2 = 1
s = 1

def f(s,x,grad):
    return obj(x + s*grad,c1,c2)

for i in range(400):
    c1 = 1000/(100+i)
    grad = dobj(x,c1,c2)
    step = sopt.golden(f,args=(x,grad))
    x = x + grad * step
    if(i == 9):
        path10 = x
    if(i == 24):
        path25 = x
    if(i == 49):
        path50 = x
    if(i == 99):
        path100 = x
    if(i == 199):
        path200 = x
final_path = x

#Draw the canvas
pt.figure(figsize=(8,8))
pt.plot(init_path[:,0], init_path[:,1], label="Initial")
pt.plot(path10[:,0],path10[:,1], label='Path after 10 iterations')
pt.plot(path25[:,0],path25[:,1], label='Path after 25 iterations')
pt.plot(path50[:,0],path50[:,1], label='Path after 50 iterations')
pt.plot(path100[:,0],path100[:,1], label='Path after 100 iterations')
pt.plot(path200[:,0],path200[:,1], label='Path after 200 iterations')

#plot the obstacles
pt.plot(obstacles[:,0], obstacles[:,1], "o", markersize=5, label="Obstacles")
pt.legend(loc="best")
