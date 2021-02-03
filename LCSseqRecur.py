"""
Longest Common Subsequence | DP using RECURSION

Given two strings s1 and s2, the task is to find the length of longest common subsequence present in both of them.

Examples:

Input: s1 = “ABCDGH”, s2 = “AEDFHR”
Output: 3
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

Input: s1 = “striver”, s2 = “raj”
Output: 1
"""
class Solution:        
    def lcs(self,t1,t2,n1,n2):
        if( n1 == 0 or n2 == 0):
            return 0
        if( t1[n1-1] == t2[n2-1]):
            return ( 1 + self.lcs(t1,t2,n1-1,n2-1))
        else:
            return max( self.lcs(t1,t2,n1,n2-1), self.lcs(t1,t2,n1-1,n2) )

if __name__ == "__main__":
    so = Solution()
    t1 = "ylqpejqbalahwr"  #"AGGTAB"   #"striver" #"ABCDGH" #"abcdefghijklmnopqrstuvwxyz" #"ylqpejqbalahwr"
    t2 = "yrkzavgdmdgtqpg"  #"GXTXAYB"  #"raj"   #"AEDFHR" #"ace"  #"yrkzavgdmdgtqpg"
    n1 = len(t1)
    n2 = len(t2)
    print(so.lcs(t1,t2,n1,n2))