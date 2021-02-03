"""
Longest Common Subsequence | DP using Memoization

Given two strings s1 and s2, the task is to find the length of longest common subsequence present in both of them.

Examples:

Input: s1 = “ABCDGH”, s2 = “AEDFHR”
Output: 3
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

Input: s1 = “striver”, s2 = “raj”
Output: 1
"""
class Solution:
    def lcs(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        col = n2 + 1
        row = n1 + 1
        dp = [[0 for i in range(col)] for i in range(row)]
        if( n1 == 0 or n2 == 0):
            return 0
        for i in range(1,row):
            for j in range(1,col):
                if( text1[i-1] == text2[j-1] ):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        return dp[n1][n2]

if __name__ == "__main__":
    so = Solution()
    t1 = "ylqpejqbalahwr"  #"AGGTAB"   #"striver" #"ABCDGH" #"abcdefghijklmnopqrstuvwxyz" #"ylqpejqbalahwr"
    t2 = "yrkzavgdmdgtqpg"  #"GXTXAYB"  #"raj"   #"AEDFHR" #"ace"  #"yrkzavgdmdgtqpg"
    n1 = len(t1)
    n2 = len(t2)
    print(so.lcs(t1,t2))