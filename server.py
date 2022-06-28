import socket

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
      msg =  str(conn.recv(1024))

      if len(msg) != 0:
        self.handle(msg)         
      else:
        print("ERROR!\n")
        self.s.close()
        
  def handle(self,msg):
    if (msg == 'h'):
      msg = self.set_new_height()
    elif ( msg == 'values'):
      print("%s",msg)
      msg = "ok"
    else:
      print("\n unknown message")
      msg = "error"
    
    self.s.send(bytes(msg))

  
  def set_new_height(self):
    h = input("\n set reference high: \n h = ")
    if (int(h) > 10):
      print("\n please, choose h < 10 m")
      self.set_new_height()
    else :
      print("\n new height set as %s m", h)
    return h


    

