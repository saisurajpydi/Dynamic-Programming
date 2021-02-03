"""
Minimum number of deletions to make a string palindrome

Given a string of size ‘n’. The task is to remove or delete the minimum number of characters from the string so that the resultant string is a palindrome. 

Note: The order of characters should be maintained. 

Examples : 

Input : aebcbda
Output : 2
Remove characters 'e' and 'd'
Resultant string will be 'abcba'
which is a palindromic string

Input : geeksforgeeks
Output : 8
"""
class Solution:
    def minNoDel(self, s1: str) -> int:
        s2 = s1[::-1]
        n1 = len(s1)
        n2 = len(s2)
        col = n2 + 1
        row = n1 + 1
        dp = [[0 for i in range(col)] for i in range(row)]
        if(n1 == 0 or n2 == 0):
            lenlcs= 0
        else:
            for i in range(1,row):
                for j in range(1,col):
                    if( s1[i-1] == s2[j-1]):
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
            lenlcs = dp[n1][n2]
        return n1 - lenlcs

if __name__ == "__main__":
    so = Solution()
    str1 =  "geeksforgeeks" #"agbcba"
    print("the minumum no of deletions required = " ,so.minNoDel(str1))