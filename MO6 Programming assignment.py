import multiprocessing
import random
from datetime import datetime
import time

def times():
    # Generates a random wait time
    wait_time = random.random()
    # Wait for the random amount of time
    time.sleep(wait_time)

     # Gets the current time and format it as a string
    time_now = datetime.now().strftime('%H:%M:%S') 
    # Prints a message indicating the name of the current process and the time it finished
    print(f'Process {multiprocessing.current_process().name} finished at {time_now}')

if __name__=='__main__':
    # Creates and starts three separate processes each running the times() function
    for i in range(3):
        # Creates a new Process object with a unique name and the times() function as the target
        process = multiprocessing.Process(target=times, name=f'Process {i}')
        # Starts the processes
        process.start()
