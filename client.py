""" The following code is a simple Cliente class for tcp/ip communication.
    Each method was implemented considering the particular application of the present work
"""

import socket
class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def connect_tcp(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        
    
    def recv(self, size):
        msg = self.s.recv(1024)
        return msg
    
    def send(self, msg):
        self.s.send(bytes( msg, encoding = 'UTF-8'))
    
    def close(self):
        self.s.close()
