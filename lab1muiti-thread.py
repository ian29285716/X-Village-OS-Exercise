import time
import threading
import numpy as np

def thread10_func(num1, num2):
    result10[num1] = np.matmul(matA10[num1], matB10)

def thread100_func(num1, num2):
    for i in range(10):
        number=i+num1*10
        result100[number] = np.matmul(matA100[number], matB100)

def thread1000_func(num1, num2):
    for i in range(100):
        number=i+num1*100
        result1000[number] = np.matmul(matA1000[number], matB1000)

def main10():
    print('=======10X10 multi-thread calculation=======')
    thread_num = 10
    threads = []

    start_time = time.time()

    for i in range(thread_num):
        thread = threading.Thread(target = thread10_func, args = (i, thread_num-1))
        threads.append(thread)
    for thread in threads:
            thread.start()
    for thread in threads:
            thread.join()

    end_time = time.time()
    print('')
    print('multi-thread')
    print('')
    print('Time elapsed:\t', end_time - start_time)
    print('Answer is correct:', np.all(np.matmul(matA10, matB10) == result10))

    start_time = time.time()

    for row in range(0, matA10.shape[0]):
        result10[row] = np.matmul(matA10[row], matB10)
    end_time = time.time()

    print('normal calculation')
    print('')
    print('Time elapsed:\t', end_time - start_time)
    print('Answer is correct:', np.all(np.matmul(matA10, matB10) == result10))

def main100():
    print('')
    print('======100X100 multi-thread calculation======',end='\n')
    thread_num = 10
    threads = []

    start_time = time.time()

    for i in range(thread_num):
        thread = threading.Thread(target = thread100_func, args = (i, thread_num-1))
        threads.append(thread)
    for thread in threads:
            thread.start()
    for thread in threads:
            thread.join()

    end_time = time.time()
    print('')
    print('multi-thread')
    print('')
    print('Time elapsed:\t', end_time - start_time)
    print('Answer is correct:', np.all(np.matmul(matA100, matB100) == result100))

    start_time = time.time()

    for row in range(0, matA100.shape[0]):
        result100[row] = np.matmul(matA100[row], matB100)
    end_time = time.time()

    print('normal calculation')
    print('')
    print('Time elapsed:\t', end_time - start_time)
    print('Answer is correct:', np.all(np.matmul(matA100, matB100) == result100))

def main1000():
    print('')
    print('=====1000X1000 multi-thread calculation=====')
    thread_num = 10
    threads = []

    start_time = time.time()

    for i in range(thread_num):
        thread = threading.Thread(target = thread1000_func, args = (i, thread_num-1))
        threads.append(thread)
    for thread in threads:
            thread.start()
    for thread in threads:
            thread.join()

    end_time = time.time()
    print('')
    print('multi-thread')
    print('')
    print('Time elapsed:\t', end_time - start_time)
    print('Answer is correct:', np.all(np.matmul(matA1000, matB1000) == result1000))

    start_time = time.time()

    for row in range(0, matA1000.shape[0]):
        result1000[row] = np.matmul(matA1000[row], matB1000)
    end_time = time.time()

    print('normal calculation')
    print('')
    print('Time elapsed:\t', end_time - start_time)
    print('Answer is correct:', np.all(np.matmul(matA1000, matB1000) == result1000))


matA10=np.random.randint(10, size = (10, 10))
matB10=np.random.randint(10, size = (10, 10))
result10=np.zeros( (10,10) )

matA100=np.random.randint(10, size = (100, 100))
matB100=np.random.randint(10, size = (100, 100))
result100=np.zeros( (100,100) )

matA1000=np.random.randint(10, size = (1000, 1000))
matB1000=np.random.randint(10, size = (1000, 1000))
result1000=np.zeros( (1000,1000) )

if __name__ == "__main__":
    main10()
    main100()
    main1000()
