import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.msgOrder = 0
        self.clientID = 1 
    
    def connect_tcp(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))

    def gets_new_height(self):
        msg = 'h'
        self.s.send(bytes(msg))
        msg = str(self.s.recv(1024)) 
        h = int(msg)
        return h
    
    def print_values(self):
        msg = 'values'
        self.s.send(bytes(msg))
        msg = str(self.s.recv(1024))
        

    def end_connection(self):
        msg = 'end'
        return msg
        
