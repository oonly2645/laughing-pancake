import numpy as np
from scipy import optimize as opt
import math as math

def func(x):
    return x[0]**2 * x[1]**2

def gradient_optimizer(f,x0,eps,t,num_iter):
    for i in range(num_iter):
        grad = opt.approx_fprime(x0, f, 0.0001)
        print('grad',grad)
        if np.all( np.abs(grad) < eps ):            
            return x0
        else:
            x0 = x0 - t * grad
print(gradient_optimizer(func,np.array([1,1]),0.001,0.01,10000))




data = np.array([1,2,3])*np.array([ [1,10], [100, 1000], [10000, 100000] ])