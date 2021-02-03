"""
Minimum number of deletions and insertions to transform one string into another


Given two strings ‘str1’ and ‘str2’ of size m and n respectively. The task is to remove/delete and insert the minimum number of characters from/in str1 to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.

Example 1: 

Input : 
str1 = "heap", str2 = "pea" 
Output : 
Minimum Deletion = 2 and
Minimum Insertion = 1
Explanation:
p and h deleted from heap
Then, p is inserted at the beginning
One thing to note, though p was required yet
it was removed/deleted first from its position and
then it is inserted to some other position.
Thus, p contributes one to the deletion_count
and one to the insertion_count.
"""
class Solution:
    def min(self,str1,str2,n1,n2):
        col = n2 + 1
        row = n1 + 1
        dp = [[0 for i in range(col)] for i in range(row)]
        if( n1 == 0 or n2 == 0):
            lenlcr = 0
        else:
            for i in range(1,row):
                for j in range(1,col):
                    if( str1[i-1] == str2[j-1]):
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max( dp[i-1][j] , dp[i][j-1])
            lenlcs = dp[n1][n2]
        print("minimum deletions required = " , n1 - lenlcs)
        print("minimum insertions required = " , n2 - lenlcs)

if __name__ == "__main__":
    so =Solution()
    str1 = "heap"
    str2 = "pea"
    n1 = len(str1)
    n2 = len(str2)
    so.min(str1,str2,n1,n2)
