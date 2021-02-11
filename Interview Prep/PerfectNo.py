"""
PERFECT NO
to check whether a given no is perfect or not
"""
class Solution():
    def perfect(self,n):
        result = 0
        for i in range(1,n):
            if( n % i == 0):
                result += i
        if(result == n):
            return True
        return False

if __name__ == "__main__":
    so = Solution()
    n = int(input())
    print(so.perfect(n))