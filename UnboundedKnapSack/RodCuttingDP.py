"""
CUTTING A ROD

Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1) 

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 3   5   8   9  10  17  17  20

"""
class Solution:
    def rodCut(self,length,price,n):
        col = n + 1
        row = n + 1
        dp = [[0 for i in range(col)] for i in range(row)]        
        for i in range(row):
            for j in range(col):
                if( i == 0 or j == 0):
                    dp[i][j] = 0
                if( length[i - 1] <= j ):
                    dp[i][j] = max( price[i-1] + dp[i][j-length[i-1]] , dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][n]


if __name__ == "__main__":
    so = Solution()
    price = [1, 5, 8, 9, 10, 17, 17, 20] 
    n = len(price)
    length = [i for i in range(1,n+1)]
    print(so.rodCut(length,price,n))
