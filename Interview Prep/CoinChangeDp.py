"""
Coin Change | DP-7

Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
"""
class Solution():
    def coin(self,val,W):
        n = len(val)
        row = n + 1
        col = W + 1
        dp = [[0 for i in range(col)] for i in range(row)]
        for i in range(col):
            dp[0][i] = 0
        for i in range(row):
            dp[i][0] = 1
        for i in range(1,row):
            for j in range(1,col):
                if(val[i-1] <= j):
                    dp[i][j] = dp[i][j-val[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][W]


if __name__ == "__main__":
    so = Solution()
    W = 10 #4
    val = [2,5,3,6] #[1,2,3]
    print(so.coin(val,W))
