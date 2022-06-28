import socket, struct

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.msgOrder = 0
        self.clientID = 1 
    
    def connect_tcp(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))

    def set_new_height(self):
        msg = "new height"
        self.s.send(struct.pack(msg,len(msg), self.msgOrder))
        self.msgOrder += 1

        msg = struct.unpack('!4H1016s', self.s.recv(1024))
        msg.decode(ascii) 
        h = msg[0]
        return h
        
