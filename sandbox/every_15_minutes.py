import time

while True: # The main loop that keeps your program running forever
    start_time = time.time()
    seconds_to_wait = 5

    print("Getting the latest data, this might take awhile...")
    print("making purchases and offers")
    time.sleep(3)

    while time.time() - start_time < seconds_to_wait: # If it has been 5 seconds since we got the last data
        print('waiting....', end='\r')
