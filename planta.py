import multiprocessing as mp
import threading, time, math, conical_tank
from client import Client
from sys import exit


def tank():
    global h,qin
    while True:
        pcs_timer.wait()
        mutex.acquire()
        h = conical_tank.rk4(qin, h, 0.01)
        print(str(h))
        mutex.release()
        

def plc():
    global h,qin
    HOST = "127.0.0.1"
    PORT = 51511
    client = Client(HOST,PORT)
    client.connect_tcp()
    print("\n connected to synoptic")
    i = 0
    while True:
        plc_timer.wait()
        mutex.acquire()
        print("\n controlador " + str(i))
        h  += 1
        mutex.release()
        client.send(h,qin,qout)

    

def timers():
    while True:
        pcs_timer.set()
        pcs_timer.clear()
        time.sleep(1)

        plc_timer.set()
        plc_timer.clear()
        time.sleep(2)
    

if __name__ == "__main__":

    #process variables:
    global qin, h

    qin = 20 #minimal qin
    h = 5 #initial h_ref
    Cv = 0.7
    qout = int( Cv * math.sqrt(h)) 

    mutex = threading.Lock()

    pcs_timer = threading.Event()
    plc_timer = threading.Event()
    
    timer_thread = threading.Thread(target = timers)
    process_thread = threading.Thread(target = tank )
    softPLC_thread = threading.Thread(target=plc)

    threads = []
    
    threads.append(timer_thread)
    threads.append(process_thread)
    threads.append(softPLC_thread)

    timer_thread.start()
    process_thread.start()
    softPLC_thread.start()

    for t in threads:
        t.join()
    