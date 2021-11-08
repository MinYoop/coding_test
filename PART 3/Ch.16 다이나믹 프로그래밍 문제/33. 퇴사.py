
# n = int(input())

# lst = []

# for _ in range(n):
#     lst.append(tuple(map(int,input().split())))


# dp = [0 for _ in range(n+1)]

# max_value = 0

# for i in range(n-1,-1,-1):

#     time = lst[i][0] + i

#     if time <= n:
#         dp[i] = max(lst[i][1] + dp[time] , max_value)

#         max_value = dp[i]
    
#     else:
#         dp[i] = max_value

# print(dp[0])




# 2회차 풀이

n = int(input())

t = []
p = []

for i in range(n):
    x, y = map(int,input().split())

    t.append(x)
    p.append(y)

dp = [0] * (n + 1)

for i in range(n-1,-1,-1):
    
    if i + t[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])

print(dp[0])

