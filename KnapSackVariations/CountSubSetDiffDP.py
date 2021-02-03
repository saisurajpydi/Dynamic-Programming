"""
Count the number of subset with a given difference 
 eg:
 arr = [1,1,2,3]
 dif = 1
 output = count of sets whose difference is given difference
          [1+3]-[1+2]
          [1+1+2]-[3]
          [1+3]-[1+2]
    COUNT = 3
"""
arr = [1,1,2,3]
sum = 0
for i in arr:
    sum += i
n = len(arr)
dif = 1
subset1 = (dif + sum)//2
col = subset1 + 1
row = n + 1
dp = [[0 for i in range(col)] for i in range(row)]
def countSubSet(subset1,arr,n):
    for i in range(col):
        dp[0][i] = 0
    for i in range(row):
        dp[i][0] = 1
    for i in range(1,row):
        for j in range(1,col):
            if(arr[i-1] <= j):
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][subset1]
print(countSubSet(subset1,arr,n))
