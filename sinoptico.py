import time, os.path
import multiprocessing as mp
from server import Server

def synoptic_process():
    HOST = "127.0.0.1"
    PORT = 51511
    server =  Server(HOST, PORT)
    address =  server.connect_tcp()
    print("\n new connection by: " + address)

    while True:
        msg = server.recv(1024)

        # if not msg:
        #     print("\n connection terminated")
        #     server.close()
        #     break
        # else:
        print(str(msg))
        time.sleep(1)

        if (os.path.isfile("historiador.txt")):
            file = open("historiador.txt", 'a') #opens existing file 
        else:
            file = open("historiador.txt","x")  #creates a new file
            
        file.write(str(msg))

        
    
    

if __name__ == "__main__":
    synoptic = mp.Process(target=synoptic_process())