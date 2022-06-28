import process_thread, softPLC_thread, synoptic 

if __name__ == "__main__":
    tank = process_thread(1, "tank")
    control = softPLC_thread(2, "control")
    synoptic = synoptic(3,"synoptic")

    tank.process_thread()
    control.softPLC_thread()
    synoptic.synoptic_process()

    threads = []
    threads.append(tank)
    threads.append(control)
    threads.append(synoptic)

    for t in threads:
        t.join()
