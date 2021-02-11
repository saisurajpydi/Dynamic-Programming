"""
Median of a Doubly Linked List
"""

"""
alist = list(map(int,input().split()))
i = 0
n = len(alist)
if( n % 2 == 0):
    median = (alist[n//2] + alist[(n//2) - 1]) / 2
else:
    median = alist[n//2]

print(median)
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class Dll:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)
        if(self.head == None):
            new_node.prev = None
            self.head = new_node
            #new_node.next = None
        else:
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
    def display(self):
        cur = self.head
        while(cur != None):
            print(cur.data)
            cur = cur.next
    
    def median(self):
        j = self.head
        length = 0
        while(j != None):
            length += 1
            j = j.next
        if(length % 2 == 0):
            location = self.head
            val = length // 2
            while(location != None and val != 0):
                val -= 1
                location = location.next
            print("medain :",(location.data + location.prev.data) / 2)
        else:
            location = self.head
            val = length // 2
            while(location != None and val != 0):
                val -= 1
                location = location.next
            print("median :",location.data)
d = Dll()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.append(6)
d.display()
d.median()

      