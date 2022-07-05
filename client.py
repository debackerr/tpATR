import socket
from sys import exit
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
    
    def send(self, h, qin, qout):
        msg = f"\n Qin: {qin}  m^3/s; h: {h} m; Qout: {qout}m^3/s"
        print(msg)
        self.s.send(bytes( msg, encoding = 'UTF-8'))
    
    def close(self):
        self.s.close()
