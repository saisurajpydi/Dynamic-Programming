"""
Partition a set into two subsets such that the difference of subset sums is minimum

Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum. 
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.
Example: 

Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11        

"""
arr = [1,6,11,8] #[1, 4, 12, 5, 3]
sum = 0
for i in arr:
    sum += i
n = len(arr)
row = n + 1
col = sum + 1
dp = [[0 for i in range(col)]for i in range(row)]
def subset(arr,sum,n):
    for i in range(col):
        dp[0][i] = False
    for i in range(row):
        dp[i][0] = True
    for i in range(1,row):
        for j in range(1,col):
            if(arr[i-1] <= j):
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    ans = [] 
    for i in range(col):
        ans.append(dp[n][i])
    #return ans
    mi = 999 # sum big value
    length = len(ans)
    for i in range(sum // 2 ,-1,-1):
        if(ans[i] == True):
            mi = min(mi, sum - (2*i))
    return mi
print(subset(arr,sum,n))