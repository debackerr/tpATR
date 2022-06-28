import threading, time
from server import Server

class synoptic(threading.Thread):
    def __init__(self, threadID, name, ):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.nome = name
    
    def synoptic_process():
        
        HOST = "127.0.0.1"
        PORT = 51511

        server =  Server()
        server.__init__(HOST, PORT)
        server.connect_tcp()
        server.receive()

        
