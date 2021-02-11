"""
str1 = "AXY"
str2 = ""ADXCPY"
output = True (is str1 is a subseq of str2 or not)

"""
class Solution:
    def seqPattern(self, A , B):
        n1 = len(A)
        n2 = len(B)
        col = n2 + 1
        row = n1 + 1
        dp = [[0 for i in range(col)] for i in range(row)]
        for i in range(1,row):
            for j in range(1,col):
                if(str1[i-1] == str2[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1] , dp[i-1][j])
        return dp[n1][n2]

if __name__ == "__main__":
    so = Solution()
    str1 = "" #"AXY"
    str2 = "ADXCPY"
    print(len(str1) == so.seqPattern(str1,str2))

