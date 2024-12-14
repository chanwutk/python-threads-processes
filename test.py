import multiprocessing as mp
from multiprocessing.pool import ThreadPool
import time
import threading


def io():
    # Simulate IO task (cpu waits for IO to complete)
    time.sleep(5)


def cpu_task():
    # Simulate CPU intensive task (cpu needs to constantly compute throughout the task)
    s = 0
    for i in range(500000000):
        s += 1
    print(s)


def main():

    print("IO tasks with 10 processes / threads")
    start = time.time()
    with mp.Pool(10) as p:
        p.apply(io)
    print("Time taken for IO task with multiprocessing: ", time.time() - start)
    
    start = time.time()
    with ThreadPool(10) as p:
        p.apply(io)
    print("Time taken for IO task with threading: ", time.time() - start)
    
    
    print("CPU-intensive tasks with 10 processes / threads")
    start = time.time()
    with mp.Pool(10) as p:
        p.apply(cpu_task)
    print("Time taken for CPU task with multiprocessing: ", time.time() - start)
    
    start = time.time()
    with ThreadPool(10) as p:
        p.apply(cpu_task)
    print("Time taken for CPU task with threading: ", time.time() - start)


if __name__ == "__main__":
    main()
