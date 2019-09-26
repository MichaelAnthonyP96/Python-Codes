import numpy as np
import numpy.linalg as la
import scipy.optimize as opt

######## EXAMPLE FOR USING MINIMIZE_SCALAR ##############
# Define function
def f(alpha,x,s):
    return rosenbrock(x + alpha*s)
# Call routine - min now contains the minimum x for the function
#min = opt.minimize_scalar(f,args=(x,s)).alpha

#########################################################

def rosenbrock(x):
    x1 = x[0]
    x2 = x[1]
    return 100*(x2 - x1**2)**2 + (1-x1)**2

def gradient(x):
    # Returns gradient of rosenbrock function at x as numpy array
    x1 = x[0]
    x2 = x[1]
    grad = np.array([400*x1**3 - 400*x1*x2 + 2*x1 -2,
                      200*(x2-x1**2)])
    return grad

def hessian(x):
    x1 = x[0]
    x2 = x[1]
    # Returns hessian of rosenbrock function at x as numpy array
    hess = np.array([[1200*x1**2 - 400*x2 + 2, -400*x1],
                     [-400*x1, 200]])
    return hess

# INSERT NEWTON FUNCTION DEFINITION
def nm(x):
    for i in range(10):
        s = la.solve(hessian(x), -gradient(x))
        x = x + s
    return x
# INSERT STEEPEST DESCENT FUNCTION DEFINITION
def sd(x):
    for i in range(10):
        s = gradient(x)
        alpha = opt.minimize_scalar(f,args=(x,s)).x
        x = x + alpha*s
    return x
# DEFINE STARTING POINTS AND RETURN SOLUTIONS
start1 = np.array([-1.,1.])
nm1 = nm(start1)
sd1 = sd(start1)
start2 = np.array([0.,1.])
nm2 = nm(start2)
sd2 = sd(start2)
start3 = np.array([2.,1.])
nm3 = nm(start3)
sd3 = sd(start3)
