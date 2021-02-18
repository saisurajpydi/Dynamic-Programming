"""
Palindrome Partitioning

Given a string, a partitioning of the string is a palindrome partitioning if every substring of the partition is a palindrome. For example, “aba|b|bbabb|a|b|aba” is a palindrome partitioning of “ababbbabbababa”. Determine the fewest cuts needed for a palindrome partitioning of a given string. For example, minimum of 3 cuts are needed for “ababbbabbababa”. The three cuts are “a|babbbab|b|ababa”. If a string is a palindrome, then minimum 0 cuts are needed. If a string of length n containing all different characters, then minimum n-1 cuts are needed. 
"""
import sys
def ispalindrome(s1):
    s2 = ""
    s2 += s1
    s1 = s1[::-1]
    if(s1 == s2):
        return True
    return False
    
def solve(s,i,j):
    if(i >= j ):
        return 0
    if(ispalindrome(s)):
        return 0
    ans = sys.maxsize
    for k in range(i,j):
        temp = 1 + solve(s,i,k) + solve(s,k+1,j)
        ans = min(temp,ans)
    return ans

if __name__ == "__main__":
    s = "ababbbabbababa" #"nitim"
    i = 0
    j = len(s)-1
    print(solve(s,i,j))