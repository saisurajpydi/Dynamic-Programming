"""
Python program for Longest Increasing Subsequence

The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
longest-increasing-subsequence

More Examples:

Input  : arr[] = {3, 10, 2, 1, 20}
Output : Length of LIS = 3
The longest increasing subsequence is 3, 10, 20

Input  : arr[] = {3, 2}
Output : Length of LIS = 1
The longest increasing subsequences are {3} and {2}

Input : arr[] = {50, 3, 10, 7, 40, 80}
Output : Length of LIS = 4
The longest increasing subsequence is {3, 7, 40, 80}
"""
class Solution():
    def lis(self,list1):
        list2 = []
        list2 += list1
        list2.sort()
        n1 = len(list1)
        n2 = len(list2)
        col = n2 + 1
        row = n1 + 1
        dp = [[0 for i in range(col)] for i in range(row)]
        for i in range(1,row):
            for j in range(1,col):
                if(list1[i - 1] == list2[j - 1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max( dp[i][j-1] , dp[i-1][j])
        return dp[n1][n2]

if __name__ == "__main__":
    so = Solution()
    list1 = list(map(int,input().split()))

    print(so.lis(list1))
# 3 10 2 1 20
