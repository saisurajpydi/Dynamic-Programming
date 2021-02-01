"""
Partition problem 

Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is the same. 

Examples: 

arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.
"""
arr = [3, 1, 1, 2, 2,1]
n = len(arr)
sum = 0
for i in arr:
    sum += i

def equalSum(arr, sum , n):
    if(sum % 2 == 0):
        sum = sum // 2    
    else:
        return False
    row = n + 1
    col = sum + 1
    dp = [[0 for i in range(col)] for i in range(row)]
    for i in range(col):
        dp[0][i] = False
    for i in range(row):
        dp[i][0] = True
    for i in range(1,row):
        for j in range(1,col):
            if( arr[i - 1] <= sum):
                dp[i][j] = dp[i-1][j-arr[i - 1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]
print(equalSum(arr,sum,n))