""" the following code simulates the dynamics of a conical tank, 
    with further implementation of the Runge-Kutta method 
    to approximate solutions of the Ordinary Differential Equations here envolved 
    """

import math

def f(Qin,h):
    R1= 1
    R0 = 2
    H = 10
    Cv = 0.7

    alpha = (R1-R0)/H
    Qout = Cv * math.sqrt(h)
    u = Qin
    
    return (- Qout/(math.pi * (R0 + alpha * h)) + (u / math.pi * (R0 + alpha * h)))


def rk4(x0,y0,step):    
    y = y0
    k1 = step * f(x0, y)
    k2 = step * f(x0 + 0.5 * step, y + 0.5 * k1)
    k3 = step * f(x0 + 0.5 * step, y + 0.5 * k2)
    k4 = step * f(x0 + step, y + k3)

    y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    return y