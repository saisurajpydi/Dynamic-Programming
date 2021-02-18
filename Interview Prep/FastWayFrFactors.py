"""
fastest way for finding factors of a given Number
"""
from functools import reduce

def factor(n):
    return set(reduce(list.__add__,([i,n//i] for i in range(1,int(n ** 0.5)) if n % i == 0)))

s = factor(10)
print(s)