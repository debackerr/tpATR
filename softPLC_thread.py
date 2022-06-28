import threading, time

from client import Client

class softPLC_thread (threading.Thread):
     
    def __init__(self, threadID, name, ):
        self.threadID = threadID
        self.nome = name

    def run(self):
        HOST = "127.0.0.1"
        PORT = 51511       

        client = Client(HOST,PORT)
        client.connect_tcp()

        while True:
            h_ref = client.gets_new_height()
            

        

        




    