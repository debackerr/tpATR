import multiprocessing as mp
import threading, time, math
from client import Client
from sys import exit

def tank(h,qin):
    while True:
        pcs_timer.wait()
        sem.acquire()
        h = h*20
        qin +=2
        sem.release()
        

def plc(h,qin):
    HOST = "127.0.0.1"
    PORT = 51511
    client = Client(HOST,PORT)
    client.connect_tcp()
    print("\n connected to synoptic")
    
    while True:
        plc_timer.wait()
        sem.acquire()
        h = h - 10
        qin = qin * 2
        sem.release()

        client.send(h,qin,qout)
    

def timers():
    while True:
        pcs_timer.set()
        pcs_timer.clear()
        time.sleep(0.05)

        plc_timer.set()
        plc_timer.clear()
        time.sleep(0.025)
    

if __name__ == "__main__":

    #process variables:
    global qin, h

    qin = 20 #minimal qin
    h = 5 #initial h_ref
    Cv = 0.7
    qout = int( Cv * math.sqrt(h)) 

    sem = threading.Semaphore()
    pcs_timer = threading.Event()
    plc_timer = threading.Event()
    
    timer_thread = threading.Thread(target = timers)
    process_thread = threading.Thread(target = tank,args = (h, qin) )
    softPLC_thread = threading.Thread(target=plc, args = (h, qin))

    threads = []
    
    threads.append(timer_thread)
    threads.append(process_thread)
    threads.append(softPLC_thread)

    timer_thread.start()
    process_thread.start()
    softPLC_thread.start()

    for t in threads:
        t.join()
    