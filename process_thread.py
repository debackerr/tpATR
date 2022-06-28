import threading, time, conical_tank

class process_thread (threading.Thread):          
    def __init__(self, threadID, name, ):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.nome = name

    def run(self):
        qin = 20  #water rate when pumped into the tank
        h =   10  #tank current level
        conical_tank.rk4(qin, h, 0.5, 0.2)
        time.sleep(0.05) #sleeps for 50ms
