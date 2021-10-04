
n = int(input())

lst = []

for _ in range(n):
    lst.append(tuple(map(int,input().split())))


dp = [0 for _ in range(n+1)]

max_value = 0

for i in range(n-1,-1,-1):

    time = lst[i][0] + i

    if time <= n:
        dp[i] = max(lst[i][1] + dp[time] , max_value)

        max_value = dp[i]
    
    else:
        dp[i] = max_value

print(dp[0])




