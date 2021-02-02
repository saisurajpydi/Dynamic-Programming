"""
Count of subsets with sum equal to X

Given an array arr[] of length N and an integer X, the task is to find the number of subsets with sum equal to X.

Examples:

Input: arr[] = {1, 2, 3, 3}, X = 6
Output: 3
All the possible subsets are {1, 2, 3},
{1, 2, 3} and {3, 3}

Input: arr[] = {1, 1, 1, 1}, X = 1
Output: 4
"""
arr = [1, 1, 1, 1]
sum = 20
n = len(arr)
row = n + 1
col = sum + 1
dp = [[0 for i in range(col)] for i in range(row)]
def subset(arr,sum,n):
    for i in range(col):
        dp[0][i] = 0
    for i in range(row):
        dp[i][0] = 1
    for i in range(1,row):
        for j in range(1,col):
            if( arr[i-1] <= j):
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]

print(subset(arr,sum,n))