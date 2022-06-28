from server import Server

def synoptic_process():
    HOST = "127.0.0.1"
    PORT = 51511
    server =  Server(HOST, PORT)
    server.connect_tcp()
    server.receive()
        

        
