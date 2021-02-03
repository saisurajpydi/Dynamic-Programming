class Solution:
    def lcSubStr(self,text1,text2):
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
                    dp[i][j] = 0
        return max(map(max, dp))

if __name__ == "__main__":
    so = Solution()
    text1 = "abcxyz"
    text2 = "abcdef"
    print(so.lcSubStr(text1,text2))