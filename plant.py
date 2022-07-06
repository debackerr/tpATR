import threading, time,  conical_tank
import numpy as np
from simple_pid import PID
from client import Client
from sys import exit
from simple_pid import PID

SIMULATION_TIME = 10.0    
# defines the execution time of the simulation - in seconds

beginning_time = time.time() 
# gets initial time of the simulation - in seconds

def tank():
    global h, qout
    global end_pcs
    t =  beginning_time

    while ( t <  beginning_time + SIMULATION_TIME):
        t = time.time()        
        pcs_timer.wait()
        # awaits for the timer to be set

        mutex.acquire()
        h, qout = conical_tank.tank_dynamic(qin,h)
        # runge-kutta method returns new value of h
        # the tank_dynamic funciton returns the value of qout

        mutex.release()

    end_pcs = bool(True)        

def plc():
    global h,qin
    global end_plc
    t =  beginning_time
    
    HOST = "127.0.0.1"  
    PORT = 51511
    client = Client(HOST,PORT)  
    client.connect_tcp()
    # creating new socket for tcp/ip communication

    print("\n connected to synoptic")
    h_ref = int(client.recv(1024))
    # gets height reference from the synoptic_process

    print("\n new height reference set as " + str(h_ref) + " m")
    print("\n turning on system...")
    print("\n starting controll process...")
    pid = PID(10, 1, 0.05, setpoint = h_ref)
    # PID controller from simple_pid library

    while ( t <  beginning_time + SIMULATION_TIME):
        t = time.time()

        plc_timer.wait()
        # awaits for the timer to be set

        mutex.acquire()
        # pid controllers sets new h
        qin = pid(h)
        qin = np.round(qin,3)
        qin = abs(qin)
        # gets qout value for new h
        mutex.release()

        msg = f"\n Qin: {qin}  m^3/s; h: {h} m; Qout: {qout}m^3/s"
        client.send(msg)
        # sends new values to the synoptic_process via socket
   
    client.close()
    # closes socket
    end_plc = bool(True)
    

def timers():
    global end_pcs, end_plc
    end_timer = bool(False)
    while (not ( end_pcs and end_plc)):
    # waits for the end of the simulation

        pcs_timer.set()
        pcs_timer.clear()
        time.sleep(0.05)
        # enables the process_thread every 50ms

        plc_timer.set()
        plc_timer.clear()
        time.sleep(0.025)
        # enables the softcPLC_thread every 25ms
    
    print("\n simulation ended")
    exit(0)

if __name__ == "__main__":
    global end_pcs, end_plc

    end_plc = bool(False)
    end_pcs = bool(False)   

    #process variables:
    global qin, h
    qin = 0 # empty tank
    h, qout = conical_tank.tank_dynamic(qin,0)  #initial conditions

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
