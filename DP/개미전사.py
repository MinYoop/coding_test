

n = int(input())

array = list(map(int,input().split()))

dp = [0] * n

dp[0] = 1
dp[1] = 3

for i in range(2,n):

    dp[i] = max(array[i]+dp[i-2],dp[i-1])

print(dp[n-1])