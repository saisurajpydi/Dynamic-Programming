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
arr = [3, 1, 1, 2, 2, 1]
n = len(arr)
sum = 0
for i in arr:
    sum += i

def equalSum(arr,sum,n):
    if(sum % 2 == 0):
        sum = sum // 2    
    else:
        return False
    row = n + 1
    col = sum + 1
    dp = [[0 for i in range(col)] for i in range(row)]    
    if( sum == 0):
        return True
    if( n == 0):
        return False
    if(arr[n-1] <= sum):
        dp[n][sum] = equalSum(arr,sum-arr[n-1],n-1) or equalSum(arr,sum,n-1)
    else:
        dp[n][sum] = equalSum(arr,sum,n-1)
    return dp[n][sum]
print(equalSum(arr,sum,n))