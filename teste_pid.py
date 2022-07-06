import numpy as np
import conical_tank
from simple_pid import PID
import matplotlib.pyplot as plt

global qin, h

qin = 20    #minimal qin
h0 = 5
cv = 0.7    #predefined Cv

h = conical_tank.rk4(qin, h0 )      
qout = cv * np.sqrt(h)

h = np.round(h,3)
qout = np.round(qout,3)


pid = PID(3, 7, 0.05, setpoint = 2)


armz = []
i = 0

while True:
    control = pid



