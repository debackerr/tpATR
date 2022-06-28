import os, process_thread, logging

if __name__ == "__main__":
    tank = process_thread.tank(1, "tank")

    tank.start()

    threads = []
    threads.append(tank)

    for t in threads:
        t.join()