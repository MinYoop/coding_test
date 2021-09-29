
# # 내 방법 아래에서 위로.

# n = int(input())

# lst = [list(map(int,input().split())) for _ in range(n)]

# print(lst)

# dp = [[] for _ in range(n-1)]

# for i in range(n-2,-1,-1):

#     print(i)
    
#     for j in range(i+1):

#         if i == n-2:
#             dp[i].append(max( lst[i+1][j] , lst[i+1][j+1] ) + lst[i][j] )
#         else:
#             dp[i].append(max( dp[i+1][j] , dp[i+1][j+1] ) + lst[i][j] )

# print(dp)
# print(dp[0][0])

# 위에서 아래로

n = int(input())

dp = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):

    for j in range(i+1):

        up_left = 0
        up = 0

        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]

        if j == i:
            up = 0
        else:
            up = dp[i-1][j]

        dp[i][j] = max(up,up_left) + dp[i][j]

print(max(dp[n-1]))