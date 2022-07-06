""" The following code is a simple Server class for tcp/ip communication.
    Each method was implemented considering the particular application of the present work
"""

import socket
from codecs import decode

class Server:

    def __init__(self, host, port):
        self.host = host
        self.port = port


    def connect_tcp(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen(5)
        print("waiting for new connections...\n")
        con, address = self.s.accept()
        self.con = con
        return str(address)

    def send_msg(self,msg):
       self.con.send(bytes(msg, encoding = 'UTF-8'))


    def recv(self, size):
        msg = self.con.recv(size)
        return msg.decode()

    def close(self):
        self.con.close()