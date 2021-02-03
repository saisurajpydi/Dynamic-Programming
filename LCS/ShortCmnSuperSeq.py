"""
Shortest Common Supersequence


Given two strings str1 and str2, the task is to find the length of the shortest string that has both str1 and str2 as subsequences.

Examples : 

Input:   str1 = "geek",  str2 = "eke"
Output: 5
Explanation: 
String "geeke" has both string "geek" 
and "eke" as subsequences.

Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
Output:  9
Explanation: 
String "AGXGTXAYB" has both string 
"AGGTAB" and "GXTXAYB" as subsequences.
"""
class Solution:
    def scs(self,str1,str2,n1,n2):
        col = n2 + 1
        row = n1 + 1
        dp = [[0 for i in range(col)] for i in range(row)] 
        if(n1 == 0 or n2 == 0):
            lenlcs = 0
        else:
            for i in range(1,row):
                for j in range(1,col):
                    if(str1[i-1] == str2[j-1]):
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
            lenlcs = dp[n1][n2]
        result = n1 + n2 - lenlcs
        return result

if __name__ == "__main__":
    so = Solution()
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    n1 = len(str1)
    n2 = len(str2)
    print(so.scs(str1,str2,n1,n2)) 