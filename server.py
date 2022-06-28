
import socket, struct

class Server:

  def __init__(self, host, port):
    self.host = host
    self.port = port

  def connect_tcp(self):
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.s.bind((self.host, self.port))
    self.s.listen()
    print("waiting for new connections...\n")

  def receive(self):
    while True:
      conn, adress = self.s.accept()
      print("new connction: {}".format(str(adress)))
      msg = struct.unpack('!4H1016s', conn.recv(1024))
      if len(msg) != 0:
        msg = msg.decoce('ascii')
      else:
        print("ERROR!\n")
        self.s.close()
        

