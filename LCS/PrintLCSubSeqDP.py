"""
Printing Longest Common Subsequence

Given two sequences, print the longest subsequence present in both of them.
Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""

def longestCommonSubsequence(a, b):
    n1 = len(a)
    n2 = len(b)
    col = n2 + 1
    row = n1 + 1
    dp = [[0 for i in range(col)] for i in range(row)]
    if( n1 == 0 or n2 == 0):
        return 0
    for i in range(1,row):
        for j in range(1,col):
            if( a[i-1] == b[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max( dp[i][j-1] , dp[i-1][j])
    #lis = []
    st = ""
    i = n1 
    j = n2 
    while( i > 0 and j > 0):
        if(a[i-1] == b[j-1]):
            st += a[i-1]
            i -= 1
            j -= 1
        else:
            if( dp[i-1][j] > dp[i][j-1] ):
                i -= 1
            else:
                j -= 1
    return st[::-1]

if __name__ == "__main__":
    a = "saisuraj"
    b = "surajpydi"
    print(longestCommonSubsequence(a, b))