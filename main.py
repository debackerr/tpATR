import process_thread, softPLC_thread, synoptic_process
import multiprocessing as mp


if __name__ == "__main__":
    tank = process_thread(1, "tank")
    control = softPLC_thread(2, "control")

    tank.start()
    control.start()

    threads = []
    threads.append(tank)
    threads.append(control)

    for t in threads:
        t.join()

    print("\n process ended")
    
    while True:
        synoptic =  mp.Process(target = synoptic_process)

