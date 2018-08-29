# Thread
## Condition variable
Mutexes allow you to avoid data races, unfortunately while they allow you to protect an operation, they don't permit you to wait until another thread completes an arbitrary activity. Condition Variables solve this problem.
https://www.cs.nmsu.edu/~jcook/Tools/pthreads/pthread_cond.html
https://gist.github.com/rtv/4989304#file-cond-c


## Readers–writer lock
https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock

## http://www.cs.cornell.edu/courses/cs4410/2015su/lectures/lec06-spin.html
Spin locks, Test and Set, compare_and_swap
