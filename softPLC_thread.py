import threading, time
from client import Client

class Control (threading.Thread):
    def __init__(self, threadID, name, ):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.nome = name

    def softPLC_thread():
        HOST = "127.0.0.1"
        PORT = 51511

        client = Client()
        client.__init__(HOST, PORT)
        
        h = client.gets_new_height()
    
    