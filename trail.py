"""
a = list(map(int,input().split()))
n = a[0] 
W = a[1]
print(len(a))
row = n + 1
col = W + 1
dp = [[0] * col]*row
p=[[0 for x in range(col)] for x in range(row)]
print(dp)
print(p)
"""
"""
n = 8
r = [i for i in range(1,n+1)]
print(r)
"""
"""
t1 = "ylqpejqbalahwr" 
print([[] * 15] * 11)
print([[0 for i in range(15)] for i in range(15)])
"""
"""
arr = "sai suraj"
print(arr[::-1])
arr = "".join(reversed(arr))
print(arr)
"""

"""
key_value ={}     
   
key_value[2] = 56       
key_value[1] = 2 
key_value[5] = 12 
key_value[4] = 24
key_value[6] = 18      
key_value[3] = 323 
print(key_value)
newdict = {k:v for k, v in sorted(key_value.items())}
ndict = {k: v for k, v in sorted(key_value.items(), key = lambda v: v[1] )}
print(newdict)
print(ndict)
"""
""" 
keys = ['hi','hello','bye']
data = dict(zip(keys, list(i for i in range(len(keys)))))
print(data)
#print(data)
#print(data(1))
#for i in range(len(data)):
 #   print(i, data(i) )
alist = list(data.items())
print(alist)
print(alist[1])
"""
"""
w = [3,1,2]
for i in range(1,len(w)):
    print(w.index(i))
"""
"""
# cook your dish here
import math
Test = int(input())
for i in range(Test):
    N = int(input())
    w = list(map(int,input().split()))
    L = list(map(int,input().split()))
    # dictionary with key = W and values = index (method 1)
    ind = {}
    s = 0
    for j in range(1,N+1):
        ind[j] = w.index(j)

    # dictionary with key = W and values = index (method 2)
"""
    """
    dictionary = dict(zip(w,list(i for i in range(N))))
    newDic = {k: v for k, v in sorted(dictionary.items())}
    print(newDic)
    """
    """
    for j in range(2,N+1):
        temp1 = ind[j]
        temp2 = ind[j-1]
        temp = 0
        if( temp1 <= temp2):
            temp =(math.ceil((temp2+1-temp1)/L[temp1]))
        s += temp
        ind[j] += temp*(L[temp1])
    print(s)
    """