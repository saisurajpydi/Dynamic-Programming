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
t = [[-1] * col] * row
def knapsack(wt,val,W,n):
    if( n == 0 or W == 0):
        return 0
    if( t[n][W] != -1):
        return t[n][W]
    if( wt[n-1] <= W):
        t[n][W] = max(val[n-1] + knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
    if( wt[n-1] > W):
        t[n][W] = knapsack(wt,val,W,n-1)
    return t[n][W]
       

print(knapsack(wt,val,W,n))

