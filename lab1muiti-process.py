import time
import threading
import numpy as np
import multiprocessing
import json

def thread10_func(process_no,result_queue):
    n={'number' : process_no,'np':np.matmul(matA10[process_no], matB10)}
    result_queue.put(n)

def thread100_func(process_no,result_queue):
    for i in range(10):
        number=i+process_no*10
        n={'number' : process_no,'np':np.matmul(matA100[process_no], matB100)}
        result_queue.put(n)

def thread1000_func(process_no,result_queue):
    for i in range(100):
        number=i+process_no*100
        n={'number' : process_no,'np':np.matmul(matA1000[process_no], matB1000)}
        result_queue.put(n)

def main10():
    print('')
    print('=======10X10 multi-process calculation=======')
    start_time = time.time()

    for row in range(0, matA10.shape[0]):
        result10[row] = np.matmul(matA10[row], matB10)
    end_time = time.time()
    print('')
    print('normal calculation')
    print('')
    print('Time elapsed:\t', end_time - start_time)
    print('Answer is correct:', np.all(np.matmul(matA10, matB10) == result10))

    result_queue= multiprocessing.Manager().Queue()
    processes =10
    jobs = []

    start_time = time.time()
    for i in range(processes):
        process = multiprocessing.Process(target = thread10_func, args = (i,result_queue))
        jobs.append(process)

    for process in jobs:
        process.start() 

    for process in jobs:
        process.join()

    while not result_queue.empty():
        n=result_queue.get()
        mumber=n['number']
        result10[mumber]=n['np']

    end_time = time.time()
    print('multi-process')
    print('')
    print('Time elapsed:\t', end_time - start_time)
    print('Answer is correct:', np.all(np.matmul(matA10, matB10) == result10))

def main100():
    print('')
    print('======100X100 multi-process calculation======')
    start_time = time.time()

    for row in range(0, matA100.shape[0]):
        result100[row] = np.matmul(matA100[row], matB100)
    end_time = time.time()
    print('')
    print('normal calculation')
    print('')
    print('Time elapsed:\t', end_time - start_time)
    print('Answer is correct:', np.all(np.matmul(matA100, matB100) == result100))

    result_queue= multiprocessing.Manager().Queue()
    processes =10
    jobs = []

    start_time = time.time()
    for i in range(processes):
        process = multiprocessing.Process(target = thread100_func, args = (i,result_queue))
        jobs.append(process)

    for process in jobs:
        process.start() 

    for process in jobs:
        process.join()

    while not result_queue.empty():
        n=result_queue.get()
        mumber=n['number']
        result100[mumber]=n['np']

    end_time = time.time()
    print('multi-process')
    print('')
    print('Time elapsed:\t', end_time - start_time)
    print('Answer is correct:', np.all(np.matmul(matA100, matB100) == result100))

def main1000():
    print('')
    print('=====1000X1000 multi-process calculation=====')
    start_time = time.time()

    for row in range(0, matA1000.shape[0]):
        result1000[row] = np.matmul(matA1000[row], matB1000)
    end_time = time.time()
    print('')
    print('normal calculation')
    print('')
    print('Time elapsed:\t', end_time - start_time)
    print('Answer is correct:', np.all(np.matmul(matA1000, matB1000) == result1000))

    result_queue= multiprocessing.Manager().Queue()
    processes =10
    jobs = []

    start_time = time.time()
    for i in range(processes):
        process = multiprocessing.Process(target = thread1000_func, args = (i,result_queue))
        jobs.append(process)

    for process in jobs:
        process.start() 

    for process in jobs:
        process.join()

    while not result_queue.empty():
        n=result_queue.get()
        mumber=n['number']
        result1000[mumber]=n['np']

    end_time = time.time()
    print('multi-process')
    print('')
    print('Time elapsed:\t', end_time - start_time)
    print('Answer is correct:', np.all(np.matmul(matA1000, matB1000) == result1000))

with open('matA10.json', 'r') as f:
    matA10=np.array(json.load(f))

with open('matB10.json', 'r') as f:
    matB10=np.array(json.load(f))

result10=np.zeros( (10,10))

with open('matA100.json', 'r') as f:
    matA100=np.array(json.load(f))

with open('matB100.json', 'r') as f:
    matB100=np.array(json.load(f))

result100=np.zeros( (100,100))

with open('matA1000.json', 'r') as f:
    matA1000=np.array(json.load(f))


with open('matB1000.json', 'r') as f:
    matB1000=np.array(json.load(f))

result1000=np.zeros( (1000,1000))

if __name__ == "__main__":
    main10()
    main100()
    main1000()

