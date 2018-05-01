from threading import Thread, Lock, Condition
import time

#
# Producer and consumer using Lock
#


class Producer(Thread):

    def __init__(self, resource_list, lock):
        Thread.__init__(self)
        self.resource_list = resource_list
        self.lock = lock

    def run(self):
        for i in xrange(6):
            self.lock.acquire()
            self.resource_list.insert(0, i)
            print 'Produced: %d' % i
            self.lock.release()
            #
            #
            # The above four lines can be re-written as
            # follows with the help of lock object's context manager
            #
            # with self.lock:
            #     self.resource_list.insert(0, i)
            #     print 'Produced: %d' % i
            time.sleep(0.2)
        # Time to exit
        self.lock.acquire()
        self.resource_list.insert(0, None)
        self.lock.release()


class Consumer(Thread):

    def __init__(self, resource_list, lock):
        Thread.__init__(self)
        self.resource_list = resource_list
        self.lock = lock

    def run(self):
        while True:
            self.lock.acquire()
            if len(self.resource_list):
                i = self.resource_list.pop()
                if i is None:
                    print 'Consumer exiting'
                    break
                print 'Consumed: %d' % i
            else:
                print 'Consumed Nothing'
            self.lock.release()
            time.sleep(0.2)


def main_lock():
    print '\n\nProd_cons using lock'
    lock = Lock()
    shared_list = []

    p_thread = Producer(shared_list, lock)
    c_thread = Consumer(shared_list, lock)

    t1 = time.time()
    p_thread.start()
    c_thread.start()

    p_thread.join()
    c_thread.join()

    print 'total time = %s' % str(time.time() - t1)
    #
    # The above code might produce something
    # like follows.
    #
    # <- This shows consumer sometime unnecessarily acquires lock ,
    # after realizing that there is no item to consume,
    # releases the lock and goes to sleep
    #
    # Produced: 0
    # Consumed: 0
    # Consumed Nothing  <-
    # Produced: 1
    # Produced: 2
    # Consumed: 1
    # Produced: 3
    # Consumed: 2
    # Produced: 4
    # Consumed: 3
    # Consumed: 4
    # Produced: 5
    # Consumed: 5
    # Consumer exiting
    # total time = 1.42084598541


#
# Producer and consumer using Condition
#


class Producer_Cond(Thread):

    def __init__(self, resource_list, condition):
        Thread.__init__(self)
        self.resource_list = resource_list
        self.condition = condition

    def run(self):
        for i in xrange(6):
            self.condition.acquire()
            self.resource_list.insert(0, i)
            print 'Produced: %d' % i
            self.condition.notify()
            self.condition.release()
            time.sleep(0.2)

        # Time to exit
        self.condition.acquire()
        self.resource_list.insert(0, None)
        self.condition.notify()

        self.condition.release()


class Consumer_Cond(Thread):

    def __init__(self, resource_list, condition):
        Thread.__init__(self)
        self.resource_list = resource_list
        self.condition = condition

    def run(self):
        #
        # https://www.cs.cmu.edu/afs/cs/academic/class/15492-f07/www/pthreads.html
        # "A condition variable must always be associated with a mutex
        # to avoid a race condition created by one thread preparing
        # to wait and another thread which may signal the condition
        # before the first thread actually waits on
        # it resulting in a deadlock"
        #
        self.condition.acquire()
        while True:
            i = self.resource_list.pop()
            if i is None:
                print 'Consumer exiting'
                break
            print 'Consumed: %d' % i
            self.condition.wait()
            time.sleep(0.2)
        self.condition.release()


def main_cond():
    print '\n\nProd_cons using condition'
    condition = Condition()
    shared_list = []

    p_thread = Producer_Cond(shared_list, condition)
    c_thread = Consumer_Cond(shared_list, condition)

    t1 = time.time()
    p_thread.start()
    c_thread.start()

    p_thread.join()
    c_thread.join()

    print 'total time = %s' % str(time.time() - t1)

    #
    # Producer notifies consumer after producing
    #

    # Produced: 0
    # Consumed: 0
    # Produced: 1
    # Consumed: 1
    # Produced: 2
    # Consumed: 2
    # Produced: 3
    # Consumed: 3
    # Produced: 4
    # Consumed: 4
    # Produced: 5
    # Consumed: 5
    # Consumer exiting
    # total time = 1.42394113541

if __name__ == '__main__':
    main_lock()
    main_cond()
