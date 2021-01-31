"""
0-1 Knapsack Problem

Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).

eg:

wt[] =  [1 , 3 , 4 , 5]
val[] = [1 , 4 , 5 , 7]
W = 7
"""
wt =  [10,20,30]            #[1,3,4,5]
val = [60,100,120] #[1,4,5,7]
n = len(wt)
W = 50
row = n + 1
col = W + 1
dp = [[0] * col]*row
def knapsack(wt,val,W,n):
    for i in range(row):
        for j in range(col):
            if( i == 0 or j == 0):
                dp[i][j] = 0
            elif( wt[i-1] <= j):
                dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]
print(knapsack(wt,val,W,n))