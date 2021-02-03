"""
Printing Shortest Common Supersequence

Given two strings X and Y, print the shortest string that has both X and Y as subsequences. If multiple shortest supersequence exists, print any one of them.

Examples:

Input: X = "AGGTAB",  Y = "GXTXAYB"
Output: "AGXGTXAYB" OR "AGGXTXAYB" 
OR Any string that represents shortest
supersequence of X and Y

Input: X = "HELLO",  Y = "GEEK"
Output: "GEHEKLLO" OR "GHEEKLLO"
OR Any string that represents shortest 
supersequence of X and Y
"""
class Solution:
    def printSCS(self,st1,str2,n1,n2):
        col = n2 + 1
        row = n1 + 1
        dp = [[0 for i in range(col)] for i in range(row)]
        if(n1 == 0):
            return str2
        if(n2 == 0):
            return str1
        for i in range(1,row):
            for j in range(1,col):
                if(str1[i-1] == str2[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        result = ""
        i = n1
        j = n2
        while( i > 0 and j > 0):
            if( str1[i-1] == str2[j-1] ):
                result += str1[i-1]
                i -= 1
                j -= 1
            else:
                if( dp[i-1][j] > dp[i][j-1]):
                    result += str1[i-1]
                    i -= 1
                else:
                    str2[j-1]
                    j -= 1
        """
        while( i > 0):
            result += str1[i-1]
            i -= 1
        while( j > 0):
            result += str2[j-1]
            j -= 1
        """    
        return result[::-1]



if __name__ == "__main__":
    so = Solution()
    str1 = "acbcf"
    str2 = "abcdaf"
    n1 = len(str1)
    n2 = len(str2)
    print(so.printSCS(str1,str2,n1,n2))