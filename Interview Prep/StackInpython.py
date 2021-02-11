"""
Implementation using queue module
Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using put() function and get() takes data out from the Queue. 
There are various functions available in this module: 
 

maxsize – Number of items allowed in the queue.
empty() – Return True if the queue is empty, False otherwise.
full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) – Put an item into the queue without blocking.
qsize() – Return the number of items in the queue. If no free slot is immediately available, raise QueueFull.

"""

from queue import LifoQueue

stack = LifoQueue()
stack.put("a")
stack.put("b")
stack.put("c")
stack.put("d")

print("the size of the stack :",stack.qsize())
print("boolean is full or not :",stack.full())
print("to check whether empty or not :",stack.empty())

print("the elements in the stack are LIFO :", end = " ")
for i in range(stack.qsize()):
    print(stack.get(i), end = " ")
h