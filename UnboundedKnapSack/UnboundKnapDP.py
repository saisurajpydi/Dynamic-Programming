"""
Given a knapsack weight W and a set of n items with certain value vali and weight wti, we need to calculate the maximum amount that could make up this quantity exactly. This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.
Examples: 

Input : W = 100
       val[]  = {1, 30}
       wt[] = {1, 50}
Output : 60
There are many ways to fill knapsack.
1) 2 instances of 50 unit weight item.
2) 100 instances of 1 unit weight item.
3) 1 instance of 50 unit weight item and 50
   instances of 1 unit weight items.
We get maximum value with option 2.

Input : W = 8
       val[] = {10, 40, 50, 70}
       wt[]  = {1, 3, 4, 5}       
Output : 110 
We get maximum value with one unit of
weight 5 and one unit of weight 3.

"""

class Solution:
    def unboundKnap(self,wt,val,W,n):
        col = W + 1
        row = n + 1
        dp = [[0 for i in range(col)] for i in range(row)]        
        for i in range(row):
            for j in range(col):
                if( i == 0 or j == 0):
                    dp[i][j] = 0
                if( wt[i - 1] <= j ):
                    dp[i][j] = max( val[i-1] + dp[i][j-wt[i-1]] , dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][W]


if __name__ == "__main__":
    so = Solution()
    wt = [5 , 10 , 15]
    val = [10, 30 ,20]
    W = 100
    n = len(wt)
    print(so.unboundKnap(wt,val,W,n))
    