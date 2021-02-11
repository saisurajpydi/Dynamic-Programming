"""
Longest Repeated Subsequence

Given a string, print the longest repeating subsequence such that the two subsequence don’t have same string character at same position, i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.

Examples:

Input: str = "aabb"
Output: "ab"

Input: str = "aab"
Output: "a"
The two subsequence are 'a'(first) and 'a' 
(second). Note that 'b' cannot be considered 
as part of subsequence as it would be at same
index in both.

"""
class Solution:
    def lrs(self, str1):
        str2 = str1
        n1 = len(str1)
        n2 = len(str2)
        col = n2 + 1
        row = n1 + 1
        dp = [[0 for i in range(col)] for i in range(row)]
        if( n1 == 0 or n2 == 0):
            return 0
        for i in range(1,row):
            for j in range(1,col):
                if(str1[i-1] == str2[j-1] and i != j):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        return dp[n1][n2]

if __name__ == "__main__":
    so = Solution()
    str1 = "aabebcdd"
    print("the longest subsequnce length is : ",so.lrs(str1))
