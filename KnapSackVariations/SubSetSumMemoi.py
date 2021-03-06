"""
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 

Example: 

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
"""
arr = [3, 34, 4, 12, 5, 2]
sum = 100
n = len(arr)
row = n + 1
col = sum + 1
dp = [[-1 for i in range(col)]for i in range(row)]
def subset(arr,sum , n):
    if( n == 0 ):
        return False
    if( sum == 0 ):
        return True
    if( arr[n-1] <= sum):
        dp[n][sum] = subset(arr,sum-arr[n-1],n-1) or subset(arr,sum,n-1)
    else:
        dp[n][sum] = subset(arr,sum , n-1)
    return dp[n][sum]

print(subset(arr,sum,n))