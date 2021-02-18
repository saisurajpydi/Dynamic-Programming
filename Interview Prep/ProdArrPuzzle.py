"""
A Product Array Puzzle | Set 3


Given an array arr[] consisting of N integers, the task is to construct a Product array of the same size without using division (‘/’) operator such that each array element becomes equal to the product of all the elements of arr[] except arr[i].

Examples:

Input: arr[] = {10, 3, 5, 6, 2}
Output: 180 600 360 300 900
Explanation:
3 * 5 * 6 * 2 is the product of all array elements except 10 is 180
10 * 5 * 6 * 2 is the product of all array elements except 3 is 600.
10 * 3 * 6 * 2 is the product of all array elements except 5 is 360.
10 * 3 * 5 * 2 is the product of all array elements except 6 is 300.
10 * 3 * 6 * 5 is the product of all array elements except 2 is 9.

Input: arr[] = {1, 2, 1, 3, 4}
Output: 24 12 24 8 6
"""
a = list(map(int,input().split()))
alen = len(a)
result = []
val = 1
for i in range(alen):
    for j in range(alen):
        if( j != i):
            val *= a[j]
    result.append(val)
    val = 1
print(result)