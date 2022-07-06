""" The following code runs 4 threads:
        1) process_thread: emulates the dynamics of the conical tank
"""

import threading, time, math, conical_tank
import numpy as np
from simple_pid import PID
from client import Client
from sys import exit

SIMULATION_TIME = 20.0    
# defines the execution time of the simulation - in seconds

beginning_time = time.time() 
# gets initial time

def tank():
    global h,qin
    global end_pcs
    t =  beginning_time

    while ( t <  beginning_time + SIMULATION_TIME):
        t = time.time()        
        pcs_timer.wait()
        # awaits for the timer to be set

        mutex.acquire()
        h = conical_tank.rk4(qin, h)
        h = np.round(h,3)
        # runge-kutta method returns new value of h
        mutex.release()

    end_pcs = bool(True)


        

def plc():
    global h,qin
    global end_pcs
    t =  beginning_time
    
    HOST = "127.0.0.1"  
    PORT = 51511
    client = Client(HOST,PORT)  
    client.connect_tcp()
    # creating new socket for tcp/ip communication

    print("\n connected to synoptic")
    h_ref = int(client.recv(1024))

    print("\n new height reference set as " + str(h_ref) + " m")
    print("\n starting controll process...")
    pid = PID(3, 9, 0.05, setpoint = h_ref)

    while ( t <  beginning_time + SIMULATION_TIME):
        t = time.time()

        plc_timer.wait()
        # awaits for the timer to be set
        mutex.acquire()
        # pid controllers sets new h
        qin = pid(h)
        qin = np.round(qin,3)

        qout =  Cv * math.sqrt(h)
        qout = np.round(qout,3)
        # gets qout value for new h
        mutex.release()

        msg = f"\n Qin: {qin}  m^3/s; h: {h} m; Qout: {qout}m^3/s"
        client.send(msg)
        # sends new values to the synoptic_process via socket
   
    client.close()
    end_pcs = bool(True)

def timers():
    while (not ( end_pcs and end_plc)):

        pcs_timer.set()
        pcs_timer.clear()
        time.sleep(0.05)
        # enables the process_thread every 50ms

        plc_timer.set()
        plc_timer.clear()
        time.sleep(0.025)
    # enables the softcPLC_thread every 25ms
    
    print("\n simulation ended")
    exit()

if __name__ == "__main__":
    global end_pcs, end_plc

    end_plc = bool(False)
    end_pcs = bool(False)   

    #process variables:
    global qin, h
    qin = 20    # initial flow rate
    h = 0       #initial height
    Cv = 0.7    #predefined Cv  

    mutex = threading.Lock()    
    # mutex for restricting access to global variables - 1 thread at a time

    pcs_timer = threading.Event()
    plc_timer = threading.Event()
    # timers used to set each thread frequency

    timer_thread = threading.Thread(target = timers, daemon = True)    # sets timers 
    process_thread = threading.Thread(target = tank, daemon = True )   # tank thread
    softPLC_thread = threading.Thread(target = plc, daemon = True)     # controller thread

    timer_thread.start()
    process_thread.start()
    softPLC_thread.start()

    threads = []    # array of created threads
    
    threads.append(timer_thread)
    threads.append(process_thread)
    threads.append(softPLC_thread)


    for t in threads:
        t.join()
    
    