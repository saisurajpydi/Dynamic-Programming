"""
Arrange given numbers to form the biggest number | Set 1

Given an array of numbers, arrange them in a way that yields the largest value. For example, if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 gives the largest value. And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives the largest value.
"""
from itertools import permutations
a = list(map(int, input().split()))
lst = []
for i in permutations(a, len(a)):
	lst.append("".join(map(str,i))) 
print(max(lst))



