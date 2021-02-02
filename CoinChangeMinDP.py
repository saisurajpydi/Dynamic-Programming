"""
Find minimum number of coins that make a given value


Given a value V, if we want to make change for V cents, and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change? 

Examples:  

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents 

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents
"""
import sys
class Solution:
    def coinMin(self,arr,sum,n):
        col = sum + 1
        row = n + 1
        dp = [[0 for i in range(col)] for i in range(row)]
        for i in range(col):
            dp[0][i] = sys.maxsize - 1 # some max value
        for i in range(row):
            dp[i][0] = 0
        for i in range(1,col):
            if( i % arr[0] == 0):
                dp[1][i] = i // arr[0]
            else:
                dp[1][i] = sys.maxsize - 1 # some big value
        for i in range(2,row):
            for j in range(1,col):
                if(arr[i-1] <= j):
                    dp[i][j] = min(dp[i][j-arr[i-1]] + 1 , dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][sum]

if __name__=="__main__":
    so = Solution()
    arr = [9,6,5,1] #[25,10,5]
    n = len(arr)
    sum = 11 #30
    print(so.coinMin(arr,sum,n))