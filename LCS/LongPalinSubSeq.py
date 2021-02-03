"""
 Longest Palindromic Subsequence


Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
"""
class Solution:
    def longestPalindromeSubseq(self, s1: str) -> int:
        s2 = s1[::-1]
        n1 = len(s1)
        n2 = len(s2)
        col = n2 + 1
        row = n1 + 1
        dp = [[0 for i in range(col)] for i in range(row)]
        if(n1 == 0 or n2 == 0):
            return 0
        for i in range(1,row):
            for j in range(1,col):
                if( s1[i-1] == s2[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        return dp[n1][n2]

if __name__ == "__main__":
    so = Solution()
    str1 = "agbcba"
    print(so.longestPalindromeSubseq(str1))
