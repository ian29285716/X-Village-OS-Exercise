import threading
import queue
import os
import random,time

buffer_size = 5

lock = threading.Lock()
queue = queue.Queue(15)
file_count=0

def producer(top_dir, queue_buffer):
    # Search sub-dir in top_dir and put them in queue

    if os.path.isdir(top_dir)==True:
        queue_buffer.put(top_dir)
        time.sleep(0.01)
        listfile=os.listdir(top_dir)
        number=len(listfile)
        for i in range(0,number):
            subfile=os.path.join(top_dir,listfile[i])
            producer(subfile,queue_buffer)
            
    else:
        return None


def consumer(queue_buffer):
    # search file in directory
    lock.acquire()
    while not queue_buffer.empty():
        filelocation=queue_buffer.get()
        time.sleep(0.1)
        if filelocation!='./testdata':
            global file_count
            file_count-=1
            number=len(os.listdir(filelocation))
            file_count+=number
        else:
            number=len(os.listdir(filelocation))
            file_count+=number
    lock.release()

def main():
    producer_thread = threading.Thread(target = producer, args = ('./testdata', queue))

    consumer_count = 20
    consumers = []
    for i in range(consumer_count):
        consumers.append(threading.Thread(target = consumer, args = (queue,)))

    producer_thread.start()
    for c in consumers:
        c.start()

    producer_thread.join()
    for c in consumers:
        c.join()

    print(file_count, 'files found.')

if __name__ == "__main__":
    main()