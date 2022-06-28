# the following code simulates the dynamics of a conical tank, 
# with further implementation of the Runge-Kutta method 
# to approximate solutions of the Ordinary Differential Equations here envolved

import math

def f(Qin,h):
    R1= 1
    R0 = 2
    H = 5
    Cv = 0.7

    alpha = (R1-R0)/H
    Qout = Cv * math.sqrt(h)
    u = Qin
    
    return (- Qout/(math.pi * (R0 + alpha * h)) + (u / math.pi * (R0 + alpha * h)))


def rk4(x0,y0,xn,n):
    
    # Calculating step size
    s = (xn-x0)/n
    
    for i in range(n):
        k1 = s * (f(x0, y0))
        k2 = s * (f((x0+s/2), (y0+k1/2)))
        k3 = s * (f((x0+s/2), (y0+k2/2)))
        k4 = s * (f((x0+s), (y0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        yn = y0 + k
       
        y0 = yn
        x0 = x0+s