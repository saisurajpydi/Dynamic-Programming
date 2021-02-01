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
dp = [[0 for i in range(col)]for i in range(row)]
def subset(arr,sum,n):
    for i in range(col):
        dp[0][i] = False
    for i in range(row):
        dp[i][0] = True 
    for i in range(1,row):
        for j in range(1,col):
            if(arr[i-1] <= j):
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]
print(subset(arr,sum,n))
    

