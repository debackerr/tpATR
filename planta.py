import multiprocessing as mp
import threading, time, math
from client import Client
from sys import exit

def tank():
    while True:
        pcs_timer.wait()
        sem.acquire()
        print("process_thread aqui" + str(time.process_time) + "\n")
        sem.release()
        

def plc():
    HOST = "127.0.0.1"
    PORT = 51511
    client = Client(HOST,PORT)
    client.connect_tcp()
    print("\n connected to synoptic")
    
    while True:
        plc_timer.wait()
        sem.acquire()
        print("softPLC aqui: rk4 \n")
        sem.release()

        client.send(h,qin,qout)
    

def timers():
    while True:
        pcs_timer.set()
        pcs_timer.clear()
        time.sleep(2)

        plc_timer.set()
        plc_timer.clear()
        time.sleep(1)
    

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
    process_thread = threading.Thread(target = tank)
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
    