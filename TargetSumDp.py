"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

eg:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

"""
nums = [0,0,0,0,0,0,0,1] #[1, 1, 1, 1, 1]
S = 1 # 3
def findTargetSumWays( nums, S):
    n = len(nums)
    sum = 0
    for i in nums:
        sum += i
    if( sum >= S):
        subset = (S + sum) // 2
        col = sum + 1
        row = n + 1
        dp = [[0 for i in range(col)] for i in range(row )]
        for i in range(col):
            dp[0][i] = 0
        for i in range(row):
           dp[i][0] = 1
        for i in range(1,row):
            for j in range(1,col):
                if(nums[ i-1 ] <= j):
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][subset]
    else:
        return 0
print(findTargetSumWays(nums,S))