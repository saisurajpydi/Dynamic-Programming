a = list(map(int,input().split()))
n = a[0] 
W = a[1]
print(len(a))
row = n + 1
col = W + 1
dp = [[0] * col]*row
p=[[0 for x in range(col)] for x in range(row)]
print(dp)
print(p)