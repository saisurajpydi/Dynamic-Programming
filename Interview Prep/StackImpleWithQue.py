"""
implementing the STACK LIFO using 2 QUEUES
"""
# can be implemented in 2 ways
# 1 -> where push operation is costly  -> should be used when more pop operations are on the stack
# 2 -> where pop operation is costly   -> should be used when more push operations are on the stack  

from queue import Queue


q1 = Queue()
q2 = Queue()

def push(ele):
    q1.put(ele)

def pop():
    for i in range(q1.qsize()-2):
        q2.put(q1.get())
    print("the poped elem :",q1.get())
    for i in range(q2.qsize()-2):
        q1.put(q2.get())

def display():
    print("the elements in the stack are :")
    for i in range(q1.qsize()):
        print(q1.get())

push(1)
push(2)
push(3)
push(4)
push(5)
display()
#pop()
#display()
