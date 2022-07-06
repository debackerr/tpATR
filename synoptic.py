""" The following code emulates a synoptic program. It runs a process responsible for opening a socket 
    for tcp/ip communication with the plant(client) program. When first executed, it asks for the operator
    for a value as height reference for the controller thread and sends it to the plan. Later, while receiving 
    values for the in/out flow rates of the controlled tank, it writes every given information on a .txt file.
"""
import time, os.path
import multiprocessing as mp
from server import Server

def synoptic_process():
    HOST = "127.0.0.1"
    PORT = 51511
    server =  Server(HOST, PORT)
    address =  server.connect_tcp()
    print("new connection by: " + address)
    h_ref = input("\nplease set a rerence height - maximum 10m : ")
    while (int(h_ref) > 10):
        h_ref = input("\nplease set a valid reference - maximum 10m : ")
        if ( int(h_ref) <= 10):
            break

    server.send_msg(h_ref)

    while True:
        msg = server.recv(1024)

        if not msg:
            print("\n connection terminated")
            server.close()
            break

        else:
            print(str(msg))
            time.sleep(1)

            if (os.path.isfile("historiador.txt")):
                file = open("historiador.txt", 'a') #opens existing file 
            else:
                file = open("historiador.txt","x")  #creates a new file
                
            file.write(str(msg))
    

if __name__ == "__main__":
    synoptic = mp.Process(target=synoptic_process())